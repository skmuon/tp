"""
If you run 10 Km in 43 minutes and 30 seconds, what is your average time per mile?
What is your average speed in miles per hour?
"""

distance_in_km = 10
distance_in_mile = distance_in_km/1.61

time_in_minutes = 43.5
time_in_hours = time_in_minutes/60

# speed = distance/time
speed_in_miles_per_hour = distance_in_mile/time_in_hours

print "Average speed in %s mph" % speed_in_miles_per_hour
