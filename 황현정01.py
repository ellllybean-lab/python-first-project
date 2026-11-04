import random

user1_count = 0
user2_count = 0

choice ={1:"가위",2:"바위",3:"보"}

print("=" * 41)
print(f"{'가위 / 바위 / 보 게임':^35}")
print("=" * 41)
print("1. 가위 / 2. 바위 3. 보")

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
        
    user_input = input("다시도전 (yes/no): ")

    if user_input == "no":
         print("게임종료")
         break
                 
    elif user_input == "yes":
        print(result)
        continue
         
        
        
    

#result = lambda x : x
#print(result())

#print(f"")
#print(f"연승기록:{}회")