from bs4 import BeautifulSoup
import requests
import urls

url_marketindex = "https://finance.naver.com/marketindex/"
html = requests.get(url_marketindex).text
soup = BeautifulSoup(html, 'html.parser')



ifrSel = "iframe#frame_ex1"
ifr = soup.select_one(ifrSel)
src = ifr.get('src')

orgUrl = urls.urljoin( urls.getHostname(url_marketindex, True), src )
# print(orgUrl)

orgHtml = requests.get(orgUrl).text
orgSoup = BeautifulSoup(orgHtml, 'html.parser')
# print(orgHtml)

# divSel = "div.tbl_area tbody td.tit a"
# divEles = orgSoup.select(divSel)
# print(divEles)

# table = orgSoup.html.tbody
# print(table)

# tr = table.tr

# print(trt)
# print(tr)


trs = orgSoup.select('tr')


for tr in trs:
    tds = tr.select('td')
    if len(tds) < 4: continue
    country = tds[0].text.strip()
    when_buy = tds[2].text.strip()
    when_sale = tds[3].text.strip()
    diff = float(tds[2].text.replace(',', '')) - float(tds[3].text.replace(',', ''))
    print("국가 >> ", country, "살 때 환율 : ", when_buy,"원  ", "팔 때 환율 : ", when_sale, "원", "  차액 : ", diff)

# for i in container:
#     td = i.get('td')
#     print("td >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n", td)

# print("td1 >>>>>>>>>>>>>>>>>", td1)
# print("td2 >>>>>>>>>>>>>>>>>", td2)


