import os

def rename_file(file_path):
	os.chdir(file_path)
	i= 0
	for file in os.listdir():
		i+=1
		filename, fileext = os.path.splitext(file)
		fileext = fileext.lower()
		if fileext == ".jpg": 
			fileext = ".png"
		elif fileext == ".jpeg":
			fileext = ".png"
			
		else:
			continue
			
		newname = '{}{}'.format(filename,fileext)

		os.rename(file , newname)
		print(i,"Done")



file_path = input(r'enter the path : ')
rename_file(file_path)

