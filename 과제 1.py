# 해당 게임은 '발더스 게이트 3'라는 게임을 배경으로, 있을 법한 어느 주인공의 이야기를 꾸며낸 것입니다.

# 주인공 정보 설정(고정)
name = "주인공"
gender = "남자"
mainclass = "클레릭"
background = "사기꾼 출신"
level = 10
health = 100
mana = 20
attack = 20
defense = 30
magic = 50

# 게임 시작
print("주인공 은(는) 사기꾼 출신(으)로, 클레릭(으)로써 모험하는 중입니다.")
print("현재 레벨: 10")
print("체력: 100, 마나: 20, 공격력: 20, 방어력: 30, 주문력: 50")

# 직업 능력 - 일단 클레릭 하나로
if mainclass == "클레릭":
    print("클레릭 은 생명을 창조하고 치유하며, 중갑을 두르고 최전방에서 둔기로 싸우는 만능 직업입니다.")

    # 서브클래스 설정
    print("서브클래스 - '생명 권역, 기만 권역, 지식 권역, 폭풍 권역' 중 선택하여 주십시오.")
    subclass = input()

    if subclass == "생명 권역":
        print("생명 권역은 생명을 치유하며 정화시키는 능력에 특화되어 있습니다.")

    elif subclass == "기만 권역":
        print("기만 권역은 생명을 기만하며 저주와 은신, 변장 등에 특화되어 있습니다.")

    elif subclass == "지식 권역":
        print("지식 권역은 지식을 바탕으로 전투보다는 주문 그 자체의 능력에 집중합니다.")

    elif subclass == "폭풍 권역":
        print("폭풍 권역은 자연에 가까운 힘 전장을 유리하게 이끕니다.")

    else :
        print("4가지 중 하나가 아니거나 오타가 났습니다. 재실행 하시기 바랍니다.")

# 사기꾼 출신
print("주인공 은(는) 사기꾼 (으)로서 그에 걸맞는 행동 - 도둑질, 소매치기 등을 할 때 고양감을 얻습니다.")
print("고양감은 주사위를 다시 돌릴 때 사용됩니다.")

# 유저 재확인
userInput = input("해당 서브클래스로 시작하시겠습니까? (예/아니오): ")

if userInput == "예":
    print("게임을 시작합니다.")
    print(" ")

else:
    print("게임을 다시 시작해주세요. 선택은 한 번 뿐입니다.")

# 스토리 1
print("당신은 어느 외계 종족 - 일리시드 - 에 속하는 비행체 속에 감금, 속박되어 있습니다.")
print("바깥 하늘은 검고, 별들은 보이지 않습니다. 밀려드는 바람에 속도가 느껴집니다.")
print("일리시드 하나가 감옥 안으로 들어옵니다. 문어를 닮은 얼굴, 보랏빛 피부, 역겹습니다.")
print("그 '일리시드' 종족 중 한 개체가, 당신의 눈에 외계 올챙이를 강제로 집어넣습니다")
print("괴롭지만, 이상한 느낌입니다. 대체 뭐가 뇌 속에 들어온 걸까요?")

if (subclass == "지식 권역") :
    print(" ")
    print("과거 오래된 문헌에서 본 바 있습니다.")
    print("뇌 속에 들어온 그 올챙이는 앞으로 일주일이 지나면 당신을 일리시드(보라색 문어대가리)로 만들 것입니다.")
    print("하루빨리 그 올챙이를 당신의 뇌에서 빼내야겠습니다...")

else :
    print("아무리 생각해도 그 올챙이의 정체는 모르겠습니다..")
    print("그저 하루빨리 그 올챙이를 당신의 뇌에서 뺴야겠다는 의지 뿐입니다.")

print("그때, 당신이 타고 있는 비행체가 갑자기 요란하게 흔들리며, 균열이 가기 시작합니다")
print("일리시드는 크게 당황하며, 그 순간 속박의 매듭이 느슨해지는 것을 느낍니다. ")
print("어떻게 하시겠습니까?")
print("1. 운명을 받아들이고 체념한다")
print("2. 있는 힘을 다해 매듭풀기를 시도한다")

IllithidLife = True
userInput = input()
if(userInput == "1") :
    print("당신은 체념했지만, 일리시드는 당신을 신경도 쓰지 않습니다")
    print("일리시드는 도망가고, 이윽고 얼마 안 가 비행체가 추락하는 것을 느낍니다.")
    IllithidLife = True
    print("비행체는 파괴되어, 당신은 자유낙하의 몸이 됩니다.")

elif(userInput == "2") :
    print("당신의 매듭이 이윽고 풀리고, 일리시드와 마주합니다.")
    print("비행체는 점점 파괴되어가는 와중, 당신은 무엇을 할 수 있을까요?")

    if subclass == "생명 권역":
        print("당신은 생명 권역으로써 자신에게 저주해제 스킬을 사용합니다.")
        mana -= 1
        print("그러나 올챙이는 생생히 살아있음이 느껴집니다. 일리시드는 도망갑니다.")
        IllithidLife = True
        print("당신은 약간 좌절합니다..")
    
    elif subclass == "기만 권역":
        print("당신은 기만 권역입니다.")
        print("당신은 은신 스킬을 사용해 눈앞의 일리시드에게서 도망치려 시도합니다.")
        mana -= 1
        print("다행히 효과는 있었던 것 같습니다. 출구로 향하기 시작합니다. 약간의 안도.")
        print("저기 일리시드가 도망치는 것이 보입니다.")
        IllithidLife = True

    elif subclass == "지식 권역":
        print("당신은 일리시드의 감염되었다는 사실을 알지만, 그래도 일단 노력 해 봅니다.")
        print("일리시드는 물리적 타격에 약하다는 것을 떠올려내어, 틈을 타 몸통박치기를 시전합니다")
        print("일리시드는 순간 고꾸라집니다.")
        IllithidLife = False

    elif subclass == "폭풍 권역":
        print("폭풍 권역으로써, 매듭이 풀리자 당신은 곧바로 전격 폭풍 스킬을 시전합니다.")
        mana -= 1
        print("당황한 일리시드에게는 치명타였습니다. 당신은 이겼습니다. 머릿속 올챙이는 그대로이지만요.")
        IllithidLife = False

    print("그 순간, 당신은 순식간에 비행체의 손상된 균열 틈으로 빨려나가 자유낙하하기 시작합니다.")

else :
    print("당신이 고민하는 찰나의 순간, 비행체의 손상된 균열 틈으로 빨려나가 자유낙하하기 시작합니다.")
    IllithidLife = True

print("자유낙하 중인 당신이 지면에 닿는다면 필수적으로 사망이므로, 그만 눈을 감도록 합니다.")
print("지면에 닿기 직전, 바로 그 순간 알 수 없는 힘이 당신을 감싸며 지면과의 박치기를 피해줍니다.")
print("몇 초 후, 지면에 던져진 당신은 순간 밀려드는 알 수 없는 어지러움에 정신을 잃고 맙니다.")



#스토리2
print("얼마 후, 당신은 의식을 차리고 눈을 뜹니다.")
print("주변을 둘러봅니다. 간간히 보이는 시체들. 시체에서 빼낸 메이스와 기본 경갑을 착용합니다.")

if IllithidLife == False:
    print("근처 파괴된 비행체의 잔해에 깔린 채로 숨만 붙어 있는 일리시드를 발견합니다.")
    print("어떻게 할까요?")
    print("1. 조용히 물러난다.")
    print("2. 무장하고 일리시드에게 공격을 가한다.")

    userInput = input()
    if userInput == "1":
        print("당신은 조용히 물러납니다. 일리시드는 당신을 눈치채지 못한 채 숨만 헐떡입니다.")
        print("아마 곧 스스로 생명이 다 할 것입니다...")

    elif userInput == "2":
        print("당신은 무장하고 일리시드를 공격합니다.")

        if subclass == "생명 권역":
            print("당신은 생명 권역의 힘을 빌려 공격합니다.")
            print("마나를 사용하지 않는 간단한 기본 불마법입니다.")

        elif subclass == "기만 권역":
            print("당신은 기만 권역의 능력을 이용해 공격합니다.")
            print("마나를 사용하지 않는 간단한 기본 불마법입니다.")


        elif subclass == "지식 권역":
            print("당신은 지식 권역의 힘을 이용해 일리시드를 도륙합니다.")
            print("마나를 사용하지 않고, 메이스로 내려칩니다.")


        elif subclass == "폭풍 권역":
            print("당신은 폭풍 권역의 마법을 사용해 일리시드에게 일격을 가합니다.")
            print("마나를 사용하지 않는 간단한 기본 불마법입니다.")

        print("가사 상태였던 일리시드는, 쉽게 목숨을 잃습니다. 약간의 분풀이.")

else:
    print("근처에 멀쩡한 상태로 순찰 중인 일리시드를 발견합니다.")
    print("어떻게 할까요?")
    print("1. 조용히 숨는다.")
    print("2. 공격을 시도한다.")

    userInput = input()

    if userInput == "1":
        print("당신은 조용히 숨어 일리시드의 시야를 피합니다.")
        print("당신의 은신은 꽤나 탁월했습니다. 성공적으로 도망칩니다.")
        print("이후 어딘가 마주칠까 약간은 두렵지만, 그건 그때의 일이겠지요.")

    elif userInput == "2":
        print("당신은 공격을 시도합니다.")

        if subclass == "생명 권역":
            if magic >= 30:
                print("당신은 생명 권역의 힘을 빌려 공격합니다. - 상처 가해")
                mana -= 1
                print("일리시드는 힘을 잃고 쓰러집니다.")
            else:
                print("당신의 공격력이 부족해 일리시드에게 피해를 주지 못했습니다.")

        elif subclass == "기만 권역":
            if  magic >= 30:
                print("당신은 기만 권역의 능력을 이용해 공격합니다. - 매혹")
                mana -= 1
                print("일리시드는 당신의 능력에 현혹되어 허무하게 쓰러집니다.")
            else:
                print("당신의 공격력이 부족해 일리시드에게 피해를 주지 못했습니다.")

        elif subclass == "지식 권역":
            if magic >= 30:
                print("당신은 지식 권역의 힘을 이용해 일리시드를 물리칩니다. - 인간형 포박")
                mana -= 1
                print("일리시드는 당신의 공격에 의해 패배합니다.")
            else:
                print("당신의 공격력이 부족해 일리시드에게 피해를 주지 못했습니다.")

        elif subclass == "폭풍 권역":
            if magic >= 30:
                print("당신은 폭풍 권역의 마법을 사용해 일리시드에게 일격을 가합니다. - 전격 폭풍")
                mana -= 1
                print("일리시드는 강력한 공격에 휩쓸려 쓰러집니다.")
            else:
                print("당신의 마법 능력이 부족해 일리시드에게 피해를 주지 못했습니다.")

        print("당신은 일리시드를 성공적으로 물리칩니다. 약간의 분이 풀립니다.")
    
#스토리3

print("이제 해야할 일을 찾아야 합니다. 머릿속 올챙이를 최대한 빨리 제거해야 합니다..")
print("일단당신은 주변 숲을 탐험하기로 합니다. 갑자기 어딘가에서 전투, 함성 소리가 들립니다.")
print("호기심에 소리가 들려오는 방향으로 이동합니다.")
print("소리가 더욱 커지면서 당신은 '티플링'과 '드루이드' 연합군이 고블린의 침략에 맞서 싸우고 있는 모습을 발견합니다.")
print("어떻게 할지 선택하세요:")
print("1. 도망친다")
print("2. 고블린에게 맞서 싸운다")

userInput = input()
if userInput == "1":
    print("당신은 필사적으로 도망쳤으나, 결국 고블린에게 발각되어 전투에 참가하게 됩니다.")
    print("당신은 고블린을 상대로 전투에 참여합니다.")

elif userInput == "2":
    print("당신은 고블린에게 맞서 싸웁니다.")

if subclass == "생명 권역":
    if magic >= 25:
        print("당신은 고블린을 공격하여 전투에 참여합니다. - 라이프소드 소환")
        mana -= 2
        print("연합군은 당신의 도움으로 승리를 거머쥐었습니다.")
    else:
        print("당신의 공격력이 부족하여 연합군이 패배하고 맙니다.")
elif subclass == "기만 권역":
    if magic >= 25:
        print("당신은 기만 권역의 능력을 이용해 공격합니다. - 감속")
        mana -= 2
        print("고블린 무리는 당신의 능력에 현혹되어 허무하게 쓰러집니다.")
    else:
        print("당신의 마법 능력이 부족하여 연합군이 패배하고 맙니다.")
elif subclass == "지식 권역":
    if magic >= 30:
        print("당신은 지식 권역의 힘을 이용해 고블린 무리 퇴치에 기여합니다. - 감속")
        mana -= 2
        print("고블린 무리는 당신의 스킬에 의해 쉽게 패배합니다.")
    else:
        print("당신의 마법 능력이 부족하여 연합군이 패배하고 맙니다.")
elif subclass == "폭풍 권역":
    if magic >= 35:
        print("당신은 폭풍 권역의 마법을 사용해 고블린 무리에게 일격을 가합니다. - 칼날 폭풍")
        mana -= 3
        print("고블린 무리는 강력한 공격에 휩쓸려 쓰러집니다.")
    else:
        print("당신의 마법 능력이 부족하여 연합군이 패배하고 맙니다.")

#패배 시 게임끝내는 방법이 현시점에선 애매?