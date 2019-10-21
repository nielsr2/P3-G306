
def f1(string, p):
    return string + "f1"


def f2(string, p):
    return string + "f2" + p


def f3(string):
    return string + "f3"


def test():
    fmap = {{f1: ()}, {2: f2}, {3: f3}}
    for i in range(3):
        print(fmap[i]("BAH"))


# **********************************************************************

# func_array = [f1("bah", "YES"), f2("bah", "YES"), f3]  # array of functions
func_array = [f1, f2, f3]  # array of functions
param_array = [{"string": "shit", "p": "blalbal"},
               {"string": "shit", "p": "balls"},
               {"string": "fuck"}]  # array of dictionary for params


def test2():
    inputString = "yay first"
    for i in range(3):
        print("parsing: ", param_array[i])
        current = param_array[i]
        current["string"] = inputString
        returnedString = func_array[i](**param_array[i])
        print(returnedString)
        inputString = returnedString
        # print(func_array[i](**param_array[i]))  # select a function and call it


# test2()

# **********************************************************************
# **********************************************************************

fArray = [{f1: {"string": "shit", "p": "blalbal"},
           f2: {"string": "shit", "p": "blalbal"}}]


def test3():
    it = iter(fArray)
    print("len(fArray)", len(fArray))
    for i in range(0, len(fArray) + 1):
        print(it())
        print(i, it, type(it))
        next(it)
    # inputString = "yay first"
    # for key in fArray:
    #     print(key)
        # print(fArray[key]())
        # print("parsing: ", param_array[i])
        # current = param_array[i]
        # current["string"] = inputString
        # returnedString = func_array[i](**param_array[i])
        # print(returnedString)
        # inputString = returnedString
        # print(func_array[i](**param_array[i]))  # select a function and call it


test3()


# **********************************************************************


fArray = {f1: {"string": "shit", "p": "blalbal"},
          f2: {"string": "shit", "p": "blalbal"}}


def test3():
    inputString = "yay first"
    for key in fArray:
        current = fArray[key]
        current["string"] = inputString
        returnedString = key(*fArray[key])
        print("RE" + returnedString)
        inputString = returnedString
