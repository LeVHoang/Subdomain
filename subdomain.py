
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

def read_file():
    filename = open('subname.txt', 'r')
    nlist = filename.read().split('\n')
    filename.close
    return nlist

def sublist(domain):
    nlist = read_file()
    for x in range(0, len(nlist)-1):
        subdomain = nlist[x] + '.' +  str(domain)
        try:
            ip = socket.gethostbyname(subdomain)
            print'IP: %s\tDomain: %s'%(ip, subdomain)
        except:
            pass

def main():
    domain = raw_input('Domain: ')
    sublist(domain)

main()