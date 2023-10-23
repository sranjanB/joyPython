import turtle
from random import randint

turtle.bgcolor("black")
drw = turtle.Turtle()

width = 5
height = 7
dot_distance = 25
drw.penup()
list_colour = ['white', 'yellow', 'cyan', 'magenta', 'green', 'red', 'blue', 'orange', 'pink', 'lavender', 'turquoise']

drw.setpos(-250, 250)

def spiral(row, col):
    flag = 0
    drw.color(list_colour[randint(0, 10)])
    rows = 0; cols = 0
    while(rows < row and cols < col):
        if(flag == 1):
            drw.right(90)
            drw.color(list_colour[randint(0, 10)])
        # first row only
        for i in range(cols, col):
            #print(arr[rows][i], end=" ")
            drw.dot()
            drw.forward(dot_distance)
        flag = 1
        rows += 1
        drw.right(90)
        drw.color(list_colour[randint(0, 10)])
        #traversing the last column
        for i in range(rows, row):
            drw.dot()
            drw.forward(dot_distance)
            #print(arr[i][row-1], end = " ")
        col -= 1
        drw.right(90)
        drw.color(list_colour[randint(0, 10)])
        if(rows < row):
            #Last row to left
            for i in range(col-1, cols-1, -1):
                drw.dot()
                drw.forward(dot_distance)
                #print(arr[row-1][i], end=" ")
            row -= 1
        drw.right(90)
        drw.color(list_colour[randint(0, 10)])
        if(cols < col):
            for i in range(row-1, rows-1, -1):
                drw.dot()
                drw.forward(dot_distance)
                # print(arr[i][cols], end=" ")
            cols += 1


# arr = []
# count = 1
# for i in range(4):
#     l = []
#     for j in range(4):
#         l.append(count)
#         count += 1
#     arr.append(l)
# print(arr)
spiral(20, 20)
turtle.done()
