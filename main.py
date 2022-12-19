import requests
import json
from lxml import etree
url = "https://play.google.com/_/PlayStoreUi/data/batchexecute?rpcids=teXCtc&source-path=/store/games&f.sid=7117283802506478010&bl=boq_playuiserver_20221213.07_p3&hl=ru&gl=US&authuser=0&soc-app=121&soc-platform=1&soc-device=2&_reqid=2302788&rt=c"
freq = '[[["teXCtc","[null,[\\"cat\\"],[10],[2,1],4]",null,"generic"]]]'



response = requests.post(url, data={"f.req": freq},
                         headers={'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'})


print(json.loads(response.text[10:-28])[0][2])

