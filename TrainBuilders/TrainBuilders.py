import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

        name = st.text_input('名前')
        mail = st.text_input('EMail')
        password = st.text_input('パスワード')
        
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
        if submit_btn:
                st.text(f'ようこそ！{name}さん！{mail}に確認のメールを送信しました')
                #coding: shift_jis
                strSMTPSvr = f'{mail}'
                intSMTPPort = 587
                strUser = f'{name}'
                strPass = f'{password}'
                str.To = f'{mail}'
                
                smtpCL = smtplib.SMTP(strSMTPSvr, intSMTPPort)
                smtpCL = starttls()
                smtpCL.login(name, password)
                msg = MIMEMultipart()
                
                msg["From"] = name
                msg["To"] = mail
                msg["Subject"] = "認証して下さい"
                body = "12ninアカウントを認証してTrainBuildersをプレイしよう\nhttps://sakitibi-com9.webnode.jp/api/trainbuilders/login/24ac77a0-013e-45ae-97d1-b6cc59fb958a"
                msg.attach(MIMEText(body, "plain"))
                
                smtpCL.send_message(msg)
                
                smtpCL.quit()
        elif cancel_btn:
                st.text('キャンセルしました')
