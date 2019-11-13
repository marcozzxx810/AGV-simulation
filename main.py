from pprint import pprint
import simpy
import random
import numpy
from GetExcelData import *
from node import *

NO_AVG = 1
Total_power = 100
Power_usage = 100 # m per unit
Walking_speed = 8.33333
Location = node(300, 300)
Power_Limit = 45 #45%
Loc_Charging_pad = node (200, 200)

FileName = 'AGVInput.xlsx'

run_time = []

def main():

    Place_list = ExceltoList( FileName )
    # pprint(len(Place_list))

    Job_list = JobGenerator( Place_list )

    env = simpy.Environment()
    AVG = avg_car(env,Total_power,Power_usage,Walking_speed,Location,Power_Limit,Job_list,Loc_Charging_pad)

    env.run(until=400)
    print(len(AVG.Job_list))

if __name__ == '__main__':
    main()