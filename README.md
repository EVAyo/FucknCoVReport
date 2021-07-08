# FucknCoVReport
An automatic python script for CUGB's COVID-19 report  
中国地质大学（北京）疫情期间每日自动进行健康打卡上报  
***免责声明（Disclaimer）：使用该脚本而可能引起的法律责任和学校追究等责任由使用者个人承担，与开发者无关，请勿滥用。为了您和他人的健康着想，请如实填写信息，在有位置变动和情况变化时手动填写申报！***
## UPDATES
### **2021/07/08 - The latest version resolved:**
- Be adapted to the new feature that needs to fill the blank in manually.
### **2021/01/24 - This update version resolved:**
- Be adapted to the new CAS certification and middle/high risk regions
### **~~2020/10/03 - This update version resolved:~~**
- ~~Add new capabilities related to school-leaving~~
### **~~2020/08/25 - The upcoming update version will resolve:~~**  
- ~~In the upcoming campus life, the university will take the MAE (Morning, Afteroon and Evening) clock-in measures.~~
- ~~Epidemic prevention should not torment students and the other ordinary people and formalism does harm.~~  
### **2020/08/14 - This update version resolved:**  
- A new feature for the site that uses base64 encoding for the username and password, and uses token.
- Fixed some bugs.
## REQUIREMENTS
pip install requests
## USER MANNUL (Updated on 2021/07/08)
### Modify
>main.py:  
>>  
>>line 16:  ```self.uname = ''  # Your Student Number, e.g. 2001200001```  
>>line 17:  ```self.upwd = ''  # Last 6 numbers of your ID card, e.g. 123456 (or the password which is set by yourself)```  
>>**For example:  
>>'200120000X' (Your Student Number), '123456' (The Last Six Number of Your ID Card)**  
>>  
>>line 81:  ```"location_longitude":"123.123123", "location_latitude":"45.45454","location_address":"XX省XX市XX街道XX小区"}'''```  
>>**Notice:  
>>The value of "location_longitude" should be like "123.123123", and the value of "location_latitude" should be like "32.32132".In addtion, the two values should be matched with the value of "location_address".**
>>  
### Run
WINDOWS:  ```python main.py```

Linux:  ```python3 main.py``` or ***(Recommend)*** set a crontab  ```30 1 * * * python3 /.../.../FucknCoVReport/main.py```
## STATEMENT
Some core code is from the author cmzz on CSDN (url: https://blog.csdn.net/qq_40965177/article/details/105986587)
