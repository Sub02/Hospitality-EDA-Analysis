import pandas as pd
from matplotlib import pyplot as plt

# Exploring all Data
df_bookings =pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\fact_bookings.csv")
df_date=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_date.csv")
df_hotels=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_hotels.csv")
df_rooms=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_rooms.csv")
df_agg_bookings=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\fact_aggregated_bookings.csv")

# Taking Column Overview
'''
print("Booking Dataset :\n", df_bookings.head(4))
print("Date Dataset :\n",df_date.head(4))
print("Booking Dataset :\n", df_hotels.head(4))
print("Rooms Dataset :\n",df_rooms.head(4))
print("Agg Booking Dataset :\n",df_agg_bookings.head(4))
'''


# Checking data sets Shapes
booking_shape=df_bookings.shape
date_shape=df_date.shape
hotels_shape=df_hotels.shape
rooms_shape=df_rooms.shape
agg_bookings_shape=df_agg_bookings.shape


# gone through all Category shares in the data

unique_rooms=df_bookings.room_category.unique()
print(unique_rooms)
hotel_category_share=df_hotels.category.value_counts()
print(hotel_category_share)
booking_platform_list=df_bookings.booking_platform.unique()
print(booking_platform_list)

#BOOKINGS

# Total types of bookings
booking_platform_shares=df_bookings.booking_platform.value_counts()

#Cheking data trend

# Bookings
plt.figure()
booking_platform_shares.plot(kind="barh", title="Booking Platform Distribution")
plt.xlabel("Count")
plt.ylabel("Platform")
plt.show()

# Hotels
plt.figure()
df_hotels["category"].value_counts().sort_values().plot(kind="barh", title="Hotel Category Distribution")
plt.xlabel("Count")
plt.ylabel("Category")
plt.show()


# Exploring KPI basic data overview

#Checking stats of booking
booking_data_stats=df_bookings.describe()
print(booking_data_stats)

# Understanding Revenue features
min_rev=df_bookings.revenue_generated.min()
max_rev=df_bookings.revenue_generated.max()
print(min_rev)


# Hotel type transactional summary
hotel_category_share=df_hotels.category.value_counts()
print(hotel_category_share)





