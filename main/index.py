import requests, json, os, keyboard
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, dotenv_values

load_dotenv()
while True:
    if keyboard.is_pressed('q'): break;
    try:
        print(f'{os.getenv("USERNAME")}, {os.getenv("PASSWORD")}')
        res = requests.get(
                'http://127.0.0.1:5000/api/v1/private', 
                auth=HTTPBasicAuth(os.getenv("USERNAME"), os.getenv("PASSWORD"))
            );

        print(f'Response Code : {str(res.status_code)}');
        if(res.status_code == 200):
            print(f'Login successful : {res.text}');
            s = json.loads(res.text);
            print(s["Maybe"]);
            
    except:
        print("error");
        continue;