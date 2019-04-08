from ftplib import  FTP
import time
ip_list=['172.31.254.2','192.168.100.2','172.28.0.130']

for ip in ip_list:
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    ftp = FTP()
    timout=600
    port=21
    ftp.connect(ip,port,timout)
    ftp.login('admin','Lucifer-0987')
    print(ftp.welcome)
    bufsize=1024
    filename=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())+'_'+ip+'_'+'vrpcfg.zip'
    file_headle=open('/root/switch_bak/'+filename,'wb').write
    ftp.retrbinary('RETR vrpcfg.zip',file_headle,bufsize)
    ftp.close()
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))