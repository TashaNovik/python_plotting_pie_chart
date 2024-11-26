import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from scipy import spatial
#Функция отображения вершин
def plot_verticles(vertices, isosurf = False):
    #Создание новой графики
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]
    if isosurf:
        ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
    else:
        ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    #Отображение файла или запись файла
    plt.show()
#Функция отображения сетки
def plot_mesh(
    your_mesh,
    size_x=10,
    size_y=10,
    dpi=80):
    # Создание нового 3D-отображения
    figure = plt.figure(figsize=(size_x, size_y), dpi=dpi)
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors, edgecolor="black"))
    figure.add_axes(axes)
    #Auto scale к размеру сетки
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    #Отображение и запись графика
    plt.show()
#Вершины верхнего основания цилиндра
vertices = np.array([[0,0,0]])
phi = 0
N=20
#Первый круг
for i in range(0,N):
    vertices_1 = np.array([[0,np.cos(2*np.pi*(i)/N),np.sin(2*np.pi*(i)/N)]])
    vertices =np.append(vertices,vertices_1, axis = 0)

# Второй круг
for i in range(0,N):
    vertices_1 = np.array([[1,np.cos(2*np.pi*(i)/N),np.sin(2*np.pi*(i)/N)]])
    vertices =np.append(vertices,vertices_1, axis = 0)
#Функция создание граней из вершин
hull = spatial.ConvexHull(vertices)
faces = hull.simplices
#Массив faces содержит описание граней

#Создание сетки
cylinder_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cylinder_mesh.vectors[i][j] = vertices[f[j],:]
plot_mesh(cylinder_mesh)
#Запись сетки в файл "cylinder_mesh.stl"
cylinder_mesh.save('cylinder_mesh.stl')