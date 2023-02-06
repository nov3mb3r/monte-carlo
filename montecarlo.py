import pandas as pd
import geoip2.database
import os
import sys

# Get the folder path from the command line argument
folder_path = sys.argv[1]

# Initialize the GeoLite2 database reader
reader = geoip2.database.Reader("GeoLite2-City.mmdb")

# Function to geolocate the country of the IP address
def get_country(ip_address):
    try:
        response = reader.city(ip_address)
        return response.country.name
    except:
        return None

# Combine all the logs into one data frame
df = pd.concat([pd.read_csv(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if f.endswith(".csv")])

# Add the country information to the data frame
df["Country"] = df["ClientIP"].apply(get_country)

# Sort the data frame based on the CreationTime
df = df.sort_values("CreationTime")

# Split the data frame into different sheets based on the username
writer = pd.ExcelWriter("MonteCarlo.xlsx", engine='xlsxwriter')
for username, data in df.groupby("UserId"):
    data.to_excel(writer, sheet_name=username, index=False)
writer.save()
