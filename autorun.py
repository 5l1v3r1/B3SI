import B3SI
from time import sleep

def main():
    done = False
    while not done:
        print(" ------------------------------------------- ")
        print(" |           Starting autopilot!           | ")
        print(" ------------------------------------------- ")
        auto = B3SI.B3()
        auto.check_temp()
        auto.a_temp()
        #auto.take_pic()
        #auto.sort_uniq()
        print(" -------------------------------------------------- ")
        print(" | Waiting a couple minutes before another loop.| ")
        print(" -------------------------------------------------- ")
        sleep(100)
    
if __name__ == '__main__': 
        main()
