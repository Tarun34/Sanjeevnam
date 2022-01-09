import streamlit as st
import streamlit.components.v1 as components
import news
import front
from PIL import Image
st.set_page_config(page_title="Sanjeevnam",
                   layout="wide",
                   page_icon="downloa.png")

def app1 ():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">',unsafe_allow_html=True)
    st.markdown("""
     <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#3498DB;">
     <a class="navbar-brand fa fa-stethoscope" style="font-size:30px" href="http://localhost:8501/" target="_blank"> Sanjeevnam </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="http://localhost:8501/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8502/" target="_blank"> Vaccine </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8503/" target="_blank">Disease</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8504/" target="_blank">Health Insurance</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
col1,col2=st.columns([3,3])
with col1:
    im=Image.open("trying.png")
    im=im.resize([800,500])
    st.image("trying.png")
    st.header("")
    st.image("creating.png")
with col2:
    st.image("computer.png")


app1()
front.app()
news.app()

