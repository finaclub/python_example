myList = [1,2,3,4,5]
print(myList) # [1,2,3,4,5]
def f(i):
	if(i<4) :
		return True
	else :
		return False
myList2 = list(filter(f, myList))
print(myList2)                                        #[1,2,3]

def g(i):
	if(i<3) :
		return i*10
	else :
		return i
myList3 = list(map(g, myList))
print(myList3)                                       #[10, 20, 3, 4, 5]

myList4 = list(zip(myList, myList2, myList3))        # 3つのリストを一つに束ねる　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
print(myList4)                                       # [(1, 1, 10), (2, 2, 20), (3, 3, 3)]
