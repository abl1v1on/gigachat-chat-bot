import uuid
import json
import requests
import streamlit as st
from requests.auth import HTTPBasicAuth


CLIEND_ID = st.secrets['CLIENT_ID']
SECRET = st.secrets['SECRET']



def get_access_token() -> str:
    url = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
    }

    response = requests.post(
        url=url,
        headers=headers,
        auth=HTTPBasicAuth(CLIEND_ID, SECRET),
        data={'scope': 'GIGACHAT_API_PERS'},
        verify=False
    )
    access_token = response.json()['access_token']
    return access_token

def get_image():
    pass


def send_prompt(message: str, token: str):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
    "model": "GigaChat",
    "messages": [
        {
        "role": "user",
        "content": message,
        }
    ]}
    )
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)

    return response.json()['choices'][0]['message']['content']


def get_result():
    pass