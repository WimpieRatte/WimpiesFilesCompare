import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, # Application and Window libraries
                             QPushButton, QLabel, # buttons & labels (can handle images too, via QPixmap below)
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, # widgets and layout managers
                             QCheckBox, # Checkbox support
                             QRadioButton, QButtonGroup) # Radiobuttons and their groupings
from PyQt5.QtGui import (QIcon, # Work with Icons
                         QFont, # Set Fonts (E.g: in labels)
                         QPixmap) # Handle images/pictures
from PyQt5.QtCore import Qt # Used for alignments (E.g: in labels) and states (E.g: in checkboxes)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool GUI App") # set Window title
        self.setGeometry(700, 300, 500, 500) # x, y, width, height (in pixels)
        self.setWindowIcon(QIcon("./img/16px/WimpiesFilesCompare.png")) # Set Window Icon
        
        # Good practise to create self.* widgets in the constructor:
        self.button = QPushButton("Click me!", self) # putting "self." in front, creates a widget instead of a variable, allowing it to be referenced in other functions.
        self.label = QLabel("Hello", self)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()
        
    # Initialise User Interface Style Sheets and Geometries (Just cleaner to do this in a seperate function)
    def initUI(self):         
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) # connect the button.clicked signal (event) to the self.on_click slot (function)
                                              # (a signal is emmitted when a widget is interacted with)
                                              
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")
        
        # Checkboxes:
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed) # connect the checkbox.checkbox_changed signal (event) to the self.checkbox_changed slot (function)
        
        # Radio buttons:
        self.radio1.setGeometry(0, 100, 300, 50)
        self.radio2.setGeometry(0, 150, 300, 50)
        self.radio3.setGeometry(0, 200, 300, 50)
        self.radio4.setGeometry(300, 100, 300, 50)
        self.radio5.setGeometry(300, 150, 300, 50)
        self.setStyleSheet("QRadioButton{"  # Set style for all controls of this type
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        
    # Button click:
    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!") # we can simply setText instead of using QLabel
        self.button.setDisabled(True) # how to disable button
        
        self.label.setText("Goodbye")
            
    # Checkbox check:
    def checkbox_changed(self, state):
        # print(state) # 0 = unchecked; 2 = checked; 1 = partially checked
        if state == Qt.Checked: # This also means "2", but it's a constant available for us that's more readable.
            print("You like food")
        else:
            print("You DO NOT like food")
            
    # Radio button changed
    def radio_button_changed(self):
        radio_button = self.sender() # returns the widget that sent the signal
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")  # get text of selected button
        
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
    