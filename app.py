from etfe import etfe
import streamlit as st
from termcolor import colored, cprint
import sqlite3
import pandas as pd
import random
import smtplib
from email.message import EmailMessage
import email.message
from PIL import Image


logo = Image.open('images/logo360.png')
st.image(logo,
		 caption='Welcome to fabrix360 free source info | fabrix360.com',
		 use_column_width=200)

def main():
	### simple login ###
	
	menue = ["Home", "Want to know more"]
	choice = st.sidebar.selectbox("Menue", menue)

	if choice == "Home":

		
		
		etfe()

	elif choice == "Want to know more":
		web = 'https://www.fabrix360.com'
		st.header(web)
		st.markdown("To know more please visit our home page ", unsafe_allow_html=True)


if __name__ == '__main__':
	main()

		