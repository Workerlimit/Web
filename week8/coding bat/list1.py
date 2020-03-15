#first_last6
def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  return False

#common_end
def common_end(a, b):
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True
  return False

#reverse3
def reverse3(nums):
  return nums[::-1]

#middle_way
def middle_way(a, b):
  arr = []
  arr.append(a[1])
  arr.append(b[1])
  return arr

#same_first_last
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[len(nums)-1]:
      return True
  return False

#sum3
def sum3(nums):
  return nums[0]+nums[1]+nums[2]

#max_end3
def max_end3(nums):
  arr = []
  max = 0
  end = len(nums)-1
  if nums[0] > nums[end] or nums[0] == nums[end]:
    max = nums[0]
  elif nums[end] > nums[0]:
    max = nums[end]
  i = 0
  for _ in range(3):
    arr.append(max)
  return arr

#make_ends
def make_ends(nums):
  arr = []
  if len(nums) > 2:
    arr.append(nums[0])
    arr.append(nums[-1])
    return arr
  elif len(nums) == 1:
    nums.append(nums[0])
    return nums
  return nums

#make_pi
def make_pi():
  arr = []
  arr.append(3)
  arr.append(1)
  arr.append(4)
  
  return arr

#rotate_left3
def rotate_left3(nums):
  n = nums[0]
  nums.pop(0)
  nums.append(n)
  return nums

#sum2
def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 0:
    return 0
  else:
    return nums[0]

#has23
def has23(nums):
  if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
    return True
  return False