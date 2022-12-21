from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from google_play_scraper import app


def home(request):
    if request.method == "POST":
        text = request.POST.get('Words')
        country = request.POST.get('Country')
        language = request.POST.get('Language')
        url = f"https://play.google.com/_/PlayStoreUi/data/batchexecute?rpcids=teXCtc&source-path=/store/games&f.sid=7117283802506478010&bl=boq_playuiserver_20221213.07_p3&hl={country}&gl={language}&authuser=0&soc-app=121&soc-platform=1&soc-device=2&_reqid=2302788&rt=c"
        freq = f'[[["teXCtc","[null,[\\"{text}\\"],[10],[2,1],4]",null,"generic"]]]'
        response = requests.post(url, data={"f.req": freq},
                                 headers={'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'})
        decode = response.text[11:-28]
        list_of_keys = list()
        for i in json.loads(json.loads(decode)[0][2])[0]:
            list_of_keys.append(i[0])
        return HttpResponse(';  '.join(list_of_keys))
    return render(request, template_name='landing/index.html')


def app_info(request):
    const_link_app = 'https://play.google.com/store/apps/details?id=com.gofieldguide&hl=ru&gl=US'
    app_id = const_link_app[46:-12]
    lang = 'en'
    country = 'us'
    return render(request, template_name='landing/app_info.html')
