import requests
headers = {
'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
}
url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'
datas = requests.get(url, headers=headers).json() 
print(datas)