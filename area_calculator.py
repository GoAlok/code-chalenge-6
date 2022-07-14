"""
    Instruction-
        - A bucket of paint can cover 5 sq. meters of wall. Give random height and width of wall, 
            calculate how many bucket of paint you will need to buy.

            -   number of bucket = (wall height X wall width) / coverage per bucket
                -   If result is in decimals round of it to next number.
        
"""
import math
def paint_calc(height, width, cover):
    area = (height * width) 
    print("Area:", area)
    num_of_bucket = math.ceil(area/cover)
    print(f"Number of paint bucket required is {num_of_bucket}.")    
test_h = int(input("Enter Height: "))
test_w = int(input("Enter Width : "))
coverage = int(input("Coverage per bucket: "))
paint_calc(height = test_h, width = test_w, cover = coverage)
