#double_char
def double_char(str):
  res = ""
  for i in range(len(str)):
    res += str[i]*2
  return res

#count_code
def count_code(str):
  x=["co"+i+"e" for i in str.lower()]
  count = 0
  index = 0
  for i in x:
    if i in str[index:]:
      index = str.find(i)+1
      count+=1
  return count

#count_hi
def count_hi(str):
  cnt = 0
  for i in range(len(str)-1):
    if str[i] == "h" and str[i+1]=="i":
      cnt += 1
      
  return cnt

#end_other
def end_other(a, b):
  a1 = a.lower()
  b1 = b.lower()
  if a1.endswith(b1) or b1.endswith(a1):
    return True
  return False

#cat_dog
def cat_dog(str):
  cnt_dog = 0
  cnt_cat = 0
  for i in range(len(str)):
    if str[i:i+3] == "dog":
      cnt_dog += 1
    elif str[i:i+3] == "cat":
      cnt_cat += 1
  
  if cnt_dog == cnt_cat:
    return True
  else:
    return False

#xyz_there
def xyz_there(str):
  if len(str) >= 3 and str[:3] == "xyz":
    return True
  
  for i in range(1, len(str)-2):
    if str[i - 1] != '.' and str[i:i + 3] == "xyz":
      return True
  
  return False
