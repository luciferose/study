from ftplib import  FTP
import time
ip_list=['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5', '10.0.0.6', '10.0.0.7', '10.0.0.8', '10.0.0.9', '10.0.0.10', '172.31.0.1', '10.0.0.254']
for ip in ip_list:
    ftp = FTP()
    timout = 600
    port = 21
    ftp.connect(ip, port, timout)
    ftp.login('admin', 'se12pa##1')
    print(ip)
    print(ftp.welcome)
    bufsize = 1024
    filename = time.strftime("%Y %a %b %d %H:%M:%S", time.localtime())+'_'+ip+'_'+'vrpcfg.zip'
    file_headle = open(filename,'wb').write
    ftp.retrbinary('RETR vrpcfg.zip',file_headle, bufsize)
