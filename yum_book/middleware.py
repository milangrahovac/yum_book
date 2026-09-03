import logging
from django.contrib.admin.models import LogEntry

logger = logging.getLogger('admin_logger')


class AdminActionLoggingMiddleware:
    """
    Middleware that intercepts POST requests to the admin panel 
    and logs created, updated, or deleted instances.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Process only successful admin actions performed by authenticated users
        if request.path.startswith('/admin/') and request.method == 'POST' and request.user.is_authenticated:
            # Grab the latest LogEntry created in this request window
            latest_entry = LogEntry.objects.filter(
                user=request.user).order_by('-action_time').first()

            if latest_entry:
                action_flag = "CREATED" if latest_entry.is_addition() else (
                    "UPDATED" if latest_entry.is_change() else "DELETED"
                )

                log_message = (
                    f"'{request.user.username}' (ID: {request.user.id}) | "
                    f"Action: {action_flag} | "
                    f"Model: {latest_entry.content_type} | "
                    f"Object: '{latest_entry.object_repr}' (ID: {latest_entry.object_id}) | "
                    f"Details: {latest_entry.get_change_message()}"
                )
                logger.info(log_message)

        return response
