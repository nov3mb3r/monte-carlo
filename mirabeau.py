import os
import sys
import csv
import glob
import argparse
import pandas as pd
import geoip2.database

parser = argparse.ArgumentParser()
parser.add_argument("path_to_csv")
parser.add_argument("output_directory")
args = parser.parse_args()
path = args.path_to_csv
outdir = args.output_directory

#handle directory input
os.chdir(path)
extension = "csv"
files = glob.glob('*.{}'.format(extension))

#handle output directory
if not os.path.isdir(outdir):
	os.mkdir(outdir)

#call geolocation db
ipreader = geoip2.database.Reader('/path/to/GeoLiteDB.mmdb')

#fore each file, find the ClientIP column and geolocate the value
for file in files:
	country_list=[]
	df = pd.read_csv(file)

	for ip in df["ClientIP"]:
		match = ipreader.country(ip)
		cname = match.country.name
		country_list.append(cname)

#write the output to a new csv
	df["Country"] = country_list
	outfile = file.split(".")[0]+"GEO.csv"
	out = outdir+"/"+outfile
	df.to_csv(out, index=False)
