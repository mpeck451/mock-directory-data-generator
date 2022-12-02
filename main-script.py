import sys
import csv
import random
import names
import departments
import patient_locations
from datetime import datetime

# 1 - Initialize Variables and Functions
print("Script Start...")
time_stamp = datetime.now().strftime("%m-%d-%Y-%H%M%S")

try:
    number_of_listings = int(sys.argv[1])
except:
    number_of_listings = 100
    print("No argument passed. Total defaults to 100 listings.")
try:
    directory_type = sys.argv[2]
except:
    directory_type = 'employee'

new_data = []
employee_fields = ['Primary Key', 'First Name', 'Last Name', 'Department', 'Home Phone', 'SMS', 'Office Phone', 'Alternate Phone', 'Pager', 'Email']
patient_fields = ['Primary Key', 'Last Name', 'First Name', 'DOB', 'Nurse Unit', 'Room', 'Bed', 'Room Ext', 'Nurse Ext', 'MRN', 'Facility', 'Admit Date', 'Discharge Date', 'Deceased', 'Privacy', 'Sex']
pk_counter = 1001
email_domain = 'fakehospital.org'

def generate_10_digit_number(chance_for_empty):
    new_number = ('555' + str(random.randint(1000000, 9999999))) if random.randint(1, 100) > chance_for_empty else ''
    return new_number

def generate_date(type):
    match type:
        case 'dob':
            new_date = f"{random.randint(1,12)}/{random.randint(1, 28)}/{random.randint(1922, 2020)}"
        case 'discharge':
            new_date = f"11/{random.randint(1, 28)}/2022"
        case 'admit':
            new_date = f"{random.randint(8,10)}/{random.randint(1, 28)}/2022"
    return new_date

# Generate New Listings
while number_of_listings > 0:
    cell_phone = generate_10_digit_number(25)
    random_name = names.generate_name()
    is_discharged_or_deceased = False if random.randint(1, 100) > 10 else True
    is_deceased = 'Yes' if is_discharged_or_deceased and random.randint(1, 100) > 75 else ''
    is_discharged = 'Yes' if is_discharged_or_deceased and not is_deceased else ''
    if (directory_type != 'employee'):
        new_listing = {
            'Primary Key': pk_counter,
            'Last Name': random_name['surname'],
            'First Name': random_name['first_name'],
            'DOB': generate_date('dob'),
            'Nurse Unit':patient_locations.generate_nurse_unit(is_discharged_or_deceased),
            'Room':patient_locations.generate_room(is_discharged_or_deceased),
            'Bed':patient_locations.generate_bed(is_discharged_or_deceased),
            'Room Ext': patient_locations.generate_room_ext(is_discharged_or_deceased),
            'Nurse Ext':patient_locations.generate_nurse_ext(is_discharged_or_deceased),
            'MRN': patient_locations.generate_mrn(is_discharged_or_deceased),
            'Facility': patient_locations.generate_facility(is_discharged_or_deceased),
            'Admit Date': generate_date('admit'),
            'Discharge Date': generate_date('discharge') if is_discharged else '',
            'Deceased': is_deceased,
            'Privacy': 'Yes' if random.randint(1, 100) > 50 and not is_discharged_or_deceased else 'No',
            'Sex': random_name['gender']
        }
    else:
        new_listing = {
            'Primary Key': pk_counter,
            'First Name': random_name['first_name'],
            'Last Name':  random_name['surname'],
            'Department': departments.generate_department(),
            'Home Phone': cell_phone,
            'SMS': cell_phone if random.randint(1, 100) > 15 else '',
            'Office Phone': generate_10_digit_number(75),
            'Alternate Phone': generate_10_digit_number(50) if len(cell_phone) == 10 else '',
            'Pager': generate_10_digit_number(85),
            'Email': random_name['first_name'][0].lower() + random_name['surname'].lower() + "@" + email_domain
        }
    new_data.append(new_listing)
    number_of_listings -= 1
    pk_counter += 1
print(new_data)

# Create New TSV File
with open(f'../mock-data-files/mock-{directory_type}-data-{time_stamp}.tsv', 'w', newline='') as mock_data_file:
    mock_data_writer = csv.DictWriter(mock_data_file, delimiter='\t', fieldnames = patient_fields if directory_type == 'patient' else employee_fields)
    mock_data_writer.writeheader()
    for listing in new_data:
        mock_data_writer.writerow(listing)

# Finalize
print("...Script End")