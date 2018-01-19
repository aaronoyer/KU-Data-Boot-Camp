import os
import csv 

csvpath = os.path.join('Resources', 'employee_data_1.csv')

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

emp_id = []
first_name = []
last_name = []
dob =[]
ssn = []
state = []

with open(csvpath, 'r') as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp_id.append(row['Emp ID'])
        first_name.append(row['Name'].split(" ")[0])
        last_name.append(row['Name'].split(" ")[1])
        dob.append(row['DOB'])
        ssn.append('***-**-' + row['SSN'].split('-')[2])
        state.append(us_state_abbrev[row['State']])
        
new_data = zip(emp_id, first_name, last_name, dob, ssn, state)

output_file = os.path.join('Output', 'clean_emp_data_1.csv')

with open(output_file, 'w') as csvwrite:
    cleanfile = csv.writer(csvwrite, delimiter = ",")
    cleanfile.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    cleanfile.writerows(new_data)

with open(output_file, 'r') as readfile:
    print(readfile.read())

