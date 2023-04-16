from model.contact import Contact
from model.group import Group

import random


def test_delete_contact_from_group(app, db):
    groups = db.get_group_list()
    if not groups:
        app.group.create(name="Test Group")
        groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contacts_in_group(group)
    if not contacts:
        app.contact.create_new_contact(Contact(lastname="Test", firstname="Contact"))
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact, group)
        contacts = db.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_contact_from_group(contact, group)
    assert not contact in db.get_contacts_in_group(group)

