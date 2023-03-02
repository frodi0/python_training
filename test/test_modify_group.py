from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="111", header="222", footer="333"))
    app.session.logout()

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()
