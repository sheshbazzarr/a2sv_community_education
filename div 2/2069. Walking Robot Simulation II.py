class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = "East"
        

    def step (self, num: int) -> None:
        num %= self.w * 2 + self.h * 2 - 4
        if num == 0:
            num = self.w * 2 + self.h * 2 - 4
        
        for _ in range(num):
            if self.dir == "East":
                if self.x == self.w - 1:
                    self.dir = "North"
                    self.y += 1
                else:
                    self.x += 1
            elif self.dir == "North":
                if self.y == self.h - 1:
                    self.dir = "West"
                    self.x -= 1
                else:
                    self.y += 1
            elif self.dir == "West":
                if self.x == 0:
                    self.dir = "South"
                    self.y -= 1
                else:
                    self.x -= 1
            elif self.dir == "South":
                if self.y == 0:
                    self.dir = "East"
                    self.x += 1
                else:
                    self.y -= 1

    def getPos(self) -> list:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dir

