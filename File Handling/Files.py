fileOperation1 = open('File Handling/Mod.txt', 'w')
print(fileOperation1.write("The real name of Reodesu is Ronald\n"))
fileOperation1.close()

fileOperation2 = open('File Handling/Mod.txt', 'a')
print(fileOperation2.write("Ronald is a web and game developer\n"))
fileOperation2.close()

fileOperation3 = open('File Handling/Mod.txt', 'r')
print(fileOperation3.read())
fileOperation3.close()
