import contact as contact


def test_read_csv():
    csv_content = contact.read_csv('contacts_2.csv')
    # print('csv', csv_content)
    assert len(csv_content) > 0

def test_phone_value_contains_digits():
    assert contact.phone_column_contains_digits('') == False
    assert contact.phone_column_contains_digits('024 422 0425') == True
    assert contact.phone_column_contains_digits('+233 53 011 8669') == True
    assert contact.phone_column_contains_digits('024 422 0425 ::: 0243433467') == True
    assert contact.phone_column_contains_digits('0245021422 ::: +974 7054 7928') == True

def test_phonenumber_does_not_have_countrycode():
    assert contact.phonenumber_does_not_have_countrycode('024 422 0425') == True
    assert contact.phonenumber_does_not_have_countrycode('+233 53 011 8669') == False
    assert contact.phonenumber_does_not_have_countrycode('024 422 0425 ::: 0243433467') == True
    assert contact.phonenumber_does_not_have_countrycode('0245021422 ::: +974 7054 7928') == True

def test_modify_phone_number():
    assert contact.modify_phone_number('024 422 0425') == '+233244220425'
    assert contact.modify_phone_number('+233 53 011 8669') == '+233530118669'
    # assert contact.modify_phone_number('024 422 0425 ::: 0243433467') == '+233244220425 ::: +233243433467'