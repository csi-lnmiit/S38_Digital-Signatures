from ecdsa import SigningKey,VerifyingKey,BadSignatureError, NIST192p
import ecdsa
import sys
#Curve details-
#NIST192p: siglen= 48, keygen=0.160s, sign=0.058s, verify=0.116s;
def generate_keys():
    priv_key = SigningKey.generate(curve=NIST192p)
    pub_key = priv_key.get_verifying_key()
    open("priv_key.pem",'w').write(priv_key.to_pem())
    open("pub_key.pem",'w').write(pub_key.to_pem())
    #print type(priv_key)
    #print type(pub_key)
    print sys.getsizeof(priv_key.to_string())
    print len(priv_key.to_string())
    print sys.getsizeof(SigningKey.from_string(priv_key.to_string(),curve=NIST192p))
    #print sys.getsizeof(pub_key.to_string())
	
def generate_sign():
    priv_key = SigningKey.from_pem(open("priv_key.pem").read())
    print "privkey" + str(sys.getsizeof(priv_key))
    message = open("message_file","rb").read()
    sign = priv_key.sign(message);
    print "sign1" + str(sys.getsizeof(sign))
    print len(sign) 
    open("signature","wb").write(sign);
    print "sign2" + str(sys.getsizeof(sign))
    

generate_keys();
generate_sign();


