import re
import time
import cloudscraper
from bs4 import BeautifulSoup 
print("Everything Looks Good! Lets Continue.")

url = "https://techymozo.com/hgSq9"  #@param {type:"string"}

"""support all domains in xpshort
#Ex:- https://xpshort.com/sJjAlGL
#Ex:- https://push.bdnewsx.com/sJjAlGL"""

# leech with credits broo
# ---------------------------------------------------------------------------------------------------------------------

def xpshort(url):
    """ Xpshort.com bypass link generator
    Based on https://github.com/JohnWickKeanue/xpshort-bypass"""
     
    client = cloudscraper.create_scraper(allow_brotli=False)
    
    
    DOMAIN = "https://push.bdnewsx.com"

    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    
    final_url = f"{DOMAIN}/{code}"
    
    ref = "https://techrfour.com/"
    
    h = {"referer": ref}
  
    resp = client.get(final_url,headers=h)
    
    soup = BeautifulSoup(resp.content, "html.parser")
    
    inputs = soup.find_all("input")
   
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    
    time.sleep(8)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("
    
# ---------------------------------------------------------------------------------------------------------------------
print(xpshort(url))
