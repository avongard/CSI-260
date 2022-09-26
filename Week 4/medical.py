"""DESCRIPTION OF THE MODULE GOES HERE

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


class Patient:
    _all_patients = {}
    _next_user_id = 1

    def __init__(self, name, address, phone, emergency_name, emergency_phone):
        """Initializes patient data, assigns id number, and increments id number for next user."""
        self.name = name
        self.address = address
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone
        print(f'Initializing patient...{self.name}')
        Patient._all_patients[self._next_user_id] = self
        print(f'{self.name} has been added to the database.')
        _next_id = self._next_user_id + 1

    def __str__(self):
        return Procedure.__str__()

    def add_procedure(self):
        """Adds a procedure for the patient"""
        # Adds procedure to patient

    @classmethod
    def get_patient(cls):

    @classmethod
    def delete_patient(cls):

    @classmethod
    def save_patients(cls):

    @classmethod
    def load_patients(cls):

class Procedure:
    _next_procedure_id = 1

    def __init__(self, procedure_name, procedure_date):
        """Initializes patients procedure name and date, assign procedure number, increment procedure id"""
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        # Assign ID number to new procedure
        # Increment ID number for next user

    def __str__(self):
        return f'Patient: {self.name} Address: {self.address} Phone: {self.phone} Emergency Contact: {self.emergency_name} Emergency Contact Phone: {self.emergency.phone} Procedure Name: {self.procedure_name} Procedure Date: {self.procedure_date}'


Michael_Portegello = Patient('Michael Portegello', '348 College Street', '732-252-3575', 'Roberta Portegello',
                             '732-614-8775')
Robert_Portegello = Patient('Robert Portegello', '37 Stratford Lane', '732-252-3577', 'Roberta Portegello',
                            '732-614-8775')
