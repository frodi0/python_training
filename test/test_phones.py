import re
from model.contact import Contact

#def test_phones_on_homepage(app):
    #contact_from_homepage = app.contact.get_contact_list()[0]
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

#def test_phones_on_contact_view_page(app):
    #contact_from_view_page = app.contact.get_contact_from_view_page(0)
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    #assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    #assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    #assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

#def test_check_contact_info(app):
    #contact_from_homepage = app.contact.get_contact_list()
    #index = randrange(len(contact_from_homepage))
    #random_contact_homepage = app.contact.get_contact_list()[index]
    #random_contact_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #assert random_contact_homepage.id == random_contact_edit_page.id
    #assert random_contact_homepage.lastname == random_contact_edit_page.lastname
    #assert random_contact_homepage.firstname == random_contact_edit_page.firstname
    #assert random_contact_homepage.address == random_contact_edit_page.address
    #assert random_contact_homepage.all_emails_from_homepage == merge_email_like_on_homepage(random_contact_edit_page)
    #assert random_contact_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(random_contact_edit_page)

def clear(s):
    return " ".join(s.split()) if s is not None else ""

def clear_phone_value(s):
    return re.sub("[/.() -]", "", s)

def clear_spaces_address(s):
    return re.sub(" +", " ", re.sub(" \n", "\n", re.sub("\n ", "\n", s))).strip() if s is not None else ""

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone_value(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x is not None and x != "", [contact.email, contact.email2, contact.email3]))

def clear_contact_homepage(contact):
    _ = clear
    __ = clear_spaces_address
    return Contact(firstname=_(contact.firstname), lastname=_(contact.lastname), address=__(contact.address),
                   homephone=_(contact.homephone), mobilephone=_(contact.mobilephone), workphone=_(contact.workphone),
                   email=_(contact.email), email2=_(contact.email2), email3=_(contact.email3),
                   secondaryphone=_(contact.secondaryphone),
                   all_phones_from_homepage=merge_phones_like_on_homepage(contact),
                   all_emails_from_homepage=merge_email_like_on_homepage(contact))


def test_all_contact_info_from_homepage(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="Firstname", lastname="Lastname", address="Address"))
    contacts_on_homepage = app.contact.get_contact_list()
    contacts_in_db = db.get_contact_list()
    assert sorted(contacts_on_homepage, key=Contact.id_or_max) == sorted(map(clear_contact_homepage, contacts_in_db), key=Contact.id_or_max)
    for i, contact in enumerate(sorted(contacts_on_homepage, key=Contact.id_or_max)):
        assert contact.firstname == clear(contacts_in_db[i].firstname)
        assert contact.lastname == clear(contacts_in_db[i].lastname)
        assert contact.address == clear(contacts_in_db[i].address)
        assert contact.all_phones_from_homepage == merge_phones_like_on_homepage(contacts_in_db[i])
        assert contact.all_emails_from_homepage == merge_email_like_on_homepage(contacts_in_db[i])


