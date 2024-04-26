from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import DetailView

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = (f"<h1>Система контроля качества</h1>"
            f"<a href='{ bug_list_url}'>Список всех багов<br></a>"
            f"<a href='{ feature_list_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)
class IndexView(View):
    def get(self):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = (f"<h1>Система контроля качества</h1>"
                f"<a href='{bug_list_url}'>Список всех багов<br></a>"
                f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
        return HttpResponse(html)



def bug_list(request):
    bug = BugReport.objects.all()
    bug_html = '<h1>Cписок отчетов об ошибках</h1><ul>'
    for bug in bug:
        bug_html += f'<li><a href="{bug.id}/">{bug.title}</a> status:{bug.status}</li>'
    bug_html +='</ul>'
    return HttpResponse(bug_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = (f'<h1>{bug.title}</h1><p>description: {bug.description} <br>'
                         f'status: {bug.status} <br>'
                         f'priority: {bug.priority} <br>'
                         f'project: {bug.project} <br>'
                         f'task: {bug.task}</p>')
        return HttpResponse(response_html)





def feature_list(request):
    feature = FeatureRequest.objects.all()
    feature_html = '<h1>Cписок отчетов об ошибках</h1><ul>'
    for feature in feature:
        feature_html += f'<li><a href="{feature.id}/">{feature.title}</a> status:{feature.status}</li>'
    feature_html +='</ul>'
    return HttpResponse(feature_html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = (f'<h1>{feature.title}</h1><p>description: {feature.description} <br>'
                         f'status: {feature.status} <br>'
                         f'priority: {feature.priority} <br>'
                         f'project: {feature.project} <br>'
                         f'task: {feature.task}</p>')
        return HttpResponse(response_html)



