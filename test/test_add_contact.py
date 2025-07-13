from model.contact import Contact

def test_add_contact(app):
    contact = Contact("Alex", "Smith", 225577, 3393457, 9826364, 652535)
    app.contact.create(contact)