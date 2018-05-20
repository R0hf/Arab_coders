import os
def rename_file() :
	list_file = os.listdir(r"C:\Users\Raouf\Desktop\Udacity\prank") ; # get all files in the folder
	my_path = os.getcwd(); # get the chemin
	os.chdir(r"C:\Users\Raouf\Desktop\Udacity\prank"); # change chemin
	for name_file in list_file :
		os.rename(name_file,name_file.translate(None,"0123456789")); # 
	os.chdir(my_path);
	print list_file ;
rename_file();	