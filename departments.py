import random

clinical = ['Casualty', 'Operating Theatre', 'Intensive Care Unit', 'Anesthesiology', 'Cardiology', 'ENT', 'Geriatric', 'Gastroenterology', 'General Surgery', 'Haematology', 'Pediatrics', 'Neurology', 'Oncology', 'Opthalmology', 'Orthopaedic', 'Urology', 'Psychiatry', 'Inpatient', 'Outpatient']
support = ['Pharmacy', 'Radiology', 'Clinical Pathology', 'Nutrition and Dietetics', 'Catering and Food Services', 'Central Sterilization Unit', 'Housekeeping']
technical = ['Clinical Engineering', 'Information Technology and Communication', 'Engineering Services']
administrative = ['Medical Records', 'Human Resources', 'Finance', 'Administration']
departments_list = [clinical, support, technical, administrative]

def generate_department():
    department_type = departments_list[random.randint(0, (len(departments_list) - 1))]
    new_department = department_type[random.randint(0, (len(department_type) - 1))]
    return new_department