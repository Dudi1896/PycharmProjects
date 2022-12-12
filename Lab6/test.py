import turtle

import matplotlib.pyplot as plt

def main():
    my_string = '03/07/2018'
    list_trip = my_string.split('/')
    print(list_trip)
    # list1 = [1, 10, 3, 6]
    # list2 = [item * 2 for item in list1 if item > 5]
    # print(list2)
    # x_coords = [0,1,2,3,4]
    # y_coords = [0,3,1,5,2]
    # plt.plot(x_coords, y_coords)
    # plt.show()
    for x in range(8):
        turtle.forward(100)
        turtle.right(45)

# def pass_it(x, y):
#     z = x*y
#     result = get_result(z)
#     return(result)
#
# def get_result(number):
#     z = number + 2
#     return(z)
#
# num1 = 3
# num2 = 4
# answer = pass_it(num1, num2)
# print(answer)
#
# price = int(68.549)
# print(price)
#
# my_array = [2, 45 ,63 ,34, 7 ,9 ,20, 12]
# new_array= my_array.sort()
# print('one',
#       'two',
#       'three')
#
# total = 0
# for count in range(4,6):
#     total += count
#     print(total)
#
# number = range(0, 9, 2)
# for n in number:
#     print(n)

if __name__ == "__main__":
    main()
