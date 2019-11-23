from django.contrib.auth.views import LoginView
from django.urls import path

from allotment.views import (
    home,
    party_view,
    public_key_create,
    signup,
)


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('party/', party_view, name='party_view'),
    path('public_key', public_key_create, name='public_key'),
]
