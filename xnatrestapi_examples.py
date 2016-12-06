import requests

userid = 'sits'
passw = '8Ne!J.JJy~+-A=W'
passwhash = '{SHA}JM4OVt7gYuiZlbV+vOZEKT2KObQ='

auth_header_value = 'Basic %s %s' % (userid, passw)

headers = {
    'Authorization': auth_header_value,
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

xnatbase = 'http://10.0.1.144:8080/xnat'

xnatoperation = "/data/archive/projects/001/subjects?format=json"

# response = requests.get("http://localhost:8082/site/@deviceenrollments/0b6fec03c35a4009acb089b758790da4",
#                          headers=headers,)

response = requests.get(xnatbase + xnatoperation, auth=(userid, passw))
