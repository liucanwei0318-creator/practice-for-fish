def search(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        guess=list[mid]
        if guess==item:
            return mid
        if guess<item:
            low=mid+1
        if guess>item:
            high=mid-1
    return None
stop=input("如果要停止程序，请输入s：")
if stop!="s":
    my_list=[int(x)for x in input("请输入你要挑选的数组：").split()]
    my_item=int(input("请输入你要寻找到数："))
    print(search(my_list,my_item))
else:
    print("欢迎下次光临")