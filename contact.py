import csv

CONTACTS___CSV = 'contacts_1.csv'

GHANA_MOBILE_PHONE_LENGTH = 10
GERMANY_MOBILE_PHONE_LENGTH = 12


def phonenumber_does_not_have_countrycode(phone_column):
    print('value is digits',phone_column_contains_digits(phone_column))
    if phone_column.find(':::'):
        split_phone_numbers = phone_column.split(':::')
        for current_number in split_phone_numbers:
            if not current_number.startswith("+"):
                return True

    return not phone_column.startswith("+")

def phone_column_contains_digits(phone_column):
    if phone_column.find(':::'):
        splitted_phone_numbers = phone_column.split(':::')
        for current_number in splitted_phone_numbers:
            current_number = current_number.replace(" ", "")
            current_number = current_number.replace("+", "")
            if current_number.isdigit():
                return current_number.isdigit()
    phone_column = phone_column.replace(" ", "")
    phone_column = phone_column.replace("+", "")
    return phone_column.isdigit()

def modify_phone_number(phone_column):
    print("original number is: " + phone_column)
    formatted_phone = ""

    if phone_column.find(':::') != -1:
        splitted_phone_numbers = phone_column.split(':::')
        for index, current_number in enumerate(splitted_phone_numbers):
            # remove all white spaces from number
            current_number = current_number.replace(" ", "")
            if len(str(current_number)) == GHANA_MOBILE_PHONE_LENGTH:
                modified_number = current_number[1:]
                modified_number = '+233' + modified_number
                print("modified ghana number is: " + modified_number)
            if len(str(current_number)) == GERMANY_MOBILE_PHONE_LENGTH:
                modified_number = current_number[1:]
                modified_number = '+49' + modified_number
                print("modified german number is: " + modified_number)

            if index != 0:
                formatted_phone += ":::" + modified_number
            else:
                formatted_phone += modified_number
        return formatted_phone

    # remove all white spaces from number
    phone_column = phone_column.replace(" ", "")
    if len(str(phone_column)) == GHANA_MOBILE_PHONE_LENGTH:
        modified_number = phone_column[1:]
        modified_number = '+233' + modified_number
        print("modified ghana number is: " + modified_number)
        phone_column = modified_number
    if len(str(phone_column)) == GERMANY_MOBILE_PHONE_LENGTH:
        modified_number = phone_column[1:]
        modified_number = '+49' + modified_number
        print("modified german number is: " + modified_number)
        phone_column = modified_number

    return phone_column


def read_csv(CONTACTS___CSV):
    try:
        with open('%s' % CONTACTS___CSV, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            csv_content = list(reader)
            return csv_content
    except FileNotFoundError:
        print("File not found.")
        return []
    except csv.Error as e:
        print(f"CSV Error: {e}")
        return []


def main():
    csv_content = read_csv(CONTACTS___CSV)
    print("csv content: ", csv_content)

main()