import random
import json

male_names = []
female_names = []
surnames = []

with open('names/surnames.json') as surnames_json:
    surnames = json.load(surnames_json)

with open('names/firstnames_m.json') as male_names_json:
    male_names = json.load(male_names_json)

with open('names/firstnames_f.json') as female_names_json:
    female_names = json.load(female_names_json)

def generate_name():
    if random.randint(0, 1):
        first_names = female_names
        gender = 'female'
    else:
        first_names = male_names
        gender = 'male'
    new_name = {
        'first_name': first_names[random.randint(0, (len(first_names) - 1))],
        'surname': surnames[random.randint(0, (len(surnames) - 1))],
        'gender': gender
    }
    return new_name
        