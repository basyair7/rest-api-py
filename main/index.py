import requests, json
from requests.auth import HTTPBasicAuth

res = requests.get('http://127.0.0.1:5000/api/v1/private', auth=HTTPBasicAuth('basyair', '1904105010004'));
print(f'Response Code : {str(res.status_code)}');
if(res.status_code == 200):
    print(f'Login successful : {res.text}');
    s = json.loads(res.text);
    print(s["Maybe"]);