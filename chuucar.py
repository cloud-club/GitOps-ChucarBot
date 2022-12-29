import os
import json
import slack_sdk
import random
from slackclient import SlackClient
from datetime import date, datetime, timezone, timedelta

slack_token = SlackClient(os.environ.get('SLACK_TOKEN'))
SLACK_CHANNEL = "#birthday"

json_path = './birthlist.json'
with open(json_path, 'r') as birth_json:
    b_dict = json.load(birth_json)

def chuucar_send_msg(slack_msg):
    slack_token.api_call("chat.postMessage", channel=SLACK_CHANNEL,text=slack_msg)

KST = timezone(timedelta(hours=9))
today=datetime.now(KST)

for key,val in b_dict.items():   
    date_of_birth = date(int(val[0:4]), int(val[4:6]), int(val[6:8]))

    if today.month==date_of_birth.month and today.day == date_of_birth.day:
        chat = "오늘은 바로바로 귀여운 클둥이, *"+ key + "* 의 생일입니다!"+" 다들 소리질러~!!"
        chuucar_send_msg(chat)