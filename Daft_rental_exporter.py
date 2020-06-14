import pandas #importing pandas for dataframes
from bs4 import BeautifulSoup #Importing for webscraping
l=[] #initialing empty list

base_url=input("Enter daft rental page link") #Please enter a daft rental site only. https://www.daft.ie/dublin-city/residential-property-for-rent/dublin-6/?s%5Bignored_agents%5D%5B0%5D=1551&searchSource=rental&offset=180
try: #Exception handling in case of incorrect website entry.
    r=requests.get(base_url,headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/62.0'})
except:
    print("Invalid website : Daft rental only")
    
    c=r.content #Store the content of the ste
    soup=BeautifulSoup(c,"html.parser") #Parse the content of the website
all=soup.find_all("div",{"class":"StandardPropertyInfo__detailsCopyContainer"}) #Analyze each listing

for i in all: #Iterate through each field of 1 listing
    d={}
    try:
        d["Price"]=i.find("strong",{"class":"PropertyInformationCommonStyles__costAmountCopy"}).text #Price of the rental
    except:
        d["Price"]="Featured property by an agent" #Agents sometimes put premium properties as normal which we want to ignore
    try:
        d["Address"]=i.find("a",{"class":"PropertyInformationCommonStyles__addressCopy--link"}).text #Address
    except:
        d["Address"]="None" #Missing address
    try:
         d["Type"]=i.find("div",{"class":"QuickPropertyDetails__propertyType"}).text.replace("\n","") #Property type
    except:
         d["Type"]="Featured property Please ignore";
    try:
         d["Bedrooms"]=i.find("div",{"class":"QuickPropertyDetails__iconCopy"}).text #Number of bedrooms
    except:
         d["Bedrooms"]="Studio(0)"; #Incase of studios this isn't populated. So we assume 0
    try:
        d["Bathroom"]=i.find("div",{"class":"QuickPropertyDetails__iconCopy--WithBorder"}).text #Number of bathrooms
    except:
         d["Bathroom"]="Studio(1)" #Incase of studios this isn't populated
    l.append(d)

df=pandas.DataFrame(l) #Creating dataframe from list
df.to_csv("rental_data10.csv") #Exporting as CSV.
