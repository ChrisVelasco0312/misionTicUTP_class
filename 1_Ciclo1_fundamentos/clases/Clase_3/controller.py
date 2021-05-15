import model

# ---Getters


def get_salary():
    return model.salary


def get_name():
    return model.name


def get_skill():
    return model.skill


def get_age():
    return model.age

# ----Setters


def set_name(name):
    model.name = name


def set_skill(skill):
    model.skill += skill


def set_age(age):
    model.age = age


def set_salary(salary):
    model.salary = salary

# ---calc bonus and taxes


def calculate_bonus_one():
    set_salary(get_salary() + model.get_bonus_one())


def calculate_bonus_two():
    set_salary(get_salary() + model.get_bonus_one())


def calculate_normal_taxes():
    discount = get_salary() * model.get_normal_taxes()
    set_salary(get_salary() - discount)


def calculate_rent_taxes():
    discount = get_salary() * model.get_rent_taxes()
    set_salary(get_salary() - discount)
