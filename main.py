#!/usr/bin/python3
# __author__ = __mrblackx__

import os
import sys
import base64
import ast 

try:
	import requests
except:
	print(f"\033[34m[\033[31mERROR\033[34m] \033[37mInstalling module requests\033[0m")
	if sys.platform == "linux":
		os.system("pip3 install requests")
	elif sys.platform == "windows":
		os.system("py -m pip install requests")
try:
	from user_agent import generate_user_agent
except:
	print(f"\033[34m[\033[31mERROR\033[34m] \033[37mInstalling module user_agent\033[0m")
	if sys.platform == "linux":
		os.system("pip3 install user_agent")
	elif sys.platform == "windows":
		os.system("py -m pip install user_agent")

x = 0
banner = """
      \033[34m██╗  ██╗████████╗██████╗  \033[35;1m    ██████╗ ██████╗ ██████╗ ███████╗\033[0m                
      \033[34m██║  ██║╚══██╔══╝██╔══██╗ \033[35;1m   ██╔════╝██╔═══██╗██╔══██╗██╔════╝\033[0m                
      \033[34m███████║   ██║   ██████╔╝ \033[35;1m   ██║     ██║   ██║██║  ██║█████╗\033[0m                  
      \033[34m██╔══██║   ██║   ██╔══██╗ \033[35;1m   ██║     ██║   ██║██║  ██║██╔══╝\033[0m                  
      \033[34m██║  ██║   ██║   ██████╔╝ \033[35;1m   ╚██████╗╚██████╔╝██████╔╝███████╗\033[0m                
      \033[34m╚═╝  ╚═╝   ╚═╝   ╚═════╝  \033[35;1m    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝\033[0m                
         \033[37m                                                                    
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                           \033[31;1;5m@ M R B L A C K X\033[0m 
                         \033[31;1;4mhttps://t.me/viperzcrew\033[0m 

                \033[0m                                                             
"""

def runner():
	useragent = generate_user_agent()
	data = {''}
	headers = f"'User-Agent': '{useragent}','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','DNT': '1','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Pragma': 'no-cache','Cache-Control': 'no-cache','TE': 'Trailers'"
	headers = ast.literal_eval("{"+headers+"}")
	response = requests.post('https://www.hackthebox.eu/api/invite/generate', headers=headers).text
	code = response.split(",")[1].split('"')[5]
	real = base64.b64decode(code).decode("utf-8")
	return real

def save(filename, content):
	temp = open(filename, "a+")
	temp.write(content)
	temp.close()

def clear():
	if sys.platform == "linux":
		os.system('clear')
	elif sys.platform == "windows":
		os.system('cls')
	else:
		os.system('clear||cls')


clear()
print(banner)
y = int(input("\033[34m[\033[32mCOUNT OF CODES\033[34m]:\033[37m "))

while x != y:
	x += 1
	code = runner()
	print(f"\033[34m[\033[32mGENERATED\033[34m] \033[37m-+- \033[35m{code} \033[37m-+-\033[0m")
	save("HackTheBox-Codes.txt", f"<(🔥)======[ I N V I T E | C O D E ======(🔥)>\n\t{code}\n")
	