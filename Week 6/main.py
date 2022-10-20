"""Week 6 Library Project

Author: Michael Portegello
Class: CSI-260-01
Assignment: Library Project
Due Date: 10/14/2022 11:59 PM

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
from libraryitem import LibraryItem
import catalog

menu: str = """
Library Catalog Menu

1. Search catalog
2. Print the entire catalog
3. Add item to catalog
4. Remove item from catalog
5. Exit

Choose an option: 
"""

while True:
    print(menu)
    choice = input()
    try:
        int_user_input = int(choice)
    except ValueError:
        print("Please enter an integer value 1-5.")
    try:
        int(choice) < 6
    except ValueError:
        print("Please enter a number from the options above.")

    if choice == '1':  # Search catalog
        catalog.search_list()
    if choice == '2':  # Print entire catalog
        catalog.print_list()
    if choice == '3':  # Add item to catalog
        catalog.add_list()
    if choice == '4':  # Remove item from catalog
        catalog.remove_list()
    if choice == '5':  # Exit
        sys.exit()