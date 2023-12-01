'''imports'''
import pygeoip
import requests


def user():

	my_ip_adress = requests.get('https://api.ipify.org').text
	gip = pygeoip.GeoIP('GeoLiteCity.dat')
	res = gip.record_by_addr(my_ip_adress)
	return res

# for key,val in res.items():
   
# 	print('%s : %s' % (key,val))


