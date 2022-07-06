import datetime

import requests
from bs4 import BeautifulSoup

courses = ["CSE3001", "CSE2006"]  # add list of courses required


config = {
    "Cookie": "",  # dev tools > request headers
    "_csrf": "",  # dev tools > payload
    "authorizedID": "",  # registration number
    "x": datetime.datetime.now(datetime.timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    ),
}

payload = {
    "_csrf": config["_csrf"],
    "courseCode": "CSE2006",
    "authorizedID": config["authorizedID"],
    "x": config["x"],
}

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "116",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": config["Cookie"],
    "DNT": "1",
    "Host": "vtop.vit.ac.in",
    "Origin": "https://vtop.vit.ac.in",
    "Referer": "https://vtop.vit.ac.in/vtop/content",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

url = "https://vtop.vit.ac.in/vtop/academics/common/getCoursesDetailForRegistration"

for i in courses:
    print(f"\n{i}:\n")
    payload["courseCode"] = i
    r = requests.post(url, data=payload, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    s = soup.select("#courseDetailFragement > div > table > tr > td > span")

    for i in range(0, len(s), 4):
        print(s[i].text, s[i + 1].text, s[i + 2].text, s[i + 3].text, sep=",")
