from django.conf.urls import patterns, include, url
from .views import IndexView, ResumeView, ContactView


urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^cv$', ResumeView.as_view(), name='resume_view'),

    # AJAX
    url(r'^ajax/form/contact$', ContactView.as_view(), name='contact_view'),

)