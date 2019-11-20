from prettytable import PrettyTable




##学生信息录入
student = {}
student1=[]
def  add_id():
    flag = 1
    while flag==1 :
        name= input('姓名：')
        old = input('年龄：')
        sex = input('性别：')
        id  = input('学号：')
        student['name'] = name 
        student['old']  = old
        student['sex']  = sex
        student['id']   = id
        student1.append(student)
        print('输入完成！')
        i = input ('是否继续输入: 是:按1\n否:按其它任意键')
        if i!='1':
           flag=0


##自动选择宿舍
def  xuanze_suse():
    k=[]
    i=0
    A = int(input('寝室分配：1为自动，2为手动'))
    if A==1:
        for xingbie in student1 :
            if  len(xingbie)==4:
                k.append(xingbie)
      
        for b in k:
            if b['sex'] == '男':
                suse = [100,101,102]
                for num in suse:
	                for d in student1:
	                    if d in k:
	                        continue
	                    elif d['suse']==str(num):
	                        i=i+1
	                if i ==4 :
	                    pass
	                else:
	                    b['suse']=str(num)
	                i = 0

               
            if b['sex'] =='女':
                suse = [200,201,202]
                for num in suse:
	                for d in student1:
	                    if d in k:
	                        continue
	                    elif d['suse']==str(num):
	                        i=i+1
	                if i ==4 :
	                    pass
	                else:
	                    b['suse']=str(num)
	                    
	                i = 0
       
        print('所有学生宿舍安排完毕!')

            
#手动选择宿舍
    elif A==2 :
        for xingbie in student1 :
            if  len(xingbie)==4:
                k.append(xingbie)
        if k==[]:
           print('所有学生已有宿舍！')
       
        for b in k:
            while b['sex'] == '女':
                print('请输入女生',b['name'],'的宿舍号:')
                suse = input('200\n201\n202\n中的一个')
                if suse == '200' or suse =='201' or suse=='202':
                    for d in student1 :

                        if len(d)==5 and d['suse'] == suse:
                            i = i + 1


                    if i == 4:
                        print('suse宿舍已满:\n请重新选择！')
                    else:
                        b['suse'] = suse
                        print('宿舍选择成功！\n',b['name'],'宿舍为:',b['suse'])
                        break
                       
                    i=0
                else:
                    print('宿舍输入错误,请重新输入!')



            i=0;
            while b['sex'] =='男' :
                print('请输入男生',b['name'],'的宿舍号:')
                suse = input('100\n101\n102\n中的一个')
                if suse =='100' or suse=='101' or suse =='102':
                    for d in student1:

                        if len(d)==5 and d['suse'] == suse:
                            i += 1

                    if i == 4:
                        print('suse宿舍已满:\n请重新选择！ ')
                    else :
                        b['suse'] = suse
                        print('宿舍选择成功！\n',b['name'],'宿舍为:',b['suse'])
                        break
         
                    i=0
                else:
                    print('宿舍输入错误,请重新输入!')
            jixu = int(input('是否继续选择宿舍：\n是:按1\n否:0!'))
            if jixu != 1:
                break





#宿舍人员名单

def mingdan_suse():
    x = PrettyTable(['宿舍号' , "姓名"])
    for b in student1:
        if len(b) == 5:
           for s in range(100,103):
               if  b['suse'] == str(s) :
                   x.add_row([b['suse'],b['name']])
            
    print('男生宿舍列表：')
    print(x)

    y = PrettyTable(['宿舍号' , "姓名"])
    for b in student1:
        if len(b) == 5:
           for s in range(200,203):
               if  b['suse'] == str(s):
                   y.add_row([b['suse'],b['name']])
            
    print('女生宿舍列表：')
    print(y)



#全部人员名单
def  mingdan_all() :
    x = PrettyTable(['姓名' , "性别", "年龄" , "学号", "宿舍"])
    for b in student1 :
        if len(b) ==5:
           x.add_row([b['name'],b['sex'],b['old'],b['id'],b['suse']])
    y = PrettyTable(['姓名' , "性别", "年龄" , "学号"])
    for c in student1 :
        if len(c) ==4:
           y.add_row([c['name'],c['sex'],c['old'],c['id']])
    print('已经分配宿舍所有学生名单：')
    print(x)
    print('未分配宿舍的所有学生名单：')
    print(y)


##############利用学号索引信息
def sousuo_id() :
    flag =1
    while flag == 1:
        xh = input('输入要查找学生的学号')
        x =0
        for b in student1 :
            if b['id'] == xh and len(b)==5:
                x = 1
                print('学生信息为:')
                c = PrettyTable(['姓名' , "性别", "年龄" , "学号", "宿舍号"])
                c.add_row([b['name'],b['sex'],b['old'],b['id'],b['suse']])
                print(c)
                jx=int(input('是否继续查找学生:\n是:按1\n否:按0\n'))
                if jx != 1:
                    flag = 0
            elif b['id'] == xh and len(b)==4:
                x = 1
                print('学生信息为:')
                c = PrettyTable(['姓名' , "性别", "年龄" , "学号"])
                c.add_row([b['name'],b['sex'],b['old'],b['id']])
                print(c)
                jx=int(input('是否继续查找学生:\n是:按1\n否:按0\n'))
                if jx != 1:
                    flag = 0
        if x ==0:
            print('输入学生id错误,请重新输入')


###################寝室调整
def  huan_suse() :
    i=0
    j=0
    flag = 1
    while flag == 1:
        t = input('输入学生id,学生id为四位：')
        for b in student1:
            if b['id'] == t and len(b)==5:
                c = b
                f = b
                print('输入正确！！！！')
                c = PrettyTable(['姓名' , "性别", "年龄" , "学号", "宿舍"])
                c.add_row([b['name'],b['sex'],b['old'],b['id'],b['suse']])
                print(c)#学生信息
                i = 1
                flag = 0
            elif b['id'] == t and len(b)==4:
                print('该学生还没有分配宿舍！！！')

        if i ==0 :
            print('学生id错误,请重新输入学生id！')


    while True :
        huan =input('输入想要换到的宿舍号:')

        for d in student1:
            if len(d)==5 and d['suse'] == huan:
                j = j + 1
        if  j == 4 :
            print('宿舍已满，请重新输入!')
            j=0
        else :
            f['suse'] = huan
            print('宿舍修改成功！')
            break




############信息存入studeng1.json
import json
def xingxi_save():
    filename='student1.json'
    with open(filename,'w') as file_obj:
        json.dump(student1,file_obj)
############信息打开时导入信息

def xingxi_daoru(student1):
    f =open('student1.json',encoding='utf-8') 
    res=f.read() 
    info = json.loads(res)
    student1.extend(info)



def interface() :
    print(30*'-')
    print('1:添加学生信息')
    print('2:选择宿舍')
    print('3:打印宿舍人员名单')
    print('4:打印所有人员名单')
    print('5:索引打印特定学生信息')
    print('6:更换学生宿舍')
    print('0:退出程序')
    

xingxi_daoru(student1)
while True :
    interface()
    yewu = int(input('输入你想要执行的业务'))
    print(30*'-')
    if yewu == 1 :
        add_id()
        xingxi_save()
    elif yewu ==2:
        xuanze_suse()
        xingxi_save()
    elif yewu ==3:
        mingdan_suse()

    elif yewu ==4:
        mingdan_all()

    elif yewu ==5:
        sousuo_id()

    elif yewu ==6:
        huan_suse()
        xingxi_save()
    elif yewu ==0:
        end = input('是否与退出:\n是:1\n否:其它任意键\n')
        if end == '1':
            break
    else:
        print('输入错误，请重新输入')




