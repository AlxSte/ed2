import time

class TraffcLight:
    __color = "red"
    def __int__(self):
        pass
    def running (self):
       while True:
        color = "red"
        print(color)
        time.sleep(7)
        color = "yellow"
        print(color)
        time.sleep(2)
        color = "green"
        print(color)
        time.sleep(3)

tf = TraffcLight()
tf.running()