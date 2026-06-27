#1.check if a matrix is square
'''def is_square(mat):
    row_len=len(mat)
    col_len=len(mat[0])
    if row_len==col_len:
        return True
    else:
        return False
mat=[[1,2],[3,4],[4,5]]
print(is_square(mat))'''


#2.print diagonal elements
'''def diagonal(mat):
    row_len=len(mat)
    col_len=len(mat[0])
    res=[]
    for i in range(row_len):
        for j in range(col_len):
            if i==j:
                res.append(mat[i][j])
    return res
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(diagonal(mat))'''


#3.print anti-diagonal elements
'''def antidiagonal(mat):
    row_len=len(mat)
    col_len=len(mat[0])
    res=[]
    for  i in range(row_len):
        for j in range(col_len):
            if i+j==2:
                res.append(mat[i][j])
    return res
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(antidiagonal(mat))'''


#4.print non-diagonal elemets
'''def non-diagonal(mat):
    row_len=len(mat)
    col_len=len(mat[0])
    res=[]
    for i in range(row_len):
        for j in range(col_len):
            if i!=j:
                res.append(mat[i][j])
    return res
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(non-diagonal(mat))'''


#5.print non antidiagoonal elements
'''def non_antidiagonal(mat):
    row_len=len(mat)
    col_len=len(mat[0])
    res=[]
    for  i in range(row_len):
        for j in range(col_len):
            if i+j != 2:
                res.append(mat[i][j])
    return res
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(non_antidiagonal(mat))'''


#6.Lower Triangle elements  of Matrix
'''def low_triangle(mat):
    row_len=len(mat)
    col_len=len(mat[0])
    res=[]
    for  i in range(row_len):
        for j in range(col_len):
            if i+j >= 2:
                res.append(mat[i][j])
    return res
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(low_triangle(mat))'''


#7.Upper Triangle elements of Matrix
def upper_triangle(mat):
    row_len=len(mat)
    col_len=len(mat[0])
    res=[]
    for  i in range(row_len):
        for j in range(col_len):
            if i+j <= 2:
                res.append(mat[i][j])
    print(res)
mat=[[1,2,3],[4,5,6],[7,8,9]]
upper_triangle(mat)


