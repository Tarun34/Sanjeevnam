import streamlit as st
Host_Country = st.selectbox('Select HomeTeamName name:',('France', 'Spain', 'Italy', 'England', 'Belgium', 'Portugal','Sweden'))
if Host_Country == "France":
    st.write("France")
