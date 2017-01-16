# nombre de selection de chaque type
# nombre de hotkey1
# vitesse de jeu

import csv


arrayOfData  = []
with open('../../datayasp/train.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		arrayOfData.append(row)
	print arrayOfData[2]
