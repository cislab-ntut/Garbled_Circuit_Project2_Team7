# coding=gbk
import random		

A_table = []							#设置A和B的对应密钥列表	
B_table = []

def random_table(table):
	r = range(1,9999)
	for x in range(0,8):
		list_row = random.sample(r,3)
		z = ""
		for y in list_row:
			z = z+str(y)+":"
		table.append(z)
	return table

A_table = random_table(A_table)
B_table = random_table(B_table)


print("-------------------------------------")			#显示A、B随机数密钥表
print("A的随机数密钥:")
print(A_table)
print("-------------------------------------")
print("B的随机数密钥:")
print(B_table)


list_x_y = []							#综合A和B的密钥所有64种结合可能得到真值表的输入部分（列表）

def init(lt,ta,tb):
	z = ""
	for x in ta:
		for y in tb:
			z = x+":"+y
			lt.append(z)
			z = ""
	return lt

list_x_y = init(list_x_y,A_table,B_table)


list_z = []							#制造输出电路64种结果的随机数列表，并打印
r = range(1,9999)
list_z = random.sample(r,64)

print("-------------------------------------")			
print("已经制造出OUTPUT随机值列表：")
print(list_z)


dict_x_y_z = {}							#按照真值表对应顺序制造对应的完整真值表（字典）
for i in range(0,64):
	dict_x_y_z[list_x_y[i]] = list_z[i]

print("-------------------------------------")
print("已制造出真值表随机数字典：")
for x in dict_x_y_z:
	print(x+":"+str(dict_x_y_z[x]))
print("-------------------------------------")


print("\n\n")							#开始传输
print("现在开始传输过程:")
print("\n")

A_number = input("A想输入的3位code是(eg.110):")		   #A按序传输3位输入（此电路A必须输入110输出才可能为1，否则输出一定为0）
A_cipher = A_table[int(A_number,2)]				 #转换为密钥并发送给B
print("A传输给B的密钥是："+A_cipher)
print("A同时传输B的密钥随机数对应表：")
print(B_table)

print("\n")

B_number = input("B想使用的3位code是(eg.110)：")	        #B得到密钥，并找到自己输入对应的密钥（B同样必须输入110输出才可能为1，否则输出一定为0）
print("B从A给的密钥表搜寻对应的密钥：")
B_cipher = B_table[int(B_number,2)]
print("B对应的密钥是："+B_cipher)
key = A_cipher+":"+B_cipher

print("\n")

print("B使用A传输过来的密钥外加自己选择出的密钥得到唯一密钥："+key)	#B结合2个密钥开盒子，得到真值密钥，并送给A
value = dict_x_y_z[key]

print("\n")

print("B使用唯一密钥打开箱子得到唯一输出值："+str(value))
print("B返还唯一输出值"+str(value)+"给A")

print("\n")

print("A根据返回值"+str(value)+"对应序列知道真值为：")			   #A根据真值密钥验证后返回真值
print("(注：本电路只有110+110=1,其他均为0,即原未打乱真值表的第54位,首位为第0位)")

def verify(value,li,bit):
	if value==li[bit]:
		return 1
	else:
		return 0

consult = verify(value,list_z,54)
print("A得到的最终结果是："+str(consult))				#得到最终结果（1/0）

# 以上代码并未做到混淆真值表的部分，应混淆真值表后再发送给B
# 睡前千万不要喝奶茶
