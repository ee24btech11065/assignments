import ctypes
import matplotlib.pyplot as plt


lib = ctypes.CDLL('./points.so')


lib.points.restype = ctypes.POINTER(ctypes.c_double)  


result = lib.points()


points = [result[i] for i in range(36)]
A1x, A1y,A1_1x, A1_1y,A11x,A11y,A11_1x,A11_1y,A2x,A2y, A2_1x, A2_1y,A22x,A22y,A22_1x,A22_1y,A3x,A3y,A3_1x,A3_1y,A33x,A33y,A33_1x,A33_1y,A4x,A4y,A4_1x,A4_1y,A44x,A44y,A44_1x,A44_1y,Bx,By,Cx,Cy = points[:36]


x_coords = [A1x, A1_1x, A11x, A11_1x,A2x,A2_1x,A22x,A22_1x,A3x,A3_1x,A33x,A33_1x,A4x,A4_1x,A44x,A44_1x,Bx,Cx]
y_coords = [A1y, A1_1y, A11y,A11_1y,A2y,A2_1y,A22y,A22_1y,A3y,A3_1y,A33y,A33_1y,A4y,A4_1y,A44y,A44_1y,By,Cy]


plt.scatter(x_coords, y_coords)



custom = ['A1','A1_1','A11','A11_1','A2','A2_1','A22','A22_1','A3','A3_1','A33','A33_1','A4','A4_1','A44','A44_1','B','C']


import matplotlib.pyplot as plt
for i, (x, y) in enumerate(zip(x_coords, y_coords)):
    label = f'{custom[i]} ({x:.2f}, {y:.2f})'  
    plt.annotate(label, xy=(x, y), xytext=(5, 5),
                 textcoords='offset points', fontsize=8)





     #Plot lines between points
# For example, connecting A1 -> B -> C -> A1_2, etc.
plt.plot([A1x, Bx], [A1y, By], 'k-', lw=2)  
plt.plot([Bx, Cx], [By, Cy], 'k-', lw=2)    
plt.plot([Cx, A1_1x], [Cy, A1_1y], 'k-', lw=2)  
plt.plot([A1_1x, Bx], [A1_1y, By], 'k-', lw=2) 
plt.plot([A2x,Cx],[A2y,Cy],'k-',lw=2)
plt.plot([A1_1x,Cx],[A1_1y,Cy],'k-',lw=2)
plt.plot([A2_1x,Bx],[A2_1y,By],'k-',lw=2)
plt.plot([A2_1x,Cx],[A2_1y,Cy],'k-',lw=2)
plt.plot([A2x, Bx], [A2y, By], 'k-', lw=2)  
plt.plot([A1x,Cx],[A1y,Cy],'k-',lw=2)
plt.plot([A11x,Bx],[A11y,By],'k-',lw=2)
plt.plot([A11x,Cx],[A11y,Cy],'k-',lw=2)
plt.plot([A11_1x,Cx],[A11_1y,Cy],'k-',lw=2)

plt.plot([A22x, Cx], [A22y, Cy], 'k-', lw=2)
plt.plot([A22_1x, Cx], [A22_1y, Cy], 'k-', lw=2)  
plt.plot([A3x, Cx], [A3y, Cy], 'k-', lw=2)  
plt.plot([A3_1x, Cx], [A3_1y, Cy], 'k-', lw=2)
plt.plot([A33x, Cx], [A33y, Cy], 'k-', lw=2)  
plt.plot([A33_1x, Cx], [A33_1y, Cy], 'k-', lw=2)  
plt.plot([A4x, Cx], [A4y, Cy], 'k-', lw=2)  
plt.plot([A4_1x, Cx], [A4_1y, Cy], 'k-', lw=2)  
plt.plot([A44x, Cx], [A44y, Cy], 'k-', lw=2)  
plt.plot([A44_1x, Cx], [A44_1y, Cy], 'k-', lw=2)  

plt.plot([A11_1x, Bx], [A11_1y, By], 'k-', lw=2)  
plt.plot([A22x, Bx], [A22y, By], 'k-', lw=2)  
plt.plot([A22_1x, Bx], [A22_1y, By], 'k-', lw=2)  
plt.plot([A3x, Bx], [A3y, By], 'k-', lw=2)  
plt.plot([A3_1x, Bx], [A3_1y, By], 'k-', lw=2)
plt.plot([A33x, Bx], [A33y, By], 'k-', lw=2)  
plt.plot([A33_1x, Bx], [A33_1y, By], 'k-', lw=2)  
plt.plot([A4x, Bx], [A4y, By], 'k-', lw=2)  
plt.plot([A4_1x, Bx], [A4_1y, By], 'k-', lw=2)  
plt.plot([A44x, Bx], [A44y, By], 'k-', lw=2)  

plt.plot([A44_1x, Bx], [A44_1y, By], 'k-', lw=2)  


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangles formed for all possible  A coordinates')
plt.grid(True)
plt.show()
