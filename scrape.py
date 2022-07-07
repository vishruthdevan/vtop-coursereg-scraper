import datetime

import requests
from bs4 import BeautifulSoup

# courses = ["CSE3001", "CSE2006"]  # add list of courses required 
courses = []

config = {
    "Cookie": "loginUserType=vtopuser; JSESSIONID=411C8D6F7969D6333A259CF437C88150; SERVERID=s1",  # dev tools > request headers
    "_csrf": "7ca9b002-e770-448c-a295-c0f849f90bfb",  # dev tools > payload
    "authorizedID": "20BDS0190",  # registration number
    "x": datetime.datetime.now(datetime.timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    ),
}

payload = {
    "_csrf": config["_csrf"],
    "courseCode": "",
    "authorizedID": config["authorizedID"],
    "x": config["x"],
    "cccategory": "",
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

if len(courses) == 0:
    url = "https://vtop.vit.ac.in/vtop/academics/common/StudentRegistrationScheduleAllocation"

    # payload["verifyMenu"] = True
    r = requests.post(url, data=payload, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    # get element with id curriculumCategory
    curriculumCategory = soup.find("select", id="curriculumCategory")
    # get all options from curriculumCategory
    options = curriculumCategory.find_all("option")
    x = [i.get("value") for i in options][1:]
    print(x)

    url = "https://vtop.vit.ac.in/vtop/academics/common/getCoursesListForCurriculmCategory"

    courses = []
    subject_name = []
    for i in x:
        payload["cccategory"] = i
        r = requests.post(url, data=payload, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        ## extract value of options
        options = soup.find_all("option")
        for option in options:
            if option.get("value") != "":
                courses.append(option.get("value"))
                subject_name.append(option.text)


url = "https://vtop.vit.ac.in/vtop/academics/common/getCoursesDetailForRegistration"

for j in range(len(courses)):
    
    # print(f"\n{j}:\n")
    payload["courseCode"] = courses[j]
    r = requests.post(url, data=payload, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    s = soup.select("#courseDetailFragement > div > table > tr > td > span")

    for i in range(0, len(s), 4):
        #write to csv
        if subject_name == "":
            with open("courses.csv", "a") as f:
                f.write(f"{courses[j]},{s[i].text},{s[i+1].text},{s[i+2].text},{s[i+3].text}\n")
        else:
            with open("courses.csv", "a") as f:
                f.write(f"{courses[j]},{subject_name[j]},{s[i].text},{s[i+1].text},{s[i+2].text},{s[i+3].text}\n")
        
