''''
1 import dependencies
2 build the web interface
3 build our image downloading function
4 Merge everythig together
'''
import streamlit as st
from simple_image_download import simple_image_download as sm

with st.sidebar:
    st.title('Image downloading web App')
    st.image('LOGO.png')

name = []
st.title('Fill the inputs below')
nameofimage = st.text_input('Name of Image')
name.append(nameofimage)
limit = st.number_input('Number of images',min_value=3)
search = st.button(label = 'search')
refresh = st.button(label = 'refresh')

def download():
    request = sm.simple_image_download
    for img  in name:
        request().download(img,limit=limit)



if search and limit and nameofimage:
    st.write('Downloading.................')
    download()
    st.write('Downloaded Sucessfully')

if refresh:
    st.write(' ')
    limit = ''
    nameofimage =  ''