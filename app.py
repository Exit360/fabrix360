from etfe import etfe
from gvalue import gvalue
import streamlit as st
from termcolor import colored, cprint
import sqlite3
import pandas as pd
import random
import smtplib
from email.message import EmailMessage
import email.message
from PIL import Image


# logo = Image.open('images/logo360_s.png')
# st.image(logo,
# 		 caption='Welcome to fabrix360 free source info | fabrix360.com',
# 		 use_column_width=150)

def main():
	### simple login ###
	
	menue = ["ETFE skylight","ETFE cushion G value", "Want to know more"]
	choice = st.sidebar.selectbox("Menue", menue)

	if choice == "ETFE skylight":
		logo = Image.open('images/logo360_s.png')
		
		st.image(logo,
		 caption='Welcome to fabrix360 free source info | fabrix360.com',
		 use_column_width=150)
		web = '<span style="font-style: italic;color: #000080;"><h6><a href="https://www.fabrix360.com/contactus">Contact us</a></h6></span>'
		st.markdown(web,unsafe_allow_html=True)
		st.header('ETFE skylight')
		


		
		
		etfe()

	elif choice == "ETFE cushion G value":
		gvalue()

	elif choice == "Want to know more":
		logo = Image.open('images/logo360_s.png')
		st.image(logo,
		 caption='Welcome to fabrix360 free source info | fabrix360.com',
		 use_column_width=150)
		web = '<span style="font-style: italic;color: #000080;"><h6><a href="https://www.fabrix360.com/contactus">Contact us</a></h6></span>'
		st.markdown(web,unsafe_allow_html=True)
		st.header('Tensile structure & ETFE skylight hub in Middle East')
		



	

if __name__ == '__main__':
	main()

		