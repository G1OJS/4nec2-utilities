# This script loops through all .nec files under the path below (including those in subfolders)
# and creates a .nec.new file containing the contents of the nec file
# if a line starts with GN, it is ignored and replaced by the string specified in "newground" below
#
# TO RUN:
# Make sure Python is installed
# Edit path and newground as appropriate
# Optionally remove the comments in the last two lines to cause the script to additionally a) rename the each nec file to .nec.old and b) rename the .nec.new file to .nec
# Open a command window, change directory to wherever you've saved this script, and type Python "Harmonise Grounds.py"
#
# USE AT YOUR OWN RISK & BACK UP important files FIRST

path=r"C:\Users\drala\OneDrive\Desktop\NEC\HF Antennas"

newground="GN 2 0 0 0 11 0.01"

for root, d_names,f_names in os.walk(path):

		for f in f_names:
			if(f.endswith(".nec")):       
				fi = open(os.path.join(root,f), "r")
				fo = open(os.path.join(root,f) + ".new", "w")
				for line in fi:
					print(line[0:2])
					if(line[0:2]=="GN"):
						fo.write(newground + "\n")
					else:
						fo.write(line)
				fo.close()
				fi.close()
#				os.rename(os.path.join(root,f), os.path.join(root,f) + ".old")
#				os.rename(os.path.join(root,f) + ".new", os.path.join(root,f))
		
