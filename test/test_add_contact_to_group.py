from model.contact import Contact
from model.group import Group

import random


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test Group"))
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(lastname="Test", firstname="Contact"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contacts_not_in_group(group)
    if not contacts:
        app.contact.create_new_contact(Contact(lastname="Test", firstname="Contact"))
        contacts = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact, group)
    assert contact in db.get_contacts_in_group(group)


