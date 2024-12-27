import base64
import os
import re
import time
import urllib
import requests
from urllib.parse import quote
import hashlib

def song_download(song_id):
    params = {'resourceType': '2', 'songId': song_id, 'toneFlag': 'PQ'}
    headers = {'user-agent': 'Mozilla/5.0 (Linux; U; Android 10; zh-cn; VOG-AL00 Build/HUAWEIVOG-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1','cookie': 'mg_uem_user_id_9fbe6599400e43a4a58700a822fd57f8=6c2e05c1-61b7-43e9-a213-e4c0d4a39a52; cookieId=1nnnbwcVIo6_WioVFkFZTQ5GdHXZ5d71704960524955; Hm_lvt_ec5a5474d9d871cb3d82b846d861979d=1704970103; migu_cookie_id=7cfda67e-1596-412b-859b-dfc560ce7111-n41706335511303; WT_FPC=id=287c4dad9807a44c7d91704960497228:lv=1706941020784:ss=1706941020784; idmpauth=true@passport.migu.cn; migu_music_status=true; migu_music_uid=91934470118; migu_music_avatar=; migu_music_nickname=%E5%92%AA%E5%92%95%E7%94%A8%E6%88%B7; migu_music_level=0; migu_music_credit_level=1; migu_music_platinum=0; migu_music_msisdn=GM01YTwX6LiciZ%2B2vPrMWg%3D%3D; migu_music_email=; migu_music_passid=338951407672556446; migu_music_sid=s%3AovhSa2zi4nlPujOG8LmIu59b_6bVEMSd.9LoLY9UndQ8PLO8zGsax%2BhQoLOYUQ5W7EC2myCVzs0U; WT_FPC=id=287c4dad9807a44c7d91704960497228:lv=1706960274622:ss=1706960274622','channel': '0146951'}
    res = requests.get(base64.b64decode(urllib.parse.unquote('aHR0cHM6Ly9hcHAuYy5uZi5taWd1LmNuL01JR1VNMi4wL3N0cmF0ZWd5L2xpc3Rlbi11cmwvdjIuNA%3D%3D')).decode('UTF-8'), headers=headers, params=params)
    song_url = re.findall('"url":"(.*?)","audioFormatType"', res.text)[0]
    song_name = re.findall('"songName":"(.*?)"', res.text)[0]
    song_author = re.findall('"name":"(.*?)","img":"', res.text)[0]
    res = requests.get(song_url)
    open(f'music/{song_name}-{song_author}.mp3', 'wb').write(res.content)
    print(f'Download completed. Enjoy it. \n\n')

# 创建文件夹
if not os.path.exists('music'):
    os.mkdir('music')

# 请求头
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0','cookie': 'mg_uem_user_id_9fbe6599400e43a4a58700a822fd57f8=6c2e05c1-61b7-43e9-a213-e4c0d4a39a52; cookieId=1nnnbwcVIo6_WioVFkFZTQ5GdHXZ5d71704960524955; Hm_lvt_ec5a5474d9d871cb3d82b846d861979d=1704970103; migu_cookie_id=7cfda67e-1596-412b-859b-dfc560ce7111-n41706335511303; WT_FPC=id=287c4dad9807a44c7d91704960497228:lv=1706941020784:ss=1706941020784; idmpauth=true@passport.migu.cn; migu_music_status=true; migu_music_uid=91934470118; migu_music_avatar=; migu_music_nickname=%E5%92%AA%E5%92%95%E7%94%A8%E6%88%B7; migu_music_level=0; migu_music_credit_level=1; migu_music_platinum=0; migu_music_msisdn=GM01YTwX6LiciZ%2B2vPrMWg%3D%3D; migu_music_email=; migu_music_passid=338951407672556446; migu_music_sid=s%3AovhSa2zi4nlPujOG8LmIu59b_6bVEMSd.9LoLY9UndQ8PLO8zGsax%2BhQoLOYUQ5W7EC2myCVzs0U; WT_FPC=id=287c4dad9807a44c7d91704960497228:lv=1706960274622:ss=1706960274622'}

while True:
    print(f'Enjoy it.')
    song_name = input('Please input the song name:')
    keyword = quote(song_name)
    cookie_id = re.findall('migu_cookie_id=(.*?);', headers['cookie'])[0]
    time_s = str(int(time.time()))
    user_agent = headers['user-agent']
    string = f'c001002Afhtmlk{cookie_id}keyword{keyword}s{time_s}u{user_agent}/220001v3.25.6'
    url_string = quote(string, safe='~()*!.\'')
    hash_i = hashlib.sha1(url_string.encode()).hexdigest()
    url = f'https://music.migu.cn/v3/search?page=1&type=song&i={hash_i}&f=html&s={time_s}&c=001002A&keyword={keyword}&v=3.25.6'
    res = requests.get(url,headers=headers)
    titles = re.findall('"title":"(.*?)",', res.text)
    song_ids = re.findall('data-mids="(.*?)"', res.text)
    singers = re.findall('"singer":"(.*?)",', res.text)
    for i in range(len(titles)):
        print(i+1, titles[i], singers[i], )
    index = int(input('Please input the sequence number (input 0 to return):'))
    if index == 0:
        continue
    song_download(song_ids[index-1])

