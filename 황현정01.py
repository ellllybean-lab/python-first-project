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

#승패기록
#history = history.append(result)

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
    print(f"나: {choice[user]} vs 컴퓨터: {choice[number]}")
    print()
    

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

    print(f"현재 스코어 나 {user1_count} : {user2_count} 컴퓨터 ")
    print()

    if user1_count == 2 or user2_count == 2:
        print("2승 달성! 경기종료")
        break


    while True:
    
        user_input = input("다시도전 (yes/no): ")

        if user_input == "yes" or user_input == "no":
             break

            print("yse or no 만 입력하세요 ")
        
    
        if user_input == "no":
            print("게임종료")
            break

        print("다시 도전")
        
    #counts = [user1_count, user2_count]
     
   # filter_counts = (max(counts, key=lambda p : p[1])) # 최고 점수 추출
    #print (f"{}판{} 승 {}승리 ")
        
    # 플래아어 이름 임력받아서 승패 기록
    # 3판 2선 승제로 최종결과 계산
    # 각 승패 목록작성
    # 재도전에 입력
    #번호에 글자 입력햇을 때 처리
    # 승리 횟수
    # 승패 판정

#result = lambda x : x
#print(result())

#print(f"")
#print(f"연승기록:{}회")