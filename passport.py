password = "bc0227"
p = 3
while p > 0:
	p = p - 1
	password = input('請輸入密碼: ')
	if password == "bc0227":
		print('登入成功!')
		break
	else:
		print('密碼錯誤!') 
		if p > 0:
			print('還剩', p, '次機會')
		else:
			print('你沒機會了')