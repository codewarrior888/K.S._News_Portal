from datetime import datetime

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User

from .models import Post


@shared_task
def send_new_post_notifications(post_id):

    post = Post.objects.get(id=post_id)
    post_category = post.category.all()

    subscribers_emails = []

    for category in post.category.all():
        subscribers_emails += User.objects.filter(subscriptions__category=category).values_list('email', flat=True)

    subject = f'Новая публикация в категории {post_category}'

    context = {
        'post_title': post.post_title,
        'post_url': f'{settings.SITE_URL}/news/{post.id}/'
    }

    text_content = (
        f'Заголовок: {post.post_title}\n'
        f'Сайт: {settings.SITE_URL}/news/{post.id}/'
    )

    html_content = render_to_string('post_created_email.html', context)

    for email in subscribers_emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    print("Рассылка сообщений успешна завершена")


@shared_task
def send_weekly_news_updates():
    latest_news = Post.objects.filter(post_time__lte=datetime.now()).order_by('-post_time')[:5]  # пять последних постов

    subscribers_emails = []

    for post in latest_news:
        for category in post.category.all():
            subscribers_emails += User.objects.filter(subscriptions__category=category).values_list('email', flat=True)

    subject = 'Недельная рассылка новостей'

    text_content = (
        f'Заголовок: {post.post_title}\n'
        f'Сайт: {settings.SITE_URL}/news/{post.id}/'
    )

    context = {
        'latest_news': latest_news,
        'site_url': f'{settings.SITE_URL}/news/',
    }

    html_content = render_to_string('weekly_posts_update.html', context)

    for email in subscribers_emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
