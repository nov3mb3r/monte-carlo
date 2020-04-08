# monte-carlo

![](https://raw.githubusercontent.com/nov3mb3r/monte-carlo/master/monte%20carlo.PNG)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Monte Carlo is a collection of 3 tools to process Office 365 Unified audit logs in incident response investigations. It is extensible and breaks the processing tasks in 3 stages (sectors): 

 - Parse Office 365 unified audit log based on specfic operations
 - Geolocate the a user account login IPs
 - Import the processed csv files into one Excel spreadsheet with unique tabs for each user account

Named after the famous turns on the 3 sectors of Monte Carlo Grand Prix track

## Sector 1 - Sainte Devote: Parse the Office 365 Unified audit log

By default 3 properties are extracted: CreationTime, UserID, ClientIP, but can be extended according to the investigation needs.
A detailed list can be found on [Microsoft documentation](https://docs.microsoft.com/en-us/microsoft-365/compliance/detailed-properties-in-the-office-365-audit-log?view=o365-worldwide).

### Usage

```powershell
PS >.\sainte-devote.ps1 -path 'directory_of_Audit Logs' -output 'directory_of_parsed_logs'
```

## Sector 2 - Mirabeau: Geolocate Office 365 operations

The geolocation feature uses the python-geoip library. To install:
```
pip install python-geoip-geolite2
```
Make sure you have downloaded locally the geolocation from [MaxMind](https://dev.maxmind.com/geoip/geoip2/web-services/) abd add the path into mirabeau.py
### Usage
```
python3 mirabeau.py directory_of_parsed_logs output_directory
```

## Sector 3 - La Piscine: Import all processed files into Excel
### Usage

```powershell
PS >.\piscine.ps1 input_directory
```


### Todos

 - Integrate Sainte Devote and Mirabeau into one file
 - Add binaries

License
----

GPLv3
 
