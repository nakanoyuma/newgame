from random import randint

import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.load("sample.pyxres")
        self.score = 0
        self.player_x = 72
        self.player_y = -1
        self.player_vy = 0
        self.floor = [0, 90, True]
        self.movefloor = [(randint(0, 104),randint(60, 70), True)]
        self.fruit = [(i * 60, randint(0, 104), randint(0, 2), True) for i in range(4)]
        self.item = [(i * 60, randint(0, 104), True) for i in range(4)]
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        self.update_player()

        self.score += 1

        self.floor[0] = self.update_floor(0, 90, True)

        for i, v in enumerate(self.movefloor):
            self.movefloor[i] = self.update_movefloor(*v)

        for i, v in enumerate(self.fruit):
            self.fruit[i] = self.update_fruit(*v)

        for i, v in enumerate(self.item):
            self.item[i] = self.update_item(*v)

    def update_player(self):
        #Shiftキーでジャンプ
        #if pyxel.btn(pyxel.KEY_SPACE) :
        #    self.player_y += -15
        #左へ進む
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
        #右へ進む
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
            
        #重力
        self.player_y += self.player_vy
        self.player_vy = min(self.player_vy + 1, 6)
    
    def update_floor(self, x, y, is_active):
        #当たり判定
        if (
            #self.player_x + 16 >= x
            #and self.player_x <= x + 40
            #and 
            self.player_y + 16 >= y
            and self.player_y <= y + 8
            and self.player_vy >= 0
            #and self.player_is_alive
        ):
            if pyxel.btn(pyxel.KEY_SPACE) :
                self.player_vy += -10
            else:
                #self.player_x += x
                self.player_y -= 1 
                self.player_vy = 0

        return x, y, is_active

    def update_movefloor(self, x, y, is_active):
    
        if is_active:
            #当たり判定
            if (
                self.player_x + 16 >= x
                and self.player_x <= x + 40
                and self.player_y + 16 >= y
                and self.player_y <= y + 8
                and self.player_vy > 0
                #and self.player_is_alive
            ):

                if pyxel.btn(pyxel.KEY_SPACE) :
                    self.player_vy += -10
                else:
                    self.player_y -= 1 
                    self.player_vy = 0
            
            #当たり判定左から
            if (self.player_x + 16 <= x + 40
                and self.player_x + 16 >= x
                and self.player_y <= y + 8
                and self.player_y + 16 >= y
                ):
                
                self.player_x -= 2
            
            #当たり判定右から
            elif (self.player_x <= x + 40
                and self.player_x >= x
                and self.player_y <= y + 8
                and self.player_y + 16 >= y
                ):
                
                self.player_x += 2


        #フロアを左に
        #x -= 4

        #左に行った場合、右に戻している。
        if x < -40:
            x += 180
            y = randint(8, 100)
            is_active = True

        return x, y, is_active

    def update_fruit(self, x, y, kind, is_active):
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            if self.score >= 100:
                self.score -= 100
            elif self.score < 100:
                self.score = 0

            y -= 140


        y += 1

        if y > 120:
            y -= 140
            x = randint(8, 100)
            kind = randint(0, 2)
        return (x, y, kind, is_active)

    def update_item(self, x, y, is_active):
        if is_active and abs(x - self.player_x) < 8 and abs(y - self.player_y) < 8:
            self.score += 100

            x += 200

        x -= 2

        if x < -40:
            x += 200
            y = randint(40, 65)

        return (x, y, is_active)

    
    def draw(self):
        pyxel.cls(15)
        #pyxel.text(55, 41, "Hello World!", pyxel.frame_count % 16)
        # draw player
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 12)
        #pyxel.blt(10, 10, 0, 0 , 0, 16, 16, 12)

        # draw floors
        #for x, y, is_active in self.floor:
        pyxel.blt(0, 90, 0, 0, 40, 160, 5, 12)

        for x, y, is_active in self.movefloor:
            pyxel.blt(x, y, 0, 0, 16, 40, 8, 12)

        # draw fruits
        for x, y, kind, is_active in self.fruit:
            if is_active:
                pyxel.blt(x, y, 0, 32 + kind * 16, 0, 16, 16, 12)
        
        # draw item
        for x, y, is_active  in self.item:
            pyxel.blt(x, y, 0, 0, 24, 8, 8, 12)

        
        

        # draw score
        s = "SCORE {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)




App()
