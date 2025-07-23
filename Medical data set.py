import csv

# Function to load list data from a CSV column
def load_list_data(csv_file, column_name):
    with open(csv_file, newline='') as csv_info:
        csv_dict = csv.DictReader(csv_info)
        return [row[column_name] for row in csv_dict]

# Define the full path to the CSV file
csv_path = 'C:/Users/hedge/Documents/Medical Project/insurance.csv'  

# Load data from each column in the CSV
ages = load_list_data(csv_path, 'age')
sexes = load_list_data(csv_path, 'sex')
bmis = load_list_data(csv_path, 'bmi')
num_children = load_list_data(csv_path, 'children')
smoker_statuses = load_list_data(csv_path, 'smoker')
regions = load_list_data(csv_path, 'region')
insurance_charges = load_list_data(csv_path, 'charges')

# Class to organize and analyze patient insurance data
class PatientsInfo:
    def __init__(self, ages, sexes, bmis, children, smokers, regions, charges):
        self.patients_ages = [int(age) for age in ages]
        self.patients_sexes = sexes
        self.patients_bmis = [float(bmi) for bmi in bmis]
        self.patients_num_children = [int(child) for child in children]
        self.patients_smoker_statuses = smokers
        self.patients_regions = regions
        self.patients_charges = [float(charge) for charge in charges]

    def analyze_ages(self):
        avg_age = sum(self.patients_ages) / len(self.patients_ages)
        return f"Average Patient Age: {round(avg_age, 2)} years"

    def analyze_sexes(self):
        females = self.patients_sexes.count('female')
        males = self.patients_sexes.count('male')
        return f"Count for female: {females}\nCount for male: {males}"

    def unique_regions(self):
        return list(set(self.patients_regions))

    def average_charges(self):
        avg_charge = sum(self.patients_charges) / len(self.patients_charges)
        return f"Average Yearly Medical Insurance Charges: {round(avg_charge, 2)} dollars"

    def create_dictionary(self):
        return {
            "age": self.patients_ages,
            "sex": self.patients_sexes,
            "bmi": self.patients_bmis,
            "children": self.patients_num_children,
            "smoker": self.patients_smoker_statuses,
            "region": self.patients_regions,
            "charges": self.patients_charges
        }

    def summary(self):
        print(self.analyze_ages())
        print(self.analyze_sexes())
        print("Unique regions:", self.unique_regions())
        print(self.average_charges())

# Instantiate and analyze patient data
patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
patient_info.summary()


patients_dict = patient_info.create_dictionary()