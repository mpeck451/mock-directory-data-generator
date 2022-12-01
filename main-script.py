import sys
import csv
import random
import names
import departments
from datetime import datetime

# 1 - Initialize Variables and Functions
print("Script Start...")
time_stamp = datetime.now().strftime("%m-%d-%Y-%H%M%S")
new_data = []
fields = ['Primary Key', 'First Name', 'Last Name', 'Department', 'Home Phone', 'SMS', 'Office Phone', 'Alternate Phone', 'Pager', 'Email']
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
    new_listing = {
        'Primary Key': pk_counter,
        'First Name': random_first_name,
        'Last Name': random_last_name,
        'Department': departments.generate_department(),
        'Home Phone': cell_phone,
        'SMS': cell_phone,
        'Office Phone': generate_10_digit_number(75),
        'Alternate Phone': generate_10_digit_number(90) if type(cell_phone) == 'int' else '',
        'Pager': generate_10_digit_number(85),
        'Email': random_first_name[0].lower() + random_last_name.lower() + "@" + email_domain
    }
    new_data.append(new_listing)
    number_of_listings -= 1
    pk_counter += 1
print(new_data)

# Create New TSV File
with open(f'../mock-data-files/mock-data-{time_stamp}.tsv', 'w', newline='') as mock_data_file:
    mock_data_writer = csv.DictWriter(mock_data_file, delimiter='\t', fieldnames=fields)
    mock_data_writer.writeheader()
    for listing in new_data:
        mock_data_writer.writerow(listing)

# Finalize
print("...Script End")