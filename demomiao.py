
import os
import time


def over_all():

    for i in range(1, 21):
        # 入口
        os.system('adb shell input tap 900 120')
        time.sleep(15)
        print("入口进入")

        # 领喵币
        os.system('adb shell input tap 940 1688')
        time.sleep(8)
        print("领喵币")

        # 去逛店
        os.system('adb shell input tap 903 843')
        time.sleep(8)
        print("去逛店")

        # 等待11秒
        time.sleep(37)
        print("等待完成")

        # 返回界面
        os.system('adb shell input keyevent 4')
        time.sleep(10)
        print("返回")

        print("第%d次完成" % ( i ) )


if __name__ == '__main__':

    over_all()