import sys
import os
from random import random

os.environ['QT_API'] = 'pyside2'  # tells qtpy to use PySide2
import ryvencore_qt as rc
from qtpy.QtWidgets import QMainWindow, QApplication
from arithmetic.random import Random
from display.DisplayOutput import PrintNode

if __name__ == "__main__":

    # creating the application and a window
    app = QApplication()
    mw = QMainWindow()

    # creating the session, registering, creating script
    session = rc.Session()
    session.design.set_flow_theme(name='pure light')
    session.register_nodes([
        PrintNode,
        Random.RandIntNode,
        Random.RandFloatNode
    ])
    script = session.create_script('hello world', flow_view_size=[1920, 1080])

    mw.setCentralWidget(session.flow_views[script])

    mw.show()
    sys.exit(app.exec_())

