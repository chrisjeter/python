fromaddr = "cjeter@gmail.com"
toaddr = "cjeter@gmail.com"
ccaddr = "7956919005@txt.att.net"
toaddrs = fromaddr + ccaddr


def door(state):
	if(state == "isopen"):
		print "Open"
	else:
		print "CloseD"
door("bob")

#def find_max(a,b):
#   if(a>b):
#      print "a is greater than b"
#   else:
#      print "b is greater than a"
#find_max(30,40)
