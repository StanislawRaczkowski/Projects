# DisplayData.py

def DisplayData(data, num_knots):
    for i in range(num_knots):
        print(f"x{i+1} = {data[i][0]}, f(x{i+1}) = {data[i][1]}, f'(x{i+1}) = {data[i][2]}")
