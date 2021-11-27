#!/usr/bin/python

"""
Name - Prajeesh Marakkaparambil Prakasan
StudeId - 21252034
Github Repository Link - https://github.com/prajeeshmp0802/ARC
"""
import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.#

'''
********* Summary ************
Used basic Python and Numpy arrays.Store and process use  python basic data structures such as
set /dictionary ,list (mostly). Total 4 solutions obtained in which 3 solutions use loop iterative model to find values 
in column wise and row wise.Among 4 solutions one required matrix rotation other3 was just the pattern and color as expected
To find the pattern & color 

Commonalities :-  Used for loop in column wise & row wise to search find the color pattern
 and color value.Here Mapping of Big graid size to small grid size is occured .Use python basic data structures and store the frequency (histogram)
 of  color values.For pattern identification used color repetition and if it is above 2 consider as pattern in most cases.
 
Difference - Only one solution one time iterate either column or row wise as per pattern. But  other two solutions
initially iterate to find the pattern . Then again repeat the row or column travel to apply pattern in output 
 
 Solution :- In the below 4 problems all training pattern is solved and also all the test pattern also solved 
********

******** 5ad4f10b.json ***********

****** Transformation **********
Output is 3x3 matrix square . Input grid value is 20x24 Matrix and the colored pattern square 
can be any number .But in output mapping each repeated pattern represented as 1 square
Output square coloring value will be the color which is not background color(black),
also not the square color in input grid.There are square grid without colorin input grid which should be plot same as black in output

*****  Code Logic Transformation  ******
Initially Iterate through column wise to find and compare the color value to 
find the repeated pattern color . If color pattern repeat more than 2time 
consider that as the output pattern in column wise.Also find the 
pattern number( 3, 4, 5 etc..).Initial identify the start column and row value where
 tha pattern begins So  execute column wise loop and check the square color exist
in that if so same color apply in output pattern using index formula 

'''

def solve_5ad4f10b(x):
    m,n = x.shape
    prev_col=-1
    patrn_col_color = 1  #counter for pattern length find
    start_row=-1  #these will map the start row & col of patern
    start_col=-1
    patrn_color=-1 # used to save the color value to aply in pattern
    fill_color=-1
    no_patrn_repeat = 0  # this wil be the length of the pattern in column wise
    first_time_bol= False # this used as a condition to set start row & col
    cur_squa_matrix=[0,0,0,0,0,0,0,0,0]# 1D array later save as 3x3 patern 2D array with values
    
    for col in range(n):  # Iterate  loop in column wise to store color & patern length 
      # col=3+
       patrn_color=-1
       patrn_col_color=1
       prev_col=-1
       v=list(x[:,col])
       for intx,val in enumerate(v): # each column value process
           if (prev_col!=0 and prev_col==val): # if repeated color value find consider it as pattern
                patrn_col_color +=1   # patrern color value countre increment 
          
           if(prev_col==patrn_color and prev_col!=val and patrn_color!=-1):
               no_patrn_repeat=patrn_col_color# once patren identifed save the lnegth before patern continuty lost again
               break  # once the patern continuty find & lost to bg color then apply break to exit loop
           if(patrn_col_color>2):
               patrn_color= val # save the color need to apply in pattren if pattern counter is >2 
           prev_col = val  # assign  for column valeu comapriosn with previous cell value in same column
       if(patrn_color!=-1): # reste values when exiting each column and before enter new column
           prev_col=-1
           patrn_col_color=1
           break
    for col in range(n):
        v=list(x[:,col])
        for intx,val in enumerate(v):
            #as per o/p patern select color will be not backgorund black , also not the input patern 
            #color, so the 3rd color value identified here 
            if(val != patrn_color and val!=0 and fill_color==-1):
                fill_color= val
            
            if (patrn_color==val and first_time_bol==False):#set row and column . This row column is maped to 3x3 dimensions
                start_row=intx
                start_col = col
                first_time_bol= True
            if(patrn_color==val and start_row>intx):# each time if alread y identfied start row in column value is less than new row in another column
                start_row=intx  #Eg- last  pattre traing pattren in his 
    
    
    for col in range(n):
       # MAPPING HIGH size  matrix to low size 3x3 2d
       v=list(x[:,col])
       for intx,val in enumerate(v):
          #Identify the first column 
           if(col==start_col and first_time_bol==True):
               #In one set of column  process each row .1st colum affect 0,3,6
               #second colum 1,4,7 etc.....
               if(intx==start_row and patrn_color==val):
                   cur_squa_matrix[0]= fill_color
               if(intx==(start_row+no_patrn_repeat) and patrn_color==val):
                   cur_squa_matrix[3]= fill_color
               if(intx==(start_row+(2*no_patrn_repeat)) and patrn_color==val):
                   cur_squa_matrix[6]= fill_color
           #Identify the column comes aftre first bloackof pattern        
           if(col==(start_col+no_patrn_repeat) and first_time_bol==True):
               if(intx==start_row and patrn_color==val):
                   cur_squa_matrix[1]= fill_color
               if(intx==(start_row+no_patrn_repeat) and patrn_color==val):
                   cur_squa_matrix[4]= fill_color
               if(intx==(start_row+(2*no_patrn_repeat)) and patrn_color==val):
                   cur_squa_matrix[7]= fill_color
            #Identify the column comes aftre second bloackof pattern     in similar of 3x3 matrix    
           if(col==start_col+(2*no_patrn_repeat) and  first_time_bol==True):
               if(intx==start_row and patrn_color==val):
                   cur_squa_matrix[2]= fill_color
               if(intx==(start_row+no_patrn_repeat) and patrn_color==val):
                   cur_squa_matrix[5]= fill_color
               if(intx==(start_row+(2*no_patrn_repeat)) and patrn_color==val):
                   cur_squa_matrix[8]= fill_color
    #print("test")
    x=np.array(cur_squa_matrix).reshape(3,3)
    return x

'''
******** 1f85a75f.json ********

****** Transformation **********
Input grid size of 30x30 is transformed to form a shape of  size same as pattern colored in 
special color  input grid. There is no predefined size . to filter the shape of pattre find color whose 
 presence is less compare dto other colro.So find minimum color value . The push the pattern row col value to another set
 Then ideal set with same row & column value created and find difference with pattern colored cell
 so we can identify where the balck colored required compared to ideal  matrix position.
 
 
 ********* Code Logic ***************
 Core logic is using set type  difference find the unmatched value this unmatched value will be cell 
 where background  black color applied . So for that initially find col row values and 
 sorted to find the color pattern- minimum color value compared to black and other color.
 So used the color pattern to fill the list with cell(x,y) values 

'''

def solve_1f85a75f(x):
    m,n = x.shape
    color= dict() # store all the color counts in pattern 
    start_col=-1  #these start end values to judge the size of pattern
    end_col=-1 
    start_row=-1
    end_row=-1
    for col in range(n):
        v=list(x[:,col])
        # Itertae loop  to store the color count 
        for ind,val in enumerate(v): 
            if val not in color:
                color[val]=1
            else:
                color[val]+=1
    word_counts = list(color.items())  # convert dict to a list of tuples for word counts
    min_color = sorted(word_counts, key=lambda x: x[1], reverse=False)
    a,b=min_color[0] # from pattern observed minmum occured color values is applied 
    pos=[]
    for col in range(n):       
        v=list(x[:,col])
        #Loop to fill the start /end column & cell value(row col) of pattern color applied number 
        for ind,val in enumerate(v):
            
            if(val == a and start_col==-1):# itertae each column and check the pattern color observed or not 
                start_col=col    # once the start of patern color observed then set start column for process
            if(val == a and start_col!=-1 and end_col!=col):
                end_col=col
            if(val == a):
               pos.append((ind,col)) # save the real cell position of each cell in pattren with color comapriosn 
    #Loop to find the start row & end row . 
    for row in range(m):
         v=list(x[row,:])
         for ind,val in enumerate(v):
            if(val == a and start_row==-1):
                start_row=row
            if(val == a and start_row!=-1 and end_row!=row):
                end_row=row      
    #identify  the pattern size 
    re_col = (end_col-start_col)+1
    re_row = (end_row-start_row)+1
    # create a dummy 2D matrix with expected color value of pattern this will
    #later aftre manpulation assign to x
    y=a*np.ones((re_row,re_col))
    #Cretae a list of ideal pattren position without any black color
    Ideal_set=[]
    for i in range(start_col,end_col+1,1):
        for j in range(start_row,end_row+1,1):
            Ideal_set.append((j,i))
    Ideal_set = set(Ideal_set)
    pos= set(pos)
    #Subtract from Ideal  to real pattern  will get which cells are not present or  with black values in pattern
    diff= Ideal_set-pos
    diff=list(diff)
    #Loop through those  cell position (row,col) values set value as 0.
    for inc,dat in enumerate(diff):
        row =dat[0]-start_row # here subtraction will plote from higher lever matrxi to smaller level o/p matrxi
        col= dat[1]-start_col
        y[row][col]=0
    #Now this y hold pattern what we really want and assign to x return x
    x= y
    return x
'''    
****** Transformation **********
Pattern direction is formed either row wise or column wise So need to identify that .
Then shift the red square in 2 cells right 

 ********* Code Logic ***************
solved by logic to check green cells in column or row pattern.Once the pattern direction
identified then shift the square points 2 cell value right/down direction.
 

'''

def solve_5168d44c(x):
    m,n = x.shape
    col_wise= False
    index_val =0
	
    #read each column wise values.
    for col in range(n):
        v=list(x[:,col])
        if(v.count(3)>2):  # check green color in column wise more than 2.
            col_wise= True
            index_val= col # Identify which column has green pattern observed
            v_1=list(x[:,col-1]) # square left side value 
            x[:,col-1] = v_1[-2:] + v_1[:-2] #shift left side valueof square  down ward 2 cell position
            v_2=list(x[:,col+1]) # square right side value
            x[:,col+1] = v_2[-2:] + v_2[:-2] # shift right side of square down ward 2 cell position 
            ind= v.index(2)  # find the start of center part of sqare
            v[ind+2]=2  # aftre transformation center top shift position 2cell
            v[ind+4]=2   # aftre transformation center bottom  shift position 2cell
            v[ind]=0  # set previous position to black color 
            x[:,col] = v
    if(col_wise==False):
        for row in range(m):  #read each row wise values.
            v=list(x[row,:]) 
            if(v.count(3)>1):  # # check green color in row wise more than 2.
                v_1=list(x[row-1,:])  # take the left part of square 
                x[row-1,:] = v_1[-2:] + v_1[:-2] #shift the square left part 2 cells right 
                v_2=list(x[row+1,:])          # take the right part of square
                x[row+1,:] = v_2[-2:] + v_2[:-2] #shift the square left part 2 cells right 
                ind= v.index(2)    # find the start of center part of sqare
                v[ind+2]=2      # # aftre transformation center  shift position 2cell
                v[ind+4]=2     # # aftre transformation center top shift position 2cell
                v[ind]=0
                x[row,:] = v
                
                
    return x

'''

******** ed36ccf7.json ***********

****** Transformation **********
Here input pattern is repeated 90 degree anti -clockwise will create the result
Color will be same as input

****** Code Logic **************
 The idea is for each square cycle, swap the elements involved with the corresponding
 cell in the matrix in anti-clockwise direction i.e. from top to left, left to bottom,
 bottom to right and from right to top one at a time using nothing but a temporary
 variable to achieve this.
'''

def solve_ed36ccf7(x):
    N=3
    for xcnt in range(0, int(N / 2)):
        for y in range(xcnt, N-xcnt-1):
            # store current cell in temp variable
            temp = x[xcnt][y]
            # move values from right to top
            x[xcnt][y] = x[y][N-1-xcnt]
            # move values from bottom to right
            x[y][N-1-xcnt] = x[N-1-xcnt][N-1-y]
            # move values from left to bottom
            x[N-1-xcnt][N-1-y] = x[N-1-y][xcnt]
            # assign temp to left
            x[N-1-y][xcnt] = temp
      
    return x

def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()

