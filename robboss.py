import urllib.request #downloading images
import os #used to delete files

from shutil import copyfile #copy files

names = []

def downloader(image_url): #used to download an image to loc
    file_name = 0
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)
    names.append("0.jpg") #initial image name

def create(): #downloads initial image, then copies it
    count = 1

    downloader("https://avatars2.githubusercontent.com/u/16223529?s=460&v=4") #image link

    amount = int(input("How many copies: ")) #copy amount

    for x in range(0,amount): #duplicates image x times
        name = str(count) + '.jpg'
        names.append(name)
        copyfile("0.jpg", name)
        count += 1

    writeremove = input("Create remove file? (y/n): ") #creates file that users can use 'removefromfile' function to remove after closing program
    writeremove = writeremove.lower()
    if(writeremove == "y"):
        with open("names.txt", "w") as file:
            for x in range(0,len(names)):
                file.write(names[x])
                file.write("\n")

def remove(): #to be used if you have not closed the program
    for x in range(-1,len(names)):
        try:
            os.remove(names[x])
        except:
            print("Couldn't remove", names[x])

def removefromfile(name): #to be used if you closed the program
    with open(name+".txt", "r") as file:
        for line in file:
            a = line.replace("\n", "")
            try:
                os.remove(a)
            except:
                print("Couldn't remove", a)
    deletefile = input("Delete txt file? (y/n): ")
    deletefile = deletefile.lower()
    if(deletefile == "y"):
        os.remove(name+".txt")
            

