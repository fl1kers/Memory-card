from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])
from MemoryCard import*
from menu_window import*

class Question():
    def __init__(self, question, right_answer,wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
questions = [
    Question("Однакова кількість звуків і букв у кожному слові рядка", "п'ятниць, їстоньки, яблунька","якість, кукурудза, український","гайок, об'єднування, сьогодення","серйозний, щебечуть, джміль"),
    Question("Однакова кількість звуків і букв у кожному слові рядка","тріщить, сум’яття, дев’ять","сьогодні, балтієць, дзижчати","тюбетейка, віджити, щипати","водяний, м’якенький, щиглик")
]

radio_buttons = [rb_ans1,rb_ans2,rb_ans3,rb_ans4]

def new_questin():
    q = choice(questions)
    lb_question.setText(q.question)
    lb_right_result.setText(q.right_answer)
    radio_buttons[0].setText(q.right_answer)    
    radio_buttons[1].setText(q.wrong_answer1)  
    radio_buttons[2].setText(q.wrong_answer2)  
    radio_buttons[3].setText(q.wrong_answer3) 
    shuffle(radio_buttons)


new_questin()

def click_ok():
    if btn_answer.text() =="Відповісти":
        group.setExclusive(False)
        for answer in radio_buttons:
            if answer.isChecked():
                if answer.text() == lb_right_result.text():
                    lb_result.setText("Правильно!")
                else:
                    lb_result.setText("Неправильно!")
                break
        group.setExclusive(True)
        gb_question.hide()
        gb_answer.show()
        btn_answer.setText("Наступне запитання")
    else:
        new_questin()
        gb_answer.hide()
        gb_question.show()
        btn_answer.setText("Відповісти")

btn_answer.clicked.connect(click_ok)

def menu_generation():s
    win.hide()
    menu_win.show()

btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    win.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question1.clear()
    le_question2.clear()
    le_question3.clear()
    le_question4.clear()

btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(),le_question1.text(), le_question2.text(),le_question3.text(), le_question4.text())
    questions.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)

app.exec_()

