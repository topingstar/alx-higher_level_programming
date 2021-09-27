#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    "divides element by element 2 lists"
    i = answer = 0
    list = []
    for i in range(list_length):
        try:
            answer = (my_list_1[i] / my_list_2[i])
        except TypeError:
            answer = 0
            print("wrong type")
        except ZeroDivisionError:
            answer = 0
            print("division by 0")
        except IndexError:
            answer = 0
            print("out of range")
        finally:
            list.append(result)
    return list
