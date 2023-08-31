import random
import os

numbers = []  # list
number = str(random.randint(0,9))  # 文字str


# 重複されないwhile
for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9))
    numbers.append(number)

# '1','2','3' インデクシングのために文字strで宣言したわけ

os.system("clear")

print("*" * 60)
print("野球ゲームをスタートします。")
print("*" * 60)


count_strike = 0 #初期化
count_ball = 0 #初期化

while count_strike < 3:

    count_strike = 0
    count_ball = 0


    num = str(input("数字3桁を入力してください : "))
    if len(num) == 3: #文字数をカウント
        for i in range(0, 3): # 0,1,2 まで連続した数値
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j:
                    count_strike += 1
                elif num[i] == numbers[j] and i !=j:
                    count_ball += 1
        if count_strike == 0 and count_ball == 0:
            print("Three Out!")
        else:
            output = ""
            if count_strike > 0:
                output += "{} Strike".format(count_strike)
            if count_ball > 0:
                output += "{}  ball".format(count_ball)

            print(output.strip()) # 空白追加
print("Game Success!")