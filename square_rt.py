def get_sqrroot(n):
	l,r = 0,n
	while l <= r:
		mid = l + (r-1)//2
		print(mid)
		if mid * mid <= n < (mid+1) * (mid+1):
			return mid
		elif n < mid * mid:
			r = mid -1
		else:
			l = mid + 1
	return mid


#print(get_sqrroot(4))
print(get_sqrroot(15))