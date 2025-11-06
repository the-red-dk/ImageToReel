import os 
import subprocess
import shutil 


cwd = os.getcwd()
out_folder = os.path.join(cwd, "outs")

def nextFolder():
    counter = 1
    while True:
        newfolder = os.path.join(out_folder, f"outs{counter}")
        if not os.path.exists(newfolder):
            return newfolder
        counter += 1

def Rename():
    
    startRange = 1
    counter = 1
    endRange = len(os.listdir(cwd))

    existing = []
    for i in range(startRange, endRange + 1):
        existing.append(f"{i}.jpg")

    # for i, files in enumerate(os.listdir(cwd)):

    for files in os.listdir(cwd):
        if files.endswith(".jpg"):
            
            if files in existing: 
                
                continue
            
            while f"{counter}.jpg" in os.listdir(cwd):
                counter += 1

            print("Existing files skipped.")
            
            newname = f"{counter}.jpg"        
            print("Renaming...")
            os.rename(files, newname)
            counter += 1

        else:
            print(f"{os.path.splitext(files)[1]} not supported, skipping...")
        
        
        
    print("Success")


def imgtovid(imginput, output):
    command = f"ffmpeg -loop 1 -i {imginput} -c:v libx264 -t 3 -n {output}"
    subprocess.run(command, shell=True)
  
  
def convert():
    for files in os.listdir(cwd):   
       if files.endswith(".jpg"):

            imginput = os.path.join(cwd, files)
            output = os.path.join(cwd, files.replace(".jpg", ".mp4"))
            
            imgtovid(imginput, output)
            
            
def out():
    
#     newfolder = nextFolder()
#     os.makedirs(newfolder)
    
    for i in range(1, len(os.listdir(cwd)) + 1):
        if not os.path.exists(os.path.join(cwd, out_folder)):
            os.makedirs(out_folder)        
        
        
    for files in os.listdir(cwd):
        if files.endswith(".jpg") or files.endswith(".mp4"):
            # shutil.move(files, out_folder)
            shutil.move(os.path.join(cwd, files), os.path.join(out_folder + f"{i}", files))
    print("Success, find your files in the outs folder!")
    
       
            
# def out():

#     newfolder = nextFolder()
#     os.makedirs(newfolder)
        
#     for files in os.listdir(cwd):
#         if files.endswith(".jpg") or files.endswith(".mp4"):
#             dest = os.path.join(out_folder, files)
#             if os.path.exists(dest):
#                 base, exten = os.path.splitext(files)
#                 count = 1
#                 newname = f"outs{count}"
#                 newdest = os.path.join(out_folder, newname)
#                 while os.path.exists(newdest):
#                     count += 1
#                     newname = f"outs{count}"
#                     newdest = os.path.join(out_folder, newname)
#                 dest = newdest
                
#             shutil.move(os.path.join(cwd, files), dest)
#     print("Success, find your files in the outs folder!")

#might be useful later, if the code doesnt run, then close all the images, and videos that are open
    
    
def main():
    Rename()
    convert()
    # imgtovid(imginput, output)
    out()    
    
    
if __name__ == "__main__":
    main()
    