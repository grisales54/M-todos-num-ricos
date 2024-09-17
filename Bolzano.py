def bolzano(x):
    y = x**5 - 2 * x**3 + +3 * x**2 - 1

    return y


a = 0
b = 1

fa = bolzano(a)
fb = bolzano(b)

if fa * fb < 0:
    print("Existe raiz")
