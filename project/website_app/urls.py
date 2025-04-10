from django.urls import path
from .views import FormSendMail

urlpatterns = [
    path('sendmail/', FormSendMail.as_view())
]
