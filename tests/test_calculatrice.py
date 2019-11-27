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


def test_cal_n_input():
    assert calculatrice.cal_n_input("MDCLXVI") == 1666
    assert calculatrice.cal_n_input("LXXVI") == 76


def test_cal_n_input_sous():
    assert calculatrice.cal_n_input_sous("IIV") == 5
    assert calculatrice.cal_n_input_sous("MCMXLIV") == 1944
    assert calculatrice.cal_n_input_sous("DIX") == 509
    assert calculatrice.cal_n_input_sous("XLV") == 45
    assert calculatrice.cal_n_input_sous("VIII") == 8
    assert calculatrice.cal_n_input_sous("MCMXCIX") == 1999


def test_plus():
    assert calculatrice.plus("IIV","IIV") == 10


def test_moins():
    assert calculatrice.moins("IIV","IIV") == 0


def test_mul():
    assert calculatrice.mul("IIV","IIV") == 25


def test_div():
    assert calculatrice.div("IIV","IIV") == 1


def test_operation():
    assert calculatrice.operation("+", "III", "MCMXLIV") == 1947
    assert calculatrice.operation("-", "IIV","IIV") == 0
    assert calculatrice.operation("*", "IIV","IIV") == 25
    assert calculatrice.operation("/", "IIV","IIV") == 1


def test_convertir_1_c():
    assert calculatrice.convertir_1_c(1) == "I"
    assert calculatrice.convertir_1_c(5) == "V"
    assert calculatrice.convertir_1_c(10) == "X"
    assert calculatrice.convertir_1_c(50) == "L"
    assert calculatrice.convertir_1_c(100) == "C"
    assert calculatrice.convertir_1_c(500) == "D"
    assert calculatrice.convertir_1_c(1000) == "M"

def test_convertir():
    assert calculatrice.convertir(1944) == "MCMXLIV"
    assert calculatrice.convertir(2006) == "MMVI"
    assert calculatrice.convertir(4) == "IV"
    assert calculatrice.convertir(1945) == "MCMXLV"