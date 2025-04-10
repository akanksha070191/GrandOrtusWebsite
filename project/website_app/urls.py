from django.urls import path
from .views import FormSendMail, UIJobProfile

urlpatterns = [
    path('sendmail/', FormSendMail.as_view()),
    path('job/', UIJobProfile.as_view()),
]
