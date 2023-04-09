import matplotlib.pyplot as plt

x3 = 0.01
s = []
c = []
step = 0.01

for j in range(200):
    x0 = x3
    for i in range(200):
        x0 = 1 - step*x0*x0
        s.append(x0)
        c.append(step)
    x3 = x0
    step += 0.01

plt.plot(c, s, 'b.', ms=1)
plt.show()
