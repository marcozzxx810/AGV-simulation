import math


class Carn:

    def __init__ (self, Carn_type, x, y):
        self.Carn_type = Carn_type
        self.x = x
        self.y = y

    def finddistance (self, node):
        distance = math.sqrt( (self.x - node.x) ** 2 + (self.y - node.y) ** 2 )
        return distance


class node:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def finddistance (self, node):
        distance = math.sqrt( (self.x - node.x) ** 2 + (self.y - node.y) ** 2 )
        return distance


class avg_car( object ):

    def __init__ (self, env, Total_Power: int, Power_usage: int, Walking_spped: int, Location: node, Power_Limit: int,
                  Job_list: Carn, Loc_Charging_pad: node):
        self.env = env
        self.Loc_Charging_pad = Loc_Charging_pad
        self.Job_list = Job_list
        self.Power_Limit = Power_Limit
        self.Location = Location
        self.Walking_spped = Walking_spped
        self.Power_usage = Power_usage
        self.Total_Power = Total_Power

        self.action = env.process( self.run() )

    def findclosestJob(self):
        distance_list = []
        for i in range(len(self.Job_list)):
            Job = self.Job_list[i]
            distance_list.append(self.Location.finddistance(Job[0]))
        return distance_list.index(min(distance_list))

    def set_totalpower(self, power):
        self.Total_Power = power

    def set_location(self, location : node):
        self.Location = location

    def run(self):
        while True:
            closest_job_index = self.findclosestJob();
            current_job= self.Job_list[closest_job_index]
            current_job_distance = current_job[0].finddistance(current_job[1])
            walk_distance = self.Location.finddistance(current_job[0])
            total_distance = current_job_distance + walk_distance
            power_required = total_distance / self.Power_usage + 4
            if ( self.Total_Power - power_required > self.Power_Limit):
                time_required = total_distance/self.Walking_spped
                print( 'AVG is doing task %d at %d' % (closest_job_index, self.env.now) )
                yield self.env.timeout(time_required)
                Total_power = self.Total_Power - power_required
                self.set_totalpower(Total_power)
                print( "AVG have %d power"  % self.Total_Power )
                self.set_location(node(current_job[1].x,current_job[1].y))
                print( "AVG at %d , %d " % (self.Location.x, self.Location.y) )
                del self.Job_list[closest_job_index]
            else :
                distance_charging_pad = self.Location.finddistance(self.Loc_Charging_pad)
                power_required = distance_charging_pad / self.Power_usage
                print( "AVG is backing to charging pad")
                time_required = distance_charging_pad / self.Walking_spped
                yield self.env.timeout( time_required )
                self.set_totalpower(100)
                print( "AVG have %d power" % self.Total_Power )
                self.set_location( self.Loc_Charging_pad )
                print( "AVG at %d , %d "% (self.Location.x, self.Location.y) )




