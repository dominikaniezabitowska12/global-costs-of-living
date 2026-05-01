import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import plotly.express as px


df = pd.read_csv('cost-of-living.csv')
df = df.fillna(df.mean(numeric_only=True))  #filling in missing data

#renaming columns
df = df.rename(columns={
    "x1" : "Meal, Inexpensive Restaurant (USD)",
    "x2" : "Meal for 2 People, Mid-range Restaurant, Three-course (USD)",
    "x3" : "McMeal at McDonalds (or Equivalent Combo Meal) (USD)",
    "x4" : "Domestic Beer (0.5 liter draught, in restaurants) (USD)",
    "x5" : "Imported Beer (0.33 liter bottle, in restaurants) (USD)",
    "x6" : "Cappuccino (regular, in restaurants) (USD)",
    "x7" : "Coke/Pepsi (0.33 liter bottle, in restaurants) (USD)",
    "x8" : "Water (0.33 liter bottle, in restaurants) (USD)",
    "x9" : "Milk (regular), (1 liter) (USD)",
    "x10" : "Loaf of Fresh White Bread (500g) (USD)",
    "x11" : "Rice (white), (1kg) (USD)",
    "x12" : "Eggs (regular) (12) (USD)",
    "x13":"Local Cheese (1kg) (USD)",
    'x14':"Chicken Fillets (1kg) (USD)",
    'x15':"Beef Round (1kg) (or Equivalent Back Leg Red Meat) (USD)",
    'x16':"Apples (1kg) (USD)",
    'x17':"Banana (1kg) (USD)",
    'x18':"Oranges (1kg) (USD)",
    'x19':"Tomato (1kg) (USD)",
    'x20':"Potato (1kg) (USD)",
    'x21':'Onion (1kg) (USD)',
    'x22':"Lettuce (1 head) (USD)",
    'x23':"Water (1.5 liter bottle, at the market) (USD)",
    'x24':"Bottle of Wine (Mid-Range, at the market) (USD)",
    'x25':'Domestic Beer (0.5 liter bottle, at the market) (USD)',
    'x26':'Imported Beer (0.33 liter bottle, at the market) (USD)',
    'x27':'Cigarettes 20 Pack (Marlboro) (USD)',
    'x28':'One-way Ticket (Local Transport) (USD)',
    'x29':'Monthly Pass (Regular Price) (USD)',
    'x30':'Taxi Start (Normal Tariff) (USD)',
    'x31':'Taxi 1km (Normal Tariff) (USD)',
    'x32':'Taxi 1hour Waiting (Normal Tariff) (USD)',
    'x33':'Gasoline (1 liter) (USD)',
    'x34':'Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car) (USD)',
    'x35':'Toyota Corolla Sedan 1.6l 97kW Comfort (Or Equivalent New Car) (USD)',
    'x36':'Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment (USD)',
    'x37':'1 min. of Prepaid Mobile Tariff Local (No Discounts or Plans) (USD)',
    'x38':'Internet (60 Mbps or More, Unlimited Data, Cable/ADSL) (USD)',
    'x39':'Fitness Club, Monthly Fee for 1 Adult (USD)',
    'x40':'Tennis Court Rent (1 Hour on Weekend) (USD)',
    'x41':'Cinema, International Release, 1 Seat (USD)',
    'x42':'Preschool (or Kindergarten), Full Day, Private, Monthly for 1 Child (USD)',
    'x43':'International Primary School, Yearly for 1 Child (USD)',
    'x44':'1 Pair of Jeans (Levis 501 Or Similar) (USD)',
    'x45':'1 Summer Dress in a Chain Store (Zara, H&M, …) (USD)',
    'x46':'1 Pair of Nike Running Shoes (Mid-Range) (USD)',
    'x47':'1 Pair of Men Leather Business Shoes (USD)',
    'x48':'Apartment (1 bedroom) in City Centre (USD)',
    'x49':'Apartment (1 bedroom) Outside of Centre (USD)',
    'x50':'Apartment (3 bedrooms) in City Centre (USD)',
    'x51':'Apartment (3 bedrooms) Outside of Centre (USD)',
    'x52':'Price per Square Meter to Buy Apartment in City Centre (USD)',
    'x53':'Price per Square Meter to Buy Apartment Outside of Centre (USD)',
    'x54':'Average Monthly Net Salary (After Tax) (USD)',
    'x55':'Mortgage Interest Rate in Percentages (%), Yearly, for 20 Years Fixed-Rate'
    })



#category grouping
df["housing"]= df[['Apartment (1 bedroom) in City Centre (USD)', 'Apartment (1 bedroom) Outside of Centre (USD)',
                'Price per Square Meter to Buy Apartment in City Centre (USD)','Price per Square Meter to Buy Apartment Outside of Centre (USD)']].mean(axis=1)
df["food"] = df[["Meal, Inexpensive Restaurant (USD)","Loaf of Fresh White Bread (500g) (USD)", "Rice (white), (1kg) (USD)", "Chicken Fillets (1kg) (USD)",
                "Tomato (1kg) (USD)","Potato (1kg) (USD)"]].mean(axis=1)
df["transport"] = df[['One-way Ticket (Local Transport) (USD)','Monthly Pass (Regular Price) (USD)','Gasoline (1 liter) (USD)']].mean(axis=1)
df["costs_of_living"]= df[["housing", "food", "transport"]].mean(axis=1)
df_country = df.groupby("country", as_index=False).mean(numeric_only=True)

#Charts
#Average salaries in countries
top = df_country.sort_values("Average Monthly Net Salary (After Tax) (USD)", ascending=False).head(5)
bottom = df_country.sort_values("Average Monthly Net Salary (After Tax) (USD)", ascending=True).head(5)
top["group"]= "Top"
bottom["group"]= "Bottom"
df_combined = pd.concat([top,bottom])
df_combined = df_combined.sort_values("Average Monthly Net Salary (After Tax) (USD)", ascending=False)
plt.figure(figsize=(14,8))
sns.barplot(x="Average Monthly Net Salary (After Tax) (USD)", y="country", hue="group", data=df_combined)
plt.title("Top and bottom average salaries in countries")
plt.tight_layout()
plt.show()

#costs of living in countries
top = df_country.sort_values("costs_of_living", ascending=False).head(5)
bottom = df_country.sort_values("costs_of_living", ascending=True).head(5)
top["group"]= "Top"
bottom["group"]= "Bottom"
df_combined = pd.concat([top,bottom])
df_combined = df_combined.sort_values("costs_of_living", ascending=False)
plt.figure(figsize=(14,8))
sns.barplot(x="costs_of_living", y="country", hue="group", data=df_combined)
plt.title("Top and bottom average costs living")
plt.tight_layout()
plt.show()

#costs of living vs salary
plt.figure(figsize=(14,8))
sns.scatterplot(x="costs_of_living", y="Average Monthly Net Salary (After Tax) (USD)", data=df_country)
Poland = df_country[df_country["country"] == "Poland"]
plt.scatter(
    Poland["costs_of_living"],
    Poland["Average Monthly Net Salary (After Tax) (USD)"],
    color= "red",
    label= "Poland",)

plt.title("Average salary vs costs of living")
plt.xlabel("Costs of living")
plt.ylabel("Average Monthly Net Salary")
plt.legend()
plt.tight_layout()
plt.show()

#regression line
plt.figure(figsize=(14,8))
sns.regplot(data=df_country, x="costs_of_living", y="Average Monthly Net Salary (After Tax) (USD)", scatter_kws={"alpha":0.7} )
x = df_country[["costs_of_living"]]
y = df_country["Average Monthly Net Salary (After Tax) (USD)"]
model = LinearRegression()
model.fit(x,y)
r2 = model.score(x,y)
plt.text(0.05,0.95, f"R2={r2:.2f}",
         transform = plt.gca().transAxes,
         fontsize = 12, verticalalignment='top',
         bbox=dict(boxstyle="round", fc="w", alpha=0.7))




plt.title("Average salary vs costs of living (regression line)")
plt.xlabel("Costs of living")
plt.ylabel("Average Monthly Net Salary (After Tax)")
plt.tight_layout()
plt.show()

#best countries to live in
df_country["quality_of_life"]= (df_country["Average Monthly Net Salary (After Tax) (USD)"]-df_country["costs_of_living"])
bests = df_country.sort_values("quality_of_life", ascending=False).head(10)
plt.figure(figsize=(14,8))
sns.barplot(x="quality_of_life", y="country", data=bests)
plt.title("Best countries to live in")
plt.xlabel("Quality of life")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

#world map (quality of life)
fig = px.choropleth(
    df_country,
    locations="country",
    locationmode="country names",
    color="quality_of_life",
    hover_name = "country",
    color_continuous_scale= "RdYlGn",
    title= "Quality of life in Countries")

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True))
fig.show()