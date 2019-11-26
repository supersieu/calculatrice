import calculatrice


def test_cal_1_input():
    assert calculatrice.cal_1_input("I") == 1
    assert calculatrice.cal_1_input("V") == 5
    assert calculatrice.cal_1_input("M") == 1000


def test_cal_2_input():
    assert calculatrice.cal_2_input("II") == 2
    assert calculatrice.cal_2_input("VV") == 10
    assert calculatrice.cal_2_input("MM") == 2000
