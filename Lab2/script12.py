dt = input("Input Departure time: ").split(":")
at = input("Input Arrival time: ").split(":")
tt = 0
dt[0] = int(dt[0])*60
at[0] = int(at[0])*60
tt = (int(at[0])+int(at[1])) - (int(dt[0])+int(dt[1]))
ht = tt/60
mt = tt%60
print("The trip time will be: ", int(ht)," hr and ",mt,"min")
