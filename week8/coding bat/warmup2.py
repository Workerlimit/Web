#string_times
def string_times(str, n):
  return str * n

#string_splosion
def string_splosion(str):
  res = ""
  for i in range(len(str)):
    res = res + str[:i+1]
  
  return res

#array_front9
def array_front9(nums):
  length = len(nums)
  if length > 4:
    length = 4
    
  for i in range(length):
    if nums[i] == 9:
      return True
  return False

#front_times
def front_times(str, n):
  length = 3
  if length > len(str):
    length = len(str)
  front = str[:length]
  
  res = ""
  for i in range(n):
    res += front
  return res

#last2
def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[len(str)-2:]
  count = 0
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
     count = count + 1
  return count

#array123
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

#string_bits
def string_bits(str):
  res = ""
  for i in range(len(str)):
    if i % 2 == 0:
      res += str[i]
  return res

#array_count9
def array_count9(nums):
  cnt = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      cnt += 1
  return cnt

#string_match
def string_match(a, b):
  shorter = min(len(a), len(b))
  cnt = 0
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      cnt += 1

  return cnt