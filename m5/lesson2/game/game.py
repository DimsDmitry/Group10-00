from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        base.camLens.setFov(90)


app = MyApp()
app.run()
