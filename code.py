# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns= {'Total': 'Total_Medals'} , inplace = True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both' ,data['Better_Event'])
better_event = (data['Better_Event'].value_counts()).idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[-1:], inplace=True)

def top_ten(top_countries, column):
    country_list = []
    top_10 = top_countries.nlargest(10, column)
    country_list = top_10.loc[:,"Country_Name"]
    return country_list

top_10_summer = list(top_ten(top_countries, "Total_Summer"))
top_10_winter = list(top_ten(top_countries, "Total_Winter"))
top_10 = list(top_ten(top_countries, "Total_Medals"))


common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))


# --------------
#Code starts here
summer_df = data[data["Country_Name"].isin(top_10_summer)]
winter_df = data[data["Country_Name"].isin(top_10_winter)]
top_df = data[data["Country_Name"].isin(top_10)]

plt.bar(summer_df["Country_Name"],summer_df["Total_Summer"])
plt.xlabel("Country")
plt.ylabel("Total Summer")
plt.xticks(rotation = 45)
plt.show()

plt.bar(winter_df["Country_Name"],winter_df["Total_Winter"])
plt.xlabel("Country")
plt.ylabel("Total Winter")
plt.xticks(rotation = 45)
plt.show()

plt.bar(top_df["Country_Name"],top_df["Total_Medals"])
plt.xlabel("Country")
plt.ylabel("Total Medals")
plt.xticks(rotation = 45)
plt.show()


# --------------
#Code starts here
summer_df["Golden_Ratio"] = (summer_df["Gold_Summer"] / summer_df["Total_Summer"])
summer_max_ratio = max(summer_df["Golden_Ratio"])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),"Country_Name"]

winter_df["Golden_Ratio"] = (winter_df["Gold_Winter"] / winter_df["Total_Winter"])
winter_max_ratio = max(winter_df["Golden_Ratio"])
winter_country_gold = winter_df.loc[winter_df["Golden_Ratio"].idxmax(),"Country_Name"]

top_df["Golden_Ratio"] = top_df["Gold_Total"]/top_df["Total_Medals"] 
top_max_ratio = max(top_df["Golden_Ratio"])
top_country_gold = top_df.loc[top_df["Golden_Ratio"].idxmax(),"Country_Name"]



# --------------
#Code starts here
data_1 = data.iloc[:-1:]
data_1["Total_Points"] = (data_1["Gold_Total"]*3)+(data_1["Silver_Total"]*2)+(data_1["Bronze_Total"])
most_points = max(data_1["Total_Points"])
best_country = data_1.loc[data_1["Total_Points"].idxmax(),"Country_Name"]


# --------------
#Code starts here
best = data[data["Country_Name"]==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']].copy()
best.plot(kind='bar', stacked=True, figsize=(8,8))
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)
plt.show()


