# -*- coding: utf-8 -*-

import os
import random
import time
import copy

map = ["┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑",
"|                                                                                                                                                                                       |",
"|                                                                                                                                                                                       |",
"|                                                                              \033[96mHi Aivle! \033[91mMerry Christmas ❤\033[0m                                                                              |",
"|                                                                           0:52 ━━━━●────────────────── 3:50                                                                           |",
"|                                                                             ⇆          ◁  ❚❚  ▷        ↻                                                                              |",
"|                                                                                                                                                                                       |",
"|      / ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣\                                                                                          ..🌙.。*                |",
"|      |                                                             |                                                                                                                  |",
"|      |    2021년, 여러분들을                                       |                                                                                                                  |",
"|      |                                                             |                                                                                                                  |",
"|      |    \033[96mKT 에이블\033[0m에서 만날 수 있게 되어 기쁩니다.                |                                                                                                                  |",
"|      |                                                             |                                                                                                                  |",
"|      |                                                             |                                                                                                                  |",
"|      |                                                             |                                                                                                                  |",
"|      |                                                             |                                                                                                                  |",
"|      |                                                             |                                                                                                                  |",
"|      |    마지막 2021년 잘 마무리 하시고,                          |                                                                                    ⭐ 　　                       |",
"|      |                                                             |                                                                                   \033[32m/\033[0m  \033[32m\\\033[0m                           |",
"|      |    2022년은 \033[96mKT 에이블\033[0m과 함께 모두 웃는 해가 되었으면 해요.  |                                                                                  (`_`')                          |",
"|      |                                                             |                                                                                 \033[32m/\033[0m      \033[32m\\\033[0m                         |",
"|      |                                                             |                                                                                (`'--.___\033[32m\\\033[0m                        |",
"|      |                                                             |                                                                                \033[32m/\033[0m`;-.,__ ')                       |",
"|      |    모두 다같이 취뽀취뽀 \033[91m❤ ❤\033[0m                                 |                                                                               \033[32m/\033[0m           \033[32m\\\033[0m                      |",
"|      |                                                             |                                                                             (`'--          \033[32m\\\033[0m                     |",
"|       ＼＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿/                                                                               \033[32m/\033[0m`;--._`''--. _\033[32m\\\033[0m                    |",
"|           　　ｏ                                                                                                                                 \033[32m/\033[0m        -.,____``)                  |",
"|           　　 。                                                                                       \033[33m__\033[0m                                      \033[32m/\033[0m                 \033[32m\\\033[0m                   |",
"|           　　　｡                                                                                     \033[33m_|__|_\033[0m             \033[35m__\033[0m                    (`""--.,_             \033[32m\\\033[0m                  |",
"|           　　∧＿∧                                                                                     ('')            \033[35m_|__|_\033[0m        \033[32m/\033[0m\033[32m\\\033[0m       \033[32m/\033[0m-.,_    ``''--....-'`)        \033[32m/\033[0m\033[32m\\\033[0m       |",
"|           　 (*　･ω･)                                                                                 <( . )>           ('')        \033[32m/\033[0m  \033[32m\\\033[0m      \033[32m/\033[0m       '--,.__   __.'\033[32m\\\033[0m       \033[32m/\033[0m  \033[32m\\\033[0m      |",
"| ＿＿＿＿＿＿(__つ/￣￣￣/_ ＿＿＿                                                                    _(__.__)_        <(  . )>      \033[32m/\033[0m  \033[32m\\\033[0m     \033[32m/\033[0m                      \033[32m\\\033[0m       \033[32m/\033[0m  \033[32m\\\033[0m      |",
"|           　　＼/　\033[96mKT\033[0m　/        |                                                                   (|       |)       (   .  )     \033[32m/\033[0m    \033[32m\\\033[0m   \033[32m/\033[0m                        \033[32m\\\033[0m     \033[32m/\033[0m    \033[32m\\\033[0m     |",
"""|                                 |                                                                .. ==========='`   ... '--`-` ...  `\033[97m||\033[0m`     \033[32m`"="==""==,,,..,="=="==="`\033[0m     `\033[97m||\033[0m`      |""",
"                                  | #####---...___...-----._##---...___...-----.##---...___...-----..__.----.(\-''#####---__.----.(\-''#####---...___...-----._##---...___...-----.##-- |",
"┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙ "]

stars = [
    '\033[96m' + '.' + '\033[0m',
    '\033[33m' + '.' + '\033[0m',
    '\033[96m' + '*' + '\033[0m',
    '\033[33m' + '*' + '\033[0m',
    '\033[95m' + '+' + '\033[0m',
    '\033[33m' + '+' + '\033[0m',
]

def main():

    x_list = [i for i in range(183)]
    y_list = [i for i in range(36)]

    while True:
        
        # To mac or linux
        # os.system("clear")
        
        # To window
        os.system("cls")
        
        
        # random value injection
        sampled_x = random.sample(x_list, 34)
        sampled_y = random.sample(y_list, 34)

        map_for_drawing = copy.deepcopy(map)

        for x, y in zip(sampled_x, sampled_y):
            try:
                list_map_xy = list(map_for_drawing[y + 1])
                if list_map_xy[x] == " ":
                    list_map_xy[x] = random.choice(stars)
                map_for_drawing[y + 1] = "".join(list_map_xy)

            except:
                pass

        print("\n".join(map_for_drawing))
        time.sleep(0.5)

if __name__ == "__main__":
    main()
