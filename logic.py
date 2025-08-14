# A Short Program: Opposite Day
today_is_opposite_day = True

# set say_it_is_opposite_day based on today_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# Flip the value of say_it_is_opposite_day if today_is_opposite_day is True
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day
    
if say_it_is_opposite_day == True:
    print("Today is Opposite Day:")
else:
    print("Today is not Opposite Day:")
  
