from datetime import date

with open('birthdaylist.txt', mode='a') as file:
    print('Enter a name: ', end='')
    name= input()
    file.write(name)
    file.write('\n')
    print("Enter year of birth: ",end='')
    year= int(input())
    while year not in range(1900, 2022):
        print("Invalid year. Please enter a valid year: ", end='')
        year= int(input())
    print("Enter month of birth: ", end='')
    month= int(input())
    while month not in range(1, 13):
        print("Invalid month. Please enter a valid month: ", end='')
        month= int(input())
    print("Enter day of birth: ", end='')
    day= int(input())
    while day not in range(1, 32):
        print("Invalid day. Please enter a valid day: ", end='')
        day= int(input())
    birthday= date(year, month, day)
    file.write(f"birthdate: {birthday}")
    file.write('\n')