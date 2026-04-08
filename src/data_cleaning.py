import pandas as pd

# All Data set importations
df_date=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_date.csv")
df_hotels=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_hotels.csv")
df_rooms=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_rooms.csv")
df_agg_bookings=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\fact_aggregated_bookings.csv")
df_bookings =pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\fact_bookings.csv")

# Checking for values formats

# Bookings Values
value_check_bookings=df_bookings.describe()
print("\n")
print(value_check_bookings)

# Error found in values[No. of Guests]
print(df_bookings[df_bookings.no_guests<=0])
print("\n")
'''Negative values found in number of guests'''

df_bookings=df_bookings[df_bookings.no_guests > 0]

''' Now data is cleaned as per the No of Guests'''


# Checking atributes validity
min_bookings=df_bookings.revenue_generated.min()
max_booking=df_bookings.revenue_generated.max()

print(f"Max booking ammount is : {max_booking}\n")
print(f"Min booking ammount is : {min_bookings}\n")

# Outlier Detection

avg_rev=df_bookings.revenue_generated.mean()
std_rev=df_bookings.revenue_generated.std()
# setting limits of standard deviation
higher_limit=avg_rev + 3*std_rev
print(f"The higher limit is : {higher_limit}")
lower_limit=avg_rev-3*std_rev
print(f"The lower limit is : {lower_limit}")
# finding outliers
print(df_bookings[df_bookings.revenue_generated>higher_limit])

# Refining the data[3-Standard_Deviation Check]
df_bookings=df_bookings[df_bookings.revenue_generated<=higher_limit]
df_bookings=df_bookings[df_bookings.revenue_generated>lower_limit]
print(df_bookings.shape)

#Checking actual earning Data
print(df_bookings.revenue_realized.describe())

# Business number checking for data Actualization

# Outliers Check
avg_rev_realized=df_bookings.revenue_realized.mean()
std_rev_realized=df_bookings.revenue_realized.std()
# setting limits of standard deviation
higher_limit_realized=avg_rev_realized + 3*std_rev_realized
print(f"The higher limit is : {higher_limit_realized}")
lower_limit_realized=avg_rev_realized-3*std_rev_realized
print(f"The lower limit is : {lower_limit_realized}")
print(df_bookings[df_bookings.revenue_realized>higher_limit])

#Checking cost validation using room category values
print(df_rooms)
print(df_bookings[df_bookings.room_category=="RT4"].revenue_realized.describe())
print(23439+3*9048)
# As the actual higher value of revenue_realized is under the calculated range of revenue_realized

#checking null values

print(df_bookings.isnull().sum())


''' Only the ratings are showing null values & its completely fine because
 its not mandate for customers to give rating always after departure'''
