import os 

cwd = os.getcwd()
  
startRange = 1
counter = 1
endRange = len(os.listdir(cwd))

existing = []
for i in range(startRange, endRange + 1):
    existing.append(f"{i}.jpg")

# for i, files in enumerate(os.listdir(cwd)):

for files in (os.listdir(cwd)):
    if files.endswith(".jpg"):
        
        if files in existing: 
            continue
        # print("Existing files skipped.")
        
        while f"{counter}" in os.listdir(cwd):
            counter += 1

        print("Existing files skipped.")
          
        newname = f"{counter}.jpg"        
        print("Renaming...")
        os.rename(files, newname)
        counter += 1

    else:
        print(f"{os.path.splitext(files)[1]} not supported, skipping...")
    
    
    
print("Success")

