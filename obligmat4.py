import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# Total lengde(romlig) og tid
L = 1 #kvadrat med lengde 1
T = 15

# Antall punkter og tidssteg
Nx = 15
Nt = 10000

h = L/(Nx-1)  #steglengde romlig
k = T/(Nt-1)  #steglengde tid

x = np.linspace(0, L, Nx)
y = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt)

gamma = k/h**2
print("Gamma:", gamma)

u = np.zeros((Nx, Nx, Nt))

# Initialbetingelser
for i in range(1, Nx - 1):
    for j in range(1, Nx - 1):
        u[i, j, 0] = np.sin(np.pi * x[i]) * np.sin(np.pi * y[j])

# Sett randbetingelser til 0 for alle sider av domenet
u[:, 0, :] = 0  
u[:, -1, :] = 0  
u[0, :, :] = 0  
u[-1, :, :] = 0  

# Eksplisitt
for k in range(0, Nt-1):
    for j in range(1, Nx-1):
        for i in range(1, Nx-1):
            u[i, j, k+1] = gamma*(u[i+1,j,k] + u[i-1,j,k] + u[i,j+1,k] + u[i,j-1,k]) + (1-4*gamma)*u[i,j,k]

#Animasjon
fps = 30 #Frames Per Second 
frame_delay = 1000/fps #Antall millisekunder mellom hver frame
frn = 75

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
meshX, meshY = np.meshgrid(x, y)
plot = [ax.plot_surface(meshX,meshY,u[:,:,0], color='tomato', rstride=1, cstride=1)]

def update(frame, u, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(meshX, meshY, u[:,:, frame], color = 'tomato')

ax.set_zlim(0, 1.1)
ani = animation.FuncAnimation(fig, update, frn, fargs=(u, plot), interval = frame_delay)

plt.show()
