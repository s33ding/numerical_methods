def bolzano(f, a, b):
    print(f"Test of Bolzano:")
    fa =  f(a) 
    fb =  f(b) 
    res =  fa * fb 
    print(f"res = fa * fb = {res}") 
    bool_val =  fa * fb < 0
    print(f"{bool_val} --> {res} < 0") 
    return bool_val
