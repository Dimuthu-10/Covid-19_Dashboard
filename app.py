import streamlit as st
import webbrowser

st.header('welcome to our dashboard !!!')
st.subheader('''
covid-19 situation report
''')

# options = st.selectbox('select mode:', ['PowerBI', 'Preprocessing & predictions'])

# if options == 'PowerBI':
#     st.markdown(
#         "https://app.powerbi.com/reportEmbed?reportId=ce47b75d-7856-48e3-bf6c-da64e4d4503b&autoAuth=true&ctid=49211f0f-e082-499f-94fb-96dff1601a14&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWVhc3QtYXNpYS1hLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D",
#         unsafe_allow_html=True)



url = 'https://app.powerbi.com/reportEmbed?reportId=ce47b75d-7856-48e3-bf6c-da64e4d4503b&autoAuth=true&ctid=49211f0f-e082-499f-94fb-96dff1601a14&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWVhc3QtYXNpYS1hLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D'

if st.button('Open browser'):
    webbrowser.open_new_tab(url)
