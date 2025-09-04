import matplotlib.pyplot as plt
import numpy as np

plt.figure(facecolor='White')
plt.title("Kiit graafik")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)


# Näited
# x = np.arange(-5, 10, 1) # -5 - 9
# y = x**2-5*x+6
# plt.plot(x, y, color='red', linestyle='-', marker='o', markersize=8, label='y=x^2-5x+6')
# plt.show()

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# plt.plot(x, y)
# plt.title("Lihtne graafik")
# plt.xlabel("x telg")
# plt.ylabel("y telg")
# plt.show()

# plt.scatter(x,y)
# plt.show()

# plt.bar(x,y)
# plt.show()

# plt.hist(x,y)
# plt.show()

# plt.pie(x)
# plt.show()



# Ülesanne Kiit
x1 = np.arange(0, 9, 0.1)
y1 = (2/27)*x1**2 - 3
plt.plot(x1, y1, color='blue', marker='s', markersize=5)
x2 = np.arange(-10, 0, 0.1)
y2 = 0.04*x2**2 - 3
plt.plot(x2, y2, color='blue', marker='s', markersize=5)
x3 = np.arange(-9, -3, 0.1)
y3 = (2/9)*(x3 + 6)**2 + 1
plt.plot(x3, y3, color='blue', marker='s', markersize=5)
x4 = np.arange(-3, 9, 0.1)
y4 = (-1/12)*(x4 - 3)**2 + 6
plt.plot(x4, y4, color='blue', marker='s', markersize=5)
x5 = np.arange(5, 8.3, 0.1)
y5 = (1/9)*(x5 - 5)**2 + 2.4
plt.plot(x5, y5, color='blue', marker='s', markersize=5)
x6 = np.arange(5, 8.5, 0.1)
y6 = (1/8)*(x6 - 7)**2 + 1.9
plt.plot(x6, y6, color='blue', marker='s', markersize=5)
x7 = np.arange(-13, -9, 0.07)
y7 = -0.75*(x7 + 11)**2 + 6
plt.plot(x7, y7, color='blue', marker='s', markersize=5)
x8 = np.arange(-15, -13, 0.1)
y8 = -0.5*(x8 + 13)**2 + 3
plt.plot(x8, y8, color='blue', marker='s', markersize=5)
x9 = np.arange(-15, -10, 0.2)
y9 = np.ones_like(x9) # x || x=y
plt.plot(x9, y9, color='blue', marker='s', markersize=5)
x10 = np.arange(3, 4, 0.1)
y10 = 3*np.ones_like(x10)
plt.plot(x10, y10, color='blue', marker='s', markersize=5)

plt.show()