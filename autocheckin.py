import requests
import json

base_url = ''

def checkin():
    '机场签到'
    email = ''
    password = ''

    email = email.split('@')
    email = email[0] + '%40' + email[1]
    session = requests.session()
    session.get(base_url, verify=False)
    login_url = base_url + '/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'email=' + email + '&passwd=' + password + '&code='
    post_data = post_data.encode()
    response = session.post(login_url, post_data, headers=headers, verify=False)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': base_url + '/user'
    }
    response = session.post(base_url + '/user/checkin', headers=headers, verify=False)
    '微信推送'
    c=response.text
    url='the url of pushplus'
    data={'token':'the token of your pushplus','title':'机场签到','content':'可用流量'+c['trafficInfo']['unUsedTraffic'],'template':'html'}
    requests.post(headers=headers,url=url,data=json.dumps(data),timeout=10)

checkin()
