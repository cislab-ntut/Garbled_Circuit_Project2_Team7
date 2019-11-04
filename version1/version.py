# coding=gbk		

# Part1-以下代码为电路拼接函式main()，最终返还一个真值表，贮存在dictionary里面：

def AND(input_x,input_y):
	return input_x*input_y

def OR(input_x,input_y):
	if input_x==0 and input_y==0:
		return 0
	else:
		return 1
	
def NOT(derive):
	if derive==0:
		return 1
	else:
		return 0

def generateTable(gate):
	if gate == "AND":
		dc = {}
		for x in [0,1]:
			for y in [0,1]:
				z = AND(x,y)
				c = ""
				c += str(x)
				c += str(y)
				c += ','
				dc[c] = z
		return dc
	elif gate == "OR":
		dc = {}
		for x in [0,1]:
			for y in [0,1]:
				z = OR(x,y)
				c = ""
				c += str(x)
				c += str(y)
				c += ','
				dc[c] = z
		return dc
	elif gate == "NOT":
		dc = {}
		for x in [0,1]:
			z = NOT(x)
			c = ""
			c += str(x)
			c += ','
			dc[c] = z
		return dc
		
And = generateTable("AND")
Or = generateTable("OR")
Not = generateTable("NOT")

change = {"And":And,"Or":Or,"Not":Not}
	
def COMBINE(left_gate,right_gate,up_gate):
	if up_gate == "AND":
		dc = {}
		for x in left_gate:
			for y in right_gate:
				i = x+y
				o = AND(left_gate[x],right_gate[y])
				dc[i] = o
		return dc
	elif up_gate == "OR":
		dc = {}
		for x in left_gate:
			for y in right_gate:
				i = x+y
				o = OR(left_gate[x],right_gate[y])
				dc[i] = o
		return dc

def LINK(gate):
	dc = {}
	dc = gate
	for x in dc:
		if dc[x] == 0:
			dc[x] = 1
		elif dc[x] == 1:
			dc[x] = 0
	return dc

def main():
	i = input("请输入有几层电路：")
	k = int(i)
	dictionary = []
	for x in range(0,k-1):
		z = []
		dictionary.append(z)
	print("————————————————————————————————————————————————")
	print("这是第1层的电路组合：")
	flag = 1
	v = 1
	while flag:
		print("这是第一层电路的第"+str(v)+"次组合：------------------")
		name = input("请输入连接至哪种类型电路（AND/OR/NOT）:")
		if name == "AND" or name == "OR":
			l = input("左边是哪个电路门（And/Or/Not）：")
			left = change[l]
			r = input("右边是哪个电路门（And/Or/Not）:")
			right = change[r]
			line = {}
			line = COMBINE(left,right,name)
			dictionary[0].append(line)
		elif name == "NOT":
			g = input("请输入这是哪个电路门（And/Or/Not）：")
			gate = change[g]
			line = {}
			line = LINK(gate)
			dictionary[0].append(line)
		v = v+1
		f = input("还要继续吗？(1/0)")
		flag = int(f)
	print("===============================")	
	for x in range(2,k):
		print("现在进入第"+str(x)+"层电路组合：")
		f = input("请输入这一层电路有几次组合：")
		j = int(f)
		for y in range(0,j):
			print("这是第"+str(y)+"次组合：")
			name = input("请输入连接至哪种类型电路（AND/OR/NOT）:")
			if name == "AND" or name == "OR":
				l = input("左边是哪个line（1,2,3...）：")
				left = int(l)
				r = input("右边是哪个line（1,2,3...）:")
				right = int(r)
				line = {}
				line = COMBINE(dictionary[x-2][left-1],dictionary[x-2][right-1],name)
				dictionary[x-1].append(line)
			elif name == "NOT":
				g = input("请输入这是哪个line（1,2,3...）：")
				gate = int(g)
				line = {}
				line = LINK(dictionary[x-2][gate-1])
				dictionary[x-1].append(line)
			print("---------------")
		print("--------------------------")
	print("以下是完整真值表：——————————————————————————————")
	for x in dictionary[k-2]:
		for y in x:
			print(y+":"+str(x[y]))
		
main()

# Part-2 以下代码为随机数加密真值表函式encry(),进入dictionary，返回一个加密后的真值表zip：

def encry(dictionary):
	
# Part-3 以下代码为混淆真值表顺序函式mess(),进入zip,返回final:

def mess(zip):
	
# Part-4 分离出2个输入方的密钥表，得到finalA,finalB：

# Part-5 传输过程与返回过程的代码函式run()：

def run():











