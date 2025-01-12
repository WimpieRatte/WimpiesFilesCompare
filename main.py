import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool GUI App") # set Window title
        self.setGeometry(700, 300, 500, 500) # x, y, width, height (in pixels)
        
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
    