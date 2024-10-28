# examples of list comps


def main():
    list1 = []
    for num in range(10):
        sq = num ** 2
        list1.append(sq)

    print(list1)

    list2 = [num ** 2 for num in range(10)]
    print(list2)

    list3 = [2 ** num for num in range(20)]
    print(list3)

    list4 = [num for num in list2 if (num % 2) != 0]
    print(list4)

main()