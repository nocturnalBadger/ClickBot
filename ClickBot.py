from pymouse import PyMouse, PyMouseEvent
import time


class ClickListener(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        if button == 1: # Ok, I stumbled upon this but here's what's I think is happening: when the listener is triggered it clicks and triggers itself. In this way it continues indefinately.
            if press:
                mouse.click(x, y)
                time.sleep(.002)
        else:
            self.stop()

mouse = PyMouse()

clickListener = ClickListener()

clickListener.run()
