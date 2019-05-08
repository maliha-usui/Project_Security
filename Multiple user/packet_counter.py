 # checking destination ip adrreses of packets  


def main():

	
	
	fp = open('IP_d_addr.txt', 'r').read()
	fp2 = open('UDP.txt', 'r').read()
	#fp3 = open('ICMP.txt', 'r').read()

	# counting ip addresses of gmail server
	gmail_1 = "172.217.194.17"
	a = fp.count(gmail_1)
	gmail_2 = "172.217.194.18"
	b = fp.count(gmail_2)
	gmail_3 = "172.217.194.19"
	c = fp.count(gmail_3)
	gmail_4 = "172.217.194.83"
	d = fp.count(gmail_4)
	gmail_5 = "74.125.24.17"
	e = fp.count(gmail_5)
	gmail_6 = "74.125.24.18"
	f = fp.count(gmail_6)
	gmail_7 = "74.125.24.19"
	g = fp.count(gmail_7)
	gmail_8 = "74.125.200.83"
	h = fp.count(gmail_8)
	gmail_9 = "74.125.200.17"
	i = fp.count(gmail_9)
	gmail_10 = "74.125.200.18"
	j = fp.count(gmail_10)
	gmail_11 = "74.125.200.19"
	k = fp.count(gmail_11)
	gmail_12 = "216.58.203.229"
	l = fp.count(gmail_12)
	
	c1=a+b+c+d+e+f+g+h+i+j+k+l

	# counting ip addresses of yahoo server
	yahoo ="106.10.250.11"
	c2 = fp.count(yahoo)

	# counting ip addresses of youtube server
	youtube = "74.125.24.136"
	c3 = fp.count(youtube)

	# counting ip addresses of facebook server
	facebook = "157.240.23.35"
	c4 = fp.count(facebook)

	#counting ip address of Prothom alo
	prothomalo = "43.245.194.146"
	c5 = fp2.count(prothomalo)

	dailystar = "107.154.81.121"
	c6 = fp2.count(dailystar)


	print ('gmail : ')
	print (c1)
	print ('yahoo : ')
	print (c2)
	print ('youtube : ')
	print (c3)
	print ('facebook : ')
	print (c4)
	print ('prothomalo : ')
	print (c5)
	print ('dailystar : ')
	print (c6)
	
	

	import matplotlib.pyplot as plt
	import numpy as np
	import pandas as pd

	plt.plot([c1,c2,c3,c4,c5,c6])
	print c1,c2,c3,c4,c5,c6
	plt.title("Uses of 2 user")
	plt.xlabel("considered sites")
	plt.ylabel("uses for each sites")
	
	#annotate
	plt.annotate(xy=[0,0], s='gmail')
	plt.annotate(xy=[.5,.5], s='yahoo')
	plt.annotate(xy=[1.5,1.5], s='youtube')
	plt.annotate(xy=[2.5,2.5], s='facebook')
	plt.annotate(xy=[3.5,3.5], s='prothomalo')
	plt.annotate(xy=[4.5,4.5], s='dailystar')


	plt.show()


	f = open('destination_addr.txt', 'r').read()

	# counting ip addresses of gmail server
	gmail_1 = "172.217.194.17"
	a = f.count(gmail_1)
	gmail_2 = "172.217.194.18"
	b = f.count(gmail_2)
	gmail_3 = "172.217.194.19"
	c = f.count(gmail_3)
	gmail_4 = "172.217.194.83"
	d = f.count(gmail_4)
	gmail_5 = "74.125.24.17"
	e = f.count(gmail_5)
	gmail_6 = "74.125.24.18"
	f = f.count(gmail_6)
	gmail_7 = "74.125.24.19"
	g = f.count(gmail_7)
	gmail_8 = "74.125.200.83"
	h = f.count(gmail_8)
	gmail_9 = "74.125.200.17"
	i = f.count(gmail_9)
	gmail_10 = "74.125.200.18"
	j = f.count(gmail_10)
	gmail_11 = "74.125.200.19"
	k = f.count(gmail_11)
	gmail_12 = "216.58.203.229"
	l = f.count(gmail_12)
	gmail_13 = "172.217.194.94		64"
	m = f.count(gmail_13)
	
	c1=a+b+c+d+e+f+g+h+i+j+k+l

	# counting ip addresses of yahoo server
	yahoo ="106.10.250.11"
	c2 = fp.count(yahoo)

	# counting ip addresses of youtube server
	youtube = "74.125.24.136"
	c3 = fp.count(youtube)

	# counting ip addresses of facebook server
	facebook = "157.240.23.35"
	c4 = fp.count(facebook)

	#counting ip address of Prothom alo
	prothomalo = "43.245.194.146"
	c5 = fp2.count(prothomalo)

	dailystar = "107.154.81.121"
	c6 = fp2.count(dailystar)


	print ('gmail : ')
	print (c1)
	print ('yahoo : ')
	print (c2)
	print ('youtube : ')
	print (c3)
	print ('facebook : ')
	print (c4)
	print ('prothomalo : ')
	print (c5)
	print ('dailystar : ')
	print (c6)
	

	import matplotlib.pyplot as plt
	import numpy as np
	import pandas as pd

	plt.plot([c1,c2,c3,c4,c5,c6])
	print c1,c2,c3,c4,c5,c6
	plt.title("Uses of 2 user")
	plt.xlabel("considered sites")
	plt.ylabel("uses for each sites")
	
	#annotate
	plt.annotate(xy=[0,0], s='gmail')
	plt.annotate(xy=[.5,.5], s='yahoo')
	plt.annotate(xy=[1.5,1.5], s='youtube')
	plt.annotate(xy=[2.5,2.5], s='facebook')
	plt.annotate(xy=[3.5,3.5], s='prothomalo')
	plt.annotate(xy=[4.5,4.5], s='dailystar')

	plt.show()


main()


