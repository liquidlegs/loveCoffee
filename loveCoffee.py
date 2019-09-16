import random, string, subprocess, time, requests, getpass

#ctypes.cdll.LoadLibrary("advapi32.dll")

#===========================================================#
# the urls for images to be downloaded from. Later on these may or may not be hard coded
urls = '''
https://cdn.pixabay.com/photo/2017/05/12/08/29/coffee-2306471_960_720.jpg
https://cdn.pixabay.com/photo/2016/03/26/13/09/cup-of-coffee-1280537_960_720.jpg
https://cdn.pixabay.com/photo/2013/08/11/19/46/coffee-171653_960_720.jpg
https://cdn.pixabay.com/photo/2015/10/12/14/54/coffee-983955_960_720.jpg
https://cdn.pixabay.com/photo/2016/03/30/21/59/coffee-1291656_960_720.jpg
https://cdn.pixabay.com/photo/2018/02/16/10/52/beverage-3157395_960_720.jpg
https://cdn.pixabay.com/photo/2013/11/05/23/55/coffee-206142_960_720.jpg
https://cdn.pixabay.com/photo/2017/04/25/08/02/coffee-beans-2258839_960_720.jpg
https://cdn.pixabay.com/photo/2017/06/02/11/49/still-life-2366084_960_720.jpg
https://cdn.pixabay.com/photo/2015/07/12/14/26/coffee-842020_960_720.jpg
https://cdn.pixabay.com/photo/2017/08/07/22/57/coffee-2608864_960_720.jpg
https://cdn.pixabay.com/photo/2016/01/02/04/59/coffee-1117933_960_720.jpg
https://cdn.pixabay.com/photo/2014/12/11/02/56/coffee-563797_960_720.jpg
'''.split()

#===========================================================#
# used for generating random character names for downloaded images
def genImageName(stringArray=[], imgExtension=".jpg", loops=1, chars=15):
	
	st = string
	randomString = ""
	randomString += st.ascii_lowercase + st.ascii_uppercase + st.digits
	
	for loops in range(loops):
		genString = "".join(random.choice(randomString) for index in range(chars))
		stringArray.append(genString + imgExtension)
	
	return stringArray	

	
#===========================================================#
# gets the name of the current user

currentUser = getpass.getuser()
#===========================================================#
# creates a folder in appdata and sets up the string ready to be used for setting for path
# for files to download to.
folderName = '"%AppData%\\testFolder\"'
downloadPath = f'C:\\Users\\{currentUser}\\AppData\\Roaming\\testFolder\\'
subprocess.run(f'md {folderName}', shell=True)
time.sleep(2)
print(folderName)

# names holds the randomly generated names that will be assigned to each image
names = []
genImageName(names, ".jpeg", len(urls), 15)

# each of the stored image paths will concatenated with the image names,
# and be created in the specfied directory.
storeImagePaths = []
for index in range(len(urls)):
	response = requests.get(urls[index])
	with open(downloadPath + names[index], "wb") as f:
		f.write(response.content)
		storeImagePaths.append(downloadPath + names[index])
		print(str(index) + " " + downloadPath + names[index])
		time.sleep(2)


#===========================================================#
# will loop forever and open pictures randomly from 30 to 300 seconds
while True:
	genValue = random.randint(0, len(storeImagePaths) -1) 
	genTime = random.randint(30, 300)
	time.sleep(genTime)
	subprocess.run("explorer " + storeImagePaths[genValue], shell=True)
	
