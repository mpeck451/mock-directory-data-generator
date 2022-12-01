import csv
import random
import names
import departments
from datetime import datetime

# 1 - Initialize Variables
print("Script Start...")
time_stamp = datetime.now().strftime("%m-%d-%Y-%H%M%S")
new_data = []
fields = ['Primary Key', 'First Name', 'Last Name', 'Department', 'Phone', 'SMS', 'Pager', 'Email']
number_of_listings = 3000
pk_counter = 1001
email_domain = 'fakehospital.org'

# Generate New Listings
while number_of_listings > 0:
    cell_phone = '555' + str(random.randint(1000000, 9999999))
    random_first_name = names.generate_name('first')
    random_last_name = names.generate_name('last')
    new_listing = {
        'Primary Key': pk_counter,
        'First Name': random_first_name,
        'Last Name': random_last_name,
        'Department': departments.generate_department(),
        'Phone': cell_phone,
        'SMS': cell_phone,
        'Pager': '555' + str(random.randint(1000000, 9999999)),
        'Email': random_first_name[0].lower() + random_last_name.lower() + "@" + email_domain
    }
    new_data.append(new_listing)
    number_of_listings -= 1
    pk_counter += 1
print(new_data)

# Create New TSV File
with open(f'mock-data-{time_stamp}.tsv', 'w') as mock_data_file:
    mock_data_writer = csv.DictWriter(mock_data_file, delimiter='\t', fieldnames=fields)
    mock_data_writer.writeheader()
    for listing in new_data:
        mock_data_writer.writerow(listing)

# Finalize
print("...Script End")