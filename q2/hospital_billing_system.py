class Patient:
    def __init__(self, name, bill_amount): # Defines the attributes of the class Patient
        self.__name = name
        self.__bill_amount = bill_amount

    @property
    def name(self):
        return self.__name # Returns the name of the patient

    @name.setter
    def name(self, given_name):
        self.__name = given_name # Sets the name of the patient

    @property
    def bill_amount(self):
        return self.__bill_amount # Returns the bill amount of the patient

    @bill_amount.setter
    def bill_amount(self, value): # Sets the bill amount of the patient
        self.__bill_amount = value

    def calculate_bill(self):
        return self.__bill_amount # Returns the total bill amount of the patient

    def display_patient_type(self):
        return "Regular Patient" # To identify the patient as a regular patient

class Senior_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount) # Calls the constructor of the parent class Patient

    def calculate_bill(self):
        return self.bill_amount * 0.8 # Returns the total bill amount of the senior patient after applying a 20% discount

    def display_patient_type(self):
        return "Senior Citizen" # To identify the patient as a senior citizen

class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount) # Calls the constructor of the parent class Patient

    def calculate_bill(self):
        return self.bill_amount * 0.85 # Returns the total bill amount of the PhilHealth member after applying a 15% discount

    def display_patient_type(self):
        return "PhilHealth Member" # To identify the patient as a PhilHealth member

patient1 = Patient("Juan Dela Cruz", 15000.00)
patient2 = Senior_Patient("Maria Santos", 15000.00)
patient3 = PhilHealth_Patient("Pedro Reyes", 15000.00)

print("Hospital Billing System")
print("-----------------------")
print(f"Patient Name: {patient1.name} \nPatient Type: {patient1.display_patient_type()} \nOriginal Bill: {patient1.bill_amount:,.2f} \nFinal Bill: {patient1.calculate_bill():,.2f}")
print(f"\nPatient Name: {patient2.name} \nPatient Type: {patient2.display_patient_type()} \nOriginal Bill: {patient2.bill_amount:,.2f} \nFinal Bill: {patient2.calculate_bill():,.2f}")
print(f"\nPatient Name: {patient3.name} \nPatient Type: {patient3.display_patient_type()} \nOriginal Bill: {patient3.bill_amount:,.2f} \nFinal Bill: {patient3.calculate_bill():,.2f}")