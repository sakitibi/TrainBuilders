import streamlit as st
from PIL import Image

st.title('TrainBuilders')
st.caption('このアプリはPython Javascript HTML CSS C#で作成されました')
st.subheader('TrainBuildersとは')
st.text('TrainBuildersは12ninstudioが開発したRPGゲームです。\n'
        'マップを歩きモンスターを倒して材料集めて建築するゲームです。')
code = '''
import streamlit as st

st.title('TrainBuilders')
'''
st.code(code, language='python')


image = Image.open('https://github.com/sakitibi/TrainBuilders/blob/main/TrainBuilders/Home.png')
st.image(image, width=200)
st.subheader('12ninアカウントでログイン')
with st.form(key='12ninaccounts'):

        name = st.text_input('名前')
        mail = st.text_input('EMail')
        password = st.text_input('パスワード')
        
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
        if submit_btn:
                st.text(f'ようこそ！{name}さん！{mail}に確認のメールを送信しました')
        elif cancel_btn:
                st.text('キャンセルしました')
