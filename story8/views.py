from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
# Create your views here.
def story8(request):
    return render(request, 'story8/story8.html')

def perantara(request):
    url = "https://www.googleapis.com/books/v1/volumes?q=" + request.GET.get('q', 'a')
    #print(url)
    ret = requests.get(url)
    #print(ret.content)
    data = json.loads(ret.content)
    #data = { ' woi' : 'keren', 'haha' : 'mantap'}
    return JsonResponse(data, safe=False)

