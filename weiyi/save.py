import telnetlib
import time

def switch_save(host):
    username='admin'
    password='se12pa##1'
    tn=telnetlib.Telnet(host,port=23,timeout=600)
    tn.read_until(b'Username:')
    tn.write(username.encode('ascii')+b'\n')
    time.sleep(1)
    tn.read_until(b'Password:')
    tn.write(password.encode('ascii')+b'\n')
    time.sleep(1)
    cmd = 'save'
    tn.write(cmd.encode('ascii') + b'\n')
    time.sleep(1)
    tn.read_until(b'Are you sure to continue?[Y/N]')
    tn.write(b'y\n')
    time.sleep(10)
    msg=tn.read_very_eager()
    print(msg.decode('utf-8'))


if __name__=='__main__':
    Host=['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5', '10.0.0.6', '10.0.0.7', '10.0.0.8', '10.0.0.9', '10.0.0.10', '172.31.0.1']
    for host in Host:
        print(host+':'+'\n')
        switch_save(host)
        print('*'*50)