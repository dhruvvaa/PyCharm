class MobilePhone:
    def __init__(self, memory):
        self.memory = memory

class Camera:
    def take_pictures(self):
        print("Say Cheeseee")

class CameraPhone(MobilePhone, Camera):
    pass

iphone = CameraPhone('16GB')
print(iphone.memory)
iphone.take_pictures()