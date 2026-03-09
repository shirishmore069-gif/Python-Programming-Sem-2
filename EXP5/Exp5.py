#  dictionary operations:dd, delete, and 

"""
Created on Mon Mar  9 15:01:11 2026

@author:aarya
"""
student = {}
# Adding key-value pairs
student["name"] = "Rahul"
student["age"] = 20
student["course"] = "Python"
print("Dictionary after adding elements:")
print(student)
# Updating a value
student["age"] = 21
print("\nDictionary after updating a value:")
print(student)
# Deleting a key-value pair
del student["course"]
print("\nDictionary after deleting a key-value pair:")
print(student)
