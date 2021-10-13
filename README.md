# FucknCoVReport

***免责声明（Disclaimer）：使用该脚本而可能引起的法律责任和学校追究等责任由使用者个人承担，与开发者无关，请勿滥用。为了您和他人的健康着想，请如实填写信息，在有位置变动和情况变化时手动填写申报！***
## FUNCTIONS
### - **Submit the personal health information automatically**
### - **Push the notifications via Email or ServerChan**
## UPDATES
### **2021/08/18 - The latest version resolved:**
- Rebuild the code (now you just need modify the config.json).
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
>config.json:  
>>  
>>{
>>        ```"username":"username",```  
>>        ```"password":"password",```  
>>        ```"data":```  
>>        ```{```  
>>                ```"xmqkb":```  
>>                ```{```  
>>                        ```"id":"4a4ce9d6725c1d4001725e38fbdb07cd"```  
>>                ```},```  
>>                ```"c1":"37.2℃及以下",```  
>>                ```"c2":"健康",```  
>>                ```"c17":"否",```  
>>                ```"c4":"否",```  
>>                ```"c5":"否",```  
>>                ```"c6":"否",```  
>>                ```"c9":"否",```  
>>                ```"c7":"否",```  
>>                ```"c19":"36.7",```  
>>                ```"c22":"36.7",```  
>>                ```"type":"YQSJCJ",```  
>>                ```"location_longitude":"116.37951",```  
>>                ```"location_latitude":"39.594672",```  
>>                ```"location_address":"北京市海淀区学院路街道中国地质大学(北京)"```  
>>        ```},```  
>>        ```"push_api": "https://sctapi.ftqq.com/[api].send"```  
>>```}```  
### Run
WINDOWS:  ```python main.py```

Linux:  ```python3 main.py``` or ***(Recommend)*** set a crontab  ```30 1 * * * python3 /.../.../FucknCoVReport/main.py```
## STATEMENT
Some core code is from the author cmzz on CSDN (url: https://blog.csdn.net/qq_40965177/article/details/105986587)
