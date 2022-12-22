from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from google_play_scraper import app, Sort, reviews


def home(request):
    if request.method == "POST":
        text = request.POST.get('Words')
        country = request.POST.get('Country')
        language = request.POST.get('Language')
        url = f"https://play.google.com/_/PlayStoreUi/data/batchexecute?rpcids=teXCtc&source-path=/store/games&f.sid=5861500990064321268&bl=boq_playuiserver_20221213.07_p3&hl={country}&gl={language}&authuser=0&soc-app=121&soc-platform=1&soc-device=1&_reqid=1245746&rt=c"
        freq = f"[[[\"teXCtc\",\"[null,[\\\"{text}\\\"],[10],[2,1],4]\",null,\"generic\"]]]"
        at = "AA6vXhQRjMn3RbH6VDEvuFBUWIZ8:1671702133506"
        response = requests.post(url, data={"f.req": freq,
                                            'at': at},
                                 headers={'Accept': '*/*',
                                          'Accept-Encoding': 'gzip, deflate, br',
                                          'Accept-Language': 'en-US,en;q=0.5',
                                          'Connection': 'keep-alive',
                                          'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                                          'Host': 'play.google.com',
                                          'Origin': 'https://play.google.com',
                                          'Referer': 'https://play.google.com/',
                                          'Sec-Fetch-Dest': 'empty',
                                          'Sec-Fetch-Mode': 'cors',
                                          'Sec-Fetch-Site': 'same-origin',
                                          'TE': 'trailers',
                                          'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv: 107.0) Gecko / 20100101Firefox / 107.0',
                                          'X-Same-Domain': '1'})
        decode = response.text[11:-28]
        list_of_keys = list()
        for i in json.loads(json.loads(decode)[0][2])[0]:
            list_of_keys.append(i[0])
        return HttpResponse(';  '.join(list_of_keys))
    return render(request, template_name='landing/index.html')


def app_info(request):
    const_link_app = 'https://play.google.com/store/apps/details?id=com.domobile.pixelfunv2&hl=ru&gl=US'
    app_id = const_link_app[46:-12]
    lang = 'en'
    country = 'us'
    result, continuation_token = reviews(
        app_id,
        lang='en',  # defaults to 'en'
        country='us',  # defaults to 'us'
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.NEWEST
        count=3,  # defaults to 100
    )
    context = {"result": result}
    return render(request, template_name='landing/app_info.html', context=context)
