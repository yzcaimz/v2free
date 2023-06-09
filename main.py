import requests
import json
import os

requests.packages.urllib3.disable_warnings()
SCKEY = os.environ.get('SCKEY')
FS_BOT = os.environ.get('FS_BOT')

def checkin(email=os.environ.get('EMAIL'), password=os.environ.get('PASSWORD'),
            base_url=os.environ.get('BASE_URL'), ):
    email = email.split('@')
    email = email[0] + '%40' + email[1]
    session = requests.session()
    session.get(base_url, verify=False)
    login_url = base_url + '/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'email=' + email + '&passwd=' + password + '&code='

    post_data = post_data.encode()

    response = session.post(login_url, post_data, headers=headers, verify=False)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36',
        'Referer': base_url + '/user'
    }
    response = session.post(base_url + '/user/checkin', headers=headers,
                            verify=False)
            
    response = json.loads(response.text)
    print(response['msg'])
    return response['msg']


result = checkin()

# post message by feishu robot
if FS_BOT != '':
  url = FS_BOT
  headers = {'Content-Type': 'application/json'}
  data = {
    "msg_type": "text",
    "content": {
      "text": result
    }
  }

  print(url, headers, data)
  response = requests.post(FS_BOT, headers=headers, data=json.dumps(data))
  if response.status_code == 200:
    print("飞书机器人消息发送成功")
  else:
    print("飞书机器人消息发送失败")
