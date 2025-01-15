import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,    # Application and Window libraries
                             QPushButton, 
                             QWidget, QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # declare controls here, above the call to self.initUI():
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    # Initialise User Interface Style Sheets and Geometries (Just cleaner to do this in a seperate function)
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        central_widget.setLayout(hbox)
        
        # Set names that we can access in a stylesheet:
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        # Set style on entire window: (via "ObjectClass" and/or "ObjectClass#ObjectName")
        self.setStyleSheet("""
           QPushButton{
               font-size: 40px;
               font-family: Arial;
               padding: 15px 75px;
               margin: 25px;
               border: 3px solid;
               border-radius: 15px;
           }                
           
           QPushButton#button1 {
               background-color: hsl(0, 100%, 64%);
           }
           QPushButton#button2 {
               background-color: hsl(122, 100%, 64%);
           }
           QPushButton#button3 {
               background-color: hsl(204, 100%, 64%);
           }
           
           QPushButton#button1:hover {
               background-color: hsl(0, 100%, 84%);
           }
           QPushButton#button2:hover {
               background-color: hsl(122, 100%, 84%);
           }
           QPushButton#button3:hover {
               background-color: hsl(204, 100%, 84%);
           }
        """)

def main(): # Starting function of the application
    # Construct the app object:
    app = QApplication(sys.argv)  # Initiate with given system Arguments/Parameters
    # Construct the window object:
    window = MainWindow()
    window.show()  # default behavior for a window is to hide it
    sys.exit(app.exec_())  # sys.exit customises a clean exit approach for the program. app.exec_() waits for user input and events, else the app would immediately close. (exec is outdated - use exec_)

# If we're running this file directly, call main() function to begin:
if __name__ == "__main__":
    main()