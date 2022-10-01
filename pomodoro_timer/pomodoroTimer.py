import time

checkmark = 0
total_mins = 0

def tasks(task):
    global checkmark
    global total_mins
    mins=0
    print('Timer for ',task,' is 25 mins.')
    start=input('Press Enter to start the timer.')
    while mins <= 25:
        time.sleep(60)
        mins = mins + 1
        total_mins += 1
        print(mins, " minutes work completed.")
    print('End of Pomodoro')
    checkmark += 1
    print('Total check mark is ',checkmark)


def breaks():
    global checkmark
    mins = 0
    if checkmark <4:
        print('Take a short break.')
        while mins!=3:
            time.sleep(60)
            mins = mins + 1
            print(mins, " minutes break completed.")
        print('Break over')

    elif checkmark >=4:
        print('Take a long break.')
        while mins !=10:
            time.sleep(60)
            mins = mins + 1
            print(mins, " minutes break completed.")
        checkmark = 0
        print('Break over.')


def main():
    carry_on = 'y'
    task=input('Welcome to Pomodoro Timer\n What task do you want to work on? ')
    while carry_on=='y'or carry_on=='Y':
        tasks(task)
        breaks()
        carry_on = input("Do you want ot carry on?(y/n)")

    print("End of task ",task,". \nTotal time worked was minutes ", total_mins, " minutes.")

if __name__ == '__main__':
    main()