import pandas as pd
from matplotlib import pyplot as plt

# All Data set importations
df_date=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_date.csv")
df_hotels=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_hotels.csv")
df_rooms=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_rooms.csv")
df_agg_bookings=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\fact_aggregated_bookings.csv")
df_bookings =pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\fact_bookings.csv")

# Ad-Hoc Analysis


# Q1. What is the average occupancy rate in each of the room?

# Occupancy percentage column addition
df_agg_bookings["occ_pct"]= df_agg_bookings["successful_bookings"]/df_agg_bookings["capacity"]
df_agg_bookings["occ_pct"]= df_agg_bookings["occ_pct"].apply(lambda x: round(x*100,2))
print(df_agg_bookings.head(2))
# Grouping for categorical rooms
each_room_rate=df_agg_bookings.groupby("room_category")["occ_pct"].mean().round(2)
print(each_room_rate)
print("\n")
# Detailed Reporting of room category
print(df_rooms)
print("\n")
df_bookings_r_b=pd.merge(df_agg_bookings,df_rooms,left_on="room_category",right_on="room_id")
print(df_bookings_r_b)
print("\n")
# Q1. Solution
each_room_rate_detailed=df_bookings_r_b.groupby("room_class")["occ_pct"].mean().round(2)
print(each_room_rate_detailed)
print("\n")

# Dropping Unnecessary columns
df_bookings_r_b.drop("room_id",axis=1,inplace=True)
print(df_bookings_r_b)
print("\n")


# Q2. Give Average Occupancy Rate per City

# Transformation : Merging df_bookings_r_b with df_hotels to get City values
city_avg_rate=pd.merge(df_bookings_r_b,df_hotels,on="property_id")
print(city_avg_rate.head(1))
print("\n")
Q2_Sol=city_avg_rate.groupby("city")["occ_pct"].mean()
print(Q2_Sol)
print("\n")

#Trend Visuals of Q2
Q2_Sol.plot(kind="bar")
plt.show()


# Q3. When was the occupancy better? Weekday or Weekend?

# Checking for required data in the current data frame
print(df_bookings_r_b.head(2))
print("\n")

# Merging date data frame for the solution
weekday_weekend=pd.merge(city_avg_rate,df_date,left_on="check_in_date",right_on="date")
print(weekday_weekend.head(2))
print("\n")

# finding the ratios
weekday_weekend_ratio=weekday_weekend.groupby("day_type")["occ_pct"].mean().round(2)
print(weekday_weekend_ratio)
print("\n")


# Q4. In the month of June, What is the occupancy for different cities

# Checking for dates
print(weekday_weekend["mmm yy"].unique())
print("\n")

# Creating categorize Data Frame
df_june_22=weekday_weekend[weekday_weekend["mmm yy"]=="Jun 22"]
print(df_june_22.head(2))
print("\n")
# Grouping the occ_pct
Q4_sol=df_june_22.groupby("city")["occ_pct"].mean().round(2)
print(Q4_sol)
print("\n")
'''Bangalore has least occupancy in June'''


# Q5. New data addition request....
df_august=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\new_data_august.csv")
print(df_august.head(2))
print("\n")

#Checking columns & shape of data
print(df_august.columns)
print("\n")
print(weekday_weekend.columns)
print("\n")
print(df_august.shape)
print("\n")
print(weekday_weekend.shape)
print("\n")

# Concating columns for analysis
updated_data=pd.concat([weekday_weekend,df_august],ignore_index=True,axis=0)
print(updated_data.tail(2))
print("\n")
print(updated_data.shape)
print("\n")


# Q6. Revenue realized per city....

# Checking for data
print(df_bookings.head(2))
print("\n")
print(df_hotels.head(2))
print("\n")

# Creating needful data
df_hotel_revenue=pd.merge(df_hotels,df_bookings,on="property_id")
print(df_hotel_revenue.head(2))
print("\n")

Q6_sol=df_hotel_revenue.groupby("city")["revenue_realized"].sum()
print(Q6_sol)
print("\n")


# Q7. Show month by month revenue...

# Checking Data dependencies
print(df_bookings.head(2))
print(df_date["mmm yy"].unique())
df_month_by_rev=pd.merge(df_hotel_revenue,df_date,left_on="check_in_date",right_on="date")
print("\n")

'''no visible data found'''

# Checking the data formats
print(df_bookings.info())
print("\n")
print(df_date.info)
print("\n")

'''Merging attribute's data type is not compatible'''

# column type conversion

'''For  Dates'''
df_date["date"]=pd.to_datetime(
	df_date["date"],
	format="mixed",
	dayfirst=True
)
print(df_date.head(2))
print("\n")
print(df_date.info())
print("\n")
'''For Bookings'''
df_hotel_revenue["check_in_date"] = pd.to_datetime(
    df_hotel_revenue["check_in_date"],
    format="mixed",
    dayfirst=True
)
print(df_hotel_revenue.head(2))
print("\n")
print(df_hotel_revenue.info())
print("\n")

# Re-merging the data dependencies
df_month_by_rev=pd.merge(df_hotel_revenue,df_date,left_on="check_in_date",right_on="date")
print(df_month_by_rev.head(2))
print("\n")

Q7_sol=df_month_by_rev.groupby("mmm yy")["revenue_realized"].sum()
print(Q7_sol)
print("\n")


# Q8. Revenue Realized as per hotel type

# for data dependencies Merging booking data with hotel data using property_id

# This helps to bring hotel category (Luxury, Business, etc.) into booking dataset
rev_real = df_bookings.merge(df_hotels, on="property_id")

# Grouping data from hotel category and calculate total revenue
Q8_sol = rev_real.groupby("category")["revenue_realized"].sum()

# Sorting values in descending order to get highest values first
Q8_sol = Q8_sol.sort_values(ascending=False)

print(Q8_sol)


# Q9. What is the average rating per city ?

# Fulfilling Data Dependencies by Merging booking data with hotel data to get city attributes
df_city = df_bookings.merge(df_hotels, on="property_id")

# Grouping by city for all targeted attributes

# NaN values are automatically ignored
Q9_sol = df_city.groupby("city")["ratings_given"].mean()

# Rounding values for readability enhancement
Q9_sol = Q9_sol.round(2)

print(Q9_sol)
print("\n")


# Q10. Provide a pie chart of revenue realized per booking platform

# Grouping data by booking platform and calculate total revenue
platform_revenue = df_bookings.groupby("booking_platform")["revenue_realized"].sum()

# Plotting pie chart for revenue distribution visualization
platform_revenue.plot(
    kind="pie", # Pie chart
    autopct="%1.1f%%"  # Show percentage values
)

# Plotting features

# Title for clear understanding
plt.title("Revenue Distribution by Booking Platform")

# Remove unwanted plot labels
plt.ylabel("")

plt.show()
