
cities = ["თბილისი", "ბათუმი", "კურორტი", "ვარკეთილი", "ზუგდიდი", "ქუთაისი"]

# 1
print("მეორე ელემენტი:", cities[1])  
print("მეექვსე ელემენტი:", cities[5])  

# 2
print("შუა ორი ელემენტი:", cities[2:4])  

# 3
import random
random.shuffle(cities)  
print("არეული თანმიმდევრობით:", cities)
