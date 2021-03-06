from os import system
from random import randint
import json
import os

os.system('color a')

filename = 'data.json'
username_have_chinese = False
time = 0
lower_limit_guess_number = 0
upper_limit_guess_number = 0
set_maximum_time = ''
maximum_guess_time = 0
number = 0
tell_player_number = ''
replay = ''
set_maximum_time_break = False

# 使用 json 文件储存用户名
try:
    # 读取文件
    with open(filename) as f_obj:
        username = json.load(f_obj)
        print('欢迎回来，' + str(username) + '!\n')

except:
    print('请输入用户名')
    username = input('> ')
    print('\n')

    while True:
        # 检查用户名是否含有中文(使用 encode 和 decode 函数编解码中文 (gbk) 时会遇到 json 无法支持这种编码的错误)
        for i in username:
            if u'\u4e00' <= i <= u'\u9fff':
                username_have_chinese = True

            else:
                username_have_chinese = False

        if username_have_chinese:
            print('用户名无法包含中文(使用 encode 和 decode 函数编解码中文 (gbk) 时会遇到 json 无法支持这种编码的错误)\n')
            print('请输入用户名')
            username = input('> ')
            print('\n')

        else:
            # 写入文件
            with open(filename, 'w') as f_obj:
                json.dump(username, f_obj)
                print('欢迎您，' + str(username) + '!\n')
                break


while True:
    time = 0
    # 设置下限
    while True:
        print("请输入下限")
        lower_limit_guess_number = input("> ")
        print('\n')

        if lower_limit_guess_number == 'q':
            exit()

        # 判断玩家输入的是否是整数
        try:
            lower_limit_guess_number = int(lower_limit_guess_number)
            break

        except:
            print("非法输入\n")

    # 设置上限
    while True:
        print("请输入上限")
        upper_limit_guess_number = input("> ")
        print('\n')

        if upper_limit_guess_number == 'q':
            exit()

        # 判断玩家输入的是否是整数
        try:
            upper_limit_guess_number = int(upper_limit_guess_number)
            break

        except:
            print("非法输入\n")

    # 如果下限大于或等于上限, 就让玩家重新输入
    if lower_limit_guess_number >= upper_limit_guess_number:
        while True:
            print("数字下限不能大于或等于数字上限")
            print("重新输入下限\n")
            lower_limit_guess_number = input("> ")
            print('\n')

            if lower_limit_guess_number == 'q':
                exit()

            # 判断玩家输入的是否是整数
            try:
                lower_limit_guess_number = int(
                    lower_limit_guess_number)

            except:
                print("非法输入\n")

            else:
                print("重新输入上限")

                upper_limit_guess_number = input("> ")
                print('\n')

                if upper_limit_guess_number == 'q':
                    exit()

                try:
                    upper_limit_guess_number = int(
                        upper_limit_guess_number)

                except:
                    print("非法输入\n")

                else:
                    if lower_limit_guess_number < upper_limit_guess_number:
                        break

    while True:
        print("你是否想设置次数上限?(y/n)")
        set_maximum_time = input("> ")
        print('\n')

        if set_maximum_time == 'q':
            exit()

        if set_maximum_time == 'y':
            print("请输入次数上限")
            maximum_guess_time = input("> ")
            print('\n')

            if maximum_guess_time == 'q':
                exit()

        elif set_maximum_time == 'n':
            break

        else:
            set_maximum_time_break = False
            print("非法输入\n")

        while set_maximum_time == 'y':
            # 判断玩家输入的是否是整数
            try:
                maximum_guess_time = int(maximum_guess_time)
                if int(maximum_guess_time) < 0:
                    print('非法输入\n')
                    print('请重新输入次数上限')
                    maximum_guess_time = input('> ')
                    print('\n')
                else:
                    set_maximum_time_break = True
                    break

            except:
                print('非法输入\n')
                print('请重新输入次数上限')
                maximum_guess_time = input('> ')
                print('\n')

            if int(maximum_guess_time) < 0:
                print('非法输入\n')
                print('请重新输入次数上限')
                maximum_guess_time = input('> ')
                print('\n')

        if set_maximum_time_break:
            break

    # 从下限和上限里随机挑选一个数
    number = randint(lower_limit_guess_number, upper_limit_guess_number)

    # 告知下限和上限
    print("猜个数字(" + str(lower_limit_guess_number) +
          " - " + str(upper_limit_guess_number) + ")\n")

    # 如果玩家设置了次数上限, 就告知玩家
    if set_maximum_time == 'y':
        print("你可以猜 " + str(maximum_guess_time) + " 次\n")

    while True:
        if tell_player_number == 'y':
            break

        if tell_player_number == 'n':
            print("猜个数字(" + str(lower_limit_guess_number) +
                  " - " + str(upper_limit_guess_number) + ")\n")

        # 如果玩家设置了次数上限, 就用设置上限的版本
        if set_maximum_time == 'y':
            if time < maximum_guess_time:
                guess_number = input("> ")
                print('\n')

                if guess_number == 'q':
                    break

                # 判断玩家输入的是否是整数
                try:
                    guess_number = int(guess_number)

                except:
                    print("非法输入\n")
                    print("猜个数字(" + str(lower_limit_guess_number) +
                          " - " + str(upper_limit_guess_number) + ")\n")

                else:
                    # 判断玩家输入的数字是否超过了玩家定义的上限
                    if guess_number > upper_limit_guess_number:
                        print("你输入的数字不能大于 " +
                              str(upper_limit_guess_number) + '\n')

                    # 判断玩家输入的数字是否超过了玩家定义的下限
                    elif guess_number < lower_limit_guess_number:
                        print("你输入的数字不能小于" +
                              str(lower_limit_guess_number) + '\n')

                    else:
                        time += 1

                        if guess_number > number:
                            print('太大了!!!\n')

                        elif guess_number == number:
                            print('正确!!!')
                            print('你猜了 ' + str(time) + ' 次\n')
                            break

                        else:
                            print('太小了!!!\n')

                        while time >= 10:
                            print("你是否想知道最终答案?(y/n)")
                            tell_player_number = input("> ")
                            print("\n")

                            if tell_player_number == 'q':
                                exit()

                            if tell_player_number == 'y':
                                print("最终答案是: " + str(number) + '\n')
                                break

                            elif tell_player_number == 'n':
                                pass

                            else:
                                print("非法输入\n")

            # 超过了玩家设定的次数上限, 就结束游戏, 并告知玩家输了
            else:
                print("你输了!!!")
                break

        # 如果玩家没有设置次数上限, 就用没有设置上限的版本
        else:
            if tell_player_number == 'y':
                break

            if tell_player_number == 'n':
                print("猜个数字(" + str(lower_limit_guess_number) +
                      " - " + str(upper_limit_guess_number) + ")")
                print('\n')

            guess_number = input("> ")
            print('\n')

            if guess_number == 'q':
                break

            else:
                # 判断玩家输入的是否是整数
                try:
                    guess_number = int(guess_number)

                except:
                    print("非法输入\n")

                else:
                    # 判断玩家输入的数字是否超过了玩家定义的上限
                    if guess_number > upper_limit_guess_number:
                        print("你输入的数字不能大于 " + str(upper_limit_guess_number) + '\n')

                    # 判断玩家输入的数字是否超过了玩家定义的下限
                    elif guess_number < lower_limit_guess_number:
                        print("你输入的数字不能小于 " + str(lower_limit_guess_number) + '\n')

                    else:
                        time += 1

                        if guess_number > number:
                            print('太大了!!!\n')

                        elif guess_number == number:
                            print('正确!!!\n')

                            print('你猜了 ' + str(time) + ' 次\n')

                            break

                        else:
                            print('太小了!!!\n')

                        # 如果玩家猜的次数超过了 10 次，询问玩家是否想要知道最终答案
                        while time >= 10:
                            print("你是否想知道最终答案?(y/n)")
                            tell_player_number = input("> ")
                            print("\n")

                            if tell_player_number == 'q':
                                exit()

                            # 告知玩家最终答案
                            if tell_player_number == 'y':
                                print('最终答案是 ' + str(number) + '\n')
                                break

                            elif tell_player_number == 'n':
                                break

                            else:
                                print("非法输入\n")
    # 询问玩家是否想要重新游玩
    while True:
        print("要不要再玩一次？(y/n)")
        replay = input("> ")
        print('\n')

        if replay == 'y':
            os.system('cls')
            break

        elif replay == 'n':
            print('再见，' + str(username) + '!\n')
            break

        else:
            print("非法输入\n")
            continue

        break

    if replay == 'y':
        continue

    else:
        break