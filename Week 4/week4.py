"""A menu system for the management of a patient. Function to add, delete, get, modify patient information. Aswelll as add
procedures for that patient saving and loading the list through the menu.

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


import sys
from medical import Patient, Procedure

menu: str = """
Enter a number 1-3:
1. Look up a patient with ID number
2. Add a new patient
3. Exit
"""

menu2: str = """
Enter a number 1-4:
1. Modify patient attributes
2. Delete a patient
3. Add a procedure
4. Exit
"""

while True:
    print(menu)
    choice = input()

    try:
        int_user_input = int(choice)
    except ValueError:
        print("Please enter an integer value 1-3.")

    try:
        int(choice) < 4
    except ValueError:
        print("Please enter a number from the options above.")

    if choice == '1':  # Look up patient by ID
        Patient.load_patients()
        input_id = input('What is the patients ID number?')
        if input_id in Patient._all_patients:
            print(Patient.get_patient(input_id))
            print(menu2)
            choice = input()
            try:
                int_user_input = int(choice)
            except ValueError:
                print("Please enter an integer value 1-3.")

            try:
                int(choice) < 4
            except ValueError:
                print("Please enter a number from the options above.")

            if choice == '1': # Modify patient attributes
                print(menu)

            if choice == '2': # Delete a patient
                Patient.delete_patient()
                print(menu)

            if choice == '3': # Add a procedure
                procedure_name = input('What is the name of the procedure?')
                procedure_date = input('What is the date of the procedure?')
                name = Procedure(procedure_name, procedure_date)

            if choice == '4': # Exit
                print(menu)
        else:
            print(menu)

    if choice == '2': # Add a new patient
        name = input('What is the patients name seperated by an underscore?')
        address = input('What is the patients address?')
        phone = input('What is the patients phone number?')
        emergency_contact = input('What is the name of the patients emergency contact?')
        emergency_phone = input('What is the phone number of the patients emergency contact?')
        name = Patient(name,address,phone,emergency_contact, emergency_phone)
        Patient.save_patients()

    if choice == '3':  # Exit menu
        Patient.save_patients()
        sys.exit()
