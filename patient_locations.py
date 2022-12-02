import random

units = ['ICU', 'ER', 'NICU', 'PACU', 'CCU', 'SICU', 'PCU', 'Psych']
facilities = ['North Campus', 'East Campus', 'South Campus', 'West Campus']
rooms = []
beds = []
room_exts = []
nurse_exts = []
mrns = []

def generate_nurse_unit(is_deceased_or_discharged):
    return '' if is_deceased_or_discharged else units[random.randint(0, (len(units) - 1))]

def generate_facility(is_deceased_or_discharged):
    return '' if is_deceased_or_discharged else facilities[random.randint(0, (len(facilities) - 1))]

def generate_room(is_deceased_or_discharged):
    new_room = random.randint(100, 99999)
    return '' if is_deceased_or_discharged else new_room

def generate_bed(is_deceased_or_discharged):
    new_bed = random.randint(1, 99999)
    return '' if is_deceased_or_discharged else new_bed

def generate_room_ext(is_deceased_or_discharged):
    new_room_ext = random.randint(10000, 99999)
    if new_room_ext in room_exts:
        return generate_room_ext(is_deceased_or_discharged)
    else:
        room_exts.append(new_room_ext)
        return '' if is_deceased_or_discharged else new_room_ext

def generate_nurse_ext(is_deceased_or_discharged):
    new_nurse_ext = random.randint(10000, 99999)
    if new_nurse_ext in nurse_exts:
        return generate_nurse_ext(is_deceased_or_discharged)
    else:
        nurse_exts.append(new_nurse_ext)
        return '' if is_deceased_or_discharged else new_nurse_ext

def generate_mrn(is_deceased_or_discharged):
    new_mrn = random.randint(100000, 999999)
    if new_mrn in mrns:
        return generate_mrn(is_deceased_or_discharged)
    else:
        mrns.append(new_mrn)
        return '' if is_deceased_or_discharged else new_mrn