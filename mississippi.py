def frequency(string):
	dic=()
	for val in string:
		dic.setdefault(val,o)
		dic[val]+=1
	dic={k: v for k, v in sorted(dic.items(),key=lambda item: item[1])}
	for k, v in reversed(dic.items()):
		print(k,"=", v,end+' ')
string=input("please enter a string")
frequency(string)
