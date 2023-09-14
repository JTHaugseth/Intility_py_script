import requests

url = "https://intility-games.intility.com/?index=&_data=routes%2Findex"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Cookie": "0aa7c04a1fc67e44b16a9339e97f7026=ba633d7942c6b5ee3a50dc2deb387f6d",  
    "Host": "intility-games.intility.com",
    "Origin": "https://intility-games.intility.com",
    "Pragma": "no-cache",
    "Referer": "https://intility-games.intility.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
}

payload = {
    "name": "Julian Haugseth",
    "number": "40087795",
    "score": 6969696969696969,
    "school": "HØyskolen Kristiania",
}

response = requests.post(url, headers=headers, data=payload)

print(response.status_code)
print(response.text)