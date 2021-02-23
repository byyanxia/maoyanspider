# -*- coding = utf-8 -*-
# @Time :2021-02-23 10.10
# @Author: YanXia
# @File : maoyan.py
# @Software: PyCharm
import requests,json,schedule,time
from lxml import etree
def save():
    url = "http://piaofang.maoyan.com/box-office?ver=normal"
    r = requests.get(url, headers=headers, timeout=1).content.decode('utf-8')
    soup = etree.HTML(r)
    name = soup.xpath('//div[@class="name-wrap"]/p[@class="movie-name"]/text()')
    pf = soup.xpath('//td[@class="tbody-col"]/div[@class="boxDesc-wrap red-color"]/text()')
    file = open("maoyan10.html", 'w+').close()
    for  i,ii in zip(name, pf):
        a=i+'的综合票房'+ii
        file = open("maoyan10.html", "a+",encoding='utf-8')
        file.write(a+"万  \n")
        file.close()
def post():
    localtime = time.asctime(time.localtime(time.time()))
    url_3 = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=填AgentId&corpsecret=填Secret"
    r = requests.get(url_3, headers=headers, timeout=1).content.decode('utf-8')
    r = json.loads(r)  # 将json格式数据转换为字典
    token = r["access_token"]
    url_2 = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token
    f = open('maoyan10.html','r',encoding='utf-8')
    a=f.read()
    data={
   "touser" : "@all",
   "toparty" : "@all",
   "totag" : "@all",
   "msgtype" : "textcard",
   "agentid" : '1000002',
   "textcard" : {
            "title" : "实时电影票房数据",
            "description" : a,
            "url" : "URL",
                        "btntxt":"更多"
   },
   "enable_id_trans": 0,
   "enable_duplicate_check": 0,
   "duplicate_check_interval": 1800
}
    send = (bytes(json.dumps(data), 'utf-8'))
    r = requests.post(url=url_2, data=send, headers=headers).text
    print("----------------------------")
    print('现在是'+localtime)
    print(r)
    print("----------------------------")
if __name__ == '__main__':
    print("""
      _  __          _  __
     | |/,'_   _    | |/,'() _
     | ,','o| / \/7 /  / /7,'o|
    /_/  |_,7/_n_/,'_n_\// |_,7
                      QQ:210246020         
                              """)
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    schedule.every(1).hours.do(save)
    schedule.every(1).hours.do(post)
    save()
    post()
    while True:
       schedule.run_pending()
       time.sleep(1)
