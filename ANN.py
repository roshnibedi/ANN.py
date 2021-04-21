#Single Output Vertex:
"""
the function aims to multiply two lists, i.e. x and w and then add a list to it, i.e. b
Inputs: three lists with numeric entries
Output:a single numeric list 

For example: 
>>> w = [1.0, 3.5]
>>> x = [3.8, 1.5]
>>> b = -1.7
>>> linear(w,x,b)
7.35

this function should be able to multiply lists and to do that it needs to iterate through the length of one list, while multiplying the elements inside.
The outputs are then stored into a new list so that it can be recalled for further operation. 

in my implementation, i chose to use a for loop with an iterable 'i' to go through each iteration within the length of the list. Since the outputs needed 
further operation on them, i.e. adding another list, i stored it in an empty list which i then modified. the solution was then printed to be displayed as the output.
"""

z = []
result = 0
sum = 0

def linear(w,x,b):
    global result
    for i in range(len(x)):
        z = x[i]*w[i]
        result = result + z

    sum = result + b

    return sum

output = linear(a,c,d)
print("linear")
print(output)

#Output Layer:
"""
the function aims to multiply two lists and then add a list to it for the outer layer of the matrix
Inputs: three numeric lists
Output: single numeric list 
For example: 
>>> x = [1, 3.5]
>>> w = [[3.8, 1.5], [-1.2, 1.1]]
>>> b = [-1.7, 2.5]
>>> linear_layer(x,w,b)
[7.35, 5.15]

like function one, this function must be able to multiply two lists by iterating through the elements in it. The outputs are stored in a new list so further 
operations can be done on it. 

i used for loops for this code as i needed to access the elements in the list to be able to multiply it. The code used two for loops as the lists given in the
example were 3D lists. the answers were then added to the new list by using the append function and printed. 
"""

def linear_layer(x, w, b):
    result = []
    for i in range(len(b)):
        product = 0
        for j in range(len(x)):
            product = product + w[i][j]*x[j]
        result.append(round(product + b[i], 2))
    return result 

result = linear_layer(x,w,b)
print("linear_layer")
print(result)


#Inner Layers:
"""
the function is supposed to multiply two lists and then add a list to it for the inner layer of the matrix

For example: 
>>> x = [1,0]
>>> w = [[2.1,-3.1], [-0.7, 4.1]]
>>> b = [-1.1, 4.2]
>>> inner_layer(x,w,b)
[1, 3.5]

like function 2, this function must be able to multiply two lists by iterating through the elements in it. The outputs are stored in a new list so further 
operations can be done on it. 

similar to function 2, i used for loops to iterate through the elements in the list and then multiplied the appropriate values. this output was then added to b and 
the final asnwer was printed
"""
def inner_layer(x1,w1,b1):
    for i in range(len(b1)):
        product = 0
        for j in range(len(x1)):
            product = product + w1[i][j]*x1[j]
        result.append(round(product + b1[i], 2))
    return result

result = inner_layer(x1,w1,b1)
print("inner_layer")
print(result)

#Full Inference: 
"""
the function is supposed to give an output of the final ANN value 

Inputs: lists of numberic inputs (tables and biases)
Output: a number list 

For example: 
>>> x=[1,0]
>>> w=[[[2.1,-3.1],[-0.7,4.1]],[[3.8,1.5],[-1.2,1.1]]]
>>> b=[[-1.1,4.2],[-1.7,2.5]]
>>> inference(x,w,b)
[7.35, 5.15]
    """
def inference(x,w,b):
    ans =[]
    n=len(w)
    b1 = b[0]
    x1=x
    for i in range(2):
        inf = linear_layer(x1,w[i],b[i])
        print(inf)
        x1=inf

#Read weights
    """
    the function must be able to access, open and read files when asked and provide information of the file (weights of ANN)
    Inputs: a string which is the name of the file that needs to be accessed
    Output: a list of tables that correspond the the weights of ANN
>>> w = read_weights("weights.txt")
>>>print(len(w))
3
>>> print(len(w[2]))
10
>>> print(len(w[1][0]))
16
"""
def read_weights(file_name):
    f = open(file_name,"r")
    l1 = []
    l2 = []
    f.readline()
    for i in f.readlines():
        i = i.rstrip("\n") # removing '\n' char at the end.
        if i == '#':
            l1.append(l2)
            l2 = list()
        else:
            l3 = list(map(float,i.split(',')))
            l2.append(l3)
    l1.append(l2)
    return l1



# read biases 
"""
 the function must be able to access, open and read files when asked and provide information of the file (biases of ANN)
    Inputs: a string which is the name of the file that needs to be accessed
    Output: a table of numbers that correspond the the biases of ANN

>>> arr = read_biases("example_biases.txt")
>>> print("read biases:")
>>> print(arr)
arr
"""
def read_biases(file_name):
    fl=open(file_name,"r")
    arr = [] #the list arr will store list of bias values
    while True:
        ln = fl.readline() # read the file line by linear_layer
        if not ln: # end of the file has been reached
             break
        if(ln[0]=='#'): # to check if the line starts with #
            continue

        ln = ln.strip() #removes '\n' character
        ls = ln.split(",") # split the values separated by comma and put them in a list
        arr.append(ls) # insert the list ls in arr
    fl.close()
    return arr





#read image file
"""
the function must be able to read an image and respond with a list of numbers coressponding to the input of ANN
Inputs: a string which is the file name of the imagine the function will read
Output: a list of numbers 

>>> x = read_image("image.txt")
>>> len(x)
784
"""
def read_image(filename):
    
  # opening file
  file = open(filename)

  # reading the content of file
  # data will be of type string
  data = file.read()

  # splitting by row, so that each row is a list
  data = data.split("\n")

  # splitting the data in each row
  data = [i.split(" ") for i in data]

  # converting every element of row to int from string
  # now data is a nested list containing data from given file in int type
  for i in data:
      for j in i:
          data = int(j)
  #data = [[int(j) for j in i] for i in data]

  return data



# Output Selection
"""
the function must be able to output the index of the max value in a list 
Inputs: a list of numbers that represent the scores computed by Ann
Outputs: a number that shows the index of the max value in a list

For example: 
>>> x = [1.3, -1.52, 3.9, 0.1, 3.9]
>>> argmax(x)
2
"""
#function to return first index of maximum element of a list
def argmax(scores): #scores is list of computed scores by the ANN
    M = max(scores) #max function returns the maximum value from a list
    print(M)

    #index method of a python list returns the first index of passed value if the passed value is in the list
    #as M is maximum value if we pass m in index it will give first index of maximum element
    return scores.index(M) #return the computed index value

a = list(input("Enter the scores computed by ANN:"))

index = argmax(a)

print("index of element with max value: ",index) #print the index

