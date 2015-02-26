import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from portfolio.models import Timeline, Skill, Education, Interest
from .forms import ContactForm


class IndexView(TemplateView):

    template_name = 'main/index.html'
    context = {}

    def get(self, *args, **kwargs):
        # Get timeline data
        timeline = Timeline.objects.all().order_by('-position')
        self.context['timeline'] = timeline
        # Skillset
        self.context['skills'] = Skill.objects.all()
        # Education
        self.context['education'] = Education.objects.all().order_by('-id')
        # Interests
        self.context['interests'] = Interest.objects.all()

        return render(self.request, self.template_name, self.context)


class ResumeView(TemplateView):

    template_name = 'main/resume.html'
    context = {}

    def get(self, *args, **kwargs):
        # Work experience
        self.context['timeline'] = Timeline.objects.all().order_by('-position')
        # Skillset
        self.context['skills'] = Skill.objects.all()
        # Education
        self.context['education'] = Education.objects.all().order_by('-id')
        # Interests
        self.context['interests'] = Interest.objects.all()

        return render(self.request, self.template_name, self.context)


class ContactView(TemplateView):

    template_name = 'main/partials/contact_form.html'
    context = {}

    def get(self, *args, **kwargs):
        self.context['form'] = ContactForm()
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        data = self.request.POST
        form = ContactForm(data)

        if form.is_valid():
            form.save()
            # Send message
            self.send_message(data)

            result = json.dumps({'email_sent': True})
            return HttpResponse(result, content_type='application/json')
        else:
            # Form has errors
            self.context['form'] = form
            return render(self.request, self.template_name, self.context)

    def send_message(self, data):
        subject = "[TOMOMOI]: " + data['name']
        sent_by = data['email']

        send_mail(subject, data['content'], sent_by, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)
