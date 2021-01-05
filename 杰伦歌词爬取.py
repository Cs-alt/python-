import requests
import html
url1='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
url='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
for i in range(5):
    param = {
'ct':'24',
'qqmusic_ver': '1298',
'new_json':'1',
'remoteplace':'sizer.yqq.song_next',
'searchid':'64405487069162918',
't':'0',
'aggr':'1',
'cr':'1',
'catZhida':'1',
'lossless':'0',
'flag_qc':'0',
'p':str(i),
'n':'20',
'w':'周杰伦',
'g_tk':'5381',
'loginUin':'0',
'hostUin':'0',
'format':'json',
'inCharset':'utf8',
'outCharset':'utf-8',
'notice':'0',
'platform':'yqq.json',
'needNewCode':'0'
}
    headers={
    'origin':'https://y.qq.com',
    'referer':'https://y.qq.com/portal/search.html',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
        }
    res=requests.get(url1,headers=headers,params=param)
    music=res.json()
    for n in range(9):
        id=music['data']['zhida']['zhida_singer']['hotsong'][n]['songID']
        params={
'nobase64':'1',
'musicid':id,
'-':'jsonp1',
'g_tk_new_20200303':'5381',
'g_tk':'5381',
'loginUin':'0',
'hostUin':'0',
'format':'json',
'inCharset':'utf8',
'outCharset':'utf-8',
'notice':'0',
'platform':'yqq.json',
'needNewCode':'0',
            }
        music_res=requests.get(url,headers=headers,params=params)
        json_music = music_res.json()
        print(html.unescape(json_music['lyric']))
