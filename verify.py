		
from ecdsa import SigningKey,VerifyingKey,BadSignatureError
#Curve details-
#NIST192p: siglen= 48, keygen=0.160s, sign=0.058s, verify=0.116s;
def verify_sig():
	vk = VerifyingKey.from_pem(open("pub_key.pem").read())
	message = open("message_file1","rb").read()
	sig = open("signature","rb").read()
	print sig
	try:
		vk.verify(sig, message)
		print "GOOD SIGNATURE"
	except BadSignatureError:
		print "BAD SIGNATURE"
verify_sig();
