from ecdsa import SigningKey,VerifyingKey,BadSignatureError
#Curve details-
#NIST192p: siglen= 48, keygen=0.160s, sign=0.058s, verify=0.116s;
def generate_keys():
    priv_key = SigningKey.generate()
    pub_key = priv_key.get_verifying_key()
    open("priv_key.pem",'w').write(priv_key.to_pem())
    open("pub_key.pem",'w').write(pub_key.to_pem())

def generate_sign():
    priv_key = SigningKey.from_pem(open("priv_key.pem").read())
    message = open("message_file","rb").read()
    sign = priv_key.sign(message);
    open("signature","wb").write(sign);
    
def verify_sig():
	vk = VerifyingKey.from_pem(open("pub_key.pem").read())
	message = open("message_file","rb").read()
	sig = open("signature","rb").read()
	try:
		vk.verify(sig, message)
		print "GOOD SIGNATURE"
	except BadSignatureError:
		print "BAD SIGNATURE"
generate_keys();
generate_sign();
verify_sig();

