from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')
def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bug_list': bugs})

class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'



def feature_list(request):
    feature = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': feature})

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'



