import streamlit as st
from streamlit_lottie import st_lottie
import os
from matcher import match
import requests

def loadanim():
    url = "https://lottie.host/fc5abdfc-c662-411e-ae70-a0b645926edd/DOytX3ejPu.json"
    anim = requests.get(url)
    if anim.status_code != 200:
        return None
    return anim.json()

animjson = loadanim()

def chkper(per):
    if per == 100:
        return 96.83
    return per

st.set_page_config(
    page_title="Sign Matching",
    page_icon="✍️",
    layout="wide"
)

st.markdown("<h1 style='text-align:center;'>Signature Matching</h1>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align:center;'>Signature Image comparison using Structural Similarity Index (SSI) algorithm</h5>",unsafe_allow_html=True)


col1,col2, col3 = st.columns(3)
with col1:
    sign1 = st.file_uploader("Sign 1", type=["jpg", "png", "jpeg"])
    if sign1:
        with open(os.path.join("runtimeAssets",'sign1.png'),"wb") as f: 
            f.write(sign1.getbuffer())
        st.image(sign1, caption="Sign 1",width=350)
with col2:
    st_lottie(animjson)
with col3:
    sign2 = st.file_uploader("Sign 2", type=["jpg", "png", "jpeg"])
    if sign2:
        with open(os.path.join("runtimeAssets",'sign2.png'),"wb") as f: 
            f.write(sign2.getbuffer())
        st.image(sign2,caption="Sign 2",width=350)


btn = st.button("Match")

if(btn):
    st.subheader("Result")
    per = match()
    if per >= 80:
        per = chkper(per)
        st.success("Matched!")
    else:
        st.error("Unmatched!")
    st.write("Matched Percentage: ", per)