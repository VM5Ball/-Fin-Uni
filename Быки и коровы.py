from random import randint

def generate_number():
    
    number_one=str(randint(0,9))
    number_two=str(randint(0,9))
    number_three=str(randint(0,9))
    number_four=str(randint(0,9))
    while number_one==number_two or number_one==number_three or number_one==number_four or number_two==number_three or number_two==number_four or number_three==number_four:
        number_one=str(randint(0,9))
        number_two=str(randint(0,9))
        number_three=str(randint(0,9))
        number_four=str(randint(0,9))
    generated_number=number_one+number_two+number_three+number_four
    #print('Number to guess: ', generated_number)
    return generated_number 

generated_number=str(generate_number())
bik=kor=0
print('Enter your number: ')
players_answer=str(input())
while generated_number!=players_answer:
    bik=kor=0
    for i in range(4):
        for j in range(4):
            if generated_number[i]==players_answer[j]:
                if i!=j:
                    kor+=1
                if i==j:
                    bik+=1
    print('Bulls: ', bik)
    print('Cows: ', kor)
    print('Enter another number')
    players_answer=str(input())
print('You won the game!')    