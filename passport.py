password = "bc0227"
p = 3
while p > 0:
	password = input('請輸入密碼: ')
	if password == "bc0227":
		print('登入成功!')
		break
	else:
		p = p - 1
		print('密碼錯誤! 還剩', p, '次機會') 