import requests

from flask_login import current_user





data = {"file": open("Documents/file_template/CNAB.txt", "rb")}
response = requests.post("http://127.0.0.1:5000/",
                         data=data, headers={'Content-Type': 'form-data'})


print(response.text)
# print(requests.Request('POST', 'http://127.0.0.1:5000/', files=data).prepare().body.decode('ascii'))


"""
data = {"new_pwd": 'pytest',
        "old_pwd": 'senha'}
response = requests.post("http://127.0.0.1:5000/change/pwd",
                         data=data)
print(response.text)
"""
