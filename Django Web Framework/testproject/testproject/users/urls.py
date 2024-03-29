from django.urls import path, reverse
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'
urlpatterns = [
    path('login', LoginView.as_view(template_name="login.html", next_page='myapp:index'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]