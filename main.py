import streamlit as st
from gigachatapi import get_access_token, send_prompt

st.title('GIGA CHAT API BOT')


if 'access_token' not in st.session_state:
    try:
        st.session_state.access_token = get_access_token()
    except:
        st.toast('Произошла ошибка, попробуйте позже...')

if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'ai', 'content': 'Введите запрос'}
    ]

for message in st.session_state.messages:
    st.chat_message(
        message['role'], 
        avatar='🧑‍💻' if message['role'] == 'user' else '🤖'
    ).write(message['content'])


if prompt := st.chat_input(placeholder='Введите запрос...'):
    st.chat_message('user', avatar='🧑‍💻').write(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.toast('Запрос отправлен, ожидайте ответа...', icon='🔥')

    with st.spinner('В процессе...'):
        try:
            res = send_prompt(prompt, st.session_state.access_token)

            st.chat_message('ai', avatar='🤖').write(res)
            st.session_state.messages.append({'role': 'ai', 'content': res})
        except:
            st.toast('Произошла ошибка, попробуйте позже', icon='🚨')
            