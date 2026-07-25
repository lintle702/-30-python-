'''用 字典（dict） 存储联系人：{姓名: 电话号码}
四个核心函数
表格
函数	功能
add_contact()	增加联系人（重名检测）
delete_contact()	删除联系人（存在性检测）
search_contact()	按姓名查询
update_contact()	修改电话号码
运行方式
bash
运行
python contact_manager.py
进入交互式菜单后，按数字选择：
1 添加 → 输入姓名和电话
2 删除 → 输入姓名删除
3 查询 → 输入姓名查找
4 修改 → 输入姓名和新号码
5 显示全部联系人
0 退出程序
每个操作都带存在性判断和友好提示，适合作为 dict 操作的入门练习。'''
from random import choice


def add_contact(contact,name,phone):
    for i in contact:
        if name==i:
            print("该用户已存在")
            return
    contact[name]=phone
    return
def delete_cotanct(contact,name):
    for i in contact:
        if i==name:
            print("不存在该用户")
            return
    contact.pop(name)
    return
def search_cotanct(contact,name):
    if not name in contact:
        print("该用户不存在")
        return
    print(contact[name])
    return
def update_contact(contact,name,new_phone):
    if not name in contact:
        print("该用户不存在")
        return
    contact[name]=new_phone
def main():
    contanct={}
    while(True):
        print(" 1 添加 → 输入姓名和电话"
              " \n 2 删除 → 输入姓名删除"
              "\n 3 查询 → 输入姓名查找"
              "\n 4 修改 → 输入姓名和新号码"
              "\n 5 显示全部联系人"
              "\n 0 退出程序")
        choice=int(input("请输入选项"))
        if choice==1:
            name=input("请输入姓名：")
            phone=input("请输入电话号码：")
            add_contact(contanct,name,phone)
        if choice==2:
            name=input("请输入要删除的联系人姓名：")
            delete_cotanct(contanct,name)
        if choice==3:
            name=input("请输入要查找的联系人")
            search_cotanct(contanct,name)
        if choice==4:
            name=input("请输入要添加/修改的联系人：")
            new_phone=input("请输入该联系人的号码：")
            update_contact(contanct,name,new_phone)
        if choice==5:
            for key,value in contanct.items():
                print(f"{key}:{value}")
        if choice==0:
            break


if (__name__=="__main__"):
    main()






