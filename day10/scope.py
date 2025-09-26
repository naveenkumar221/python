# x=20
# def hunt():
#     print(x)
# hunt()

# def hunt():
#     x=20
#     print("hi")
# hunt()
# print(x)


def hunt1():
    def hunt2():
        x=30
        print("hi")
    hunt2()
    print("hello")
hunt1()