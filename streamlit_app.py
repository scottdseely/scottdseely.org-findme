import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/scottdseely/links.svg?logo=github&style=social)](https://gitHub.com/scottdseely/find-me)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Scott Seely')

st.info('Developer Advocate, Database, Data Analytics, Basketball')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/scottdseely/', 'Follow me on LinkedIn', icon_size)
st_button('youtube', 'https://youtube.com/scottdseely', 'Data Professor YouTube channel', icon_size)
st_button('youtube', 'https://youtube.com/scottdseely', 'Coding Professor YouTube channel', icon_size)
st_button('medium', 'https://medium.com/@ScottDSeely/lists', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/scottdseely/', 'Follow me on Twitter', icon_size)
st_button('newsletter', 'https://sendfox.com/scottdseely/', 'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/scottdseely/', 'Buy me a Coffee', icon_size)
