n, m = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] == list2[j]:
        i += 1
        j += 1
    else:
        j += 1


if i == len(list1):
    print("Yes")
else:
    print("No")
