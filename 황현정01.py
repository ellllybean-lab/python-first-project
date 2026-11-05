#랜덤으로하기
import random

player_name = input ("플레이어 이름: ")

# 게임 카운터 횟수 시작
user1_count = 0
user2_count = 0


# 가위바위보 고르기
choice ={1:"가위",2:"바위",3:"보"}

# 시작 꾸미기
print("=" * 41)
print(f"{'가위 / 바위 / 보 게임':^35}")
print("=" * 41)
print("1. 가위 / 2. 바위 3. 보")





#게임시작
while True:

    user_input = input("번호를 선택하세요. : ")
    number = random.randint(1, 3)
    user = int(user_input) 

    if user <= 0 or user > 3:
            print("1~3 사이값을 입력하세요.")
            continue

    print()
    print("[게임 결과]")
    print(f"{player_name}: {choice[user]} vs 컴퓨터: {choice[number]}")
    
    if user == number:
        result=("비김")
        print(result)
        

    elif (
        (user == 1 and number == 3) or
        (user == 2 and number == 1) or
        (user == 3 and number == 2)
    ):
        result=("이김")
        print(result)
        user1_count += 1

    else:
        result=("패배")
        print(result)
        user2_count += 1

    print()
    print(f"현재 스코어 {player_name} {user1_count} : {user2_count} 컴퓨터 ")
    print()

    if user1_count >= 2:
        print(f"{player_name} {user1_count}승 달성! 경기종료")
        user_input = input("다시도전 (yes/no): ")
        if user_input == "yes":
            user1_count = 0
            user2_count = 0
            continue
        elif user_input == "no": 
            print("게임종료")
            break
         
    elif user2_count >=2:
        print(f"컴퓨터 {user2_count}승 달성! 경기종료")
        user_input = input("다시도전 (yes/no): ")
        if user_input == "yes":
            user2_count = 0
            user1_count = 0
            continue 
        elif user_input == "no": 
            print("게임종료")
            break


        
    #컴퓨터 난수를 발생시켜 가위 바위 보 데이터 저장 : ok
    #플레이어 화면에 가위 바위 보 번호를 입력 : ok
    #승패판정결과 : ok
    
    #플레이어 이름 입력 받아서 승패 기록에 표시 : ok
    #3판2선 승제로 최종 결과 계산 : ok
    #각 판별 승패 목록 표시 : 
    #연승기록 누적해서 표시 : 
