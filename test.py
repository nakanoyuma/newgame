import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.load("sample.pyxres")
        self.player_x = 72
        self.player_y = -1
        self.player_vy = 0
        self.floor = [0, 90, True]
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        self.update_player()

        
        self.floor[0] = self.update_floor(0, 90, True)


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
        self.player_vy = min(self.player_vy + 1, 2)
    
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
                self.player_vy += -12
            else:
                #self.player_x += x
                #self.player_y = y
                self.player_vy = 0

        return x, y, is_active



    def draw(self):
        pyxel.cls(5)
        pyxel.text(55, 41, "Hello World!", pyxel.frame_count % 16)
        # draw player
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 12)
        #pyxel.blt(10, 10, 0, 0 , 0, 16, 16, 12)

        # draw floors
        #for x, y, is_active in self.floor:
        pyxel.blt(0, 110, 0, 0, 16, 120, 5, 12)



App()
