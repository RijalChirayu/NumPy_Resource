import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection = '3d')
x_data = np.arange(-5 , 5 , 0.5)
y_data = np.arange(-5 , 5 , 0.5)

X , Y = np.meshgrid(x_data  , y_data)


Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X , Y  , Z , cmap='Spectral')

# ax.plot(x_data , Z , color='blue' , marker = '*' , alpha = 0.3 )
ax.set_title('3d Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

