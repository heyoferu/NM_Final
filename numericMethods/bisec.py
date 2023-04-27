def f(x):
     return x**3 + x**2 - 3*x - 3 

def bisec(a,b,n):
    iterations = n
    while iterations != 0:

        aprox_r = (a + b) / 2

        if f(a) * f(aprox_r) < 0:
             b = aprox_r
        
        elif f(a) * f(aprox_r) > 0:
             a = aprox_r

        elif f(a) * f(aprox_r) == 0:
             break
        
        iterations -= 1
             
bisec(1,2,10)
