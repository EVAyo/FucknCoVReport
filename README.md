# FucknCoVReport
An automatic python script for CUGB's COVID-19 report  
中国地质大学（北京）疫情期间每日自动进行健康打卡上报
## REQUIREMENTS
pip install requests
## USER MANNUL
### Moddify
>main.py:  
>>  
>>line 27:  ```data = {'username': 'example', 'password': 'example'}```  
>>**For example:  
>>'200119000X' (Your Student Number), '123456' (The Last Six Number of Your ID Card)**  
>>  
>>line 34:  ```cookie = cookie + "; username=example; menuVisible=0"```  
>>**For example:  
>>200119000X (Your Student Number)**  
>>  
>>line 54:  ``` ...,"location_address":"浙江省XX市XX街道XX社区","location_longitude":"123.123123","location_latitude":"32.32132",..."```  
>>**Notice:  
>>The value of "location_longitude" should be like "123.123123", and the value of "location_latitude" should be like "32.32132".In addtion, the two values should be matched with the value of "location_address".**
>>  
>iMessage.py:
>>line 10:  ```"from": "example@example.com",``` **e.g. username(send_from)@163.com**  
>>line 11:  ```"to": "example@example.com",``` **e.g. username(send_to)@gmail.com**  
>>line 12:  ```"hostname": "smtp.example.com",``` **e.g. smtp.163.com**  
>>line 13:  ```"username": "example@example.com",``` **e.g. username(send_from)@163.com**  
>>line 14:  ```"password": "******",``` **e.g. 163mail API key**
>>  
### Run
WINDOWS:  ```python main.py```

Linux:  ```python3 main.py``` or set a crontab  ```30 1 * * * python3 /.../.../FucknCoVReport/main.py```
## Statement
Some core code is from the author cmzz on CSDN (url: https://blog.csdn.net/qq_40965177/article/details/105986587)
