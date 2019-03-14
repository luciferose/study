import hashlib
import base64


def handle_md5(hd_object):
    return hashlib.md5(hd_object.encode('utf-8')).hexdigest()


def handle_base64(hd_object):
    return str(base64.b64decode(hd_object))[2:-1]


def parse(ig_hs, ct):
    count = 4
    contains = handle_md5(ct)
    ig_hs_copy = ig_hs
    p = handle_md5(contains[0:16])
    m = ig_hs[0:count]
    c = p + handle_md5(p + m)
    n = ig_hs[count:]
    l = handle_base64(n)
    k = []
    for h in range(256):
        k.append(h)
    b = []
    for h in range(256):
        b.append(ord(c[h % len(c)]))
    g = 0
    for h in range(256):
        g = (g + k[h] + b[h]) % 256
        tmp = k[h]
        k[h] = k[g]
        k[g] = tmp
    u = ''
    q = 0
    z = 0
    for h in range(len(l)):
        q = (q + 1) % 256
        z = (z + k[q]) % 256
        tmp = k[q]
        k[q] = k[z]
        k[z] = tmp
        u += chr(ord(l[h]) ^ (k[(k[q] + k[g]) % 256]))
    u = u[26:]
    u = handle_base64(ig_hs_copy)
    return u

if __name__=='__main__':
    img_hash='Ly93dzMuc2luYWltZy5jbi9tdzYwMC8wMDczdExQR2d5MWZ6cG44MTJnZTZqMzB4YzBpcmp2Ni5qcGc='
    content='CJnxgemql-ACFctiYAod3sUFyQ'
    print(parse(img_hash,content))