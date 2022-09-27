"""A management system for medical information that takes a users personal information and procedure information.
The information is attached to a unique ID that can be used to get this information through menus.

Author: Michael Portegello
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: September 27, 2022, 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
import pickle


class Patient:
    """"Protected list of all patients"""
    _all_patients = {}
    """Protected value for the next user ID"""
    _next_user_id = 1

    def __init__(self, name, address, phone, emergency_name, emergency_phone):
        """Initializes patient data"""
        self.name = name
        self.address = address
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone
        self.user_id = self._next_user_id

        print(f'Initializing patient...{self.name}')
        Patient._all_patients[self._next_user_id] = self
        print(f'{self.name} has been added to the database with an ID of {self.user_id}.')
        """Adds patient to list of all patients"""
        Patient._next_user_id += 1
        """Increments user id for the next user to be initialized"""

    def __str__(self):
        return f'Patient: {self.name} Address: {self.address} Phone: {self.phone} Emergency Contact: {self.emergency_name} Emergency Contact Phone: {self.emergency_phone} '

    def add_procedure(self):
        """Adds a procedure for the patient"""
        procedure_name = input('What is the name of the procedure?')
        procedure_date = input('What is the date of the procedure?')
        name = Procedure(procedure_name, procedure_date)

    @classmethod
    def get_patient(cls, user_id):
        """Returns information about the patient with corresponding ID"""
        return cls._all_patients[user_id]

    @classmethod
    def delete_patient(cls, user_id):
        """Deletes a patient with corresponding ID number from database"""
        del cls._all_patients[user_id]
        print('User has been deleted.')

    @classmethod
    def save_patients(cls):
        """Saves a list of patients to /all.patients.pkl"""
        with open('all_patients.pkl', 'wb') as f:
            pickle.dump(Patient._all_patients, f)
            print('Current patients have been saved to /all_patients.pkl')

    @classmethod
    def load_patients(cls):
        """Loads a list of patients from /all.patients.pkl"""
        with open('all_patients.pkl') as f:
            all_patients = pickle.load(f)
            print('Patients loaded from /all_patients.pkl')


class Procedure:
    _all_procedures = {}
    _next_procedure_id = 1

    def __init__(self, procedure_name, procedure_date):
        """Initializes patients procedure name and date, assign procedure number, increment procedure id"""
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.procedure_id = self._next_procedure_id
        Procedure._all_procedures[self._next_procedure_id] = self
        print(f'{self.name} has been added to the database.')
        Procedure._next_procedure_id += 1

    def __str__(self):
        return f'Procedure Name: {self.procedure_name} Procedure Date: {self.procedure_date}'

