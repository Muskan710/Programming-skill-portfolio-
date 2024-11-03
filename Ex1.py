import random
import tkinter as tk
from tkinter import messagebox

# fllowing are Function to display quiz selection menu
def displayMenu():
    global root
    root = tk.Tk()
    root.title("Math Quiz") 

    label = tk.Label(root, text="Choose your LEVEL", font=("calibri", 18)) #  label for the menu (heading)
    label.pack(pady=10)  # adding some space around the label (heading)

    easy_button = tk.Button(root, text="1. Easy", width=20,font=("Times New Roman",14), command=lambda: startQuiz(1)) # a button for easy level
    easy_button.pack(pady=5) # giving some  space between the buttons 

    moderate_button = tk.Button(root, text="2. Moderate", width=20, font=("Times New Roman",14) ,command=lambda: startQuiz(2)) #  a button for moderate level
    moderate_button.pack(pady=5) #  giving some  space between the buttons 

    advanced_button = tk.Button(root, text="3. Advanced", width=20, font=("Times New Roman",14) ,command=lambda: startQuiz(3))  #  a button for advanced level
    advanced_button.pack(pady=5)  #  giving some  space between the buttons 

    root.mainloop() # to  start the main loop of the GUI 
   
    # Function to start the quiz
# Function to generate random integers based on level the user will choose 
def randomInt(difficul): 
    if difficul == 1:  # if difficul (level) is 1 then return random integer between 1 and 10.
        return random.randint(1, 9) 
    elif difficul == 2:   # if difficul (level) is 2 then return random integer between 2 digit number.
        return random.randint(10, 99)
    elif difficul == 3:    # if difficul (level) is 3 then return random integer between 3 digit number.
        return random.randint(1000, 9999) 

# This Function is use to decide random operation (addition or subtraction
def decide_Operation():
    return random.choice(['+', '-']) #  it will return  (give) random choice between '+' and '-'

# This Function will check user's answer and provide feedback 
def ifCorrect(useranswer, correct_answer, attempt):     #  useranswer is the answer given by user, correct_answer is the correct answer and attempt is the number
    try:
        useranswer = int(useranswer) #   convert user's answer to integer
        if useranswer == correct_answer:  # if user's answer is equal to correct answer then  fllowing massage will be displayed.
            if attempt == 1: #  if it is first attempt then display 
                messagebox.showinfo("Result", "Correct! You got 10 points.") #  this massage if answer is coorrect 
                return 10 #  and giving 10 points 
            else:  # if it is not first attempt then display  
                messagebox.showinfo("Result", " You are Correct on second attempt. You got 5 points.")  # display this massage if  answer was correct  on second attempt.
                return 5  #  and giving 5 points 
        else:   # if user's answer is not equal to correct answer then fllowing massage will be displayed
            messagebox.showinfo("Result", " Your answer is Incorrect. Try again.") #  display this massage if answer is incorrect
            return 0  #  and giving 0 points 
    except ValueError:  #  if user's answer is not integer then display fllowing massage
        messagebox.showerror("Error", "Invalid input. Please Enter a number.") 
        return 0   #  and giving 0 points 

# This Function is use to display any questions and manage score
def display_Problem(num1, num2, operation, problem_number, score):   # num1 and num2 are the numbers to be used as a question, operation is to add or subtract , problem_number  and score is the current score
    problem_frame = tk.Toplevel(root) 
    problem_frame.title(f"Question {problem_number + 1}") 

    def checkAnswer(attempt): #   this function will check user's answer and provide feedback 
        answer = entry.get() #   get the answer from entry box
        correct_answer = eval(f"{num1} {operation} {num2}")  # it  will calculate the correct answer
        points = ifCorrect(answer, correct_answer, attempt)  # again  it will check user's answer and provide feedback 
        if points > 0 or attempt == 2:  #  if user's answer is correct or it is second attempt then 
            problem_frame.destroy()   #   it will destroy the current window
            score.append(points)   # and so  add the points to the list
            if len(score) < 10: #   if the length of the list is less than 10 then 
                askQuestion(len(score), score)   #  it will call the function to ask next question
            else:   #  if the length of the list is 10 then 
                displayResults(sum(score))   #  it will call the function to display the results

    question_label = tk.Label(problem_frame, text=f"{num1} {operation} {num2} =", font=("Arial", 14)) #   it will display the question
    question_label.pack(pady=10) #   it will add some space between the question and entry box

    entry = tk.Entry(problem_frame, width=10) #    it will create entry box
    entry.pack(pady=5)  #   it will add some space between entry box and button

    submit_button = tk.Button(problem_frame, text="Check", command=lambda: checkAnswer(1))  #   it will create button to check the answer
    submit_button.pack(pady=5)   #   it will add some space between button and retry button

    retry_button = tk.Button(problem_frame, text="Retry", command=lambda: checkAnswer(2))   #   it will create button to retry the answer
    retry_button.pack(pady=5)  #    it will add some space between button and retry button

# Function to ask a new question
def askQuestion(problem_number, score):   #  problem_number is the current question number and score is the current score
    difficulty = int(difficulty_level.get()) #   it will get the difficulty level from the variable
    num1, num2 = randomInt(difficulty), randomInt(difficulty)  #   it will generate two random numbers based on  level
    operation = decide_Operation()   #   it will decide the operation to be used in the question (add or subtract)
    if operation == '-' and num1 < num2:  # it will Ensure  that there is no negative results
        num1, num2 = num2, num1 #    it will check the numbers if num1 is less than num2
    display_Problem(num1, num2, operation, problem_number, score) #    it will call the function to display the question

# Function to display final score and rank
def displayResults(final_score): # to display final score 
    frame_result = tk.Toplevel(root)  # it will create a new window
    frame_result.title("Results of the Quiz") # setting  the title of the window

    result_label = tk.Label(frame_result, text=f"Your final score is: {final_score}/100", font=("Arial", 16)) # label  to display the final score
    result_label.pack(pady=10)

    if final_score > 90:  # if the final score is more than 90 then 
        rank = "A+"  #  it will assign rank A+
    elif final_score > 80:   # if the final score is more than 80 then 
        rank = "A"   #  it will assign rank A
    elif final_score > 70:    # if the final score is more than 70 then 
        rank = "B"    #  it will assign rank B
    elif final_score > 60:     # if the final score is more than 60 then 
        rank = "C"      #  it will assign rank C
    else:    # otherwise if the final score is less than 60 then 
        rank = "D"       #  it will assign rank D
     
    score_label = tk.Label(frame_result, text=f"Rank: {rank}", font=("Arial", 14))  # label to display the rank / scores
    score_label.pack(pady=10)   # it will add some space between rank and exit button

    play_again_button = tk.Button(frame_result, text="Wanna Play Again", command=lambda: [frame_result.destroy(), startQuiz(int(difficulty_level.get()))])   # this is a button to play again
    play_again_button.pack(pady=10)   #  adding some space between button and exit button

    exit_button = tk.Button(frame_result, text="Exit", command=root.quit)   # this is a button to exit the quiz
    exit_button.pack(pady=5)   #  adding some space between button and exit button

# Function to start the quiz with selected difficulty
def startQuiz(difficulty):    # this to  is the selecte the difficulty level
    global difficulty_level #  it will get the level from the variable
    difficulty_level = tk.StringVar()   # it will create a variable to store the difficulty level
    difficulty_level.set(str(difficulty))   #  it will set the difficulty level to the variable
    askQuestion(0, [])    # this  will call the function to ask the first question

# Main program entry point
if __name__ == "__main__":   # this is the main program entry point , here we  will call the startQuiz function.
    displayMenu()    # this will call the function to display the menu





