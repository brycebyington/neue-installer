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
        chrome_button = QPushButton("Install Chrome")
        chrome_button.clicked.connect(bd.download_chrome)
        firefox_button = QPushButton("Install Firefox")
        firefox_button.clicked.connect(bd.download_firefox)
        browser_layout.addWidget(chrome_button)
        browser_layout.addWidget(firefox_button)
        self.layout.addLayout(browser_layout)
        
        # Gaming downloads
        gaming_section_label = QLabel("Gaming Downloads")
        self.layout.addWidget(gaming_section_label)
        
        gaming_layout = QHBoxLayout()
        steam_button = QPushButton("Install Steam")
        steam_button.clicked.connect(gd.download_steam)
        discord_button = QPushButton("Install Discord")
        discord_button.clicked.connect(gd.download_discord)
        gaming_layout.addWidget(steam_button)
        gaming_layout.addWidget(discord_button)
        self.layout.addLayout(gaming_layout)
        
        # App downloads
        app_section_label = QLabel("App Downloads")
        self.layout.addWidget(app_section_label)
        
        app_layout = QHBoxLayout()
        spotify_button = QPushButton("Install Spotify")
        spotify_button.clicked.connect(ad.download_spotify)
        vscode_button = QPushButton("Install VS Code")
        vscode_button.clicked.connect(ad.download_vscode)
        app_layout.addWidget(spotify_button)
        app_layout.addWidget(vscode_button)
        self.layout.addLayout(app_layout)
        
        for widget in self.layout.parentWidget().findChildren(QPushButton):
            widget.setFixedSize(100, 40)
            s.applyButtonStyles(self, widget)
            
        for widget in self.layout.parentWidget().findChildren(QLabel):
            s.applyLabelStyles(self, widget)
    
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
