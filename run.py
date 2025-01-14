import time
with open("txtthingy.txt") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 7):
        print(''.join(lines[i:i+7]))
        time.sleep(0.3)
