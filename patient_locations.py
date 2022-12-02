import random

units = ['ICU', 'ER', 'NICU', 'PACU', 'CCU', 'SICU', 'PCU', 'Psych']
facilities = ['North Campus', 'East Campus', 'South Campus', 'West Campus']
rooms = []
beds = []
room_exts = []
nurse_exts = []
mrns = []

def generate_nurse_unit():
    return units[random.randint(0, (len(units) - 1))]

def generate_facility():
    return facilities[random.randint(0, (len(facilities) - 1))]

def generate_room():
    pass

def generate_bed():
    pass

def generate_room_ext():
    pass

def generate_nurse_ext():
    pass

def generate_mrn():
    pass