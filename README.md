# Lisp_interpreter
This is an interpreter of programming language LISP written on python.
<br>
<br>
Here I built Mandelbrot fractal & bifurcation diagram on Lisp.
<br>
<br>
Code for Mandelbrot fractal was created with the help of ChatGPT:
```
# Define the function to calculate the Mandelbrot set
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < 255:
        z = z*z + c
        n += 1
    if n == 255:
        return "#FFFFFF" # black if in the set
    else:
        return "#" + "{0:02x}{1:02x}{2:02x}".format(n, n, n) # gray scale based on iteration count
```
Result:
<br>
![image](https://user-images.githubusercontent.com/71407757/230757546-1c3f21d9-251d-4b10-af72-df34f0c2c6d1.png)

Here is the code for bifurcation diagram from wiki:

```
import matplotlib.pyplot as plt

x3 = 0.01
s = []
c = []
l = 0.01
for j in range(200):
    x0=x3
    for i in range(200):
        x0 = 1 - l*x0*x0
        s.append(x0)
        c.append(l)
    x3=x0
    l += 0.01

plt.plot(c,s,'r.',ms=1)
plt.show()
```
Result:
<br>
![image](https://user-images.githubusercontent.com/71407757/230757636-25f5bbec-a964-4074-ac1c-62bc9866dadb.png)
<br>

