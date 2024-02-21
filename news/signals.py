from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .tasks import send_new_post_notifications
from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, sender, **kwargs):
    if kwargs['action'] == 'post_add':
        send_new_post_notifications.delay(instance.id)
