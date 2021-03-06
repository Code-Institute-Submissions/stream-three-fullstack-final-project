from django.conf.urls import url
from .views import manage_jobs, delete_job

urlpatterns = [
    
    url(r'^manage_jobs/(?P<username>[\w.@+-]+)$', manage_jobs, name='manage_jobs'),
    url(r'^manage_jobs/(?P<username>[\w.@+-]+)/(?P<job_id>\d+)/delete$', delete_job, name='delete_job'),

]
