def print_horizontal_line(user_size):
    print(' --- ' * user_size)

def print_vertical_line(user_size):
    print('|    ' * (user_size + 1))


def main():
    user_size = int(input('What size game board u want to draw(from 3): '))

    for index in range(user_size):
        print_horizontal_line(user_size)
        print_vertical_line(user_size)
    print_horizontal_line(user_size)





if __name__ == "__main__":
    main()

