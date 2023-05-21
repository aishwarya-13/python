from random import choice
"""
Print numbers from 1 to 10
"""
number = 1
while number<=10:
    print(number)
    number+=1

"""
Print even numbers from 1 to 20
"""
num=1
while num<=20:
    if num % 2 == 0:
        print(num)
    num+=1

"""
Keep on asking question until the answer is "just"
"""

questions = ["Why is sky blue?: ", "Why is moon far away?: ", "Why is sea vast?: "]
question = choice(questions)
answer = input(question).strip().lower()
while answer != "just":
    answer = input("Why is sky blue?: ").strip().lower()