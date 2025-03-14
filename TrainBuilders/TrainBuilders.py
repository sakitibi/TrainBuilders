import streamlit as st

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

st.subheader('12ninアカウントでログイン')
with st.form(key='12ninaccounts'):
        st.subheader('12ninアカウントでログイン')
        submit_btn = st.form_submit_button('ログイン')
        cancel_btn = st.form_submit_button('キャンセル')
        if submit_btn:
                st.text('ここにアクセスして下さい\nhttps://sakitibi-com9.webnode.jp/api/trainbuilders/login/24ac77a0-013e-45ae-97d1-b6cc59fb958a/')
        elif cancel_btn:
                st.text('キャンセルしました')
