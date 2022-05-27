# -*- coding: utf-8 -*-
"""
Created on Fri May 27 11:57:37 2022

@author: USER
"""

def convert(hours, minute): 
    numbers = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen", 
            "twenty", "twenty one", "twenty two", 
            "twenty three", "twenty four", 
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine"]; 
    if hours  <= 23 and minute  <= 59 :
        if (minute == 0): 
            print(numbers[hours], "o' clock"); 
  
        elif (minute == 15): 
            print("quarter past", numbers[hours]); 
  
        elif (minute == 30): 
            print("half past", numbers[hours]); 
  
        elif (minute == 45): 
            print("quarter to", (numbers[(hours % 12) + 1])); 
  
        elif ( 1 < minute < 30): 
            print(numbers[minute],"minutes past", numbers[hours]); 
  
        elif (30 < m < 59): 
            print(numbers[60 - minute], "minutes to", numbers[(hours % 12) + 1]); 
    else: 
        print('incorrect entry') 

  
 
h = int(input('enter time')); 
m = int(input('enter minute')); 
convert(h, m);
