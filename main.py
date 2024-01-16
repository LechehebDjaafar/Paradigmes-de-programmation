from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5.QtCore import QMargins
from analyse import Analyse
from unification import Unification
from equation import Equation

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(" Paradigmes de Programmation - TP 4")

        # إعداد واجهة المستخدم
        g_layout = QVBoxLayout()
        self.ops_layout = QVBoxLayout()

        ops_label = QLabel("Inserer les deux termes:", self)
        g_layout.addWidget(ops_label)

        self.ops_left_inputs = []
        self.ops_right_inputs = []

        ops_widget = QWidget(self)
        ops_widget.setLayout(self.ops_layout)
        g_layout.addWidget(ops_widget)

        # إضافة حقول إدخال جديدة لإدخال المصطلحات
        self.insert_new_op()

        # زر التحقق والتفعيل/التعطيل بناءً على محتوى الحقول
        self.validate_btn = QPushButton('&Valider', self)
        self.validate_btn.setFixedWidth(80)
        self.validate_btn.setDisabled(True)
        self.validate_btn.clicked.connect(self.on_validate)
        g_layout.addWidget(self.validate_btn)

        # زر الخروج
        exit_btn = QPushButton('&Exit', self)
        exit_btn.setFixedWidth(80)
        exit_btn.clicked.connect(self.on_exit)
        g_layout.addWidget(exit_btn)

        # عنوان النصوص الموحدة
        unification_label = QLabel("La table de l'unification:", self)
        self.unification_holder = QPlainTextEdit()
        self.unification_holder.setReadOnly(True)
        g_layout.addWidget(unification_label)
        g_layout.addWidget(self.unification_holder)

        g_widget = QWidget(self)
        g_widget.setLayout(g_layout)

        self.setCentralWidget(g_widget)

        # ربط حدث التغيير في الحقول بفحص الحقول
        for left_input, right_input in zip(self.ops_left_inputs, self.ops_right_inputs):
            left_input.textChanged.connect(self.check_fields)
            right_input.textChanged.connect(self.check_fields)

    def insert_new_op(self, dropable=False):
        # إضافة حقل إدخال للمصطلح الأيسر والمصطلح الأيمن
        self.ops_left_inputs.append(QLineEdit(self))
        self.ops_right_inputs.append(QLineEdit(self))

        op_layout = QHBoxLayout()
        op_layout.setContentsMargins(QMargins())
        op_layout.addWidget(self.ops_left_inputs[-1])
        op_layout.addWidget(QLabel("=", self))
        op_layout.addWidget(self.ops_right_inputs[-1])

        op_widget = QWidget(self)
        op_widget.setLayout(op_layout)
        self.ops_layout.addWidget(op_widget)

    def check_fields(self):
        # فحص حالة الحقول وتفعيل/تعطيل زر التحقق بناءً على محتوى الحقول
        enable_button = all(left.text() and right.text() for left, right in zip(
            self.ops_left_inputs, self.ops_right_inputs))
        self.validate_btn.setDisabled(not enable_button)

    def on_validate(self):
        # عند الضغط على زر "Valider"
        unification = Unification([])

        for left_input, right_input in zip(self.ops_left_inputs, self.ops_right_inputs):
            if not left_input.text() or not right_input.text():
                continue

            liste_gauche = Analyse.analyse_lexical(left_input.text())
            liste_droite = Analyse.analyse_lexical(right_input.text())

            liste_gauche = Analyse.termes_separateur(liste_gauche)
            liste_droite = Analyse.termes_separateur(liste_droite)

            liste_gauche = Analyse.analyse_syntaxique(liste_gauche)
            liste_droite = Analyse.analyse_syntaxique(liste_droite)

            if len(liste_gauche) != len(liste_droite):
                continue

            liste_min = min(len(liste_gauche), len(liste_droite))

            for gauche, droite in zip(liste_gauche[:liste_min], liste_droite[:liste_min]):
                equation = Equation(gauche, droite)
                unification.equations.append(equation)

        # عرض نتائج الموحدة في مربع النص
        self.unification_holder.setPlainText(unification.moteur_unification())

    def on_exit(self):
        # عند الضغط على زر "Exit"
        reply = QMessageBox.question(
            self, 'Exit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            app.quit()


# إعداد التطبيق وعرض النافذة
app = QApplication(sys.argv)
window = MainWindow()
window.resize(750, 500)
window.move(80, 100)
window.show()

app.exec_()
