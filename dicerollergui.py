import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sip

class Gui(QMainWindow):

	def __init__(self):
		super(Gui,self).__init__()
		self.widget = QWidget()
		self.widget.setStyleSheet("background: black")

		self.setWindowTitle("Dice Roller Game")
		self.setCentralWidget(self.widget)

		self.splash_screen()

	def splash_screen(self):
		self.spl_label = QLabel()
		self.spl_label.setText("DICE ROLLER GAME")
		self.spl_label.setStyleSheet("color: white;font-size:30px;font-weight:bold")

		pixmap = QPixmap("dice-icon.png")
		self.spl_image = QLabel()
		self.spl_image.setPixmap(pixmap)

		self.spl_btn = QPushButton()
		self.spl_btn.setText("START")
		self.spl_btn.setStyleSheet("background:red;color:white")
		self.spl_btn.clicked.connect(self.menu_window)

		self.spl_btn_h_layout = QHBoxLayout()
		self.spl_btn_h_layout.insertWidget(1,self.spl_btn)

		self.spl_image_h_layout = QHBoxLayout()
		self.spl_image_h_layout.insertStretch(0)
		self.spl_image_h_layout.insertWidget(1,self.spl_image)
		self.spl_image_h_layout.insertStretch(2)


		self.spl_h_layout = QHBoxLayout()
		self.spl_h_layout.insertStretch(0)
		self.spl_h_layout.insertWidget(1,self.spl_label)
		self.spl_h_layout.insertStretch(2)

		self.spl_v_layout = QVBoxLayout()
		self.spl_v_layout.insertStretch(0)
		self.spl_v_layout.insertLayout(1,self.spl_h_layout)
		self.spl_v_layout.insertStretch(2)
		self.spl_v_layout.insertLayout(3,self.spl_image_h_layout)
		self.spl_v_layout.insertStretch(4)
		self.spl_v_layout.insertLayout(5,self.spl_btn_h_layout)
		self.widget.setLayout(self.spl_v_layout)

	def menu_window(self):
		self.mw_widget = QWidget()
		self.mw_widget.setStyleSheet("background:black")
		self.setCentralWidget(self.mw_widget)
		
		self.menu_title = QLabel()
		self.menu_title.setText("CHOOSE A MODE")
		self.menu_title.setStyleSheet("color:red;font-weight:bold;font-size:30px")

		self.pvp_btn = QPushButton()
		self.pvp_btn.setText("Player vs Player")
		self.pvp_btn.setStyleSheet("background:red;color:black")
		self.pvp_btn.clicked.connect(self.pick_a_dice)

		self.pvc_btn = QPushButton()
		self.pvc_btn.setText("Player vs Computer")
		self.pvc_btn.setStyleSheet("background:red;color:black")

		self.exit_btn = QPushButton()
		self.exit_btn.setText("EXIT")
		self.exit_btn.setStyleSheet("background:red;color:black")
		self.exit_btn.clicked.connect(sys.exit)

		self.h_menu_title = QHBoxLayout()
		self.h_menu_title.insertStretch(0)
		self.h_menu_title.insertWidget(1,self.menu_title)
		self.h_menu_title.insertStretch(2)323w3w3

		self.h_pvp_btn = QHBoxLayout()
		self.h_pvp_btn.insertStretch(0)
		self.h_pvp_btn.insertWidget(1,self.pvp_btn)
		self.h_pvp_btn.insertStretch(2)

		self.h_pvc_btn = QHBoxLayout()
		self.h_pvc_btn.insertStretch(0)
		self.h_pvc_btn.insertWidget(1,self.pvc_btn)
		self.h_pvc_btn.insertStretch(2)

		self.h_exit_btn = QHBoxLayout()
		self.h_exit_btn.insertStretch(0)
		self.h_exit_btn.insertWidget(1,self.exit_btn)
		self.h_exit_btn.insertStretch(2)

		self.mw_v_layout = QVBoxLayout()
		self.mw_v_layout.insertStretch(0)
		self.mw_v_layout.insertLayout(1,self.h_menu_title)
		self.mw_v_layout.insertLayout(2,self.h_pvp_btn)
		self.mw_v_layout.insertLayout(3,self.h_pvc_btn)
		self.mw_v_layout.insertLayout(4,self.h_exit_btn)
		self.mw_v_layout.insertStretch(5)

		self.mw_widget.setLayout(self.mw_v_layout)
		self.mw_widget.show()

	def pick_a_dice(self):
		self.pick_a_dice_widget = QWidget()
		self.pick_a_dice_widget.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	myapp = Gui()
	myapp.show()
	sys.exit(app.exec_())	