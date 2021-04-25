class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")
        return super().__new__(cls)

    def __init__(self):
        print("player init")


player = MusicPlayer()
print(player)
