
import requests
import time
import sqlite3
import random

page = 1
citycode = 681
empcode = None
empcode1 = [100000000]
#

def get_store():

        
        
    for x in empcode1:
        empcode = x
        page = 0
    

        for i in range(1, 35):

        
            url ='https://xiaoyuan.zhaopin.com/api/sou?S_SOU_FULL_INDEX=&S_SOU_POSITION_SOURCE_TYPE=&pageIndex='+str(page)+'&S_SOU_POSITION_TYPE=2&S_SOU_WORK_CITY='+str(citycode)+'&S_SOU_JD_INDUSTRY_LEVEL=' +str(empcode)+ '&S_SOU_COMPANY_TYPE=&S_SOU_REFRESH_DATE=&order=12&pageSize=30&at=eaebb746d4c547739c430010bab05264&rt=28fd4c000b3b45968d69087c7af219b7&_v=0.66343928'

            data = requests.get(url=url).json()


            if data["data"]["data"] == None:
                print("职业：",empcode,"已无数据，即将进入下一职业爬取")
                continue
            else:

                for i in data["data"]["data"]["list"]:
                    name = i["name"]
                    education = i["education"]
                    salary60 = i["salary60"]
                    workCity = i["workCity"]
                    companyId = i["companyId"]
                    companyName = i["companyName"]
                    con = sqlite3.connect('empdata.db')
                    cur = con.cursor()
        
                    cur.execute("SELECT * FROM employ WHERE name = ? AND companyId = ?", (name, companyId))
                    if cur.fetchone():
                        continue
                    else:
                        if salary60[-1] == "议" or salary60[-1] == "下":             
                            continue
                        else:
                            salaryMin = salary60.split('-')[0]
                            if salaryMin.find("万") != -1:
                                salaryMin = salaryMin.replace("万", "")
                                salaryMin = int(float(salaryMin)) * 10000
                            elif salaryMin.find("千") != -1:
                                salaryMin = salaryMin.replace("千", "")
                                salaryMin = int(float(salaryMin)) * 1000
    
                            salaryMax = salary60.split('-')[1]
                            if salaryMax.find("万") != -1:
                                salaryMax = salaryMax.replace("万", "")
                                salaryMax = int(float(salaryMax)) * 10000
                            elif salaryMax.find("千") != -1:
                                salaryMax = salaryMax.replace("千", "")
                                salaryMax = int(float(salaryMax)) * 1000
 
                            cur.execute(
                            "INSERT INTO employ(name,education,salaryMax,salaryMin,companyName,companyId,empcode,workCity) VALUES(?,?,?,?,?,?,?,?)", (name,education,salaryMax,salaryMin,companyName,companyId,empcode,workCity))
                        con.commit()
                        con.close()

                        print(name,education,salaryMax,salaryMin,companyName,companyId,empcode,workCity)

                page += 1
            
                print("第" +str(page)+ "页数据处理结束") 

                time.sleep(random.randint(5, 8))

        print("城市代码：",citycode,"职位代码：",empcode,"已结束")

try:
    get_store()

except Exception as e:
    time.sleep(60)
    get_store()
