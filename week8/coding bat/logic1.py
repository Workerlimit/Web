#cigar_party
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  if cigars >= 40 and cigars <= 60:
    return True
 
  return False

#caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed > 65 and speed <=85:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed > 60 and speed <= 80:
      return 1
    else:
      return 2

#love6
def love6(a, b):
  if a == 6 or b ==6 or a + b == 6 or a - b == 6 or b - a == 6:
    return True
  else:
    return False

#date_fashion
def date_fashion(you, date):
  if you == 2 or date == 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1

#sorta_sum
def sorta_sum(a, b):
  summa = a+ b
  if summa >= 10 and summa <= 19:
    return 20
  return summa

#in1to10
def in1to10(n, outside_mode):
  if outside_mode:
    if n <= 1 or n >= 10:
      return True
  else:
    if n >= 1 and n <= 10:
      return True
  return False

#squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer:
    if temp <= 100 and temp >= 60:
      return True
  else:
    if temp >= 60 and temp <= 90:
      return True
  return False

#alarm_clock
def alarm_clock(day, vacation):
  if vacation:
    if day >= 1 and day <= 5:
      return "10:00"
    else:
      return "off"
  else:
    if day >= 1 and day <= 5:
      return "7:00"
    else:
      return "10:00"

#near ten
def near_ten(num):
  if num%10 <= 2 or (10-num%10) <= 2:
    return True
  return False
