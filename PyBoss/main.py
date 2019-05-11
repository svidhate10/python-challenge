# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:15:50 2019

@author: Shubha
"""

import os
import csv
import pandas as pd

# set the path for csv 
csvpath = os.path.join("..\\..", 'RUTJC201904DATA3','hw',"week3","ExtraContent","Instructions","PyBoss","employee_data.csv")

# Declare empty lists
fullname = []
firstname = []
lastname = []
date_of_birth = []
dob = []
ssn = []
ssnPrivate = []
abbrev = []
employeeid = []


# Dictionary containing states names as keys and abbreviations as values (provided) 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open CSV 
with open(csvpath,newline="") as employee_data:
    csvreader = csv.reader(employee_data,delimiter=",") 

    # Skip the header 
    csvheader = next(csvreader)     
    
    # Iterate through each row stored in csvreader
    for rows in csvreader:

    
        employeeid.append(rows[0])


        # Split full name into first name and last name lists 
    
        fullname = rows[1].split(" ")   
        firstname.append(fullname[0])
        lastname.append(fullname[1])

        
        # Split the date of birth and append it to dob list
        date_of_birth = rows[2].split("-")
        dob.append(date_of_birth[1] + "/" + date_of_birth[2] + "/" + date_of_birth[0])
        

        # Split the SSN by "-"
        # Split the ssn and append it ssnPrivate
        ssn = rows[3].split("-")
        ssnPrivate.append("***-**-" + ssn[2])


        abbrev.append(us_state_abbrev[rows[4]])


new_df = pd.DataFrame({"Employee Id": employeeid, "First Name": firstname, "Last Name": lastname, "DOB": dob, "SSN":ssnPrivate, "State": abbrev})

# print formatted data in csv
new_df.to_csv(os.path.join("employee_data_formated.csv"), index=False, header=True)

print(new_df.head())