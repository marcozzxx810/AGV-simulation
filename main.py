from pprint import pprint
import simpy
import random
import numpy
from GetExcelData import *
from node import *
from Car import *


NO_AVG = 1
Total_power = 100
Power_usage = 100 # m per unit
Walking_speed = 3
Location = node(300, 300)
Power_Limit = 45 #45%
Loc_Charging_pad = node (200, 200)



run_time = []

def main():

    taskdone =[]

    for i in range (10) :
        env = simpy.Environment()
        AVG = avg_car(env,Total_power,Power_usage,Walking_speed,Location,Power_Limit, Loc_Charging_pad,1)
        env.run(until=1200)
        taskdone.append(min(AVG.data))

    avg = sum(taskdone)/ len(taskdone)
    print(taskdone)
    print(avg)
if __name__ == '__main__':
    main()