
def f1(string, p):
    return string + "f1" + p


def f2(string, p):
    return string + "f2" + p


def f3(string):
    return string + "f3"


fArray = {f1: {"string": "thisisastring", "p": "blalbal1"},
          f2: {"string": "shouldbeanimagetho", "p": "blalbal2"}}


def test3():
    inputString = "keeppassingme"
    for key in fArray:
        current = fArray[key]
        print("current", current)
        current["string"] = inputString
        returnedString = key(**current)  # https://realpython.com/python-kwargs-and-args/
        print("RE" + returnedString)
        inputString = returnedString


test3()
