import csv

# Define constants (lists)
GHANA_PHONE_LENGTH = 10

def phonenumber_has_countrycode(row):

    if row[34].contains(':::'):
        splitted_phone_numbers = row[34].split(':::')
        for number in splitted_phone_numbers:
            

    # Check if phone starts with country code
    return row[34].startswith("+")

def modify_phone_number(row):
    original_number = row[34]
    print("original number is: " + original_number)

    #remove all white spaces from number
    original_number = original_number.replace(" ","")

    if len(str(original_number)) == GHANA_PHONE_LENGTH:
        modified_number = original_number[1:]
        modified_number = '+233' + modified_number
        print("modified number is: " + modified_number)
        row[34] = modified_number
    return row

def print_index(input_list):
    # Check if the list is not empty
    if input_list:
        print(input_list[34])
    else:
        print("Input list is empty.")

with open('contacts_1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("original row: ", row)
        if phonenumber_has_countrycode(row) == False:
            print("modified row: ", modify_phone_number(row))