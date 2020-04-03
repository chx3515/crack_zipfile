# 生成从000000到999999的密码表
with open('passdict.txt', 'w') as f:
    for id in range(1000000):
        password = str(id).zfill(6) + '\n'
        f.write(password)
