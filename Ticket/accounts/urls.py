from django.urls import path

from accounts.views import SignupUserView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupUserView.as_view()),
    path('login/', LoginView.as_view()),
]
