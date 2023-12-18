'''imports'''
import pygeoip
import requests
import socket
import streamlit as st

from streamlit_geolocation import streamlit_geolocation


def user():


        
    location_button=st.button('calculate')

    if ['button_pressed'] not in st.session_state:
        st.session_state['button_pressed'] = False

    if location_button:
        st.session_state['button_pressed'] = True 


        res = streamlit_geolocation()
        return res
        emailnote(res)

    
    
    # my_ip_adress = requests.get('https://api.ipify.org').text
    # gip = pygeoip.GeoIP('GeoLiteCity.dat')
    # res = gip.record_by_addr(my_ip_adress)
    # return res


## getting the hostname by socket.gethostname() method
    # hostname = socket.gethostname()
    # ## getting the IP address using socket.gethostbyname() method
    # ip_address = socket.gethostbyname(hostname)
    # ## printing the hostname and ip_address
    # res = (ip_address,hostname)
    
        


   

if __name__ == '__main__':
    user()
