#make_bricks
def make_bricks(small, big, goal):
  return (goal%5)<=small and (goal-(big*5))<=small

#no_teen_sum
def no_teen_sum(a, b, c):
  def fix_teen(n):
    return n if n not in [13,14,17,18,19] else 0

  return fix_teen(a)+fix_teen(b)+fix_teen(c)

#make_chocolate
def make_chocolate(small, big, goal):
  if goal >= 5 * big:
    remainder = goal - 5 * big
  else:
    remainder = goal % 5
        
  if remainder <= small:
    return remainder
        
  return -1  

#lone_sum
def lone_sum(a, b, c):
  sum = 0
  sum += a if a not in [b,c] else 0
  sum += b if b not in [a,c] else 0
  sum += c if c not in [a,b] else 0
  return sum

#round_sum
def round_sum(a, b, c):
  def round10(num):
   return (num+5)/10*10

  return round10(a)+round10(b)+round10(c)

#lucky_sum
def lucky_sum(a, b, c):
  sum = 0
  list = [a,b,c,13]
  for n in list[:list.index(13)]:
    sum += n
  return sum

#close_far
def close_far(a, b, c):
  a_b_diff = abs(a - b)
  a_c_diff = abs(a - c)
  b_c_diff = abs(b - c)

  return ((a_b_diff <= 1 and a_c_diff >= 2 and b_c_diff >= 2) !=(a_c_diff <= 1 and a_b_diff >= 2 and b_c_diff >= 2))
