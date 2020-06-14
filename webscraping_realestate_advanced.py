import pandas #importing pandas for dataframes
from bs4 import BeautifulSoup #Importing for webscraping
l=[] #initialing empty list
base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=" #base url 
r=requests.get(base_url+"0"+".html",headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content #extracting content of the page, headers parameter has been used above to make it look like we are using a browser 
soup=BeautifulSoup(c,"html.parser") #parsing thesite
pg_no=soup.find_all("a",{"class":"Page"})[-1].text #-1 to extract last element of the list

for pg in range(0,int(pg_no)*10,10):
    
    website=base_url+str(pg)+".html"
    print(base_url+str(pg)+".html")
    r=requests.get(base_url+str(pg)+".html",headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    
    for i in all:
        d={}
        d["Price"]=i.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Address"]=i.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["Locality"]=i.find_all("span",{"class":"propAddressCollapse"})[1].text
        try:
            d["Beds"]= i.find("span",{"class","infoBed"}).find("b").text
        except:
            d["Beds"]=None
        try:
            d["Full Baths"]=i.find("span",{"class","infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None
        try:
            d["Area"]= i.find("span",{"class","infoSqft"}).find("b").text
        except:
            d["Area"]=None
        
        for cg in i.find_all("div",{"class":"columnGroup"}):
            for fg,fn in zip(cg.find_all("span",{"class":"featureGroup"}),cg.find_all("span",{"class":"featureName"})):
                if "Lot Size" in fg.text:
                    d["Lot Size"] =fn.text
        l.append(d)
df=pandas.DataFrame(l)
df.to_csv("scraped_data.csv")