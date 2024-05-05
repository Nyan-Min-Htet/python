import random
user_score = 0
computer_score = 0
draw_time = 0 
option = ['rock','paper','scissor']

while True:
    user_input = input("Type 'Rock', 'Paper', 'Scissor' or 'Q' to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in option:
        continue
    
    random_num = random.randint(0,2)
    computer_picked = option[random_num]
    print("Computer picked " + computer_picked)
    
    if user_input == computer_picked:
        print("Draw")
        draw_time += 1
    
    elif user_input == 'rock' and computer_picked == 'scissor':
        print("You Won")
        user_score += 1
    
    elif user_input == 'paper' and computer_picked == 'rock':
        print("You Won")
        user_score += 1
    
    elif user_input == 'scissor' and computer_picked == 'paper':
        print("You Won")
        user_score += 1
    
    else:
        print("Computer Won")
        computer_score += 1
    
print("Bye Bye")
print(f"You won {user_score} times")
print(f"Computer won {computer_score} times")
print(f"Draw {draw_time} times")