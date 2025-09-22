from django.shortcuts import render
from .models import Notification, Member

# Create your views here.
def list_notifications(request):
    notifications = Notification.objects.all()
    return render(request, "task/list_notifications.html", {"notifications": notifications})

def list_user_notifications(request, username):
    # Try to get the member; if not found, show an informative message in the template
    try:
        user = Member.objects.get(username=username)
    except Member.DoesNotExist:
        return render(request, "task/list_notifications.html", {
            "notifications": [],
            "missing_user": username
        })

    notifications = user.notification_set.all()
    return render(request, "task/list_notifications.html", {
        "notifications": notifications,
        "selected_user": user
    })