# Imports
import streamlit as st
from plot import create_plot

st.markdown(""" <style> .font {
font-size:50px ; font-family: 'GothamBook'; color: #1DB954;} 
</style> """, unsafe_allow_html=True)

st.markdown('<p class="font">Spoticry Wrapped </p>', unsafe_allow_html=True)

create_plot()
st.image('figures/pie.jpg')

st.markdown(
        """
        <style>
@font-face {
  font-family: 'GothamBook';
  font-style: normal;
  font-weight: 400;
  src: url('Spotify-Font/GothamBook.ttf') format('ttf');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

    html, body, [class*="css"]  {
    font-family: 'GothamBook';
    font-size: 48px;
    }
    </style>

    """,
        unsafe_allow_html=True,
    )

"# Hello"

# average cries 

