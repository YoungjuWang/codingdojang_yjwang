def in_list(inl):
    num = inl[0]

    l1 = inl[1:]

    l1 = l1[-num:] + l1[:-num]

    for i in range(len(l1)): print(l1[i]),


if __name__ == "__main__":
    str1 = raw_input()

    str1 = [int(x) for x in str1.split(" ")]

    in_list(str1)