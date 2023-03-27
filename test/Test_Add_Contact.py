# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test", middlename="Test", lastname="Test", nickname="wow", file="C:\Games\LEtXJtJk.jpg", title="title", company="company",
                      address="11 22 33", homephone="444555666", mobilephone="89992224455", workphone="787565", fax="1456", email="test@mail.kek",
                      email2="test1@mail.kek", email3="test2@mail.kek", homepage="homepage", bday="13", bmonth="January", byear="1900", aday="29", amonth="May",
                      ayear="2000", address2="Wowcity, Wowstreet, 55", secondaryphone="yes", notes="none")
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
