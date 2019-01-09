class Node:

    def __init__(self, first, last, street, phone, email):
        self.first = first
        self.last = last
        self.street = street
        self.phone = phone
        self.email = email

    def __str__(self):
        toString = 'Name: ', self.first, ' Last: ', self.last, ' Street: ', self.street, ' Phone: ', self.phone, ' Email: ', self.email
        return(toString)

