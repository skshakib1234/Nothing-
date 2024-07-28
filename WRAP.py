import urllib.request,json,datetime,random,string,time,os,sys
from rich.markdown import Markdown
from rich.console import Console
from rich import print
from os import system as MD
console = Console()
MD("clear")
console.print("""[blink white]
  ┏┓┳┳┳┓┓┏
  ┣ ┃┃┣┫┗┫
  ┻ ┗┛┛┗┗┛
 [blink green]╭───────────────────────╮
 [blink green]│[blink white] TOOL NAME [blink green]:[blink white] FURY     [blink green] │
 [blink green]│[blink white]   OWNER   [blink green]:[blink white] MD SHAKIB [blink green]│ 
 [blink green]│[blink white]  GIT-HUB  [blink green]:[blink white] SHAKIB-71 [blink green]│
 [blink green]╰───────────────────────╯               
""",style="bold")
referrer  = console.input("  [blink white]WRAP ID [blink green]:[blink white] ")
console.print("[bright_white]━"*50)

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print("")		    
def digitString(stringLength):
	try:
		return ''.join((random.choice(string.digits) for i in range(stringLength)))    
	except Exception as error:
	  print("")
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print("")

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g += 1
		print(f"  YOU HAVE EARNED {g} GB DATA")
		for i in range(10,0,-1):
#			sys.stdout.write(f"\r  WAIT {i} SECOND")
	#		sys.stdout.flush()
		  time.sleep(1)
	else:
		b += 1
		print(f"  REQUESTS ARE FAILD")
		for i in range(10,0,-1):
	#		sys.stdout.write(f"\r  WAIT {i} SECOND")
		#	sys.stdout.flush()
			time.sleep(1)