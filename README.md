# FucknCoVReport
An automatic python script for CUGB's COVID-19 report  
中国地质大学（北京）疫情期间每日自动进行健康打卡上报
***免责声明（Disclaimer）：使用该脚本而可能引起的法律责任和学校追究等责任由使用者个人承担，与开发者无关。为了您和他人的健康着想，请在有位置变动和情况变化时手动填写申报！***
## UPDATES
**2020/08/25 (Upcoming) - The upcoming update version will resolve:** 
1.In the upcoming campus life, the Big Brother will take the MAE (Morning, Afteroon and Evening) clock-in measures.
2.Epidemic prevention should not torment students and the other ordinary people and formalism does harm.
**2020/08/14 - This update version resolved:**  
1.A new feature for the site that uses base64 encoding for the username and password, and uses token
2.Fixed some bugs
## REQUIREMENTS
pip install requests
## USER MANNUL (Updated on 2020/08/14)
### Modify
>main.py:  
>>  
>>line 33:  ```uname = 'example'  # Your Student Number, e.g. 2001200001```  
>>line 34:  ```upwd = 'example'  # You ID card: last 6 numbers, e.g. 123456```  
>>**For example:  
>>'200120000X' (Your Student Number), '123456' (The Last Six Number of Your ID Card)**  
>>  
>>line 64:  ``` ...,"location_address":"浙江省XX市XX街道XX社区","location_longitude":"123.123123","location_latitude":"32.32132",..."```  
>>**Notice:  
>>The value of "location_longitude" should be like "123.123123", and the value of "location_latitude" should be like "32.32132".In addtion, the two values should be matched with the value of "location_address".**
>>  
>iMessage.py:
>>line 9:  ```"from": "example@example.com",``` **e.g. username(send_from)@163.com**  
>>line 10:  ```"to": "example@example.com",``` **e.g. username(send_to)@gmail.com**  
>>line 11:  ```"hostname": "smtp.example.com",``` **e.g. smtp.163.com**  
>>line 12:  ```"username": "example@example.com",``` **e.g. username(send_from)@163.com**  
>>line 13:  ```"password": "******",``` **e.g. 163mail API key**
>>  
### Run
WINDOWS:  ```python main.py```

Linux:  ```python3 main.py``` or ***(Recommend)*** set a crontab  ```30 1 * * * python3 /.../.../FucknCoVReport/main.py```
## STATEMENT
Some core code is from the author cmzz on CSDN (url: https://blog.csdn.net/qq_40965177/article/details/105986587)
