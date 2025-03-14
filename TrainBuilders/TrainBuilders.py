import streamlit as st
import webbrowser

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
        
        html = '''
        <body>
                <button type="submit" id="open">ログイン</button>
                <script>
                        document.getElementById('open').addEventListener('click', function() {
                                location.href = 'https://sakitibi-com9.webnode.jp/api/trainbuilders/login/24ac77a0-013e-45ae-97d1-b6cc59fb958a';
                        });
                </script>
        </body>
        '''
        cancel_btn = st.form_submit_button('キャンセル')
        if cancel_btn:
                st.text('キャンセルしました')
