import random


# 生成 1 到 100 之间的随机整数
secret_number = random.randint(1, 100)
attempts = 0

print("欢迎来到猜数字小游戏！我已经想好了一个 1 到 100 之间的数字，你可以开始猜啦。")

while True:
    try:
        # 获取用户输入
        guess = int(input("请输入你猜测的数字: "))
        attempts = attempts + 1

        if guess < secret_number:
            print("猜的数字太小了，再试一次。")
        elif guess > secret_number:
            print("猜的数字太大了，再试一次。")
        else:
            print(f"恭喜你，猜对了！你一共用了 {attempts} 次尝试。")
            break
    except ValueError:
        print("输入无效，请输入一个整数介于1-100之间。")
    