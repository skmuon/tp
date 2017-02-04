"""
If I leave my house at 6.52 am and I run 1 mile at an easy pace (8:15 per mile),
then 3 miles at temp (7:12 per mile) and 1 mile at easy pace again, what time
do I get home for breakfast?
"""


# Converting everything to minutes (The question was confusing, especially the notation)

starting_hour = 6
starting_mins = 52

total_time_for_the_run_in_mins = (((7*60) + 12)*2 + ((8*60)+15)*3)/60

ending_mins = (starting_mins + total_time_for_the_run_in_mins) % 60
ending_hour = starting_hour + 1
print "Arrival time is %d:%d" % (ending_hour , ending_mins)

