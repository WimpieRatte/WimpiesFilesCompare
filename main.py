import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, # Application and Window libraries
                             QPushButton, QLabel, # buttons & labels (can handle images too, via QPixmap below)
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout) # widgets and layout managers
from PyQt5.QtGui import (QIcon, # Work with Icons
                         QFont, # Set Fonts (E.g: in labels)
                         QPixmap) # Handle images/pictures
from PyQt5.QtCore import Qt # Used for alignments (E.g: in labels)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool GUI App") # set Window title
        self.setGeometry(700, 300, 500, 500) # x, y, width, height (in pixels)
        self.setWindowIcon(QIcon("./img/16px/WimpiesFilesCompare.png")) # Set Window Icon
        
        # Good practise to create self.* widgets in the constructor:
        self.button = QPushButton("Click me!", self) # putting "self." in front, creates a widget instead of a variable, allowing it to be referenced in other functions.
        self.label = QLabel("Hello", self)
        self.initUI()
        
    # Initialise User Interface (Just cleaner to do this in a seperate function)
    def initUI(self):         
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) # connect the button.clicked signal (event) to the self.on_click slot (function)
                                              # (a signal is emmitted when a widget is interacted with)
                                              
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")
        
    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!") # we can simply setText instead of using QLabel
        self.button.setDisabled(True) # how to disable button
        
        self.label.setText("Goodbye")
            
        
        
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
    