import telnetlib
import time

def switch_reboot(host):
    username='admin'
    password='se12pa##1'
    tn=telnetlib.Telnet(host,port=23,timeout=600)
    tn.read_until(b'Username:')
    tn.write(username.encode('ascii')+b'\n')
    time.sleep(0.5)
    tn.read_until(b'Password:')
    tn.write(password.encode('ascii')+b'\n')
    time.sleep(0.5)
    cmd = 'save'
    tn.write(cmd.encode('ascii') + b'\n')
    time.sleep(1)
    tn.read_until(b'The current configuration will be written to the device. Are you sure? [Y/N]:')
    tn.write(b'y\n')
    time.sleep(5)
    tn.read_until(b'(To leave the existing filename unchanged, press the enter key)')
    tn.write(b'\n')
    time.sleep(5)
    tn.read_until(b'flash:/startup.cfg exists, overwrite? [Y/N]:')
    tn.write(b'y\n')
    time.sleep(5)
    msg = tn.read_very_eager()
    print(msg.decode('utf-8'))


if __name__ == '__main__':
    Host = ['172.31.4.2', '192.168.16.6']
    for host in Host:
        print(host + ':' + '\n')
        switch_reboot(host)
        print('*' * 50)