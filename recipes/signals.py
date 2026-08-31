# myapp/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Recipe
import logging
from django.contrib.auth.models import User


# Create a logger
# logger = logging.getLogger('django')

# Set up a logger for group actions
logger = logging.getLogger('admin_actions')


# @receiver(post_save, sender=Group)
# def log_group_creation(sender, instance, created, **kwargs):
#     """Logs when a new group is created."""
#     if created:  # Only log when a new group is created
#         logger.info(f"New group created: {instance.name} (ID: {instance.id})")


@receiver(post_save, sender=User)
def log_user_creation(sender, instance, created, **kwargs):
    if created:  # Only log when a new user is created
        logger.info(
            f"New user created: {instance.username} (ID: {instance.id})")


@receiver(post_delete, sender=User)
def log_user_deletion(sender, instance, **kwargs):
    """Log when a user is deleted."""
    # Get the current request
    logger.info(
        f"Admin deleted user {instance.username} (ID: {instance.id})")

# @receiver(post_save, sender=Recipe)
# def log_change(sender, instance, created, **kwargs):
#     if created:  # If a new Recipe is created
#         logger.info(
#             f"Admin user {instance._meta.app_label} added a new Recipe: {instance.name} (ID: {instance.id})")
#     else:  # If an existing Recipe is updated
#         logger.info(
#             f"Admin user {instance._meta.app_label} updated Recipe: {instance.name} (ID: {instance.id})")


# @receiver(post_delete, sender=Recipe)
# def log_deletion(sender, instance, **kwargs):
#     logger.info(
#         f"Admin user {instance._meta.app_label} deleted Recipe: {instance.name} (ID: {instance.id})")
