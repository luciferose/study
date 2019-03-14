from ftplib import  FTP
import time
ip_list=['192.168.16.6','172.31.4.2']
for ip in ip_list:
    ftp = FTP()
    timout=600
    port=21
    ftp.connect(ip,port,timout)
    ftp.login('admin','se12pa##1')
    print(ftp.welcome)
    bufsize=1024
    filename=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())+'_'+ip+'_'+'startup.cfg'
    file_headle=open(filename,'wb').write
    ftp.retrbinary('RETR startup.cfg',file_headle,bufsize)
    filename1 = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + '_' + ip + '_' + 'system.xml'
    file_headle = open(filename1, 'wb').write
    ftp.retrbinary('RETR system.xml', file_headle, bufsize)
    ftp.close()
