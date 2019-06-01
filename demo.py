
import os
import time


def over_all():

    for i in range(1, 51):
        # 领喵币
        os.system('adb shell input tap 888 1617')
        time.sleep(0.5)

        # 去逛店
        os.system('adb shell input tap 927 1288')
        time.sleep(2.5)

        # 等待11秒
        time.sleep(11)

        # 领取喵币
        os.system('adb shell input tap 976 947')
        time.sleep(3)

        # 确认领取
        os.system('adb shell input tap 537 1235')
        time.sleep(2)

        # 返回界面
        os.system('adb shell input keyevent 4')
        time.sleep(1)

        print("第%d次完成" % ( i ) )


if __name__ == '__main__':

    over_all()