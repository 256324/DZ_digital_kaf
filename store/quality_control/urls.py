from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name ='main'),
    path('bugs/', views.BugsListView.as_view(), name='bug_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('bugs/new/', views.BugReportCreateView.as_view(), name='create_bugreport'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bugs'),
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug'),
    path('features/', views.FeatureListView.as_view(), name='feature_list'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('features/new/', views.FeatureRequestCreateView.as_view(), name='create_featurerequest'),
    path('features/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_features'),
    path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature'),
]