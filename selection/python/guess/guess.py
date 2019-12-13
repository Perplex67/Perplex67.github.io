# time                          -       猜数字时间上限
# guess_number                  -       你猜的数字
# lower_limit_guess_number      -       数字的下限
# upper_limit_guess_number      -       数字的上限
# set_maximum_time              -       是否设置猜数字的次数上限
# maximum_guess_time            -       猜数字的次数上限
# number                        -       要猜的数字
# tell_player_number            -       告诉玩家数字答案
# replay                        -       重新游玩

# 从 random 库导入 randint 函数，这是一个随机数的函数
from random import randint


def play():
    tell_player_number = 0
    time = 0
    guess_number = 0

    print("游戏开始!")
    print('================================')

    print("输入 q 来退出")
    print('================================')

    while True:
        print("请输入要猜的数字的下限")
        lower_limit_guess_number = input("> ")
        print('================================')

        if lower_limit_guess_number == 'q':
            exit()

        else:
            # 判断玩家输入的是否是整数
            try:
                lower_limit_guess_number = int(lower_limit_guess_number)

            except:
                print("非法输入...")

                print('================================')

            else:
                if lower_limit_guess_number < 0:
                    print("你输入的数字太小啦!!!")
                    print('================================')

                elif lower_limit_guess_number > 9999999:
                    print("你输入的数字太大啦!!!")
                    print('================================')

                else:
                    break

    while True:
        # 设置要猜的数字的上限
        print("请输入要猜的数字的上限")

        upper_limit_guess_number = input("> ")
        print('================================')

        if upper_limit_guess_number == 'q':
            exit()

        # 判断玩家输入的是否是整数
        try:
            upper_limit_guess_number = int(upper_limit_guess_number)

        except:
            print("非法输入...")
            print('================================')

        else:
            if upper_limit_guess_number > 9999999:
                print("你输入的数字太大啦!!!")
                print('================================')

            elif upper_limit_guess_number <= 0:
                print("你输入的数字太小啦!!!")
                print('================================')

            else:
                break

# 如果要猜的数字的最小数大于或等于最大数, 就让玩家重新输入
    if lower_limit_guess_number >= upper_limit_guess_number:
        while True:
            print("数字下限不能大于或等于数字上限")

            print("重新输入要猜的数字的下限")
            print('================================')

            lower_limit_guess_number = input("> ")
            print('================================')

            if lower_limit_guess_number == 'q':
                exit()

            else:
                # 判断玩家输入的是否是整数
                try:
                    lower_limit_guess_number = int(
                        lower_limit_guess_number)

                except:
                    print("非法输入...")
                    print('================================')

                else:
                    if lower_limit_guess_number < 0:
                        print("你输入的数字太小啦!!!")
                        print('================================')

                    elif lower_limit_guess_number > 9999999:
                        print("你输入的数字太大啦!!!")
                        print('================================')

                    else:
                        print("重新输入要猜的数字的下限")

                        upper_limit_guess_number = input("> ")
                        print('================================')

                        if upper_limit_guess_number == 'q':
                            exit()

                        try:
                            upper_limit_guess_number = int(
                                upper_limit_guess_number)

                        except:
                            print("非法输入")
                            print('================================')

                        else:
                            if upper_limit_guess_number >= 9999999:
                                print("你输入的数字太大啦!!!")
                                print('================================')

                            elif lower_limit_guess_number < upper_limit_guess_number:
                                break

                            else:
                                pass

    while True:
        print("你是否想设置猜数字的次数上限?(y/n)")
        set_maximum_time = input("> ")
        print('================================')

        if set_maximum_time == 'q':
            exit()

        if set_maximum_time == 'y':
            print("请输入猜数字的次数上限")
            maximum_guess_time = input("> ")
            print('================================')

            if maximum_guess_time == 'q':
                exit()

            else:
                # 判断玩家输入的是否是整数
                try:
                    maximum_guess_time = int(maximum_guess_time)

                except:
                    print("非法输入")
                    print('================================')

                else:
                    if maximum_guess_time <= 0:
                        print("你输入的数字太小啦!!!")
                        print('================================')

                    elif maximum_guess_time >= 999:
                        print("你输入的数字太大啦!!!")
                        print('================================')

                    else:
                        break
        elif set_maximum_time == 'n':
            break

        else:
            print("非法输入")
            print('================================')

    # 从数字的下限和上限里随机挑选一个数
    number = randint(lower_limit_guess_number, upper_limit_guess_number)

    # 告知要猜的数字的下限和要猜的数字的上限
    print("猜个数字(" + str(lower_limit_guess_number) +
          "-" + str(upper_limit_guess_number) + ")")
    print('================================')

    # 如果玩家设置了猜数字的次数上限, 就告知玩家
    if set_maximum_time == 'y':
        print("你可以猜 " + str(maximum_guess_time) + " 次.")
        print('================================')

    while True:
        if tell_player_number == 'y':
            break

        if tell_player_number == 'n':
            print("猜个数字(" + str(lower_limit_guess_number) +
                  "-" + str(upper_limit_guess_number) + ")")
            print('================================')

        # 如果玩家设置了猜数字的次数上限, 就用设置上限的版本
        if set_maximum_time == 'y':
            if time < maximum_guess_time:
                guess_number = input("> ")
                print('================================')

                if guess_number == 'q':
                    break

                else:
                    # 判断玩家输入的是否是整数
                    try:
                        guess_number = int(guess_number)

                    except:
                        print("非法输入")
                        print('================================')

                    else:
                        # 判断玩家输入的数字是否超过了玩家定义的数字上限
                        if guess_number > upper_limit_guess_number:
                            print("你输入的数字不能大于 " + str(upper_limit_guess_number))
                            print('================================')

                        # 判断玩家输入的数字是否超过了玩家定义的数字下限
                        elif guess_number < lower_limit_guess_number:
                            print("n你输入的数字不能小于" + str(lower_limit_guess_number))
                            print("================================")

                        else:
                            time += 1

                            if guess_number > number:
                                print('太大了!!!')
                                print('================================')

                            elif guess_number == number:
                                print('正确!!!')
                                print('你猜了 ' + str(time) + ' 次')
                                print('================================')
                                break

                            else:
                                print('太小了!!!')
                                print('================================')

                            while time >= 10:
                                print("你是否想知道最终答案?(y/n)")
                                tell_player_number = input("> ")
                                print("================================")

                                if tell_player_number == 'q':
                                    exit()

                                if tell_player_number == 'y':
                                    print("最终答案是: " + str(number))
                                    print("================================")
                                    break

                                elif tell_player_number == 'n':
                                    pass

                                else:
                                    print("非法输入")
                                    print("================================")

            # 超过了玩家设定的猜数字的次数上限, 就结束游戏, 并告知玩家输了
            else:
                print("你输了!!!")
                break

        # 如果玩家没有设置猜数字的次数上限, 就用没有设置上限的版本
        else:
            if tell_player_number == 'y':
                break

            if tell_player_number == 'n':
                print("猜个数字(" + str(lower_limit_guess_number) +
                      "-" + str(upper_limit_guess_number) + ")")
                print('================================')

            guess_number = input("> ")
            print('================================')

            if guess_number == 'q':
                break

            else:
                # 判断玩家输入的是否是整数
                try:
                    guess_number = int(guess_number)

                except:
                    print("非法输入")
                    print('================================')

                else:
                    # 判断玩家输入的数字是否超过了玩家定义的数字上限
                    if guess_number > upper_limit_guess_number:
                        print("你输入的数字不能大于 " + str(upper_limit_guess_number))
                        print('================================')

                    # 判断玩家输入的数字是否超过了玩家定义的数字下限
                    elif guess_number < lower_limit_guess_number:
                        print("你输入的数字不能小于 " + str(lower_limit_guess_number))
                        print("================================")

                    else:
                        time += 1

                        if guess_number > number:
                            print('太大了!!!')
                            print('================================')

                        elif guess_number == number:
                            print('正确!!!')
                            print('================================')

                            print('你猜了 ' + str(time) + ' 次')
                            print('================================')

                            break

                        else:
                            print('太小了!!!')
                            print('================================')

                        # 如果玩家猜的次数超过了 10 次
                        while time >= 10:
                            # 询问玩家是否想要知道最终答案
                            print("你是否想知道最终答案?(y/n)")
                            tell_player_number = input("> ")
                            print("================================")

                            if tell_player_number == 'q':
                                exit()

                            # 告知玩家最终答案
                            if tell_player_number == 'y':
                                print("最终答案是 " + str(number))
                                print("================================")
                                break

                            elif tell_player_number == 'n':
                                break

                            else:
                                print("非法输入")
                                print("================================")

    # 递归
    while True:
        # 询问玩家是否想要重新游玩
        print("要不要再玩一次?(y/n)")

        replay = input("> ")
        print('================================')

        if replay == 'y':
            play()

        elif replay == 'n':
            break

        else:
            print("非法输入")
            print('================================')


# 游玩游戏的代码被放到了一个函数里，也就是 play() 这个函数，里面用到了递归，指的是在函数里调用本身
play()