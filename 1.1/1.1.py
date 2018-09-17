
import json

import requests

import time
url='https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
for pn in range(1,31):
#json 数据
    dat={'first':'false',
         'pn':pn,
         'kd':'python'}
    header={


            'Referer': 'https://www.lagou.com/jobs/list_Python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'

    }
    time.sleep(2)
    html=requests.post(url,headers=header,data=dat)

    jsonData=(html.json()['content']['positionResult']['result'])
    for item in  jsonData:
        print(item['companyFullName'])
        print(item['salary'])

    with open('laGou.json','a',encoding='UTF-8') as fp:
        salary=json.dumps(item,ensure_ascii=False) +'\n'
        fp.write(salary)