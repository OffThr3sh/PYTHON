from itertools import groupby

if __name__ == "__main__":

    s = input().strip()

    ans_list = []

    for char, group in groupby(s):
        count = len(list(group))
        ans_list.append(f"({count}, {char})")

    print(" ".join(ans_list))