import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'msg_moive'
sheet['A1'] = '评分'
sheet['B1'] = '电影名称'
sheet['C1'] = '推荐句子'
sheet['D1'] = '观看网址'
headers = {
    'Referer': 'https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-4830389020085397&output=html&h=250&slotname=1983604743&adk=2656724884&adf=367891091&w=300&lmt=1584963541&psa=1&guci=2.2.0.0.2.2.0.0&format=300x250&url=https%3A%2F%2Fmovie.douban.com%2Ftop250&flash=27.0.0&wgl=1&dt=1584963541101&bpp=44&bdt=3030&fdt=143&idt=144&shv=r20200316&cbv=r20190131&ptt=9&saldr=aa&abxe=1&cookie=ID%3D071eabe8c1be0d7a%3AT%3D1584153564%3AS%3DALNI_MbAh6pQhsww8kZUrSOzDgNePnjxqA&crv=1&correlator=4477976426812&frm=20&pv=2&ga_vid=1375321358.1584153565&ga_sid=1584963539&ga_hid=502445164&ga_fc=1&iag=0&icsg=2147491968&dssz=29&mdo=0&mso=0&u_tz=480&u_his=1&u_java=0&u_h=1080&u_w=1920&u_ah=1030&u_aw=1920&u_cd=24&u_nplug=15&u_nmime=25&adx=1170&ady=328&biw=1899&bih=915&scr_x=0&scr_y=0&eid=42530291%2C42530312%2C332260030%2C332260040&oid=3&pvsid=2270337163678529&pem=228&ref=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D8l0aI7KtOulD1ONnj4Z0uBaCAZuK2OWewO_A7dYwVTiUZ3psCiHmiFvcLuKLSPRP%26wd%3D%26eqid%3Dbd9e243f0004d8d0000000065e789fce&rx=0&eae=0&fc=896&brdim=0%2C88%2C0%2C88%2C1920%2C0%2C1920%2C915%2C1920%2C915&vis=1&rsz=%7C%7CoeE%7C&abl=CS&pfx=0&fu=24&bc=29&ifi=1&uci=a!1&xpc=GRDhglCNLU&p=https%3A//movie.douban.com&dtd=208',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
for n in range(9):
    url = 'https://movie.douban.com/top250?start=' + str(25 * n) + '&filter='
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    for titles in soup.find_all(class_="info"):
        num = titles.find('span', class_="rating_num").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span', class_="inq").text
        url_movie = titles.find('a')['href']
        sheet.append([num, title, comment, url_movie]

        wb.save('movie.xlsx')