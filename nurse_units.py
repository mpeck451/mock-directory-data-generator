import random

units = ['ICU', 'ER', 'NICU', 'PACU', 'CCU', 'SICU', 'PCU', 'Psych']

def generate_nurse_unit():
    new_unit = units[random.randint(0, (len(units) - 1))]
    return new_unit