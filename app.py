# app.py
# -*- coding: utf-8 -*-
import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QMessageBox
)
from PySide6.QtCore import Qt

def main():
    app = QApplication(sys.argv)

    # Cria a janela principal
    win = QMainWindow()
    win.setWindowTitle("App Remoto - D'Signer")

    # Layout
    central = QWidget()
    layout = QVBoxLayout(central)

    lbl = QLabel("✅ App remoto carregado do Vercel")
    lbl.setAlignment(Qt.AlignCenter)

    btn = QPushButton("Testar conexão HTTP")

    def do_http():
        try:
            r = requests.get("https://httpbin.org/get", timeout=5)
            QMessageBox.information(win, "Sucesso", f"HTTP {r.status_code}")
        except Exception as e:
            QMessageBox.critical(win, "Erro", str(e))

    btn.clicked.connect(do_http)
    layout.addWidget(lbl)
    layout.addWidget(btn)

    win.setCentralWidget(central)
    win.resize(500, 250)
    win.show()

    sys.exit(app.exec())  # Mantém a janela aberta

if __name__ == "__main__":
    main()
