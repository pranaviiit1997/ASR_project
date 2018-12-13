import os
thisdir = os.getcwd()
fp = open("testfinal", "a+")
for r, d, f in os.walk(thisdir):
	for file in f:
		if ".WAV" in file:
			k = os.path.join(r,file)
			fp.write("%s \n" % k)