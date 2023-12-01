import sys

FILE = sys.argv[1]

##
## The calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
##
def computeCalibrationValue1(line):
  firstDigit = 0
  lastDigit = 0
  for c in line:
    if c.isdigit():
      firstDigit = c
      break
  for c in reversed(line):
    if c.isdigit():
      lastDigit = c
      break

  return int(firstDigit + lastDigit)

##
## It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
##
def computeCalibrationValue2(line):
  numbers = { 
    "one" : 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, 
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
  }

  minIdx = -1
  minVal = None
  maxIdx = -1
  maxVal = None

  for n in numbers.keys():
    idx = line.find(n)
    rIdx = line.rfind(n)
    if idx >= 0 and (idx < minIdx or minIdx < 0):
      minIdx = idx
      minVal = numbers[n]
    if rIdx >= 0 and (rIdx > maxIdx):
      maxIdx = rIdx
      maxVal = numbers[n]
  
  print(int(str(minVal) + str(maxVal)))
  return int(str(minVal) + str(maxVal))
  

## Main
sum1 = 0
sum2 = 0
with open(FILE) as fp:
  for line in fp:
    sum1 += computeCalibrationValue1(line)
    sum2 += computeCalibrationValue2(line)

print(f'Sum of calibration values (#1) = {sum1}')
print(f'Sum of calibration values (#2) = {sum2}')