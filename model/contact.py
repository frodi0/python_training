from sys import maxsize
class Contact:


    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, file="", title=None,
                 company=None, address=None, homephone=None, mobilephone=None, workphone=None,
                 fax=None, email=None, email2=None, email3=None, homepage=None, bday="-", bmonth="-", byear=None,
                 aday="-", amonth="-", ayear=None, address2=None, secondaryphone=None, notes=None, id=None,
                 all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.file = file
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)\
            and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)\
            and (self.address is None or other.address is None or self.address == other.address)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
