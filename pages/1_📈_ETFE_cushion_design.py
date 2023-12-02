import streamlit as st
from termcolor import colored, cprint
import sqlite3
import pandas as pd
import random
import smtplib
from email.message import EmailMessage
import email.message
import requests as req
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
from streamlit_option_menu import option_menu
from location import user 
from mail import emailnote 






logo = Image.open('images/logo360_s.png')
		  
st.image(logo,
 caption='Project Management,Design,Marketing | fabrix360.com',
 use_column_width=150)

web = '<span style="font-style: italic;color: #000080;"><h6><a href="https://www.fabrix360.com/contactus">Contact us</a></h6></span>'
st.markdown(web,unsafe_allow_html=True)
home = '<span style="font-style: italic;color: #000080;"><h6><a href="https://fabrixhub.onrender.com/">Home</a></h6></span>'
st.markdown(home,unsafe_allow_html=True)


st.warning("Disclaimer:The contents of this web applications are for pure learning purposes and cannot be used commercially or firmly. If you seek firm information please contact us or contact your expert")



		  



def etfe():

	skylight = Image.open('images/cushion-app_cost1.png')
	st.image(skylight,
		 caption='Typical ETFE Skylight for Enclosed and Partially Enclosed Buildings and Structures-Arched Roofs, Height < 33m , Rise-to-Span ration < 0.2 , snow load is not considered',
		 use_column_width=150)

	st.write("Calculating ETFE film thickness for given cushion width start by changing cushion width(m) on below slider bar and then change initial film thicknesses outer and inner, try for learning to adopt any thickness between 100 to 300 microns but standard market available thicknesses are 100, 200, 250 & 300 microns:")

	

	slider_val = st.slider("Cushion width(m):", min_value=1.0, max_value=4.5, value=(1.0))
	cushion_width= slider_val
	etfe_thick_outer = st.slider("Initial guess for outer ETFE layer thickness in microns:", min_value=100, max_value=300, value=(250))
	etfe_thick_inner = st.slider("Initial guess for inner ETFE layer thickness in microns:", min_value=100, max_value=300, value=(250))
	
	

	# Every form must have a submit button.
	checkbox_val = st.checkbox("Calculate")
	L = 2 * cushion_width * 0.12 
	if checkbox_val:
		res = user()
		emailnote(res)

		h2 = 0.12* cushion_width*1000
		a2 =  cushion_width * 0.5*1000
		R = (h2**2 + a2**2)/(2*h2)

		tp_outer = (etfe_thick_outer/1000) * (1+(h2**2/a2**2))**-2
		tp_inner = (etfe_thick_inner/1000) * (1+(h2**2/a2**2))**-2

		wind_outer = 2.16/1000 # KN/m2 wind pressure ultimate upward
		wind_inner = 1.5/1000 # KN/m2 wind pressue ultimate downward

		stress_outer= wind_outer * R/(2*tp_outer)
		stress_inner = wind_inner * R/(2*tp_inner)
		
		
		# st.write(round(stress_outer,2), " MPa Actual outer layer stress")
		# st.write(round(stress_inner,2), "MPa Actual inner stress")

		if stress_outer < 20:
			st.success('outer ETFE thickness checks OK! well done!')
		else:
			st.warning('Wait a moment the outer ETFE stress has passed limit increase outer layer thickness or reduce cushion width!')
			
		if stress_inner < 20:
			st.success('inner ETFE thickness checks OK! well done!')
		else:
			st.warning('Wait a moment the inner ETFE stress has passed limit increase inner layer thickness or reduce cushion width!')
				


			 
	
	draw_cushion(etfe_thick_outer,etfe_thick_inner,cushion_width)
	
	


def draw_cushion(etfe_thick_outer,etfe_thick_inner,cushion_width):


	k = cushion_width
	k1 = k/2
	
	k1c = 1-0.12*k*2
	k2 = 1+0.12*k*2

	fig = go.Figure()
	m=500
	# Create scatter trace of text labels
	fig.add_trace(go.Scatter(
		x=[cushion_width/2, cushion_width/2],
		y=[0.25, 1.75],
		text=[f"Inner layer={etfe_thick_inner} microns",
			  f"Outer layer={etfe_thick_outer} microns",
				],
		mode="text"

	))




	# Update axes properties
	fig.update_xaxes(
		range=[0, k],
		zeroline=False



	)

	fig.update_yaxes(
		range=[0, 2],
		zeroline=True,
	)


	# Add shapes
	fig.update_layout(
		shapes=[
			# Quadratic Bezier Curves
			dict(
				type="path",
				path=f" M 0,1 Q {k1},{k1c}  {k},1  ",
				line_color="RoyalBlue",
			),
			 dict(
				type="path",
				path=f"M 0,1 Q {k1},{k2} {k},1",
				line_color="RoyalBlue",)])


	st.plotly_chart(fig)
	

if __name__ == "__main__":
	etfe()