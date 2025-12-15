
try:
    time = int(input("Enter any Seconds"))

    hours =time//3600

    minutes= (time%3600)//60

    seconds= time - (hours*3600 + minutes*60)


    print(f"Hours: {hours } \nMinutes: {minutes} \nSeconds: {seconds}")
except Exception as e:
    print("Invalid Input",e)