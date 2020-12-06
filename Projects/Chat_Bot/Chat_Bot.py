def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print('Question 1. In the context of software programming, what does IDE stand for?')
    print('1. Implemented Development Environment')
    print('2. Integrated Development Environment')
    print('3. International DevelopmeIntegrated Development Environmentnt Environment')
    print('4. Integrated Design Environment')
    ans: int = int(input('Your answer is ?'))
    while ans!=2:
        ans= int(input('Please, try again.'))
    print('Right answer, Integrated Development Environment\n')

def test2():
    print('Question 2.Programmer who writes system software is called ?')
    print('1. System programmer')
    print('2. Analysis programmer')
    print('3. Train programmer')
    print('4. design programmer')
    ans: int = int(input('Your answer is ?'))
    while ans!=1:
        ans= int(input('Please, try again.'))
    print('Right answer, Programmer who writes system software is called System programmer\n')

def test3():
    print('Question 3.Programmer who works with high level language and have better understanding with applications are considerd as ?')
    print('1. design programmer')
    print('2. Train programmer')
    print('3. Analysis programmer')
    print('4. Application programmer')
    ans: int = int(input('Your answer is ?'))
    while ans!=4:
        ans= int(input('Please, try again.'))
    print('Right answer, Programmer who works with high level language and have better understanding with '+ 
          'applications are considerd as Application programmer\n')
    

def end():
    print('Congratulations, have a nice day!')


greet('BOT', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
test2()
test3()
end()