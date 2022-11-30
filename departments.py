import random

clinical = ['Casualty', 'Operating Theatre', 'Intensive Care Unit', 'Anesthesiology', 'Cardiology', 'ENT', 'Geriatric', 'Gastroenterology', 'General Surgery', 'Haematology', 'Pediatrics', 'Neurology', 'Oncology', 'Opthalmology', 'Orthopaedic', 'Urology', 'Psychiatry', 'Inpatient', 'Outpatient']
support = ['Pharmacy', 'Radiology', 'Clinical Pathology', 'Nutrition and Dietetics', 'Catering and Food Services', 'Central Sterilization Unit', 'Housekeeping']
technical = ['Clinical Engineering', 'Information Technology and Communication', 'Engineering Services']
administrative = ['Medical Records', 'Human Resources', 'Finance', 'Administration']

def generate_department():
    department_type = []
    new_department = ''
    match random.randint(1, 4):
        case 1:
            department_type = clinical
        case 2:
            department_type = support
        case 3:
            department_type = technical
        case 4:
            department_type = administrative
    new_department = department_type[random.randint(0, (len(department_type) - 1))]
    return new_department