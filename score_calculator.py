def calculate_average(scores):
    """Calculate the average of a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def main():
    print("Welcome to the Student Score Calculator!")
    
    # Get the number of scores to be entered
    while True:
        try:
            num_scores = int(input("Enter the number of scores you want to input: "))
            if num_scores <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    scores = []
    
    # Collect scores from the user
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score {i + 1}: "))
                if score < 0:
                    print("Please enter a non-negative score.")
                    continue
                scores.append(score)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Calculate the average score
    average_score = calculate_average(scores)
    
    # Display the result
    print(f"The average score is: {average_score:.2f}")

if __name__ == "__main__":
    main()
