import pgzrun

TITLE = "quiz master"
WIDTH = 870
HEIGHT = 650
marquee_message = ""
question_index = 0
question_count = 0
time_left = 10
question_file_name = "questions.txt"

marquee_box = Rect(0, 0, 880, 80)
question_box = Rect(0, 0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []

def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, "navy blue")
    screen.draw.filled_rect(skip_box, "dark green")
    
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "dark orange")
    marquee_message = "Welecome to Quiz Master..."
    marquee_message = marquee_message + f"Q:{question_index} of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color = "white")
    screen.draw.textbox(str(time_left), timer_box, color = "white", shadow = (0.5, 0.5), scolor = "dim grey")
    screen.draw.textbox("Skip", skip_box, color = "black", angle = -90)
    #screen.draw.textbox(questions[0].strip(), question_box, color = "white", shadow = (0.5, 0.5), scolor = "dim gray")

    index = 1 
    #for answer_box in answer_boxes:
        #screen.draw.textbox(question[index].strip, answer_box, color = "black")
        #index = index + 1

def update():
    move_marquee()

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

pgzrun.go()