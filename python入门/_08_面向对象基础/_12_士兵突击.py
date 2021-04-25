class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count == 0:
            print("没子弹了")
            return
        self.bullet_count -= 1
        print("[%s] 突突突... [%d]"
              % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("[%s]好没有枪" % self.name)
            return
        print("冲啊...【%s】" % self.name)
        self.gun.add_bullet(100)
        while self.gun.bullet_count != 0:
            self.gun.shoot()


ak47 = Gun("AK47")
# ak47.add_bullet(100)
#
# ak47.shoot()

xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
