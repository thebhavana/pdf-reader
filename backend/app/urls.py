from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('upload-pdf/', views.UploadPDF.as_view(), name='upload-pdf'),
    path('query/', views.QueryView.as_view(), name='query'),

    # Catch-all to serve React frontend for any other URL
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
