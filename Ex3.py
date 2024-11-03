import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Main window
app = tk.Tk()
app.title("Student Management System")



# Function to load student data from the file
def load_students_data(): 
    students = [] #  List to store student data
    with open(r"/Users/mac/Desktop/exercise/studentMarks.txt") as file:  # Open the file
        num_students = int(file.readline().strip())  # Read the number of students
        for line in file:
            parts = line.strip().split(',')   # Split the line into parts
            student_id = int(parts[0])         # Get the student ID part [0] means  the first part from  the list
            name = parts[1]                     # Get student name part
            coursework_marks = list(map(int, parts[2:5]))   #  Get coursework marks parts and convert them to integers
            exam_mark = int(parts[5])               # Get exam mark part [5]mean  the fifth part from the list
            total_coursework = sum(coursework_marks)    # Calculate total coursework marks
            total_score = total_coursework + exam_mark     # add  exam mark and course work then Calculate total score
            percentage = (total_score / 160) * 100     # now Calculate percentage
            grade = calculate_grade(percentage)   #  call the function to calculate grade
            students.append({     # Append means  to add a new element to the list 
                'id': student_id,    
                'name': name,             # Add student ID,name,exam,coursework,percentage,grade to the dictionary
                'coursework': total_coursework,  
                'exam': exam_mark,      
                'total': total_score,   
                'percentage': percentage,
                'grade': grade
            })
    return students, num_students  #  Return the list of students and the number of students because  we need to display the number of students in the label 

# Function to calculate grades based on percentage
def calculate_grade(percentage): 
    if percentage >= 70: #  if percentage is greater than or equal to 70 then grade is A
        return 'A'
    elif percentage >= 60:  # if not then  check if percentage is greater than or equal to 60 then grade is B
        return 'B'
    elif percentage >= 50:  # if not then  check if percentage is greater than or equal to 50 then grade is C
        return 'C'
    elif percentage >= 40:  # if not then  check if percentage is greater than or equal to 40 then grade is D
        return 'D' 
    else:
        return 'F'    #  if not then grade is F

# Function to display all students' results
def display_all_students():
    output_text.delete(1.0, tk.END)  #  Clear the text box 
    output_text.insert(tk.END, "All Student Records:\n\n") #  Insert the header 
    for student in students:
        output_student(student)
    avg_percentage = sum(s['percentage'] for s in students) / len(students)    #  Calculate average percentage
    output_text.insert(tk.END, f"\nTotal students: {len(students)}\n")    #  Insert the total number of students
    output_text.insert(tk.END, f"Class average percentage: {avg_percentage:.2f}%\n")  #   Insert the average percentage

# Function to print individual student record
def output_student(student): 
    output_text.insert(tk.END, f"Name: {student['name']}, ID: {student['id']}\n") #   Insert student name and ID from list
    output_text.insert(tk.END, f"Coursework: {student['coursework']}, Exam: {student['exam']}\n")  #   Insert coursework and exam marks from list 
    output_text.insert(tk.END, f"Total Score: {student['total']}, Percentage: {student['percentage']:.2f}%\n") #    Insert total score and percentage from the list 
    output_text.insert(tk.END, f"Grade: {student['grade']}\n\n") #    Insert grade from the list 

# Function to view a single student record
def view_single_student():
    search_id = id_entry.get()   #  Get the ID from the entry box when user inputs id number or name
    try:
        search_id = int(search_id) #   Convert the ID to integer
        student = next((s for s in students if s['id'] == search_id), None) #    Search for the student with the ID number
        output_text.delete(1.0, tk.END)   #  Clear the text box function 
        if student:
            output_student(student) #    If student is found then print the student record
        else:
            output_text.insert(tk.END, "Student not found.\n") #    If student is not found then print this  message
    except ValueError: 
        messagebox.showerror("Input Error", "Please enter a valid student ID.")  #   If user inputs something other than integer then show this error message

# Function to display the top student with heigher percentage
def show_top_student(): 
    top_student = max(students, key=lambda s: s['total']) #    Find the student with the highest total score 
    output_text.delete(1.0, tk.END)  #    Clear the text box 
    output_text.insert(tk.END, "Student with Highest Score:\n\n")  #    Insert the header 
    output_student(top_student)  #   and Print the student record with the highest score

# Function to display the lowest student
def show_bottom_student(): 
    bottom_student = min(students, key=lambda s: s['total'])  #    Find the student with the lowest total score 
    output_text.delete(1.0, tk.END)   #    Clear the text box 
    output_text.insert(tk.END, "Student with Lowest Score:\n\n")   #    Insert the header 
    output_student(bottom_student)   #   and Print the student record with the lowest score

# Function to open the add student window
def open_add_student_window():
    def add_student():
        try:
            student_id = int(id_entry_add.get())   #   take the ID from the entry box
            name = name_entry.get()    #    and then take the name from the entry box
            coursework_marks = list(map(int, coursework_entry.get().split(',')))   #   take the coursework marks from the entry box
            exam_mark = int(exam_entry.get())      #    and then take the exam mark from the entry box
            total_coursework = sum(coursework_marks)  #    calculate the total coursework marks
            total_score = total_coursework + exam_mark #     calculate the total score
            percentage = (total_score / 160) * 100   #     calculate the percentage
            grade = calculate_grade(percentage)   #     calculate the grade
            students.append({   #    Create a dictionary for the student record to be  added
                'id': student_id,  
                'name': name,
                'coursework': total_coursework,  #     Insert the total id,name,coursework marks,exam,total,percentage,grade 
                'exam': exam_mark,
                'total': total_score,
                'percentage': percentage,
                'grade': grade
            })
            messagebox.showinfo("Success", "Student added successfully!")  # display this massage when student is added in the list 
            add_window.destroy() #     close the add student window
        except Exception as e: 
            messagebox.showerror("Input Error", str(e))  #    If user inputs something other than integer then show this error message

    add_window = tk.Toplevel(app) # function for addind new student
    add_window.title("Add Student") 

    tk.Label(add_window, text="Student ID:").grid(row=0, column=0) #     Create a label for the ID
    id_entry_add = tk.Entry(add_window)  #     Create an entry box for the ID
    id_entry_add.grid(row=0, column=1) #       Placing the entry box in the window

    tk.Label(add_window, text="Name:").grid(row=1, column=0)  
    name_entry = tk.Entry(add_window)   #     Create an entry box for the name of students
    name_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Coursework Marks (comma separated):").grid(row=2, column=0)
    coursework_entry = tk.Entry(add_window)   #     Create an entry box for the coursework marks
    coursework_entry.grid(row=2, column=1) 

    tk.Label(add_window, text="Exam Mark:").grid(row=3, column=0)
    exam_entry = tk.Entry(add_window)    #     Create an entry box for the exam mark
    exam_entry.grid(row=3, column=1)

    add_button = tk.Button(add_window, text="Add Student", command=add_student)   #     Create a button to add the student
    add_button.grid(row=4, columnspan=2)  

# Function to open window and delete student from the list
def open_delete_student_window():
    def delete_student():  
        try:
            student_id = int(id_entry_delete.get())    #   take the ID from the entry box
            global students 
            students = [s for s in students if s['id'] != student_id] 
            messagebox.showinfo("Success", "Student deleted successfully!")   # display this massage when student is deleted from the list 
            delete_window.destroy()  #     close the delete student window
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid student ID.")   #    If user inputs something other than integer then show this error message
    
    delete_window = tk.Toplevel(app)  # function for deleting student
    delete_window.title("Delete Student") #      Create a window for deleting student
    
    tk.Label(delete_window, text="Student ID:").grid(row=0, column=0)   #     Create a label for the ID 
    id_entry_delete = tk.Entry(delete_window)   #     Create an entry box for the ID so that user input
    id_entry_delete.grid(row=0, column=1) 

    delete_button = tk.Button(delete_window, text="Delete Student", command=delete_student)    #     Creating a button to delete the student
    delete_button.grid(row=1, columnspan=2)

# Function to open the update student window
def open_update_student_window():
    def update_student():
        try:
            student_id = int(id_entry_update.get())     #   take the ID from the entry box
            student = next((s for s in students if s['id'] == student_id), None)   #   find the student with the given ID
            if student:
                student['name'] = name_entry_update.get() or student['name']    #   update the name of the student
                coursework_marks = list(map(int, coursework_entry_update.get().split(',')))    #  then update the coursework marks
                student['coursework'] = sum(coursework_marks) if coursework_marks else student['coursework'] 
                student['exam'] = int(exam_entry_update.get()) if exam_entry_update.get() else student['exam']     #   update the exam mark
                total_coursework = student['coursework']  
                total_score = total_coursework + student['exam'] #    calculate the total score by adding  coursework and exam marks
                percentage = (total_score / 160) * 100      #    calculate the percentage by dividing the total score by 160 and multiplying by 100
                student['percentage'] = percentage  if percentage <= 100 else 100  #    update the percentage in the student dictionary
                student['total'] = total_score   #    now update the total score in the student dictionary
                student['grade'] = calculate_grade(percentage) #     calculate the grade of the student
                messagebox.showinfo("Success", "Student updated successfully!")      #  display this massage when student is updated from the list 
                update_window.destroy() # close  the window 
            else:
                messagebox.showerror("Error", "Student not found.")   #   if student is not found then show this error message
        except Exception as e:
            messagebox.showerror("Input Error", str(e))    #   if user inputs something other than integer then show this error message

    update_window = tk.Toplevel(app)
    update_window.title("Update Student")  # Create a window for updating student

    tk.Label(update_window, text="Student ID:").grid(row=0, column=0)   # Create a label for the ID 
    id_entry_update = tk.Entry(update_window)    # Create an entry box for the ID so that user input
    id_entry_update.grid(row=0, column=1)

    tk.Label(update_window, text="New Name:").grid(row=1, column=0)    # Create a label for the name 
    name_entry_update = tk.Entry(update_window)     # Create an entry box for the name so that user input
    name_entry_update.grid(row=1, column=1)

    tk.Label(update_window, text="New Coursework Marks (comma separated):").grid(row=2, column=0)     # Create a label for the coursework marks 
    coursework_entry_update = tk.Entry(update_window)      # Create an entry box for the coursework marks so that user input
    coursework_entry_update.grid(row=2, column=1)

    tk.Label(update_window, text="New Exam Mark:").grid(row=3, column=0)      # Create a label for the exam mark 
    exam_entry_update = tk.Entry(update_window)        # Create an entry box for the exam mark so that user input
    exam_entry_update.grid(row=3, column=1) 

    update_button = tk.Button(update_window, text="Update Student", command=update_student)     # Creating a button to update the student
    update_button.grid(row=4, columnspan=2)     #     Creating a button to update the student

# Function to open the sort students window
def open_sort_students_window(): 
    def sort_students(): 
        if sort_var.get() == "Ascending":  #    making an option, if the sort option is ascending
            students.sort(key=lambda s: s['total']) #  then sort the students in ascending order
        elif sort_var.get() == "Descending":
            students.sort(key=lambda s: s['total'], reverse=True)  #  then sort the students in descending order
        messagebox.showinfo("Success", "Students sorted successfully!")   #  display this massage when students are sorted
        sort_window.destroy() #  close  the window 

    sort_window = tk.Toplevel(app)
    sort_window.title("Sort Students")   # now Create a window for sorting students 

    sort_var = tk.StringVar()   #  Create a variable to hold the sort option
    tk.Radiobutton(sort_window, text="Ascending", variable=sort_var, value="Ascending").pack()  #   Creating a radio button for the ascending 
    tk.Radiobutton(sort_window, text="Descending", variable=sort_var, value="Descending").pack() # descending option

    sort_button = tk.Button(sort_window, text="Sort", command=sort_students)   #  Creating a button to sort the students
    sort_button.pack()    #  closing  the window 

# Load student data when the application starts
students, num_students = load_students_data()   #  load the student data

# GUI Layout
frame = tk.Frame(app)
frame.pack(pady=10)

# Creating buttons individually
button_display_all = tk.Button(frame, text="Display All",bg='#f9ffbf' ,command=display_all_students)   #  Creating a button to display all students
button_display_all.grid(row=0, column=0, padx=10, pady=10)

button_top_student = tk.Button(frame, text="Top Student", bg='#d8ffcf' , command=show_top_student)    #  Creating a button to display the top student
button_top_student.grid(row=0, column=1, padx=10, pady=10)

button_lowest_student = tk.Button(frame, text="Lowest Student", bg='#e39d9d' ,command=show_bottom_student)   #   Creating a button to display the lowest student
button_lowest_student.grid(row=0, column=2, padx=10, pady=10)

button_add_student = tk.Button(frame, text="Add Student", bg='#bfeeff',command=open_add_student_window)    #  Creating a button to add a student
button_add_student.grid(row=1, column=0, padx=10, pady=10)

button_delete_student = tk.Button(frame, text="Delete Student",bg="#ff5454" ,command=open_delete_student_window)    #  Creating a button to delete a student
button_delete_student.grid(row=1, column=1, padx=10, pady=10)

button_update_student = tk.Button(frame, text="Update Student",bg='#ffd1ba' ,command=open_update_student_window)     #  Creating a button to update a student
button_update_student.grid(row=1, column=2, padx=10, pady=10)

button_sort_students = tk.Button(frame, text="Sort Students", bg='#baffde' , command=open_sort_students_window)     #  Creating a button to sort the students
button_sort_students.grid(row=2, column=0, padx=10, pady=10)

# Search ID entry
id_label = tk.Label(frame, text="Search by ID:")    #  Creating a label for the search entry
id_label.grid(row=3, column=0)

id_entry = tk.Entry(frame, bg="#fffadb")     #  Creating an entry for the search
id_entry.grid(row=3, column=1)

# View Student button placed to the right of Search ID entry
view_button = tk.Button(frame, text="View Student", bg='#ffdbe7' ,command=view_single_student)     #  Creating a button to view a student
view_button.grid(row=3, column=2, padx=10)

output_text = tk.Text(app, bg='#f1e3fa' ,width=80, height=20)      #  Creating a text box to display the output
output_text.pack(pady=10)

# Run the application
app.mainloop()
