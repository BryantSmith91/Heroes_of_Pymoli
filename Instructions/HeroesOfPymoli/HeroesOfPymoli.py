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


print(PurchaseSum)
print(genderdf)
