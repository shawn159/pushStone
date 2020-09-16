from bangtal import *

#마우스로 초록색 공을 움직여서, 파란색 공을 밀어, 빨간 땅에 모두 넣으면 비밀의 문이 열립니다!!

scene1 = Scene('방1', 'images/scene1.png')
scene2 = Scene('방2', 'images/scene2.png')
player = Object('images/player.png')
stair1 = Object('images/stair.png')
stair2 = Object('images/stair.png')
stone1 = Object('images/stone.png')
stone2 = Object('images/stone.png')
door = Object('images/door.png')

T = 0
D = 1
R = 2
L = 3

VER_LEN = 114
HOR_LEN = 118

VER_BASE = 104
HOR_BASE = 195

player_loc = [0, 4]
stone1_loc = [3, 3]
stone2_loc = [6, 1]

PLY_NUM = 2
STN_NUM = 3
STR_NUM = 8
HOLE_NUM = 9
FIN_NUM = 5

scenes = [scene1, scene2]
stones = [stone1, stone2]
stone_loc = [stone1_loc, stone2_loc]

scene_num = 0

finish1 = False
finish2 = False

map_data1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1],
             [1,0,1,8,1,0,0,3,0,0,1,1,1,1,1,0,1],
             [1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1],
             [1,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,1],
             [1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1],
             [1,0,0,0,0,0,1,0,0,0,0,0,0,3,1,1,1],
             [1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1],
             [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_data2 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
             [1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1],
             [1,1,1,8,1,0,0,0,0,0,0,0,0,0,1,1,1],
             [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1],
             [1,5,1,1,1,0,0,0,0,0,1,0,0,0,0,5,1],
             [1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
             [1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_data = [map_data1, map_data2]

x = HOR_BASE + player_loc[0] * HOR_LEN
y = VER_BASE + player_loc[1] * VER_LEN
player.locate(scenes[scene_num], x, y)
x = HOR_BASE + stone1_loc[0] * HOR_LEN
y = VER_BASE + stone1_loc[1] * VER_LEN
stone1.locate(scenes[scene_num], x, y)
x = HOR_BASE + stone2_loc[0] * HOR_LEN
y = VER_BASE + stone2_loc[1] * VER_LEN
stone2.locate(scenes[scene_num], x, y)
stair1.locate(scene1, 310, 445)
stair1.setScale(0.5)
stair2.locate(scene2, 310, 445)
stair2.setScale(0.5)
player.show()
stair1.show()
stair2.show()
stone1.show()
stone2.show()

def stone_move_check(dir):
    stone_num = 0

    if dir == T:
        if stone1_loc[0] == player_loc[0] and stone1_loc[1] == player_loc[1] + 1:
            stone_num = 0
        elif stone2_loc[0] == player_loc[0] and stone2_loc[1] == player_loc[1] + 1:
            stone_num = 1
        else:
            pass
        map_x = 1 + stone_loc[stone_num][0] * 2
        map_y = 1 + (4 - stone_loc[stone_num][1]) * 2
        if map_y - 2 > 0 and map_data[scene_num][map_y - 1][map_x] != 1:
            return stone_num, True
    elif dir == D:
        if stone1_loc[0] == player_loc[0] and stone1_loc[1] == player_loc[1] - 1:
            stone_num = 0
        elif stone2_loc[0] == player_loc[0] and stone2_loc[1] == player_loc[1] - 1:
            stone_num = 1
        else:
            pass
        map_x = 1 + stone_loc[stone_num][0] * 2
        map_y = 1 + (4 - stone_loc[stone_num][1]) * 2
        if map_y + 2 < 16 and map_data[scene_num][map_y + 1][map_x] != 1:
            return stone_num, True
    elif dir == L:
        if stone1_loc[0] == player_loc[0] - 1 and stone1_loc[1] == player_loc[1]:
            stone_num = 0
        elif stone2_loc[0] == player_loc[0] - 1 and stone2_loc[1] == player_loc[1]:
            stone_num = 1
        else:
            pass
        map_x = 1 + stone_loc[stone_num][0] * 2
        map_y = 1 + (4 - stone_loc[stone_num][1]) * 2
        if map_x - 2 > 0 and map_data[scene_num][map_y][map_x - 1] != 1:
            return stone_num, True
    elif dir == R:
        if stone1_loc[0] == player_loc[0] + 1 and stone1_loc[1] == player_loc[1]:
            stone_num = 0
        elif stone2_loc[0] == player_loc[0] + 1 and stone2_loc[1] == player_loc[1]:
            stone_num = 1
        else:
            pass
        map_x = 1 + stone_loc[stone_num][0] * 2
        map_y = 1 + (4 - stone_loc[stone_num][1]) * 2
        if map_x + 2 < 16 and map_data[scene_num][map_y][map_x + 1] != 1:
            return stone_num, True
    else:
        pass

    return stone_num, False

def move_check(dir):
    global scene_num

    map_x = 1 + player_loc[0] * 2
    map_y = 1 + (4 - player_loc[1]) * 2
    if dir == T:
        if map_y - 2 > 0 and map_data[scene_num][map_y - 1][map_x] != 1:
            if map_data[scene_num][map_y - 2][map_x] == STN_NUM:
                stone_num, check = stone_move_check(T)
                if check:
                    map_data[scene_num][map_y - 4][map_x] = STN_NUM
                    stone_loc[stone_num][1] += 1
                    stone_x = HOR_BASE + stone_loc[stone_num][0] * HOR_LEN
                    stone_y = VER_BASE + stone_loc[stone_num][1] * VER_LEN
                    stones[stone_num].locate(scenes[scene_num], stone_x, stone_y)
                    return True
            elif map_data[scene_num][map_y - 2][map_x] == 0:
                return True
            elif map_data[scene_num][map_y - 2][map_x] == STR_NUM:
                return True
            else:
                pass
    elif dir == D:
        if map_y + 2 < 10 and map_data[scene_num][map_y + 1][map_x] != 1:
            if map_data[scene_num][map_y + 2][map_x] == STN_NUM:
                stone_num, check = stone_move_check(D)
                if check:
                    map_data[scene_num][map_y + 4][map_x] = STN_NUM
                    stone_loc[stone_num][1] -= 1
                    stone_x = HOR_BASE + stone_loc[stone_num][0] * HOR_LEN
                    stone_y = VER_BASE + stone_loc[stone_num][1] * VER_LEN
                    stones[stone_num].locate(scenes[scene_num], stone_x, stone_y)
                    return True
            elif map_data[scene_num][map_y + 2][map_x] == 0:
                return True
            elif map_data[scene_num][map_y + 2][map_x] == STR_NUM:
                return True
            else:
                pass
    elif dir == L:
        if map_x - 2 > 0 and map_data[scene_num][map_y][map_x - 1] != 1:
            if map_data[scene_num][map_y][map_x - 2] == STN_NUM:
                stone_num, check = stone_move_check(L)
                if check:
                    map_data[scene_num][map_y][map_x - 4] = STN_NUM
                    stone_loc[stone_num][0] -= 1
                    stone_x = HOR_BASE + stone_loc[stone_num][0] * HOR_LEN
                    stone_y = VER_BASE + stone_loc[stone_num][1] * VER_LEN
                    stones[stone_num].locate(scenes[scene_num], stone_x, stone_y)
                    return True
            elif map_data[scene_num][map_y][map_x - 2] == 0:
                return True
            elif map_data[scene_num][map_y][map_x - 2] == STR_NUM:
                return True
            else:
                pass
    elif dir == R:
        if map_x + 2 < 16 and map_data[scene_num][map_y][map_x + 1] != 1:
            if map_data[scene_num][map_y][map_x + 2] == STN_NUM:
                stone_num, check = stone_move_check(R)
                if check:
                    map_data[scene_num][map_y][map_x + 4] = STN_NUM
                    stone_loc[stone_num][0] += 1
                    stone_x = HOR_BASE + stone_loc[stone_num][0] * HOR_LEN
                    stone_y = VER_BASE + stone_loc[stone_num][1] * VER_LEN
                    stones[stone_num].locate(scenes[scene_num], stone_x, stone_y)
                    return True
            elif map_data[scene_num][map_y][map_x + 2] == 0:
                return True
            elif map_data[scene_num][map_y][map_x + 2] == STR_NUM:
                return True
            else:
                pass
    else:
        pass
    
    return False



def player_action(x, y, action):
    global scene_num
    global finish1
    global finish2

    map_x = 1 + player_loc[0] * 2
    map_y = 1 + (4 - player_loc[1]) * 2
    if action == MouseAction.DRAG_DOWN:
        if move_check(D):
            player_loc[1] -= 1
            map_data[scene_num][map_y][map_x] = 0
            map_data[scene_num][map_y + 2][map_x] = PLY_NUM
        else:
            showMessage('아래가 막혀있어요')
            return
    elif action == MouseAction.DRAG_UP:
        if move_check(T):
            player_loc[1] += 1
            map_data[scene_num][map_y][map_x] = 0
            map_data[scene_num][map_y - 2][map_x] = PLY_NUM
        else:
            showMessage('위에가 막혀있어요')
            return
    elif action == MouseAction.DRAG_LEFT:
        if move_check(L):
            player_loc[0] -= 1
            map_data[scene_num][map_y][map_x] = 0
            map_data[scene_num][map_y][map_x - 2] = PLY_NUM
        else:
            showMessage('왼쪽이 막혀있어요')
            return
    elif action == MouseAction.DRAG_RIGHT:
        if move_check(R):
            player_loc[0] += 1
            map_data[scene_num][map_y][map_x] = 0
            map_data[scene_num][map_y][map_x + 2] = PLY_NUM
        else:
            showMessage('오른쪽이 막혀있어요')
            return
    else:
        pass

    player_x = HOR_BASE + player_loc[0] * HOR_LEN
    player_y = VER_BASE + player_loc[1] * VER_LEN
    player.locate(scenes[scene_num], player_x, player_y)
    if player_loc[0] == 1 and player_loc[1] == 3:
        if scene_num == 0:
            scene_num = 1
        elif scene_num == 1:
            scene_num = 0
        else:
            pass

        player.locate(scenes[scene_num], player_x, player_y)
        scenes[scene_num].enter()

    if scene_num == 0:
        map_x = 1 + 4 * 2
        map_y = 1 + (4 - 2) * 2
        if map_data2[map_y][map_x] == 0 and stone1_loc[0] == 4 and stone1_loc[1] == 2:
            map_data1[map_y][map_x] = 0
            map_data2[map_y][map_x] = STN_NUM
            stone_x = HOR_BASE + stone1_loc[0] * HOR_LEN
            stone_y = VER_BASE + stone1_loc[1] * VER_LEN
            stone1.locate(scene2, stone_x, stone_y)
        elif map_data2[map_y][map_x] == 0 and stone2_loc[0] == 4 and stone2_loc[1] == 2:
            map_data1[map_y][map_x] = 0
            map_data2[map_y][map_x] = STN_NUM
            stone_x = HOR_BASE + stone2_loc[0] * HOR_LEN
            stone_y = VER_BASE + stone2_loc[1] * VER_LEN
            stone2.locate(scene2, stone_x, stone_y)

    if not finish1:
        if (stone1_loc[0] == 0 and stone1_loc[1] == 2) or (stone2_loc[0] == 0 and stone2_loc[1] == 2):
            finish1 =True
    if not finish2:
        if (stone1_loc[0] == 7 and stone1_loc[1] == 2) or (stone2_loc[0] == 7 and stone2_loc[1] == 2):
            finish2 =True

    if finish1 and finish2:
        door.locate(scene2, 600, 250)
        door.show()

def door_click(x, y, action):
    if action == MouseAction.CLICK:
        endGame()

door.onMouseAction = door_click

player.onMouseAction = player_action

startGame(scene1)
