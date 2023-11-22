def time_text(minutes):
    heures = minutes // 60
    minutes = minutes - (heures * 60)
    print("{} heures et {} minutes".format(heures, minutes))

time_text(152)
time_text(239)
time_text(42)
time_text(4)