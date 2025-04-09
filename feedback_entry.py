import os

def collect_feedback():
    print("Welcome to the Student Feedback System!")
    
    # Collecting student information
    student_name = input("Please enter your name: ")
    student_id = input("Please enter your student ID: ")
    
    # Collecting feedback
    feedback = input("Please provide your feedback: ")
    
    # Create a feedback entry
    feedback_entry = f"Name: {student_name}, ID: {student_id}, Feedback: {feedback}\n"
    
    # Save feedback to a file
    save_feedback(feedback_entry)
    
    print("Thank you for your feedback!")

def save_feedback(entry):
    # Define the file path
    file_path = "student_feedback.txt"
    
    # Check if the file exists, if not create it
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("Student Feedback:\n")
    
    # Append the feedback entry to the file
    with open(file_path, 'a') as file:
        file.write(entry)

if __name__ == "__main__":
    collect_feedback()
