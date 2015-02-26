from django.conf.urls import patterns, include, url
from .views import FeedbackView



urlpatterns = patterns('',

    url(r'^feedback$', FeedbackView.as_view(), name='feedback_view'),

)