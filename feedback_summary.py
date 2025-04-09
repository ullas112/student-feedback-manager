def read_feedback(file_path):
    """Read feedback from the specified file."""
    try:
        with open(file_path, 'r') as file:
            feedback_lines = file.readlines()
        return feedback_lines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return []

def summarize_feedback(feedback_lines):
    """Summarize the feedback entries."""
    total_entries = len(feedback_lines) - 1  # Exclude the header line
    feedback_messages = [line.strip() for line in feedback_lines[1:]]  # Skip the header
    return total_entries, feedback_messages

def display_summary(total_entries, feedback_messages):
    """Display the summary of feedback."""
    print(f"Total Feedback Entries: {total_entries}")
    print("\nFeedback Messages:")
    for message in feedback_messages:
        print(f"- {message}")

def main():
    file_path = "student_feedback.txt"
    feedback_lines = read_feedback(file_path)
    
    if feedback_lines:
        total_entries, feedback_messages = summarize_feedback(feedback_lines)
        display_summary(total_entries, feedback_messages)

if __name__ == "__main__":
    main()
