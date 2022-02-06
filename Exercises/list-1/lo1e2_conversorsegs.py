# This exercise converts seconds to the equivalent in days, hours, minutes and seconds remaining


seconds_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_s = int(seconds_str)

minutes = total_s // 60
remaining_s = total_s % 60

hours = minutes // 60
remaining_mins = minutes % 60

days = hours // 24
remaining_hrs = hours % 24

print(days,"days,",remaining_hrs,"hours,",remaining_mins,"minutes","and",remaining_s,"seconds.")


