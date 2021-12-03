import string
import random

class Characters:

    def __init__(self,symbols,numbers):
        self.symbols=symbols
        self.numbers=numbers

    def capital_alphabets(self):
        capital_letters=list(string.ascii_uppercase)
        return capital_letters

    def small_alphabets(self):
        small_letters=list(string.ascii_lowercase)
        return small_letters

    def _numbers(self):
        numbers = self.numbers.split(" ")
        return numbers

    def _symbols(self):
        symbols=self.symbols
        return symbols.split(" ")

class Password:
    def generating_password(self):
        nums="0 1 2 3 4 5 6  7 8 9  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5"
        sign= "~ ` @ # $ % ^ & * ( ) _ - + = [ ] { } \ | ' : ; < > , . / ? "
        ch=Characters(sign,nums)
        capital_letters=ch.capital_alphabets()
        small_letters=ch.small_alphabets()
        numbers=ch._numbers()
        symbols=ch._symbols()
        characters=[capital_letters,small_letters,numbers,symbols]
        password=""
        length= int(input("How Long Password You Want?? "))
        for length in range(0,length):
            index1=int(random.uniform(0,4))
            index2=int(random.uniform(0,26))
            character=characters[index1][index2]
            password+= str(character)
        return password

def main():
    ps=Password()
    password=ps.generating_password()
    print(f"Password: {password}")
    return password

main()