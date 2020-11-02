from random import randint

#функция создания рандомного числа с разными цифрами
def generate_number():
    
    number_one=str(randint(0,9))  #первое рандомное число
    number_two=str(randint(0,9))   #второе рандомное число
    number_three=str(randint(0,9))  #третье рандомное число
    number_four=str(randint(0,9))  #четвёртое рандомное число
    #цикл перебирающий все пары чисел, что цифры не равны, то есть все цифры разные
    while number_one==number_two or number_one==number_three or number_one==number_four or number_two==number_three or number_two==number_four or number_three==number_four:
        number_one=str(randint(0,9))
        number_two=str(randint(0,9))
        number_three=str(randint(0,9))
        number_four=str(randint(0,9))
    generated_number=number_one+number_two+number_three+number_four
    #print('Number to guess: ', generated_number)
    return generated_number 

generated_number=str(generate_number())  #загаданное число
bik=kor=0  #количество быков и коров
players_answer=str(input('Enter your number: \n'))  #считываем ответ игрока
while generated_number!=players_answer:
    bik=kor=0 #обнуляем счётчик быков и коров
    for i in range(4):           #цикл перебора всех пар цифр
        for j in range(4):
            if generated_number[i]==players_answer[j]:  #пока цифра загаданного числа не равна цифре из ответа игрока 
                if i!=j:    #если у них не равны позиции, то это корова
                    kor+=1
                if i==j:    #если равны позиции, то бык
                    bik+=1
    print('Bulls: ', bik)
    print('Cows: ', kor)
    players_answer=str(input('Enter another number: \n'))
print('You won the game!')    