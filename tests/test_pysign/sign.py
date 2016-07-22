from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256 as SHA
#openssl genrsa -out private.pem 1024
#~ key = RSA.importKey(open("private.pem").read())
#~ message = open("message").read()[:-1] # skip last newline
#~ h = SHA.new(message)
#~ p = PKCS1_v1_5.new(key)
#~ signature = p.sign(h)
#~ signature_trim = p.sign(h)[:-1] # will give same output as openssl dgst -sign
#~ import sys
#~ sys.stdout.write( signature)    # remove print when not using hexdump
print dir(RSA)
def sign_rsa(message, private_rsa):
   """Sign a request using RSASSA-PKCS #1 v1.5.

   Per `section 3.4.3`_ of the spec.

   .. _`section 3.4.3`: http://tools.ietf.org/html/rfc5849#section-3.4.3

   """

   key = RSA.importKey(private_rsa)
   #~ message = prepare_base_string(method, url, params)
   h = SHA.new(message)
   p = PKCS1_v1_5.new(key)
   return p.sign(h)
#~ The RSA-SHA1 Verification

def verify_rsa(message, public_rsa, signature):
   """Verify a RSASSA-PKCS #1 v1.5 base64 encoded signature.

   Per `section 3.4.3`_ of the spec.

   .. _`section 3.4.3`: http://tools.ietf.org/html/rfc5849#section-3.4.3

   """

   key = RSA.importKey(public_rsa)
   #~ message = prepare_base_string(method, url, params)
   h = SHA.new(message)
   p = PKCS1_v1_5.new(key)
   #~ signature = binascii.a2b_base64(urllib.unquote(signature))
   return p.verify(h, signature)
message="Test Hello World"

def read_keys(priv=None,pub=None):
    if priv==None and pub==None:
        key=RSA.generate(2048)
        assert key.has_private()
        return key,key.publickey()
    priv_key=None
    pub_key=None
    if priv!=None :
        priv_key=RSA.importKey(priv)
        assert priv_key.has_private(),"priv_key wrong " + str(priv_key.has_private())
    if pub != None:
        pub_key=RSA.importKey(pub)
    if priv_key is not None and pub_key is None:
        return priv_key,priv_key.publickey()
    assert pub_key.has_private() is False

    return priv_key,pub_key
#unit test for read_keys
# read from files
with open("private.pem","r") as priv, open("public.pem","r") as pub:
    pr,pu=priv.read(),pub.read()
    priv_key,pub_key=read_keys(pr,pu)
    print priv_key,pub_key    # expect it is not None
    print   read_keys(priv=None,pub=pu)
    print   read_keys(priv=pr,pub=None)
    print   read_keys(priv=None,pub=pu)
    print   read_keys()
# try fail cases
try:

    print read_keys(priv="private.pem",pub="public.pem")
    assert False
except ValueError as e:
    print str(e)
try:
    print read_keys(priv=pu)
    assert False
except AssertionError as e:
    if e.message.startswith("priv_key"):
        print "PASS"
    else:
        raise
with open("private.pem","r") as f:
    priv_key=f.read()
with open("b","r") as f:
    pub_key=f.read()
sign=sign_rsa(message,priv_key)
v=verify_rsa(message,pub_key,sign)
print v
def generateKey():
    key=RSA.generate(2048)
    return key.exportKey("OpenSSH")

print generateKey()

