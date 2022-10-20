catalog = []


def add_list():
    name = input("What is the name of the book?")
    isbn = input("What is the isbn of the book?")
    tag = input("What is the tag of the book?")
    item = list((name, isbn, tag))
    catalog.append(item)
    print(f'{name} has been added to the catalog.')


def remove_list():
    item_to_remove = input("What is the name of the item to remove?")
    item_to_remove = str(item_to_remove)
    for item in catalog:
        if item_to_remove in item:
            catalog.remove(item_to_remove)


def print_list():
    print(catalog)


def search_list():
    search_term = input("What is the name/isbn/tag of the book to search?")
    for item in catalog:
        if search_term in item:
            print(item)
