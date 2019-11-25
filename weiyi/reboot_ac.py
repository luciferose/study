import telnetlib
import time

def switch_reboot(host):
    username='bxsadmin'
    password='se12pa##1'
    tn=telnetlib.Telnet(host,port=23,timeout=600)
    tn.read_until(b'Username:')
    tn.write(username.encode('ascii')+b'\n')
    time.sleep(1)
    tn.read_until(b'Password:')
    tn.write(password.encode('ascii')+b'\n')
    time.sleep(1)
    cmd = 'reboot'
    tn.write(cmd.encode('ascii') + b'\n')
    time.sleep(1)
    tn.read_until(b'Warning: System will reboot! Continue ? [y/n]:')
    tn.write(b'y\n')
    time.sleep(5)
    #print(msg.decode('utf-8'))


if __name__=='__main__':
    Host=['192.168.111.1']
    for host in Host:
        print(host+':'+'\n')
        switch_reboot(host)
        print('*'*50)