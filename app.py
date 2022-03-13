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
	
	menue = ["ETFE skylight","ETFE cushion G value", "About us"]
	choice = st.sidebar.selectbox("Site content menue", menue)

	if choice == "ETFE skylight":
		logo = Image.open('images/logo360_s.png')
		
		st.image(logo,
		 caption='Project Management,Design,Marketing | fabrix360.com',
		 use_column_width=150)
		web = '<span style="font-style: italic;color: #000080;"><h6><a href="https://www.fabrix360.com/contactus">Contact us</a></h6></span>'
		st.markdown(web,unsafe_allow_html=True)
		st.header('ETFE skylight')
		st.warning("Disclaimer:The contents of this web applications are for pure learning purposes and cannot be used commercially or firmly. If you seek firm information please contact us or contact your expert")
		


		
		
		etfe()

	elif choice == "ETFE cushion G value":
		logo = Image.open('images/logo360_s.png')
		st.image(logo,
		 caption='Project Management,Design,Marketing | fabrix360.com',
		 use_column_width=150)
		web = '<span style="font-style: italic;color: #000080;"><h6><a href="https://www.fabrix360.com/contactus">Contact us</a></h6></span>'
		st.markdown(web,unsafe_allow_html=True)
		st.header('ETFE cushion G value')
		st.warning("Disclaimer:The contents of this web applications are for pure learning purposes and cannot be used commercially or firmly. If you seek firm information please contact us or contact your expert")
		gvalue()

	elif choice == "About us":
		logo = Image.open('images/logo360_s.png')
		st.image(logo,
		 caption='Project Management,Design,Marketing | fabrix360.com',
		 use_column_width=150)
		web = '<span style="font-style: italic;color: #000080;"><h6><a href="https://www.fabrix360.com/contactus">Contact us</a></h6></span>'
		st.markdown(web,unsafe_allow_html=True)
		st.header('About us')
		st.header('Tensile structure & ETFE skylight hub in Middle East')
		about = """ fabrix360, Middle East based, is wide scope expert composed of conglomerate of elite expats Engineers and Project Managers with vast experience in tensile structures and air filled cushions(ETFE), robust and real field experience with iconic projects undertaken in Middle East and Worldwide in the last 2 decades.

 fabrix360 aims to offer and extend such vast expertise directly to Fabricators, Clients, Developers, Architects and Consultants into most innovative and feasible way.

We bring to our clients reliable, immediate productive and experienced resources and we strive constantly to be a company that delivers an outstanding results with maximum satisfaction prior, during and after construction.



<h3>Our competences: </h3>

- ETFE design management. 

- ETFE construction management.

- ETFE project management.

- Retractable roofs or Umbrellas ePTFE. 

- PTFE & PVC Tensile structures design.

- Hard cladding, envelopes, curtain walls, technical facades.

- Estimation and BOQ.

- Cost management & Procurement.

- QA/QC supervision.

- Installation Supervision.

- Preventive & Corrective Maintenance.

- Marketing & sales of new architectural fabric materials & solutions.

- Coaching resources & training """ 


		st.markdown(about,unsafe_allow_html=True)
		st.warning("Disclaimer:The contents of this web applications are for pure learning purposes and cannot be used commercially or firmly. If you seek firm information please contact us or contact your expert")



	

if __name__ == '__main__':
	main()

		