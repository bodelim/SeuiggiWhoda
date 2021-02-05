#sexSeuiggi.py
import sex

count = 0
def POWERSEX(name: str = "승기 [ 모쏠 아다 병신 ]", partner: str = "이름", manIsHyunja: bool = True, tools: list = ['고자승기']):
    while True:
        sex.push("Penis", "Pussy") # 자지로 밀다 PP
        sex.setTime(3000) #ms
        sex.start()
        if count > 5:
            sex.seuiggi()
            count = 0
        count += 1
        if girlIsUpset == True:
            print('{}: \"야(아) 너무 빨리 쌌잖아\"'.format(partner))
            print('{}: \"그.. 다시세워볼까?\"'.format(name))
            print('{}: 자기야 나 부랄이 띵해'.format(partner))
            sex.motelOut()
            print('{}: \"{}야(아) 다신 만나지말자\"'.format(partner, name))
            break
        if manIsHyunja == True:
            print('하..싸버렸어')
            print('좀만 쉬자')
            sex.rest(10000) #ms
            sex.setTools(tools)
            print('자기야 도구로 가버리게 해줄께')
            manIsHyunja = False
            POWERSEX(name, partner, manIsHyunja)
        else:
            rand = random.randrange(1,10)
            manIsHyunja = True
            if rand > 9:
                girlIsUpset = True
            POWERSEX(name, partner, manIsHyunja)

POWERSEX()
print("승기 모쏠 아다")