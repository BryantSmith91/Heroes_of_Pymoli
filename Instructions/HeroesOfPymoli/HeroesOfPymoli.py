# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

groupeddata = purchase_data.groupby(["SN"])
playercount = len(groupeddata)
print(f"There are {playercount} unique players.")

uniqueitems = purchase_data.groupby(["Item ID"])
averageprice = round(purchase_data["Price"].mean(),2)
numpurchases = purchase_data.groupby(["Purchase ID"])
totalrevenue = purchase_data["Price"].sum()
PurchaseSum = pd.DataFrame({
    "Total Unique Items" :[len(uniqueitems)],
    "Average Purchase Price" :[averageprice],
    "Total Number of Purchases" :[len(numpurchases)],
    "Total Revenue" :[totalrevenue]
})

genderdata = groupeddata['Gender'].max().value_counts()

malecount = genderdata['Male']
malepercent = (malecount/playercount)*100

femcount = genderdata['Female']
fempercent = (femcount/playercount)*100

othcount = genderdata['Other / Non-Disclosed']
othpercent = (othcount/playercount)*100

genderdf = pd.DataFrame([
    [malecount,malepercent],[femcount,fempercent],[othcount,othpercent]],
    index=['Male','Female','Other/Non-Disclosed'],
    columns = ['Max','Percent']
)

genderdf = genderdf.style.format({'Percent': '{:,.2f}%'})

maleonlydf = purchase_data[purchase_data['Gender']=='Male']
femonlydf = purchase_data[purchase_data['Gender']=='Female']
otheronlydf = purchase_data[purchase_data['Gender']=='Other / Non-Disclosed']

#male demographics
malepurchasecount = maleonlydf['Purchase ID'].count()
maleavgprice = maleonlydf['Price'].mean()
maletotalrev = maleonlydf['Price'].sum()
maleperperson = (maletotalrev/malecount)

#female demographics
femepurchasecount = femonlydf['Purchase ID'].count()
femavgprice = femonlydf['Price'].mean()
femtotalrev = femonlydf['Price'].sum()
femperperson = (femtotalrev/femcount)

#other demographics
otherpurchasecount = otheronlydf['Purchase ID'].count()
otheravgprice = otheronlydf['Price'].mean()
othertotalrev = otheronlydf['Price'].sum()
otherperperson = (othertotalrev/othcount)


genderdemodf = pd.DataFrame({
    "Gender":['Male','Female','Other/Non-Disclosed'],
    "Total Purchases":[malepurchasecount,femepurchasecount,otherpurchasecount],
    "Average Price":[maleavgprice,femavgprice,otheravgprice],
    "Total Revenue":[maletotalrev,femtotalrev,othertotalrev],
    "Avg Price/Gender":[maleperperson,femperperson,otherperperson]

 })
genderdemodf = genderdemodf.set_index('Gender')
genderdemodf = genderdemodf.style.format({'Average Price': '${:,.2f}','Total Revenue': '${:,.2f}','Avg Price/Gender': '${:,.2f}'})
genderdemodf



print(PurchaseSum)
print(genderdf.format(data_pandas))
print(genderdemodf.format(data_pandas))
