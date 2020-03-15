#sleep_in
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False

#diff21
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

#near_hundred
def near_hundred(n):
  return ((abs(100-n) <= 10) or (abs(200-n) <= 10))  

#missing_char
def missing_char(str, n):
  return str[:n]+str[n+1:]

#monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True or a_smile == False and b_smile == False:
    return True
  else:
    return False

#parrot_trouble
def parrot_trouble(talking, hour):
  if talking == True:
    if hour < 7 or hour > 20:
      return True
  return False

#pos_neg
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

#front_back
def front_back(str):
  if len(str) <= 1:
    return str
  
  return str[len(str)-1] + str[1:len(str)-1] + str[0]

#sum_double
def sum_double(a, b):
  sum = a + b

  if a == b:
    sum = sum*2
  return sum

#makes10
def makes10(a, b):
  return (a == 10 or b == 10 or a + b == 10)

#not_string
def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str

#front3
def front3(str):
  front = 3
  if len(str) < front:
    front = len(str)
  fr = str[:front]
  return fr*3