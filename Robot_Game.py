from random import randint
from gasp import *
from random import randint
begin_graphics(width=800, height=600, title="Robo Game", background=color.YELLOW)

Circle((300,200),40)
Circle((285,210),5)
Circle((315,210),5)
Line((290,190),(300,210))
Line((290,190),(310,190))
Arc((300,200),30,225,315)
Arc((285,210),10,150,30)
Arc((315,210),10,150,30)

Circle((600,400),40)
Circle((585,410),5)
Circle((615,410),5)
Line((590,390),(600,410))
Line((590,390),(610,390))
Arc((600,400),30,225,315)
Arc((585,410),10,150,30)
Arc((615,410),10,150,30)



update_when('key_pressed')
end_graphics()
