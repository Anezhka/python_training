from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group("PythonTestName", "testHeader", "testFooter")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count() # app.group.count - хэш для предварительной проверки
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group("", "", "")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



