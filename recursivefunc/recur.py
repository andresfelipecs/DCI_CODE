# 20 minutes, trying to rewrite this to use a recursive style
# def get_sum(list):
#     total = 0
#     for i in list:
#         total += i
#     return total


def get_sum(list):

    print(list)
    if len(list) == 0:
        return 0
    else:
        sum = list[0] + get_sum(list[1:])
        return sum


if __name__ == "__main__":

    list = [1, 5, 9, 5, 2, 2]
    print(get_sum(list))
