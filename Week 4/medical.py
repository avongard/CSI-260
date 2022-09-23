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
    _next_id = 1

    def __init__(self, name, address, phone, emergency_name, emergency_phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

        print("Initializing patient...".format(self.name))
        Patient.all_patients[self._next_id] = self


Michael_Portegello = Patient('Michael Portegello', '348 College Street', '732-252-3575', 'Roberta Portegello',
                             '732-614-8775')
