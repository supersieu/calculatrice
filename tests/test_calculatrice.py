import calculatrice


def test_cal_1_input():
    assert calculatrice.cal_1_input("I") == 1
    assert calculatrice.cal_1_input("V") == 5
    assert calculatrice.cal_1_input("M") == 1000
