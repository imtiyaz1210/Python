import requests
from bs4 import BeautifulSoup as bs
import lxml
import openpyxl
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Jobs_Filter"
sheet.append(["Company Name","Skills Req","Job Link"])

try:
    source=requests.get("https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=Python&pDate=I&sequence=2&startPage=1")
    source.raise_for_status()
    soup=bs(source.content,"lxml")
    jobs=soup.find_all("li",class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        postdate=job.find("span",class_="sim-posted").text
        if "few" in postdate:
            cname=job.find("header",class_="clearfix").h3.text
            skills=job.find("span",class_="srp-skills").text.replace(" ","")
            link=job.find("ul",class_="list-job-dtl clearfix").a["href"]
            print(f"Company Name:{cname.strip()}")
            print(f"Skills Requirests:{skills.strip()}")
            print(f"More Info:{link}")
            print()
            sheet.append([cname,skills,link])
except Exception as e:
    print(e)

excel.save("Job_satatus.xlsx")


