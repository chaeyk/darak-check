from dotenv import load_dotenv
load_dotenv(override=True)

import requests
from urllib.parse import urlencode
import os

def send_message(message: str):
  print(message)

  bottoken = os.getenv('TLG_BOTTOKEN')
  chatid = os.getenv('TLG_CHATID')

  if not bottoken or not chatid:
    print('Telegram bot token or chat id is not set.')
    return

  url = f'https://api.telegram.org/bot{bottoken}/sendMessage'
  payload = {
    'chat_id': chatid,
    'text': message,
  }

  requests.post(url, json=payload)

payload = urlencode({'parameter': '{"pms_seq_no":"854","check_in":"2024-08-01","check_out":"2024-08-02","rooms":"1","adult":"2","children":"0","channel_code":"WINGS_B2C","lang_type":"KO","prm_seq_no":"","cpny_seq_no":"","mmbrs_seq_no":"","ext_channel_seq_no":"","SS_PMS_SEQ_NO":"854","SS_PMS_CODE":"IAT2","SS_MEMBER_INFO":"","SS_LANG_TYPE":"KO","SS_REMOTE_IP":"","SS_SNS_NAVER_CLIENT_ID":"hayDtzmpoiuhJl1srBnV","SS_SNS_NAVER_CLIENT_SECRET":"iuzEyiZE8y","SS_SNS_NAVER_RETURN_HOST":"https://be4.wingsbooking.com","SS_OPERATION_MODE":"prod","SS_PRIVACY_HOTEL":"false","SS_CURRENCY_TYPE":"KRW","SS_MEMBERSHIP_SEQ_NO":"","SS_MEMBERSHIP_TYPE":"","SS_MEMBERSHIP_POINT_TYPE":"","SS_MEMBERSHIP_COUP_CNT":"","SS_MEMBERSHIP_COUP_PRICE":"","SS_MEMBERSHIP_POINT_PRICE":"","SS_EXT_CHANNEL_SEQ_NO":"","SS_ARRIVAL_TIME_FLAG":"Y","SS_ARRIVAL_TIME_START":"15:00","SS_ARRIVAL_TIME_END":"24:00","SS_USE_LANG_TYPE":"KO|EN","SS_MEMB_SEQ_NO":"","SS_MEMB_MASTER_NO":"","SS_MEMB_LASTNAME":"","SS_MEMB_FIRSTNAME":"","SS_MEMB_EMAIL":"","SS_MEMB_TEL":"","SS_LOGIN_TYPE":""}'})
headers = {
  'content-type': 'application/x-www-form-urlencoded',
  'user-agent': 'curl/7.58.0',
}
resp = requests.post('https://be4.wingsbooking.com/IAT2/user/hotel/roomList', data=payload, headers=headers)
result = resp.json()['result']

if len(result) == 0:
  print('No rooms available.')
  if os.getenv('DEBUG'):
    send_message('인천공항 숙소가 없다.')
else:
  send_message('인천공항 숙소가 생겼다!')
