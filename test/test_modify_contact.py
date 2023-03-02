from model.contact import Contact

def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="123", middlename="123", lastname="123", nickname="123", file="C:\Games\LEtXJtJk.jpg", title="123", company="123",
                                address="123", home="123", mobile="123", work="123", fax="123", email="123",
                                email2="123", email3="123", homepage="123", bday="11", bmonth="April", byear="2000", aday="26", amonth="July",
                                ayear="1990", address2="123", phone2="123", notes="123"))