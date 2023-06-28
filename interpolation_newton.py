import pandas as pd

# Create a matrix as a Pandas DataFrame
matrix_data = [
    [95, 1548],
    [99, 1544],
    [104, 1538],
    [110, 1532]
]

df = pd.DataFrame(matrix_data, columns=['x', 'f(x)'])



def get_x_i(pair_key):
    idx = int(pair_key.split(',')[0].split('x')[-1])
    print("i:",idx)
    x = matrix_data[idx][0]
    return x 
    
def get_x_ii(pair_key):
    idx = int(pair_key.split('x')[-1][0])
    print("i:",idx)
    x = matrix_data[idx][0]
    return x 

lst_res = []
for i in range(len(matrix_data) - 1):
    x_i= matrix_data[i][0]
    fx_i = matrix_data[i][1]
    x_ii = matrix_data[i+1][0]
    fx_ii = matrix_data[i+1][1]
    result = (fx_ii - fx_i) / (x_ii - x_i)
    pair_key = f"f[x{i},x{i+1}]"
    packing = [pair_key, result]
    print(packing)
    lst_res.append(packing)

for i in range(len(lst_res) - 1):
    pair_key_i = lst_res[i][0]
    x_i = get_x_i(pair_key_i)
    fx_i = lst_res[i][1]
    pair_key_ii = lst_res[i+1][0]
    x_ii = get_x_ii(pair_key_ii)
    fx_ii = lst_res[i+1][1]
    result = (fx_ii - fx_i) / (x_ii - x_i)
    print(f"({fx_ii} - {fx_i}) / ({x_ii} - {x_i})")
    print(result)
