import time
import main
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp = int(time.strftime("%H"))
# print(timestamp)
# timestamp = int(time.strftime("%M"))
# print(timestamp)
# timestamp = int(time.strftime("%S"))
# print(timestamp)

if(timestamp >= 5 and timestamp <= 12):
    print("Good Morning")
elif(timestamp >12 and timestamp <= 18):
    print("Good Afternoon")
elif(timestamp > 18 and timestamp <= 22):
    print("Good Evening")
else:
    print("Good Night")

main.welcome()