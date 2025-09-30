#!/usr/bin/env python3

counter = 0
while counter <= 0:
  print("User Input: ")
  counter = int(input())
  if counter > 0:
    break
  else:
    print("\nPlease input a positive integer")

print("Expected Output: ")
a = 0
b = 0
c = 1
while a < counter:
  print(b)
  temp = b + c
  b = c
  c = temp
  a += 1
  
# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
