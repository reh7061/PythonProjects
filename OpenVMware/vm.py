import os
import subprocess
import time
import pyautogui

# Pasted
#def process_exists(process_name):
    #call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    #output = subprocess.check_output(call).decode()
    #last_line = output.strip().split('\r\n')[-1]
    #return last_line.lower().startswith(process_name.lower())

# Open vmware.exe using raw text
#os.system(r'"C:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"')

# while (not process_exists("vmware.exe")):
  #  time.sleep()

time.sleep(5)
# pyautogui simulations
pyautogui.hotkey('ctrl', 'b')

time.sleep(10)

pyautogui.click(0,0)