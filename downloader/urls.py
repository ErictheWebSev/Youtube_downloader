from django.urls import path
from .views import index, download_video

urlpatterns = [
	path('', index, name = 'home'),
	path('download/', download_video, name = 'download')
]