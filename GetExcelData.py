from random import randrange
import pandas as pd
import itertools
from node import *


def exceltoList (str):
    from pprint import pprint
    data = pd.read_excel( str, sheet_name='Sheet1' )
    df = pd.DataFrame( data, columns=['Type', 'x-axis', 'y-axis'] )

    Excel_arraylist = df.values
    nodes_list = []

    # Transform excel data to nodes object
    for i in Excel_arraylist:
        nodes_list.append( Carn( i[0], i[1], i[2] ) )

    return nodes_list

def jobGenerator (Carn_list: Carn):
    JobList = []
    with open("test.txt",'w',encoding = 'utf-8') as f:
        for i in range( len( Carn_list ) ):
            tmp1 = randrange(len(Carn_list))
            tmp2 = randrange(len(Carn_list))
            Job = [Carn_list[tmp1], Carn_list[tmp2]]
            JobList.append( Job )
            f.write("Start: "+ "x: "+ str(Job[0].x)+" y:"+ str(Job[0].y)+" "+ "End: x:"+ str(Job[1].x)+" y:"+ str(Job[1].y) + "\n"  )
    

    return JobList
