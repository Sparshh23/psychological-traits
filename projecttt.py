def print_question(question):
    """PRINT THE QUESTION AND PROMPT FOR USER RESPONSE."""
    print(question)
    response = input("Enter your answer (A/B/C/D): ")
    return response.upper()

def assess_personality():
    """Assess the user's personality traits based on their responses."""
    print("Welcome to the Personality Assessment Quiz!")
    print("Please answer the following questions:")
    responses = []
    
    
    questions = ["Q1: What is your preferred way of spending weekends?",
                 "Q2: How do you handle stressful situations?",
                 "Q3: What type of movies do you enjoy the most?",
                 "Q4: How do you handle criticism or negative feedback?"]
    
    options = ["A. Going out with friends", "B. Staying at home and relaxing",
               "C. Engaging in physical activities", "D. Pursuing a hobby",
               "A. Getting angry or upset", "B. Taking deep breaths and trying to calm down",
               "C. Seeking support from others", "D. Finding a solution to the problem",
               "A. Action/Adventure", "B. Romance/Drama", "C. Comedy", "D. Sci-Fi/Fantasy",
               "A. Getting defensive or argumentative", "B. Taking feedback positively and trying to improve",
               "C. Ignoring the feedback", "D. Seeking clarification and understanding"]
    
    
    for i in range(len(questions)):
        print_question(questions[i])
        response = print_question(options[i*4] + "\n" + options[i*4 + 1] +
       "\n" + options[i*4 + 2] + "\n" + options[i*4 + 3])
        responses.append(response)
    
    
    trait_A = responses.count("A")
    trait_B = responses.count("B")
    trait_C = responses.count("C")
    trait_D = responses.count("D")
    
    
    print("Results:")
    print(f"Trait A: {trait_A} out of {len(responses)} responses")
    print(f"Trait B: {trait_B} out of {len(responses)} responses")
    print(f"Trait C: {trait_C} out of {len(responses)} responses")
    print(f"Trait D: {trait_D} out of {len(responses)} responses")

if __name__ == "__main__":
    assess_personality()
