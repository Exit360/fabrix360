import math
import streamlit as st


def uvalue(L):
	import math

	ther_exp = 3.2717E-3
	ther_con = 0.026526
	kin_v = 1.6271E-5
			
	ther_dif = 2.2810E-5
	Pr = 0.71332

	theta= 2.35619
	Tf = 32.5
	




	Gr = (9.81 * ther_exp * 25 * L ** 3) / kin_v ** 2
	Nu = 1 + ((0.035 * (Gr * Pr) ** 0.38) - 1) * math.sin(theta)
	hcv = (Nu * ther_con) / L
	hrd = (4 * 5.67E-8 * Tf ** 4) / 1.35
	R = (1/(hrd + hcv))
	U = 1 / R
	U = round(U, 2)
 
	winter = f"U value = {U} W/k.m2"
	st.markdown(winter,unsafe_allow_html=True)
	# print("U 90 < theta <= 180")
	# print(U)

	# Gr = (9.81 * ther_exp * 25 * L ** 3) / kin_v ** 2
	
	# Nu = (0.035 * (Gr * Pr) ** 0.38) * math.sin(theta-((theta-(math.pi/2)) * 2)) ** 0.25
	# hcv = (Nu * ther_con) / L
	# hrd = (4 * 5.67E-8 * Tf ** 4) / 1.35
	# R = (1 / (hcv + hrd))
	# Us = 1 / R
	# Us = round(Us, 2)

	# summer = f"U value at summer {Us} W/k.m2"
	# st.markdown(summer,unsafe_allow_html=True)
	

	# print("Us for 90 > theta <= 180")
	# print(Us)
