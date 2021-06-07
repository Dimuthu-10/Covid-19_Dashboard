import streamlit as st

st.header('welcome to our dashboard !!!')
st.subheader('''
covid-19 situation report
''')

options = st.selectbox('select mode:', ['PowerBI', 'Preprocessing & predictions'])

if options == 'PowerBI':
    st.markdown(
        "https://app.powerbi.com/links/XhfxWNlUmU?ctid=49211f0f-e082-499f-94fb-96dff1601a14&pbi_source=linkShare")
