import sys
import re
from filecmp import dircmp
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, # Application and Window libraries
                             QPlainTextEdit,  # Multiline Textboxes
                             QHBoxLayout
                             )
from PyQt5.QtGui import QIcon  # Work with Icons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create controls:
        self.txt_files_left_side = QPlainTextEdit(self)
        self.txt_files_right_side = QPlainTextEdit(self)
        self.initUI()  # format controls
        
        # run the comparison:
        filepath1 = r"C:\Users\asseb\AppData\Roaming\PrismLauncher\instances\Colonies And Technologies\.minecraft\mods"
        filepath2 = r"C:\Users\asseb\AppData\Roaming\PrismLauncher\instances\Colonies And Technologies (WIP-backup)\.minecraft\mods"
        dcmp = dircmp(filepath1, filepath2)
        self.txt_files_left_side.setPlainText("\n".join(dcmp.left_only))
        self.txt_files_right_side.setPlainText("\n".join(dcmp.right_only))
        
    # Initialise User Interface Style Sheets and Geometries (Just cleaner to do this in a seperate function)
    def initUI(self):
        self.setWindowTitle("Wimpie's Files Compare") # set Window title
        self.setGeometry(700, 300, 500, 500) # x, y, width, height (in pixels)
        self.setWindowIcon(QIcon("./img/16px/WimpiesFilesCompare.png")) # Set Window Icon
        
        self.txt_files_left_side
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.txt_files_left_side)
        hbox.addWidget(self.txt_files_right_side)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(hbox)
    
def main(): # Starting function of the application
    # Construct the app object:
    app = QApplication(sys.argv) # Initiate with given system Arguments/Parameters
    # Construct the window object:
    window = MainWindow()
    window.show() # default behavior for a window is to hide it
    sys.exit(app.exec_()) # sys.exit customises a clean exit approach for the program. app.exec_() waits for user input and events, else the app would immediately close. (exec is outdated - use exec_)

# If we're running this file directly, call main() function to begin:
if __name__ == "__main__":
    main()
    