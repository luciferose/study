from ftplib import  FTP
import time
ip_list=['192.168.111.1']
for ip in ip_list:
    ftp = FTP()
    timout = 600
    port = 21
    ftp.connect(ip, port, timout)
    ftp.login('bxsadmin', 'se12pa##1')
    print(ftp.welcome)
    bufsize = 1024
    filename = time.strftime("%Y %a %b %d %H:%M:%S", time.localtime())+'_'+ip+'_'+'vrpcfg.zip'
    file_headle = open(filename,'wb').write
    ftp.retrbinary('RETR vrpcfg.zip',file_headle, bufsize)