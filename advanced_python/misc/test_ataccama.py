#!/usr/bin/python
if __name__ == "__main__":

    for i in range (1,101):
        if i%3 == 0 and i%5 == 0 :
            print("TickTock")
        elif i%3 == 0:
            print("Tick")
        elif i%5 == 0:
            print("Tock")
        else:
            print(i)
