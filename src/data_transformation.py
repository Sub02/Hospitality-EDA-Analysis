import pandas as pd

# All Data set importations
df_date=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_date.csv")
df_hotels=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_hotels.csv")
df_rooms=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\dim_rooms.csv")
df_agg_bookings=pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\fact_aggregated_bookings.csv")
df_bookings =pd.read_csv(r"C:\Users\kundu\OneDrive\Desktop\Desktop\STAGE_0\DATA ANALYSIS\CODE_BASICS\PYTHON\PROJECT_1\PROJECT_1\source-code\3_project_hospitality_analysis\datasets\fact_bookings.csv")

#Checking column names
print(df_agg_bookings.info())

# feature Engineering

# Occupancy percentage column addition
df_agg_bookings["occ_pct"]= df_agg_bookings["successful_bookings"]/df_agg_bookings["capacity"]
df_agg_bookings["occ_pct"]= df_agg_bookings["occ_pct"].apply(lambda x: round(x*100,2))
print(df_agg_bookings.head(2))
