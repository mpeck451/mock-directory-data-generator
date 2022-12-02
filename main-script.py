import sys
import csv
import random
import names
import departments
import nurse_units
from datetime import datetime

# 1 - Initialize Variables and Functions
print("Script Start...")
time_stamp = datetime.now().strftime("%m-%d-%Y-%H%M%S")
new_data = []
directory_type = sys.argv[2] or 'Employee'
employee_fields = ['Primary Key', 'First Name', 'Last Name', 'Department', 'Home Phone', 'SMS', 'Office Phone', 'Alternate Phone', 'Pager', 'Email']
patient_fields = ['Primary Key', 'Last Name', 'First Name', 'DOB', 'Nurse Unit', 'Room', 'Bed', 'Room Ext', 'Nurse Ext', 'MRN', 'Facility', 'Admit Date', 'Discharge Date', 'Deceased', 'Privacy', 'Sex']
try:
    number_of_listings = int(sys.argv[1])
except:
    number_of_listings = 100
    print("No argument passed. Total defaults to 100 listings.")
pk_counter = 1001
email_domain = 'fakehospital.org'

def generate_10_digit_number(chance_for_empty):
    new_number = ('555' + str(random.randint(1000000, 9999999))) if random.randint(1, 100) > chance_for_empty else ''
    return new_number

# Generate New Listings
while number_of_listings > 0:
    cell_phone = generate_10_digit_number(25)
    random_first_name = names.generate_name('first')
    random_last_name = names.generate_name('last')
    new_employee_listing = {
        'Primary Key': pk_counter,
        'First Name': random_first_name,
        'Last Name': random_last_name,
        'Department': departments.generate_department(),
        'Home Phone': cell_phone,
        'SMS': cell_phone if random.randint(1, 100) > 15 else '',
        'Office Phone': generate_10_digit_number(75),
        'Alternate Phone': generate_10_digit_number(50) if len(cell_phone) == 10 else '',
        'Pager': generate_10_digit_number(85),
        'Email': random_first_name[0].lower() + random_last_name.lower() + "@" + email_domain
    }
    new_patient_listing = {
        'Primary Key': pk_counter,
        'Last Name': random_last_name,
        'First Name': random_first_name,
        'DOB': '',
        'Nurse Unit': '',
        'Room': 0,
        'Bed': 0,
        'Room EXT': 0,
        'Nurse Ext': 0,
        'MRN': 0,
        'Facility': '',
        'Admit Date': '',
        'Discharge Date': '',
        'Deceased': False,
        'Privacy': True,
        'Sex': ''
    }
    new_data.append(new_employee_listing)
    number_of_listings -= 1
    pk_counter += 1
print(new_data)

# Create New TSV File
with open(f'../mock-data-files/mock-data-{time_stamp}.tsv', 'w', newline='') as mock_data_file:
    mock_data_writer = csv.DictWriter(mock_data_file, delimiter='\t', fieldnames=employee_fields)
    mock_data_writer.writeheader()
    for listing in new_data:
        mock_data_writer.writerow(listing)

# Finalize
print("...Script End")