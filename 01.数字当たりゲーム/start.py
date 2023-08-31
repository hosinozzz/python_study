import random ##ランダムライブラい
import os ##osコマンドライブラい

## 整数ではないと繰り返しになる変数
def input_check(msg, casting=int): ##intで宣言
    while True:
        try:
            user_input = casting(input("いくつでしょうか？"))
            return user_input
        except:
            continue

chance = 10 ## 機会を10回与える
count = 0 ## 0からカウントする

number = random.randint(1,99)
# os.system("cls") ##windowsコマンド
os.system("clear") ##linuxコマンド

print("1から99までの数字を10回で当てててください")



while count < chance:
    count += 1
    user_input = input_check("いくつでしょうか?") ##変数を呼び出す
    if number == user_input:
        break
    elif user_input < number:
        print("{}より大きい数字です".format(user_input))
    elif user_input > number:
        print("{}より小さい数字です".format(user_input))    
    else:
        print("不正解")

if user_input == number:
    print("成功です！{}が正解です。".format(number))
else:
    print("失敗、正解は{}です".format(number))