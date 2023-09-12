
from django.shortcuts import render
from django.http import JsonResponse
from pytube import YouTube
import os

def index(request):
    return render(request, 'downloader.html')

def download_video(request):
    if request.method == 'POST':
        vid_url = request.POST.get('video_url')
        try:
            yt = YouTube(vid_url)
            stream = yt.streams.get_highest_resolution()
            download_path = 'storage/emulated/0/Videos'
            os.makedirs(download_path, exist_ok=True)
            stream.download(download_path)
            video_title = yt.title
            file_path = os.path.join(download_path, video_title + '.mp4')

            response = {
                'message': 'Video Downloaded',
                'file_path': file_path,
            }
        except Exception as e:
            response = {
                'error': str(e)
            }
        return JsonResponse(response)
    return JsonResponse({'error': 'Invalid request'})
    