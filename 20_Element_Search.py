from bisect import bisect_left
from bisect import bisect_right

def check_left(random_list, user_num):
    i = bisect_left(random_list, user_num)
    print(i)
    if i != len(random_list) and random_list[i] == user_num:
        return print(True)
    else:
        return print(False)

def check_right(random_list, user_num):
    i = bisect_right(random_list, user_num)
    print(i)
    if i != len(random_list) + 1 and random_list[i-1] == user_num:
        return print(True)
    else:
        return print(False)



def main():
    user_num = int(input('Check if number exist in list: ' ))
    random_list = [1, 3, 5, 23, 27, 30, 41, 42, 50, 55]
    check_left(random_list, user_num)
    check_right(random_list, user_num)


if __name__ == "__main__":
    main()
