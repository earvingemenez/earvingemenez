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
from main.forms import ContactForm


class FeedbackView(AjaxResponseMixin, JSONResponseMixin, View):

    def get(self, *args, **kwargs):
        response = Feedback.objects.all()
        return self.render_json_object_response(response)


class ContactView(AjaxResponseMixin, JSONResponseMixin, View):

    def post(self, *args, **kwargs):
        data = self.request.POST
        form = ContactForm(data)

        if form.is_valid():
            form.save()
            # Response
            return self.render_json_response({'sent': True})
        else:
            return self.render_json_response({'error': True})


