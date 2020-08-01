def sum_of_numbers(num):
	sum=0	
	for x in range(0,int(num)+1):
		sum+=x
	return sum
if __name__=='__main__':
	n=input()
	print(sum_of_numbers(n))
	