import random

user1_count = 0
user2_count = 0

choice ={1:"가위",2:"바위",3:"보"}

print("=" * 41)
print(f"{'가위 / 바위 / 보 게임':^35}")
print("=" * 41)
print("1. 가위 / 2. 바위 3. 보")

while True:

    user_input = input("번호를 선택하세요. :")
    number = random.randint(1, 3)
    user = int(user_input) 

    if user <= 0 or user > 3:
            print("1~3 사이값을 입력하세요.")
            continue

    print("[게임 결과]")
    print(f"나:{choice[user]} vs 컴퓨터:{choice[number]}")
    

    if user == number:
        print("비김")

    elif user>= number:
        print("이김")
        user1_count += 1
    else:
        print("패배")
        user2_count += 1

    print(f"현재 스코어 나{user1_count} : {user2_count}컴퓨터 ")
    print(f"다시도전 (yes/no)")
        

    while True: 

        retry = input("다시도전 (yes/no)")
    
        if  retry == "no":
           print("게임종료")
           break
    
        if retry =="yes":
           print("다시도전")
           break


#print(f"")
#print(f"연승기록:{}회")