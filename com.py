#Comprehension 
#In python,list Comprehension means a shortcut for making a list.
# Here no need to write long line codes.

#for example : [x for x in range(5)]
#output:0,1,2,3,4

#(without a comprehension)
squares=[]
for x in range(1,6):
    squares.append(x**2) 
    print(squares)


#(with a comprehension)
squares=[x**2 for x in range(1,6)]
print(squares)

