#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

#Function to get and validate user input
def get_num_terms():
  while True:
    print("How many terms of the fibbonacci sequence do you want?")
    num = input()
    if num.isdigit():
        num = int(num)
        if num > 0:
          return num
    else: 
      print("Error please input a positive number")

# Function to make fibbonacci sequence
def fibonacci_sequence(n):
  sequence = []
  a, b = (0, 1)
  for _ in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence

#function to print the sequence
def print_sequence(seq):
  print("\nFibbonacci Sequence: ", seq)

def main():
  num_terms = get_num_terms()
  seq = fibonacci_sequence(num_terms)
  print_sequence(seq)
  
if __name__ == "__main__":
  main()
