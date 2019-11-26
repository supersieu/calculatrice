import calculatrice


def test_cal_1_input():
    assert calculatrice.cal_1_input("I") == 1
    assert calculatrice.cal_1_input("V") == 5
    assert calculatrice.cal_1_input("M") == 1000


def test_cal_2_input_ide():
    assert calculatrice.cal_2_input_ide("II") == 2
    assert calculatrice.cal_2_input_ide("VV") == 10
    assert calculatrice.cal_2_input_ide("MM") == 2000


def test_cal_n_input_ide():
    assert calculatrice.cal_n_input_ide("IIIIII") == 6
    assert calculatrice.cal_n_input_ide("VVVV") == 20
    assert calculatrice.cal_n_input_ide("MMM") == 3000
