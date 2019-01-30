# def gen():
#     for i in range(10):
#         yield i + 1

# for x in gen():
#     print(x)
#     print("===============================================")

# lst = [0]
# for x in lst:
#     print(x)
#     print("============================================")
#     lst.pop(0)
#     lst.append(x+1)



def gen():
    lst = ["가", "나", "다", "라", "마", "바", "사"]
    for i in lst:
        yield i

for x in gen():
    print(x)



# for x in range(1):
#     print(x)

# for x in range(2):
#     print(x)