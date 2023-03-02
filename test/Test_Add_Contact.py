# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create_new_contact(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="wow", file="C:\Games\LEtXJtJk.jpg", title="title", company="company",
                                address="11 22 33", home="444555666", mobile="89992224455", work="787565", fax="1456", email="test@mail.kek",
                                email2="test1@mail.kek", email3="test2@mail.kek", homepage="homepage", bday="13", bmonth="January", byear="1900", aday="29", amonth="May",
                                ayear="2000", address2="Wowcity, Wowstreet, 55", phone2="yes", notes="none"))