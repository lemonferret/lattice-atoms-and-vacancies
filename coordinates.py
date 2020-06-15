import numpy as np
import matplotlib.pyplot as plt
import copy as copy
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations

# For bcc
def cell(n):
	init1 = np.array([0, 0, 0]) # x, y, z
	init2 = np.array([0.5, 0.5, 0.5])
	
	mask = np.empty([0, 3])
	for k in range(0, n[0]):#x
		for j in range(0, n[1]):#y 
			for i in range(0, n[2]):#z
				mask = np.vstack((mask, [init1[0]+k, init1[1]+j, init1[2]+i]))
				mask = np.vstack((mask, [init2[0]+k, init2[1]+j, init2[2]+i]))
	return mask

#for 3x3x3
#monovac 1/1
def vac_mono(coor):
	return np.delete(coor, [27], 0), 'Mono'
#divac 3/3
def vac_di(coor, config): #*Atomic_simulation_of_the_vacancies_in_BCC_metals_w.pdf
	if config==1:
		vac =  [27, 26]
		title ='Di1. the first-nearest-neighbor (FN)'
	elif config==2:
		vac =  [44, 26]
		title ='Di2. the second-nearest-neighbor (SN)'
	elif config==3:
		vac =  [50, 26]
		title ='Di3. the third-nearest-neighbor (TN)'
	return np.delete(coor, vac, 0), title 
#trivac 8/8
def vac_tri(coor, config): #*Atomic_simulation_of_the_vacancies_in_BCC_metals_w.pdf
	if config==1:
		vac = [27, 26, 25]
		title ='Tri1. two first- and one second-nearestneighbor [112]'
	elif config==2:
		vac = [50, 27, 26]
		title ='Tri2. two first- and one third-nearest-neighbor [113]'
	elif config==3:
		vac = [52, 27, 26]
		title ='Tri3. two first- and one fifth-nearest-neighbor [115]'
	elif config==4:
		vac = [45, 27, 26]
		title ='Tri4. one first-, one second- and one forth-nearest-neighbor [124]'
	elif config==5:
		vac = [46, 44, 26] 
		title ='Tri5. two second- and one third-nearest-neighbor [223]'
	elif config==6:
		vac = [44, 26, 8]
		title ='Tri6. two second- and one sixth-nearest-neighbor [226]'
	elif config==7:
		vac = [52, 44, 26]
		title ='Tri7. one second-, one third- and one fifth-nearest-neighbor[235]'
	elif config==8:
		vac = [46, 34, 26]
		title ='Tri8. three third-nearest-neighbor [333]'
	return np.delete(coor, vac, 0), title 
#tetravac 4/???		
def vac_tetra(coor, config):
	if config==1:
		vac = [46, 44, 28, 26]
		title ='Tet1.'
	elif config==2:
		vac =  [45, 44, 27, 26]
		title ='Tet2.'
	elif config==3:
		vac =  [44, 32, 27, 26]
		title ='Tet3.'
	elif config==4:
		vac = [32, 27, 26, 9]
		title ='Tet4.'
	return np.delete(coor, vac, 0), title 
	
def plotter(mask, coor, title):
	fig = plt.figure()
	ax1 = fig.add_subplot(111, projection='3d')
	
	#Draw one cell
	r = [1, 2]
	for s, e in combinations(np.array(list(product(r, r, r))), 2):
		if np.sum(np.abs(s-e)) == r[1]-r[0]:
			ax1.plot3D(*zip(s, e), color="blue")
	
	#Draw atoms and vacancies
	ax1.scatter(mask[:, 0], mask[:, 1], mask[:, 2], zdir='z', s=50, c=None, depthshade=False,  color='red')
	ax1.scatter(coor[:, 0], coor[:, 1], coor[:, 2], zdir='z', s=60, c=None, depthshade=False,  color='khaki')    

	#Draw numbers for places 
	for i in range(0, len(mask)):
		label = '%d' % (i)
		#ax1.text(mask[i, 0], mask[i, 1], mask[i, 2], label, zdir='x')
	
	ax1.view_init(25, -75)
	ax1.set_title(title)
	ax1.grid(False)
	ax1.set_xlabel('X ')
	ax1.set_ylabel('Y ')
	ax1.set_zlabel('Z ')
	
	#plt.savefig(title[0:4] +'.png', bbox_inches='tight')
	plt.show()	

	
def main():
	mask = cell([3, 3, 3])
	coor = mask.copy()
	title = 'none'
	#coor, title = vac_mono(coor)
	#coor, title = vac_di(coor, 3)
	#coor, title = vac_tri(coor, 8)
	coor, title = vac_tetra(coor, 4)
	plotter(mask, coor, title)
	for i in coor:
		print(*i)
	print('')
	print(len(coor))
if __name__ == '__main__':
	main()



