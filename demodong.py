
import os
import time


def over_all():

    for i in range(1, 40):
        os.system('adb shell input tap 536 1600')

        # 逛店铺
        os.system('adb shell input tap 533 1730')
        time.sleep(3)
        print("逛店铺")

        # 返回
        os.system('adb shell input keyevent 4')
        time.sleep(10)

        # 投喂包包
        os.system('adb shell input tap 533 1730')
        time.sleep(3)
        print("投喂包包")

        print("第%d次完成" % ( i ) )


if __name__ == '__main__':

    over_all()