import unidecode
import sys

iFile = sys.argv[1]
oFile = sys.argv[2]
converAll = sys.argv[3]
print (iFile)
print (oFile)
print (converAll)
#input file
fin = open(iFile, "rt")
#output file to write the result to
fout = open(oFile, "wt")
#for each line in the input file
x=0
for line in fin:
	#read replace the string and write to output file
	#fout.write(line.replace('pyton', 'python'))
	#print(line)
	if converAll == "All":
		fout.write( unidecode.unidecode(line))
	else:
		x+=1
		if x ==1:
			fout.write( unidecode.unidecode(line))
		else:
			fout.write( line)
#close input and output files
			
fin.close()
fout.close()