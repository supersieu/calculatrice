def cal_1_input(char):
    list_char = [["I", 1], ["V", 5], ["X", 10], ["L", 50], ["C", 100], ["D", 500], ["M", 1000]]
    val = 0
    for i in range(len(list_char)):
        if list_char[i][0] == char:
            val = list_char[i][1]
    return val


def cal_2_input(char):
    return cal_1_input(char[0])*2
