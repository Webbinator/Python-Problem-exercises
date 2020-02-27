def convert():
    kilos = float(input("Enter Kilos..."))
    miles = kilos * 0.6214
    print(format(miles,'.3f'))


def convert2():
    miles = float(input('Enter miles...'))
    convert_miles = miles * 1.60934
    print('Number of kilometers = ',format(convert_miles,'.3f'),'km')





convert2()
convert()