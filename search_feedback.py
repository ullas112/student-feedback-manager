def read_feedback(file_path):
    """Read feedback from the specified file."""
    try:
        with open(file_path, 'r') as file:
            feedback_lines = file.readlines()
        return feedback_lines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return []

def search_feedback(feedback_lines, student_name):
    """Search for feedback entries by student name."""
    matching_feedback = []
    for line in feedback_lines[1:]:  # Skip the header
        if student_name.lower() in line.lower():  # Case-insensitive search
            matching_feedback.append(line.strip())
    return matching_feedback

def display_feedback(matching_feedback):
    """Display the matching feedback entries."""
    if matching_feedback:
        print("\nMatching Feedback Entries:")
        for feedback in matching_feedback:
            print(f"- {feedback}")
    else:
        print("No feedback found for the specified student.")

def main():
    input_file_path = "student_feedback.txt"
    feedback_lines = read_feedback(input_file_path)
    
    if feedback_lines:
        student_name = input("Enter the student's name to search for feedback: ")
        matching_feedback = search_feedback(feedback_lines, student_name)
        display_feedback(matching_feedback)

if __name__ == "__main__":
    main()
