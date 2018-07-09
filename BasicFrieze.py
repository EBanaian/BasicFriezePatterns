def BasicFrieze(quid, m=50, F = RR[x]): 
	#input: quid is the quiddity row of your frieze, add some cap to number of rows in case you do not want all of them, or to prevent an infinite process, and include what field to consider.
	#In general, if we have a orbifold point of order p, then work over Rp = QuotientRing(QQ[x],x^3 - x^2 -2*x + 1), and include the special value 2cos(pi/p) as x.
	#Will need to adjust if we have multiple lambda values
	if type(quid) != list and type(quid) != tuple:
		raise ValueError, 'please input either a list or a tuple for the quiddity row'
	#initializing the dictionary of rows of the frieze
	d = {}
	d[0] = []
	n = len(quid)
	for i in range(n):
		d[0].insert(i,1)
	d[1] = quid
	j = 2
	#we use the zeroset to check for when we have included a row with one zero (which in our cases should imply a row of all zeroes)
	zeroset = {0}
	testset = {1}
	#we keep making rows while we have yet to find a zero (so working in the case of a quiddity row of positive integers, or with positive integer combinations of roots of unity), and while we have yet to reach the cap
	while len(d) < m and testset.issuperset(zeroset) == false:
		#print 'x'
		d[j] = []
		for i in range(n):
			d[j].insert(i,1)
		for i in range(n):
 			d[j][i] = (F(d[j-1][i-n])*F(d[j-1][i-n+1]) - 1)*(F(d[j-2][i-n+1])**(-1))
			testset.add(d[j][i])
			#print d[j][i]
		j = j+1
	return d
