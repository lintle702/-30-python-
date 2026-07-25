print("hallo worid")
#7月12日
##格式化
###小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2-s1)*100/s1
print(f'小明成绩提升的百分点{r:.2f}%')

#使用list和tuple
###list是一种数据类型，
#len(list)获取列表元素个数，
# 索引list[0]到list[len(list)-1] list[-1]最后一个
#append list.apppend("a") 增加列表元素到末尾
#insert list.insert(2,"a") 插入元素到列表对应索引号位置中
#pop list.pop() 删除列表末尾的元素 pop(1)删除对应索引号位置的元素
#tuple是一种不可改变的列表，指向不改变 a=(1,) () (1,2,3)

#if elif else
#int(input('input your name'))（将输入的字符串变成数字）
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果

weight=80.5
hight=1.75
BIM=weight/hight*2
if BIM<18.5:
    print("过轻")
elif 18.5<=BIM<25:
    print("正常")
elif 25<=BIM< 28:
    print("过重")
elif 28<=BIM<32:
    print("肥胖")
else:
    print("严重肥胖")
##模式匹配
#match casege = 15

##match age:
   # print(f'< 10 years old: {x}')
    #case 10:
       # print('10 years old.')
    #case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
    #case 19:
       # print('19 years old.')
    #case _:
        #print('not sure.')
#循环 for i in list:
#     for i in range(1,101):
#while n<100 :  while循环
#dict={'a'=1,'b'=2} key,value
#dict['a']  |'a' in dict |dict.get('a',9)|dict.pop('a')|
#set={1,2,3,}|set.add(7)|set.remove(2)|s1&s2交集 s1|s2并集
#sort list.sort()对list进行排序 |replace str='abc'  str.replace('a','A')='Abc'
#函数：  def abs(a,n=1):
#切片 list[0:3]==list[:3] 提取第一个到第三个元素
#list[-2:-1]==list[-1:] 提取倒数第二个元素到最后一个元素
#list[:10:2]取前十个数，每两个取一个数字
# 'ABCDEFG'[:3]  'ABC'   'ABCDEFG'[::2]   'ACEG' 字符串也可看作列表做切片
#列表生成式 [x*x for x in range(1,4) if x%2==0]    [m+n for m in 'ABC' for n in 'abc'] [操作 迭代]
#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
#[x if x%2==0 else -x in range(1,4)]  前if else 为计算表达式，而后if 是筛选条件


