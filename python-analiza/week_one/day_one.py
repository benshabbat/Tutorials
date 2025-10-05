#exercise 1
def matrix(size):
    for i in range(size):
       for j in range(size):
           print((j+1)*(i+1), end="")
       print()
       
# matrix(3)
    

# exercise 2
def triangle(height):
    for i in range(height+1):
       for j in range(i):
           print(j+1, end="")
       print()
       
       
# triangle(4)

# exercise 3
def triangle_stars(height):
    for i in range(height):
       for j in range(i + 1):
           print("*", end="")
       print()
       
       
# triangle_stars(5)


# exercise 4
def matrix_slanted(size):
    for i in range(size):
        for j in range(size):
            if j==i:
                print(1, end="")
            else:
                print(0, end="")
        print()
        
        
# matrix_slanted(5)


# exercise 5
def matrix_chessboard(size):
    for i in range(size):
        for j in range(size):
            if (i+j)%2==0:
                print(1, end="")
            else:
                print(0, end="")
        print()
        
        
# matrix_chessboard(5)


# exercise 6
def matrix_sum(size):
    sum=0
    for i in range(size):
       for j in range(size):
            sum+=(j+1)*(i+1)
            print((j+1)*(i+1), end="")
       print()       
    print("Sum:", sum)
   
   
matrix_sum(3)