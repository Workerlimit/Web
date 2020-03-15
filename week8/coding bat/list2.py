#count_events
def count_evens(nums):
  cnt = 0
  for i in range(len(nums)):
    if nums[i]%2==0:
      cnt+= 1
  return cnt

#sum13
def sum13(nums):
  nums += [0]
  return sum(n for i, n in enumerate(nums) if n != 13 and nums[i-1] != 13)

#big_diff
def big_diff(nums):
  min = nums[0]
  max = 0
  for i in range(len(nums)):
    if nums[i] > max:
      max = nums[i]
  
  for i in range(len(nums)):
    if nums[i] < min:
      min = nums[i]
      
  return max-min

#sum67
def sum67(nums):
  state=0
  s=0
  for n in nums:
    if state == 0:
      if n == 6:
        state=1
      else:
        s+=n
    else:
      if n == 7:
        state=0
  return s

#centered_average
def centered_average(nums):
  max_value = nums[0]
  min_value = nums[0]
  sum = 0
  for x in nums:
    max_value = max(max_value, x)
    min_value = min(min_value, x)
    sum += x

  return (sum - max_value - min_value) / (len(nums) - 2)

#has22
def has22(nums):
  for x in range(len(nums)-1):
    if (nums[x] == 2) and (nums[x+1] == 2):
      return True
  return False
