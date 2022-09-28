import pyautogui
import cv2
import random
import datetime

pyautogui.PAUSE = 0.2

pos = []
mp = [[0 for i in range(4)] for j in range(4)]

click_map = [[650, 550], [920, 550], [1150, 550], [650, 800], [920, 800], [1150, 800], [650, 1050], [920, 1050],
             [1150, 1050]]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
pos_zero = [-1, -1]
click_queue = []


def check(x, y):
    if 1 <= x <= 3 and 1 <= y <= 3:
        return 1
    return 0


def stop():
    img_path = 'stop.png'
    res = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
    pyautogui.click(res)


def make(pos):
    n = 0
    m = 0
    # print(len(pos))

    for i in range(len(pos)):
        x = pos[i][0]
        y = pos[i][1]
        # print(x, y)
        if 650 <= x <= 720:
            n = 1
        elif 920 <= x <= 980:
            n = 2
        elif 1150 <= x <= 1220:
            n = 3

        if 450 <= y <= 500:
            m = 1
        elif 700 <= y <= 750:
            m = 2
        elif 950 <= y <= 1000:
            m = 3
        # print(i, n, m)
        mp[m][n] = i + 1


def match(i):
    img_path = str(i) + ".png"
    res = pyautogui.locateCenterOnScreen(img_path, confidence=0.75)
    return res


def check():
    for i in range(1, 9):
        res = match(i)
        if res:
            pos.append(res)
    f = 1
    cnt = 1
    ans = 0
    for i in range(1, 4):
        for j in range(1, 4):
            if mp[i][j] == cnt:
                ans += 1
            cnt += 1

    return ans


# def solve(pos_zero):
#     while checkall() == 0:
#         key = random.randint(0, 3)
#         # for i in range(key, 4):
#         nx = pos_zero[0] + dx[key]
#         ny = pos_zero[1] + dy[key]
#         if check(nx, ny) == 1:
#             pyautogui.click(click_map[(nx - 1) * 3 + ny - 1])
#             click_queue.append([nx, ny])
#             t = mp[nx][ny]
#             mp[nx][ny] = mp[pos_zero[0]][pos_zero[1]]
#             mp[pos_zero[0]][pos_zero[1]] = t
#             pos_zero = [nx, ny]


def remake():
    img_path = "remake.png"
    res = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
    pyautogui.click(res)
    return


if __name__ == "__main__":

    # for now in click_map:
    #     pyautogui.click(now)
    begin = (datetime.datetime.now())
    stop()
    # print(res)
    make(pos)
    while (check() < 5):
        make(pos)
        remake()
    # for i in range(1, 4):
    #     for j in range(1, 4):
    #         if mp[i][j] == 0:
    #             pos_zero = [i, j]
    #             break

    # solve(pos_zero)

    print("Playing Time = ", datetime.datetime.now() - begin)
