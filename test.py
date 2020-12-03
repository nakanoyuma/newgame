import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.load("sample.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(5)
        pyxel.text(55, 41, "Hello World!", pyxel.frame_count % 16)
        # draw player
        pyxel.blt(10, 10, 0, 0, 0, 16, 16, 12)



App()
