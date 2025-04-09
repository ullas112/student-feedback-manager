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

def generate_report(total_entries, feedback_messages, report_file):
    """Generate a feedback report and save it to a file."""
    with open(report_file, 'w') as file:
        file.write("Feedback Report\n")
        file.write("====================\n")
        file.write(f"Total Feedback Entries: {total_entries}\n\n")
        file.write("Feedback Messages:\n")
        for message in feedback_messages:
            file.write(f"- {message}\n")
    print(f"Report generated and saved to '{report_file}'.")

def main():
    input_file_path = "student_feedback.txt"
    report_file_path = "feedback_report.txt"
    
    feedback_lines = read_feedback(input_file_path)
    
    if feedback_lines:
        total_entries, feedback_messages = summarize_feedback(feedback_lines)
        generate_report(total_entries, feedback_messages, report_file_path)

if __name__ == "__main__":
    main()
