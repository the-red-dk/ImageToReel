import subprocess
import os

def imgtovid(imginput, output):
  command = f"ffmpeg -loop 1 -i {imginput} -c:v libx264 -t 3 -y {output}"
  subprocess.run(command, shell=True)
  
cwd = os.getcwd()

for files in os.listdir(cwd):
  if files.endswith(".jpg"):
  
    imginput = os.path.join(cwd, files)
    output = os.path.join(cwd, files.replace(".jpg", ".mp4"))
    
    imgtovid(imginput, output)