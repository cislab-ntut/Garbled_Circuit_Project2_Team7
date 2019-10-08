# coding=gbk
# Notice: This is the test file , just for reference.
# 設有用戶A、B,A設置壹個門電路,使用後得到真值表,並用密鑰替換真值表得到新的密文真值表,將密文真值表和B輸入的密鑰對應表發送給B
# A發送加密後的訊息x給B,B使用A發送的對應表找到自己訊息的對應密鑰y,使用密文真值表得到唯壹結果z,將z返回給A
# 以下實現僅壹個門電路的傳輸過程
# 现改成多个固定结构的门电路
# 第一层电路有三个，依次是 与1 与2 或1
# 第二层电路有2个，依次是 与3  非1
# 第三层电路有一个，为 与4
# 第一层的 与1 和 与2 连接 接到第二层的 与3 上面，第一层的 或1 接到第二层的 非1 上面
# 第二层的 与3 和 非1 连接 接到第三层的 与4 上
# 此电路 A 有3个输入，B有3个输入，但只有A输入110，B输入110，输出电路唯一为1，其他排列输出均为0
# 对于A的三个输入分别取10的随机得到6个密钥，B同理
# 对越第一层到第二层的3条线路状态10取随机数得到6个输出密钥
# 对于第二层到第三层的2条线路状态10取随机数得到4个输出密钥
# 对于第三层的状态输出随机化得到2个随机密钥
# 8*8=64原真值表共64行，每行7条数据，A3个B3个最终输出1个
# 原真值表全部加密后混淆
# 睡了睡了

import random

total_dict = {}
input_A = input("A 's plaint message:(eg: 100)")
input_B = input("B 's palint message:(eg: 011)")

list_A = list(input_A)
list_B = list(input_B)

dict_A = {}
dict_B = {}

def random_you(input_list,input_dict):
	dir = 0
	for x in input_list:
		y = random.randint(0,1999)
		input_dict[dir] = y
		dir = dir+1
	return input_dict

dict_A = random_you(list_A,dict_A)
dict_B = random_you(list_B,dict_B)

circle_1_and = 
	

def gate_and(x,y):
	if(x=='a0' and y=='b0'):
		z='c0'
	if(x=='a1' and y=='b0'):
		z='c0'
	if(x=='a0' and y=='b1'):
		z='c0'
	if(x=='a1' and y=='b1'):
		z='c1'
	return z

def gate_or(x,y):
	if(x=='0' and y=='b0'):
		z='c0'
	if(x=='a1' and y=='b0'):
		z='c0'
	if(x=='a0' and y=='b1'):
		z='c0'
	if(x=='a1' and y=='b1'):
		z='c1'
	return z

def gate_not(x):
	if(x=='a0' and y=='b0'):
		z='c0'
	if(x=='a1' and y=='b0'):
		z='c0'
	if(x=='a0' and y=='b1'):
		z='c0'
	if(x=='a1' and y=='b1'):
		z='c1'
	return z

tran_A = {"1":"a1","0":"a0"}
tran_B = {"1":"b1","0":"b0"}
tran_C = {"1":"c1","0":"c0"}

list_a = ['a0','a1']
list_b = ['b0','b1']
list_c = ['c0','c1']

plain_A = input("A want to send the plain code is (1/0)：")
cipher_A = tran_A[plain_A]

print("A send the message is "+cipher_A)

plain_B = input("B's plain code is (1/0):")
cipher_B = tran_B[plain_B]

print("B get the cipher is "+cipher_B)

cipher_C = gate_example(cipher_A,cipher_B)

print("B return the cipher is "+cipher_C)
print("A get cipher:"+cipher_C+" and start to tranlate it:")

for x in tran_C:
  if tran_C[x] == cipher_C:
    z = x

print("A get the result from B is:"+z)


# 太困难了，我做不出来
# PS： 晚上千万别喝奶茶，喝完700cc包你睡意全无
# 233333333333333333333333333333333333333333333333



