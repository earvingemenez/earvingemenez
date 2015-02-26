from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView, View

from braces.views import (
    JSONResponseMixin,
    AjaxResponseMixin,
)

from .models import Feedback


class FeedbackView(AjaxResponseMixin, JSONResponseMixin, View):

    def get(self, *args, **kwargs):
        response = Feedback.objects.all()
        return self.render_json_object_response(response)