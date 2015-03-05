from django.conf.urls import patterns, include, url
from .views import FeedbackView, ContactView



urlpatterns = patterns('',

    url(r'^feedback$', FeedbackView.as_view(), name='feedback_view'),
    url(r'^message$', ContactView.as_view(), name='contact_view'),

)