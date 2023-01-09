import numpy as np
import matplotlib.pyplot as plt

# Create a NumPy vector t using np.linspace() from t0=-10.0 to tf=10.0, for N = 1000 points.
# Create variables a=1.0 and b=0.2

t0 = -10.0
tf = 10.0
N = 1000
t_ = np.linspace(t0,tf, N)

a = 1.0
b = 0.2

#Calculate x and y using the above expressions. Do this without using a loop, e.g. if you wanted
#to calculate z(t) = sin(2 ∗ t) then the syntax would be z = np.sin(2*t), assuming t was
#created as indicated in the previous step.

def f_x(t):
    return a * np.exp(b * t) * np.cos(t)

def f_y(t):
    return a * np.exp(b * t) * np.sin(t)

x = f_x(t_)
y = f_y(t_)

# Plot (x, y), save your plot. It should look something like fig. 1.
plt.plot(x,y)
plt.grid()
plt.show()
