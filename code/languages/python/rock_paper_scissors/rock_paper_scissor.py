from random import choice  # 무작위 선택을 위해 choice 함수를 import

# 게임 타이틀을 출력
print("======================================")
print("    Rock Paper Scissors Game!")
print("======================================")

# 게임 루프 시작
while True:
    # 사용자에게 선택 옵션을 보여줌
    print("\nOptions:\n- Rock\n- Paper\n- Scissors")
    player1 = input("Enter your choice: ")  # 사용자 입력 받기
    choices = ["ROCK", "PAPER", "SCISSORS"]  # 가능한 선택지
    player2 = choice(choices)  # 컴퓨터의 무작위 선택
    print("\nSHOOT!!!")
    print(f"Player 2 played {player2}")  # 컴퓨터의 선택 출력

    # 승패 결정 로직
    if player1.upper() != player2:
        if (player1.upper() == "ROCK" and player2 == "SCISSORS") or \
           (player1.upper() == "SCISSORS" and player2 == "PAPER") or \
           (player1.upper() == "PAPER" and player2 == "ROCK"):
            print("\n** Player 1 wins! **")  # 플레이어 1 승리
        else:
            print("\n** Player 2 wins! **")  # 플레이어 2 승리
    else:
        print("\n** It's a tie! **")  # 비김

    # 게임 계속 여부 확인
    print("---------------------------------------")
    flag = input("Do you want to continue? (yes/no): ")
    if flag.lower() == "no":
        break  # 루프 종료

# 게임 종료 메시지
print("\nThank you for playing!")
