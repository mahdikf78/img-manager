from PIL import Image
import glob
import os
import send2trash
import random

os.system('color')

#give all images in directory in a LIST
formats = ['PNG','WEBP','JPEG','JFIF','AVIF']
all_imgs = glob.glob(f'*.{formats[0]}')
all_imgs.extend(glob.glob(f'*.{formats[1]}'))
all_imgs.extend(glob.glob(f'*.{formats[2]}'))
all_imgs.extend(glob.glob(f'*.{formats[3]}'))
all_imgs.extend(glob.glob(f'*.{formats[4]}'))

print('')

user = input("\033[34mOnly change to JPG type '1' and for all changes type '2' : \033[0m")

def Change_ToJPG():
    for i in all_imgs :
        img = Image.open(i)
        print(all_imgs.index(i),':', i, '>>>>>')
        if img.format in formats :
            img.convert('RGB').save("img"+str(all_imgs.index(i))+str(random.randrange(5555))+".jpg", quality=100)
            send2trash.send2trash(i)
            print('\033[32m======== Images Changed to JPG ========\033[0m')
            print('')
        else :
            print('\033[33m======== No Needed ========\033[0m')
            print('')
def Change_and_Resize():
    new_size = (412,412)
    if len(all_imgs) == 0 :
        print('')
        print('\033[31m<<<<<<< No Pic >>>>>>>>\033[0m')
        print('')
        print('')
    else :
        for i in all_imgs :
            img = Image.open(i)
            #Get images sizes
            w, h = img.size
            print(all_imgs.index(i),':', i, '>>>>>')
            print('Size is :',w,h)
            #Check if bigger than 412 * 412
            if w > 412 or h > 412 :
                img.resize(new_size).convert('RGB').save("img"+str(all_imgs.index(i))+str(random.randrange(5555))+".jpg", quality=100)
                send2trash.send2trash(i)
                print('\033[32m======== Image Resized to 412 * 412 and Changed to JPG ========\033[0m')
                print('')
            else :
                print('\033[33m======== No Needed ========\033[0m')
                print('')
def Get_List():
    print('')
    for i in all_imgs :
        print(all_imgs.index(i),':', i, '>>>>>')
    print('')

if int(user) == 1:
    Change_ToJPG()
elif int(user) == 2 :
    Change_and_Resize()
elif int(user) == 3 :
    Get_List()