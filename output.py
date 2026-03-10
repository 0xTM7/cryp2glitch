import base64 as b64,zlib as zl,hashlib as hs,random as rn,sys as sy
hcwqwtkgnuyf=1092503560;yzbtuxygfj=3079356385;xapbevqqfhqza=3753338909;oqubpbawgocspr=3020866394;obfnsggema=3243037892;bgxobpypybhkp=1992688994;mizuwkrhmyj=2946730946
def derivekey(sd):
    k=hs.sha3_512(sd).digest()
    for i in range(1337):k=hs.sha3_512(k+sd).digest()
    return k
def xorstream(d,k):
    o=bytearray(len(d));kl=len(k)
    for i,b in enumerate(d):o[i]=b^k[i%kl]^((i*0x5A^0xA5)&0xFF)
    return bytes(o)
def unshuffle(d,k):
    sd=int.from_bytes(hs.md5(k).digest(),'big');rng=rn.Random(sd)
    ix=list(range(len(d)));rng.shuffle(ix);o=bytearray(len(d))
    for nw,ol in enumerate(ix):o[ol]=d[nw]
    return bytes(o)
def deobfstr(s):
    us=''.join(chr(ord(c)-3)if c.isalpha()else c for c in s)
    return b64.b85decode(us.encode()).decode()
def run():
    salt='4Ma4xLRFQUBJYEa756PIp64nD4oX7CXpyIcfnOsWP6U=';chk='CLdF0eAbT9noJm/yOsd+XbCYUzIw0ptZwIkWPD/hS74=';obk='DZ&j*e9]o\\ZE';chunks=['YhdC3uGv9pF91OXPdSkRRztYuwUf8N/apLNxUbhL']
    pw=input(deobfstr(obk)+': ').encode()
    key=derivekey(b64.b64decode(salt)+pw)
    raw=b''.join(b64.b64decode(c)for c in chunks)
    raw=unshuffle(raw,key)
    raw=xorstream(raw,key)
    try:
        raw=zl.decompress(raw)
    except Exception:
        print('\033[31m[!] Wrong password or corrupted file.\033[0m');sy.exit(1)
    if hs.sha3_256(raw).digest()!=b64.b64decode(chk):
        print('\033[31m[!] Integrity check failed.\033[0m');sy.exit(1)
    exec(compile(raw,'<protected>','exec'),{'__name__':'__main__'})
run()
