import sys
import os
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QMessageBox
from PySide6.QtGui import QColor, QIcon
import browser_downloads as bd
import gaming_downloads as gd
import app_downloads as ad
import styles as s

class MainWindow(QMainWindow):
    
    def sizeHint(self):
        return QSize(1280, 720)
    
    def __init__(self):
        super().__init__()
        
        app_downloads = [
            ("Install VS Code", ad.download_vscode),
            ("Install Spotify", ad.download_spotify),
            ("Install VLC", ad.download_vlc)
        ]
        
        browser_downloads = [
            ("Install Firefox", bd.download_firefox),
            ("Install Chrome", bd.download_chrome)
        ]
        
        gaming_downloads = [
            ("Install Steam", gd.download_steam),
            ("Install Discord", gd.download_discord),
            ("Install EGL", gd.download_epic_games_launcher)
        ]

        self.setWindowTitle("Neue Installer")
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
        
        self.setWindowIcon(QIcon('logo.png'))
        
        central_widget.setAutoFillBackground(True)
        palette = central_widget.palette()
        palette.setColor(central_widget.backgroundRole(), QColor(0, 0, 0))
        central_widget.setPalette(palette)

        # Browser downloads
        browser_section_label = QLabel("Browser Downloads")
        self.layout.addWidget(browser_section_label)
        
        browser_layout = QHBoxLayout()
        
        for text, download_func in browser_downloads:
            button = QPushButton(text)
            button.clicked.connect(download_func)
            self.layout.addWidget(button)
            
        
        self.layout.addLayout(browser_layout)
        
        # Gaming downloads
        gaming_section_label = QLabel("Gaming Downloads")
        self.layout.addWidget(gaming_section_label)
        
        gaming_layout = QHBoxLayout()
        
        for text, download_func in gaming_downloads:
            button = QPushButton(text)
            button.clicked.connect(download_func)
            self.layout.addWidget(button)
        
        self.layout.addLayout(gaming_layout)
        
        # App downloads
        app_section_label = QLabel("App Downloads")
        self.layout.addWidget(app_section_label)
        
        app_layout = QHBoxLayout()
        
        for text, download_func in app_downloads:
            button = QPushButton(text)
            button.clicked.connect(download_func)
            self.layout.addWidget(button)
        
        self.layout.addLayout(app_layout)
            
        for widget in self.layout.parentWidget().findChildren(QLabel):
            s.applyLabelStyles(self, widget)
            
        for widget in self.layout.parentWidget().findChildren(QPushButton):
            widget.setFixedSize(100, 40)
            s.applyButtonStyles(self, widget)
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', "All installation files will be cleared. Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            current_dir = os.getcwd()
            for file in os.listdir(current_dir):
                if file.endswith(".exe"):
                    os.remove(os.path.join(current_dir, file))
            event.accept()
        else:
            event.ignore()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
