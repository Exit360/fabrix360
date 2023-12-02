'''imports'''
import pygeoip
import requests
import socket


def user():
    
	# my_ip_adress = requests.get('https://api.ipify.org').text
	# gip = pygeoip.GeoIP('GeoLiteCity.dat')
	# res = gip.record_by_addr(my_ip_adress)
	# return res


## getting the hostname by socket.gethostname() method
	hostname = socket.gethostname()
	## getting the IP address using socket.gethostbyname() method
	ip_address = socket.gethostbyname(hostname)
	## printing the hostname and ip_address
	res = (ip_address,hostname)
	
	return res




if __name__ == '__main__':
	user()
