
# coding: utf-8

# In[41]:


def validSolution(board):
    TrueFalse = []
    for j in range(len(board)):
        for k in range(len(board)):
            if board[j][k] == 0:
                TrueFalse.append(False)
            else : TrueFalse.append(True)
    for i2 in board:
        #pass
        #print(i2)
        if len(set(i2)) == len(i2): TrueFalse.append(True)
        else: TrueFalse.append(False)
    for i1 in range(len(i2)):
        #pass
        a = [x[i1] for x in board]
        #print(a)
        if len(set(a)) == len(a): TrueFalse.append(True)
        else : TrueFalse.append(False)
    list2 =[]
    for m in range(len(board)//3):
        for n in range(len(board)//3):
            list2 =[]
            for j in range(3):
                for k in range(3):
                    list2.append(board[j+m*3][k+n*3])
            if len(list2) == len(set(list2)):
                TrueFalse.append(True)
            else: TrueFalse.append(False)
    if False in TrueFalse: return False
    else: return True
    
    
validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]])


# In[ ]:


def validSolution(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows

def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if not check_one_to_nine(nums):
                return False
    return True

def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True
    
def validate_rows(board):
    for row in board:
        if not check_one_to_nine(row):
            return False
    return True
            

def check_one_to_nine(lst):
    check = range(1,10)
    return sorted(lst) == check

