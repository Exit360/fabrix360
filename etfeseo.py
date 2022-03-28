from googlesearch import search
import streamlit as st
import re

def getWordsFromURL(url):
    return re.compile(r'[\:/?=\-&]+',re.UNICODE).split(url)

def etfeseo():
	menue = ["Select Key Word","ETFE in Middle East","ETFE in Europe","ETFE in Africa", 
	"ETFE in USA", "ETFE in East Asia","ETFE in Australia"]
	choice = st.selectbox("Select Geographic Area", menue)

	if choice ==  "ETFE in Middle East":

		q = "ETFE in Middle East"

		seo(q)

	elif choice ==  "ETFE in Europe":

		q = "ETFE in Europe"
		seo(q)

	elif choice ==  "ETFE in Africa":

		q = "ETFE in Africa"
		seo(q)

	elif choice ==  "ETFE in USA":

		q = "ETFE in USA"
		seo(q)

	elif choice ==  "ETFE in East Asia":

		q = "ETFE in East Asia"
		seo(q)

	elif choice ==  "ETFE in Australia":

		q = "ETFE in Australia"
		seo(q)


def seo(q):

	for url in search(q,tld='com', lang='en', num=20, stop=20, pause=2.0):
		words = getWordsFromURL(url)
		if "uaeyellowpagesonline.com" not in words:
			if "www.constructionweekonline.com" not in words:
				if "www.aeconline.ae" not in words:
					if "www.yello.ae"not in words:
						if "uae.tradeford.com" not in words:
							if "www.gulfshade.com" not in words:
								if "structurflex" not in words:
									st.markdown(url)

						
						
				

			
			
					


		
		
		