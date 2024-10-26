import ctypes
import matplotlib.pyplot as plt


lib = ctypes.CDLL('./points.so')


lib.points.restype = ctypes.POINTER(ctypes.c_double)  


result = lib.points()


points = [result[i] for i in range(20)]
Aax, Aay,Aa_1x, Aa_1y,Abx,Aby,Ab_1x,Ab_1y,Acx,Acy, Ac_1x, Ac_1y,Adx,Ady,Ad_1x,Ad_1y,Bx,By,Cx,Cy = points[:20]


x_coords = [Aax, Aa_1x, Abx, Ab_1x,Acx,Ac_1x,Adx,Ad_1x,Bx,Cx]
y_coords = [Aay, Aa_1y, Aby,Ab_1y,Acy,Ac_1y,Ady,Ad_1y,By,Cy]


plt.scatter(x_coords, y_coords)



custom = ['Aa','Aa_1','Ab','Ab_1','Ac','Ac_1','Ad','Ad_1','B','C']


import matplotlib.pyplot as plt
for i, (x, y) in enumerate(zip(x_coords, y_coords)):
    label = f'{custom[i]} ({x:.2f}, {y:.2f})'  
    plt.annotate(label, xy=(x, y), xytext=(5, 5),
                 textcoords='offset points', fontsize = 8)
plt.plot([Aax, Bx], [Aay, By], 'k-', lw=2)  
plt.plot([Aax, Cx], [Aay, Cy], 'k-', lw=2)  
plt.plot([Aa_1x, Bx], [Aa_1y, By], 'k-', lw=2)  
plt.plot([Aa_1x, Cx], [Aa_1y, Cy], 'k-', lw=2)  
plt.plot([Abx, Bx], [Aby, By], 'k-', lw=2)  
plt.plot([Abx, Cx], [Aby, Cy], 'k-', lw=2)  
plt.plot([Ab_1x, Bx], [Ab_1y, By], 'k-', lw=2)  
plt.plot([Ab_1x, Cx], [Ab_1y, Cy], 'k-', lw=2)  
plt.plot([Acx, Bx], [Acy, By], 'k-', lw=2)  
plt.plot([Acx, Cx], [Acy, Cy], 'k-', lw=2)  
plt.plot([Ac_1x, Bx], [Ac_1y, By], 'k-', lw=2)  
plt.plot([Ac_1x, Cx], [Ac_1y, Cy], 'k-', lw=2)  
plt.plot([Adx, Bx], [Ady, By], 'k-', lw=2)  
plt.plot([Adx, Cx], [Ady, Cy], 'k-', lw=2)  
plt.plot([Ad_1x, Bx], [Ad_1y, By], 'k-', lw=2)  
plt.plot([Ad_1x, Cx], [Ad_1y, Cy], 'k-', lw=2)  

plt.plot([Cx, Bx], [Cy, By], 'k-', lw=2)  



plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangles formed for all possible  A coordinates')
plt.grid(True)
plt.show()
