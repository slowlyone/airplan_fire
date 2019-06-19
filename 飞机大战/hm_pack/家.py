class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):
        return "家具名称[%s] ,占地面积%.2f"%(self.name,self.area)


class House:
    def __init__(self,house_type,area):
        self.area=area
        self.house_type=house_type

        self.free_area=area

        self.item_list=[]
    def __str__(self):
        return ("户型:%s\n面积%.2f "
               "[剩余:%.2f]\n家具%s"
               %(self.house_type,self.area,
                  self.free_area,self.item_list))

    def add_item(self,item):
        print("要添加%s"%item)
        if item.area > self.free_area:
            print("%s太大了，房子装不下" %item.name)
            return

        self.item_list.append(item.name)
        self.free_area -= item.area

bed =HouseItem("席梦思",4)
chest=HouseItem("衣柜",55)
table=HouseItem("餐桌",1.5)
#print(bed)
#print(chest)
#print(table)
myhome=House("两室一厅",60)
myhome.add_item(bed)
myhome.add_item(chest)
myhome.add_item(table)
print(myhome)