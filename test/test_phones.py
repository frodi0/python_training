import re
from random import randrange

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def test_check_contact_info(app):
    contact_from_homepage = app.contact.get_contact_list()
    index = randrange(len(contact_from_homepage))
    random_contact_homepage = app.contact.get_contact_list()[index]
    random_contact_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert random_contact_homepage.id == random_contact_edit_page.id
    assert random_contact_homepage.lastname == random_contact_edit_page.lastname
    assert random_contact_homepage.firstname == random_contact_edit_page.firstname
    assert random_contact_homepage.address == random_contact_edit_page.address
    assert random_contact_homepage.all_emails_homepage == merge_email_like_on_homepage(random_contact_edit_page)
    assert random_contact_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(random_contact_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))

