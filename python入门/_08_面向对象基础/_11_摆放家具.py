class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "户型：%s \n总面积：%.2f[剩余：%.2f]\n家具：%s" \
               % (self.house_type, self.area,
                  self.free_area, self.item_list)

    def add_item(self, house_item):
        print("要添加：%s" % house_item)
        if self.free_area - house_item.area >= 0:
            self.free_area -= house_item.area
            self.item_list.append(house_item.name)
        else:
            print("不能添加 %s 剩余面积不够" % house_item.name)


bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 18)
table = HouseItem("餐桌", 10.5)

print(bed)
print(chest)
print(table)

my_home = House("两室一厅", 60)
print(my_home)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
