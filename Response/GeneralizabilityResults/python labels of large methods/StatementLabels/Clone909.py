def __init__(self) :
	super(Dialog, self).__init__()
	***layoutMain = QtGui.QVBoxLayout(self)
	***listWidget = QtGui.QListWidget(self)
	***gripper = QtGui.QSizeGrip(listWidget)
	***l = QtGui.QHBoxLayout(listWidget)
	***l.setContentsMargins(0, 0, 0, 0)
	***l.addWidget(gripper, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
	***layoutMain.addWidget(listWidget)
	***layoutMain.addWidget(QtGui.QLabel("Test", self))
	***self.setGeometry(200, 500, 200, 500)


def __init__(self, parent, move_widget) :
	super(Grip, self).__init__(parent)
	***self.move_widget = move_widget
	***self.setText("+")
	***self.min_height = 50
	***self.mouse_start = None
	***self.height_start = self.move_widget.height()
	***self.resizing = False
	***self.setMouseTracking(True)
	***self.setCursor(QtCore.Q.SizeVerCursor)

