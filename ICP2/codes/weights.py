lst = []
out= []
n = int(input("enter the number of weights of students in lbs"))
for i in range(0, n):
    weights = float(input("Enter input in lbs"))
    lst.append(weights)
print("the input in lbs",lst)
for j in range(n):
    v= (0.45)* lst[j]
    out.append(v)
print("the output in kgs",out)