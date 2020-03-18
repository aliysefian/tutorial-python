lst = ['1', 2, 3, ['111', 2]]
print("print part", lst[1:])
print(lst[2:3])
print(lst[:3])
print(lst[:])
print("step list ", lst[::2])
print("reverse list ", lst[::-1])
print("origin lst", lst)
lst2 = lst[::-1]
print("lst2: revese  ", lst2)
st = "Alireza"
print(st[1:3])
print(st[:4])
print(st[::2])
print(st[::-1])
for item in st:
    print(item)
for item in range(0, len(st), 2):
    print("step", st[item])
print("<<<<<<<<<+++++++++++++++++++++>>>>>>>>>>>....")
lst3 = lst.copy()
print(lst)
lst.append("ali")
print(lst)
print("lst3======", lst3)
# lst.clear()
print(lst)
lst4 = ["ali", "reza"]
lst.extend(lst4)
print(lst)
print("apppend ", lst + lst4)
# SET
