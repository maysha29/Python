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

#Control flow in comprehension

#Control flow in comprehension means if,else and for conditions can be applied in comprehension.
#example : if 
a=[x for x in range(10) if x%2==0]
print(a)

#if...else
b=['Even' if x % 2== 0 else 'odd' for x in range(5)]
print(b)

#nested loop
c=[(i,j) for i in range(2) for j in range(3)]
print(c)