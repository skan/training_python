import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# game loop
 

while True:
   space_x, space_y = [int(i) for i in raw_input().split()]
   highestMounain = 0
   highestMounain_x = 0
   for i in xrange(8):
      mountain_h = int(raw_input())  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
      if mountain_h > highestMounain:
         highestMounain = mountain_h
         highestMounain_x = i
   print >> sys.stderr, space_x, space_y, highestMounain_x      

   if space_y > highestMounain and space_x == highestMounain_x :
      action = "FIRE"
   else:
     action = "HOLD"
   
   print action

