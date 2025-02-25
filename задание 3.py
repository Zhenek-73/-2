import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
X = np.linspace(-12, -2, 50)
Y = np.linspace(3, 14, 50)
X_grid, Y_grid = np.meshgrid(X, Y)
Z_grid = np.sin(np.sqrt(X_grid**2 + Y_grid**2)) * 2 + np.cos(Y_grid) * 1.5
ls = LightSource(azdeg=315, altdeg=45)
shaded_Z = ls.shade(Z_grid, cmap=plt.cm.terrain, vert_exag=0.2, blend_mode='soft')
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_grid, Y_grid, Z_grid, facecolors=shaded_Z, rstride=1, cstride=1)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()


