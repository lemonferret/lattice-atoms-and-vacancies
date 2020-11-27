'''5 alkuainetta 4x4x4 128 atomia
 kgrid 12 --> 3
 10koppia
 perus-vasp- ei _pos_
 ei cutoff testejä-- 450 ev niinkuin kaikissa alkuaineissakin
 k tsti yhdelle systeemille, --< alustava relakaatio 3x3x3 kgridillä griditesti atomipaikat kiinnitettynä
 --> kaikki laskut 3x3x3 griddissä kuitenkin
 HILAVAKIOT: tilavuus per atomi kullekkin alkuaineelle._--> seoskopin kokonaistilavuus montako kutakin atomia siinä on. kuutiojuuri. 
 --> relaksoi atomien paikat kopin sisälä  positronilasku muut vaiheet. 
 '''
import random as ran #Mersenne Twister 
import math as math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from itertools import product, combinations


def add_items(num):
	mix=['W', 'Ta', 'Nb', 'V', 'Mo']*math.ceil(num/5)
	return mix

def remove_items(num, mix):
	rm=[]
	i=0
	while i < math.ceil(num/5)*5-num:
		n = ran.randint(0, 128)
		if mix[n] not in rm:
			rm.append(mix[n])
			mix.pop(n)
			i+=1
	return mix 
		
def cell(n):
	init1 = np.array([0, 0, 0]) # x, y, z
	init2 = np.array([0.5, 0.5, 0.5])
	
	coor = np.empty([0, 3])
	for k in range(0, n[0]):#x
		for j in range(0, n[1]):#y 
			for i in range(0, n[2]):#z
				coor = np.vstack((coor, [init1[0]+k, init1[1]+j, init1[2]+i]))
				coor = np.vstack((coor, [init2[0]+k, init2[1]+j, init2[2]+i]))
	return coor
	
def plotter(coor, mix, seed):
	fig = plt.figure()
	ax1 = fig.add_subplot(111, projection='3d')
	
	#Draw one cell
	#r = [1, 2]
	#for s, e in combinations(np.array(list(product(r, r, r))), 2):
	#	if np.sum(np.abs(s-e)) == r[1]-r[0]:
	#		ax1.plot3D(*zip(s, e), color="blue")
	
	#Draw atoms and vacancies
	#ax1.scatter(mask[:, 0], mask[:, 1], mask[:, 2],  zdir='z', alpha=1, s=50, c='red')
	for n, i in enumerate(mix):
		if mix[n] == 'W': c='blue'
		if mix[n] == 'Ta': c='green'
		if mix[n] == 'Nb': c='orange'
		if mix[n] == 'V': c='red'
		if mix[n] == 'Mo': c='black'
		ax1.scatter(coor[n, 0], coor[n, 1], coor[n, 2],  zdir='z', alpha=1, s=20, c=c)


	#Draw numbers for places 
	#for i in range(0, len(mask)):
	#	label = '%d' % (i)
	#	ax1.text(mask[i, 0], mask[i, 1], mask[i, 2], label, zdir='x')
	
	#ax1.view_init(25, -75)
	ax1.set_title('HEA, config: ' + seed)
	ax1.grid(False)
	ax1.set_xlabel('X ')
	ax1.set_ylabel('Y ')
	ax1.set_zlabel('Z ')
	
	plt.savefig('HEA, config: ' + str(seed) + '.png', bbox_inches='tight')
	#plt.show()
	
def calc_a(num, mix):
	aW= 3.172
	aTa= 3.247
	aNb= 3.264
	aV= 2.912
	aMo=3.107
	vcell = mix.count('W')*aW**3+mix.count('Ta')*aTa**3 + mix.count('Nb')*aNb**3 +mix.count('V')*aV**3+mix.count('Mo')*aMo**3
	
	return (vcell/num)**(1/3)
	
def main():
	seed=10
	ran.seed(seed)
	num = 128
	
	mix=add_items(num)
	ran.shuffle(mix)
	mix=remove_items(num, mix)
	
	#for bcc
	coor = cell([4, 4, 4])
	plotter(coor, mix, str(seed))
	for n, i in enumerate(mix):
		if i=='W':
			print(*coor[n])
	for n, i in enumerate(mix):
		if i=='Ta':
			print(*coor[n])
	for n, i in enumerate(mix):
		if i=='Nb':
			print(*coor[n])
	for n, i in enumerate(mix):
		if i=='V':
			print(*coor[n])
	for n, i in enumerate(mix):
		if i=='Mo':
			print(*coor[n])
			
	print('\n' + str(len(coor)))
    
	print('\nW:%d, Ta:%d, Nb:%d, V:%d, Mo:%d' %(mix.count('W'), mix.count('Ta'), mix.count('Nb'), mix.count('V'), mix.count('Mo')))

	a = calc_a(num, mix)
	print(a)


if __name__ == '__main__':
	main()
	
	#01 a= 3.144963659125074
	#02 a= 3.1448213398481957
	#03 a= 3.143704515036081
	#04 a= 3.1443151448775386
	#05 a= 3.1455738002528717
	#06 a= 3.1443151448775386
	#07 a= 3.1443151448775386
	#08 a= 3.147473496153611
	#09 a= 3.146358553689762
	#10 a= 3.146968154099399
	
