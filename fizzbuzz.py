# FizzBuzz
# Q 1から100までの数を順に出力するプログラム。
#    ただし、３の倍数のときは「Fizz」
#    5の倍数のときは「Buzz」
#    3と5の両方の倍数の場合には「FizzBuzz」を出力。

i = 0
for i in range(i, 51):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz", end="\n")
    elif i % 3 == 0:
        print("Fizz", end="\n")
    elif i % 5 == 0:
        print("Buzz", end="\n")
    else:
        print(i, end="\n")



