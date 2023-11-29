import random, subprocess, re


charList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

newMac = ""
for i in range(12):
    newMac += random.choice(charList)
# print(newMac)

ifconfigResult = subprocess.check_output("ifconfig en0", shell=True).decode() 
# print(ifconfigResult)

oldMac = re.search("ether (.+) ",ifconfigResult).group().split(" ")[1]
# print(oldMac)
# oldMac = re.search("ether(.*?)txqueuelen",ifconfigResult).group(1).strip() # target pc "ifconfig eth0"

subprocess.check_output("ifconfig eth0 down", shell=True)
subprocess.check_output("ifconfig eth0 hw ether " + newMac, shell=True)
subprocess.check_output("ifconfig eth0 up", shell=True)

print("Old Mac : ", oldMac)
print("New Mac : ", newMac)