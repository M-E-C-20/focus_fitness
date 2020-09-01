from django.urls import path
from . import views
from home.views import AboutView, ContactView, IndexView, TermsView, PrivacyView


urlpatterns = [


    # path('', IndexView.as_view(), name='home'),
    path('', IndexView, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('contact/',  ContactView.as_view(), name='contact')
]
