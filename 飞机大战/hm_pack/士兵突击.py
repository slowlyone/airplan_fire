class Gun:
    def __init__(self,model):
        self.model=model
        self.bullet_count=0
    def add_bullet(self,count):
        self.bullet_count += count
    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s] 子弹不够了"%self.model)
        self.bullet_count -= 1
        print("[%s] 打打打打...[余%d]"%(self.model,self.bullet_count))


class Solder:
    def __init__(self,name):
        self.name=name
        self.gun=None
    def shoot(self):
        if self.gun is None:
            print("[%s] 没有枪"%self.name)

        self.gun.add_bullet(50)
        print("gogo")
        self.gun.shoot()
ak47=Gun("ak47")
#ak47.add_bullet(50)
#ak47.shoot()

xusanduo=Solder("许三多")
#print(xusanduo.gun)
xusanduo.gun=ak47
xusanduo.shoot()