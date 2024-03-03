from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance,  created, **kwargs):
    if created:
        user = instance
        subject = 'Welcome to Kabu Hub'
        message = 'we are glad to have you join the community'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently= False,
        )

# @receiver(post_save, sender=Profile)


post_save.connect(createProfile, sender=User)
        
