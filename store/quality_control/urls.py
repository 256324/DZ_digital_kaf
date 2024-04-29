from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name ='main'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('bugs/new/', views.create_bugreport, name='create_bugreport'),
    path('features/', views.feature_list, name='feature_list'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('features/new/', views.create_featurerequest, name='create_featurerequest'),
]