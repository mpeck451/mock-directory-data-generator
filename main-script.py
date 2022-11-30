import csv
import random
import departments


# 1 - Initialize Variables
print("Script Start...")
new_data = []
fields = ['Primary Key', 'First Name', 'Last Name', 'Department', 'Phone', 'SMS', 'Pager', 'Email']
number_of_listings = 100
pk_counter = 1
email_domain = 'fakehospital.org'
test_listing = {
    'primary_key': 1,
    'first_name': "John",
    'last_name': "Smith",
    'department': "Cardiology",
    'phone': 5551234567,
    'sms': 5551234567,
    'pager': 5559876543,
    'email': "jsmith1@fakehospital.org"
}

# Generate New Listings
while number_of_listings > 0:
    cell_phone = '555' + str(random.randint(1000000, 9999999))
    random_first_name = 'John'
    random_last_name = 'Smith'
    new_listing = {
        'primary_key': pk_counter,
        'first_name': random_first_name,
        'last_name': random_last_name,
        'department': departments.generate_department(),
        'phone': cell_phone,
        'sms': cell_phone,
        'pager': '555' + str(random.randint(1000000, 9999999)),
        'email': random_first_name[0].lower() + random_last_name.lower() + "@" + email_domain
    }
    new_data.append(new_listing)
    number_of_listings -= 1
    pk_counter += 1

print(new_data)
# Finalize
print("...Script End")