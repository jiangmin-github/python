# coding:utf-8

"This is a program to calculate the days in a year by a given date"

# initial the days in every months
daysinyear = [31,28,31,30,31,30,31,31,30,31,30,31]

# suppose input the wrong date
inputfail = 1
while(inputfail):
    inputmsg = input("Please input the date : ")
    # all digits input 
    if inputmsg.isdigit():
        year = int(inputmsg[0:4])
        mon = int(inputmsg[4:6])
        day = int(inputmsg[6:8])

        # is this year a leap year?
        if ((year % 100) != 0) and ((year % 4) == 0):
        	daysinyear[1] = 29
        else:
        	daysinyear[1] = 28
        
        # check the month and day input 
        if mon == 0 or mon > 12:
        	print("Input the wrong Month")
        elif day == 0 or day > daysinyear[mon-1]:
        	print("Input the wrong Day")
        else:
        	# if you have a correct input,change the flag to quit the loop
        	inputfail = 0
    else:
    	print("You should input the digits!")

i = 1
totdays = 0
while i < mon:
    totdays += daysinyear[i-1]
    # print(i-1,totdays)
    i += 1
totdays += day

print(totdays," days in ",year,".") 