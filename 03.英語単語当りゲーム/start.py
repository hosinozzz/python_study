import random

words_dict = {  # dic 
    "ライオン": "lion",
    "タイガー": "tiger",
    "リンゴ": "apple",
    "飛行機": "airplane"
}

words = [] # keyだけlistに入れる

for word in words_dict:
    words.append(word)

random.shuffle(words)

chance = 3
for i in range(0, len(words)):
    q = words[i]
    for j in range(0, chance):
        user_input = str(input("{}の単語を入力してください > ".format(q)))
        english = words_dict[q]
        
        if user_input.strip().lower() == english.lower():
            print("正解です")
            break
        else:
            print("不正解です")
    if user_input != english:
        print("正解は{}です".format(english))

print("すべての問題を解きました")