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
from PIL import ImageDraw






def gvalue():

	logo = Image.open('images/logo360_s.png')

	st.image(logo,
		 caption='Welcome to fabrix360 free source info | fabrix360.com',
		 use_column_width=150)
	web = '<span style="font-style: italic;color: #000080;"><h6><a href="https://www.fabrix360.com/contactus">Contact us</a></h6></span>'
	st.markdown(web,unsafe_allow_html=True)
	st.header('ETFE cushion G value')
	w,h = 400,300
	slider_val = st.slider("G value through ETFE cushions skylight, slide the bar and see how it differ looking at the pictures", min_value=0.2, max_value=0.95, value=(0.5))
	g = slider_val
	col1, col2 = st.columns(2)
	with col2:

		skyview = Image.open('images/sky.jpg')
		st.image(skyview,
			 caption='Natural sky view' ,
			 use_column_width=100)
		

	with col1:
	
		img = Image.open('images/sky.jpg')
		if g <= 0.35:
			g = g/4
			
			draw = ImageDraw.Draw(img)
			step =3
			for n in range(step,w,step):
					for y in range(step,h,step):
						draw.regular_polygon(((n),(y),1), 6, rotation=0, fill="#A9A9A9", outline="silver")
			imgfrit = Image.new("RGB",(w,h), "#A9A9A9")
			imgsk=Image.blend(imgfrit,img,(g))

			return st.image(imgsk,
				caption=f'G value = {g} (Typical viewer standing below skylight)',
				use_column_width=100)

	
			
						
		


		else:
			draw = ImageDraw.Draw(img)
			step =3
			for n in range(step,w,step):
					for y in range(step,h,step):
						draw.regular_polygon(((n),(y),1), 6, rotation=0, fill="silver", outline="silver")
			imgfrit = Image.new("RGB",(w,h), "silver")
			imgsk=Image.blend(imgfrit,img,(g))

			return st.image(imgsk, 
				caption=f'G value = {g}(Typical viewer standing below skylight)',
				use_column_width=100)
	







# st.sidebar.markdown(f'<h1 style="color:#F63366;font-size:24px;">Want to know more? Send us message below:</h1>', unsafe_allow_html=True)

# useremail = st.sidebar.text_input("Please insert your email")
# message = st.sidebar.text_area("Please insert your info and message")
# submit = st.sidebar.button("mail your message")

# if submit:
# 	if not useremail:
# 		st.warning("Please insert your email address")
# 	if not message:
# 		st.warning("Please insert your message")

# 	else:

# 		st.success("Your message has been sent, thank you!")
# 		email(useremail,message)
		



				
				



					
				# with col1:
					
				# 	skyfrit = imgsk.show()


				# with col2:
					
				# 	skyview = Image.open('images/sky.jpg')
				# 	st.image(skyview,
				# 		 caption='Natural sky view' ,
				# 		 use_column_width=150)

