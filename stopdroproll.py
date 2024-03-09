from pwn import *
r = remote('83.136.253.78', 53876)

#get the inital greeting screen
for i in range(12):
    print(r.recvline())
r.sendline(b'y')
print(r.recvline())

#main loop
firstround = True
count = 0
while True:
    answer = ""
    command = (r.recvline())
    strcmd = command.decode()
    print(strcmd)
    cmdstrip = strcmd.strip("\n")
    if not firstround:
        cmdstrip = cmdstrip.strip("What do you do?")
    #print(cmdstrip)
    cmd = cmdstrip.split(',')
    #print(cmd)

    # remove the white spaces
    for i in range(len(cmd)):
        cmd[i] = cmd[i].strip(" ")
    
    # answer loop
    for j in range(len(cmd)):
        #print(j)
        #print(cmd[j])
        if cmd[j] == "GORGE":
            answer = answer + "STOP"
        if cmd[j] == "PHREAK":
            answer = answer + "DROP"
        if cmd[j] == "FIRE":
            answer = answer + "ROLL"
        if len(cmd)-1 > (j):
            answer = answer + "-"
    encans = str.encode(answer)
    print(encans)
    r.sendline(encans)
    firstround = False
    count = count +1
    print("Round: " + str(count))
