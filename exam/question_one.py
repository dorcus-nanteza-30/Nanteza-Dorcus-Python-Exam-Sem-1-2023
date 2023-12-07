#radius of a circle
area=pi*r**2
area=pi*5**2
radius = 5
#print(area)


#removing and inserting in alist
java=["1","3","5","7","9"]
java.remove("3")
print(java)

java=["1","3","5","7","9"]
java.insert("10")
print(java)

java = ["2", "4", "6", "8", "10"]
newlist = []

#for x in java:
 # if "a" in x:
   # newlist.append(x)

#print(newlist)

numbers_list = [2, 4, 6, 8, 10]

# Call the function and pass the list as an argument
even_numbers(numbers_list)


def total_even_odd(number):
    count_odd=0
    count_even=0
    for x in number:
        if not x % 2:
            count_even+=1
        else:
            count_odd+=1
total_even_odd(1,2,3,4,5,6,7,8)


#update and adding in a dictionary
student_info = {
  "Name ": "Alice",
  "Age": "20",
  "grade": "A"
}
thisdict["city"] = "NewYork"
print(thisdict)

#update dictionary
student_info = {
  "Name ": "Alice",
  "Age": "20",
  "grade": "A"
}
thisdict.update({"Age": "25"})


#comprehension of a dictionary with only key-values