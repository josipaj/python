import random

def equals(num, user, cow, bull):
    for i in range(0, 4):            #ovo za bull
                if num[i] == user[i]:
                    bull += 1
    for i in num:
        if i in user:
            cow += 1

    return cow, bull

if __name__=="__main__":
    number = random.randint(1000, 9999)   #ovako za 4-znam br, mogla i priko petlje, ovako najjednostavnije
    print(number)
    number1 = [int(i) for i in str(number)]     #pretvori broj u niz
    print("Welcome to Cows and Bulls Game!")
    inp = int(input("Enter a 4-digit number: "))
    input1 = [int(i) for i in str(inp)]

    count = 0
    while number != inp:
        if inp not in range(1000, 9999):
                inp = int(input("Error! Please enter a 4-digit number: "))
        input1 = [int(i) for i in str(inp)]
        count += 1
        cows = bulls = 0
        cows, bulls = equals(number1, input1, cows, bulls)

        print(str(cows-bulls) + " Cows, " + str(bulls) + " Bulls")        #triba oduzet jer ce i ove sta su na dobrom mistu smatrat za cow

        inp = int(input("Enter a 4-digit number: "))

    print("You won in " + str(count) + " guesses!")