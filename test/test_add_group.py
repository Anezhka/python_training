from model.group import Group

def test_add_group(app):
    app.group.create(Group("PythonTestName", "testHeader", "testFooter"))

def test_add_empty_group(app):
    app.group.create(Group("", "", ""))



