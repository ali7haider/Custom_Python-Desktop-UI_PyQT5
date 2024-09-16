from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent

import sys
import resources_rc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the .ui file
        uic.loadUi('main_ui.ui', self)  # Adjust the path to your .ui file
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Connect the maximizeRestoreAppBtn button to the maximize_window method
        self.maximizeRestoreAppBtn.clicked.connect(self.maximize_window)
        
        # Connect the closeAppBtn button to the close method
        self.closeAppBtn.clicked.connect(self.close)

        # Connect the minimizeAppBtn button to the showMinimized method
        self.minimizeAppBtn.clicked.connect(self.showMinimized)


        # Initialize UI elements and layout
        self.generate_calibration_file_ui()

    def generate_calibration_file_ui(self):
        # Sample data
        data = [
            ['Warning-1', '2024-09-01 - 08:15:20', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
            ['Warning-2', '2024-09-02 - 10:22:30', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
            ['Warning-3', '2024-09-03 - 12:33:45', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
            ['Warning-4', '2024-09-04 - 14:44:50', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
            ['Warning-5', '2024-09-05 - 16:55:55', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
            ['Warning-6', '2024-09-06 - 18:05:10', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
            ['Warning-7', '2024-09-07 - 20:15:25', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
            ['Warning-8', '2024-09-08 - 22:25:35', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
            ['Warning-9', '2024-09-09 - 09:52:05', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],
                        ['Warning-9', '2024-09-09 - 09:52:05', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json'],

            ['Warning-9', '2024-09-09 - 09:52:05', 'Failed to load config file:/opt/acs/nexus/cont/app_discriptor.json']

        ]


        scroll_content_widget = QWidget()
        scroll_content_layout = QVBoxLayout(scroll_content_widget)

        for profile in data:
            warning_name = profile[0]
            date = profile[1]
            link = profile[2]
            
            frame = QWidget()
            frame.setObjectName(warning_name)
            frame.setStyleSheet("background-color: white; border-bottom: 1px solid #C8C9D6; ")  # Set background color to white and customize border
            frame.setMaximumSize(QtCore.QSize(16777215, 100))
            frame_layout = QHBoxLayout(frame)
            frame_layout.setContentsMargins(6, 6, 6, 6)
            frame_layout.setSpacing(4)
            
            # Warning button
            btn_warning = QPushButton()
            btn_warning.setObjectName('btnWarning')
            btn_warning.setMinimumSize(QtCore.QSize(0, 38))
            btn_warning.setMaximumSize(QtCore.QSize(150, 38))
            btn_warning.setFlat(True)
            btn_warning.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            # Set icon for the button
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/icons/warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Adjust the path to your icon
            btn_warning.setIcon(icon)
            btn_warning.setIconSize(QtCore.QSize(25, 25))  # Set icon size

            # Set button text with underline, color, and spacing between icon and text
            btn_warning.setStyleSheet("""
                QPushButton {
                    color: #A0104E;                                      
                }
            """)
            btn_warning.setText("    WARNING")


            # Uncomment and connect to the click handler if needed
            # btn_warning.clicked.connect(functools.partial(self.btn_warning_click, warning_name))
            
            # Date label
            date_label = QLabel()
            date_label.setObjectName('lblDateTime')
            date_label.setMaximumSize(QtCore.QSize(250, 38))

            date_label.setStyleSheet("background-color:transparent; color:#5E5F68; padding: 4px;border:none;")
            date_label.setText(date)
            
            # Link label
            link_label = QLabel()
            link_label.setObjectName('lblLink')
            link_label.setText(link)
            link_label.setStyleSheet("background-color:transparent; color:#5E5F68; padding: 4px;border:none;")
            
            # Add components to layout
            frame_layout.addWidget(btn_warning)
            frame_layout.addWidget(date_label)
            frame_layout.addWidget(link_label)
            
            scroll_content_layout.addWidget(frame)
        
        # Add spacer if there are few profiles
        if len(data) <= 6:
            space = len(data)
            spacerItem1 = QSpacerItem(20, 350 // space, QSizePolicy.Expanding, QSizePolicy.Minimum)
            scroll_content_layout.addItem(spacerItem1)
        
        # Set the widget to the scroll area
        self.scrollArea.setWidget(scroll_content_widget)

    def btn_warning_click(self, warning_name):
        print(f"Warning button clicked for: {warning_name}")
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPos)
            event.accept()

    def maximize_window(self):
        # If the window is already maximized, restore it
        if self.isMaximized():
            self.showNormal()
        # Otherwise, maximize it
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
