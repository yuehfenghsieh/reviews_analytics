data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000000 == 0:
			print(len(data))
print('總計有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)
print('平均', sum_len/len(data), '筆資料')

#print(len(data))
#print(data[0])
#print('-------')
#print(data[3])