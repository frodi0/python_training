from model.contact import Contact
import random

def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname='test'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_edit = Contact(firstname="123", middlename="123", lastname="123", nickname="123", file="C:\Games\LEtXJtJk.jpg", title="123", company="123",
                      address="123", homephone="123", mobilephone="123", workphone="123", fax="123", email="123",
                      email2="123", email3="123", homepage="123", bday="11", bmonth="April", byear="2000", aday="26", amonth="July",
                      ayear="1990", address2="123", secondaryphone="123", notes="123")
    contact_edit.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact_edit)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_edit)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_birthday_and_anniversary(app):
    #if app.contact.count() == 0:
        #app.contact.create_new_contact(Contact(firstname='test'))
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(bday="12", bmonth="July", byear="2010", aday="14", amonth="June", ayear="1980")
    #contact.id = old_contacts[0].id
   # app.contact.modify_first_contact(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
   # old_contacts[0] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
