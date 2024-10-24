import ctypes
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./points.so')

# Define the return type and argument types of the C function
lib.points.restype = ctypes.POINTER(ctypes.c_double)  # Assuming the function returns a pointer to doubles

# Call the C function to get the points
result = lib.points()

# Extract the coordinates from the result
# Assuming the result is an array of 12 doubles (2 coordinates for each of 6 points)
points = [result[i] for i in range(12)]
A1x, A1y, A2x, A2y, A1_2x, A1_2y, A2_2x, A2_2y,Bx,By,Cx,Cy = points[:12]

# Prepare points for plotting (assuming these are the coordinates you want to plot)
x_coords = [A1x, A1_2x, A2x, A2_2x,Bx,Cx]
y_coords = [A1y, A1_2y, A2y, A2_2y,By,Cy]

# Plot the points
plt.scatter(x_coords, y_coords)

custom = ['A1','A1_2','A2','A2_2','B','C']
# Label the points
for i, (x, y) in enumerate(zip(x_coords, y_coords)):
    label = f'{custom[i]}({x:.2f},{y:.2f})'
    plt.text(x, y, label)



     #Plot lines between points
# For example, connecting A1 -> B -> C -> A1_2, etc.
plt.plot([A1x, Bx], [A1y, By], 'k-', lw=2)  # Line between A1 and B
plt.plot([Bx, Cx], [By, Cy], 'k-', lw=2)    # Line between B and C
plt.plot([Cx, A1_2x], [Cy, A1_2y], 'k-', lw=2)  # Line between C and A1_2
plt.plot([A1_2x, Bx], [A1_2y, By], 'k-', lw=2)  # Line between A1_2 and A2
plt.plot([A2x,Cx],[A2y,Cy],'k-',lw=2)
plt.plot([A1_2x,Cx],[A1_2y,Cy],'k-',lw=2)
plt.plot([A2_2x,Bx],[A2_2y,By],'k-',lw=2)
plt.plot([A2_2x,Cx],[A2_2y,Cy],'k-',lw=2)
plt.plot([A2x, Bx], [A2y, By], 'k-', lw=2)  # Line between A2 and A2_2
plt.plot([A1x,Cx],[A1y,Cy],'k-',lw=2)

# Display the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangles formed for all possible  A coordinates')
plt.grid(True)
plt.show()
