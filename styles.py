def applyButtonStyles(self, button):
    button.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            text-align: center;
            text-decoration: none;
            font-size: 12px;
            font-family: Roboto;
            border-radius: 10px;
        }
        QPushButton:hover {background-color: #45a049;}
        QPushButton:pressed {background-color: #3e8e41;}
    """)
    
def applyLabelStyles(self, label):
    label.setStyleSheet("""
        color: white;
        font-family: Roboto;
        font-weight: bold;
        font-size: 24px;
        margin-bottom: 10px;
        margin-top: 10px;
    """)

            
    
