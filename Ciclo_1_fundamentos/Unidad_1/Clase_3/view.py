import controller as con


def run():
    print("Salario inicial", con.get_salary())
    con.calculate_bonus_one()
    print("Con primer bonus", con.get_salary())
    con.calculate_rent_taxes()
    print("Menos impuesto de renta", con.get_salary())
    con.calculate_bonus_two()
    print("Más segundo bonus", con.get_salary())
    con.calculate_normal_taxes()
    print("Menos impuesto normal", con.get_salary())


if __name__ == '__main__':
    run()
