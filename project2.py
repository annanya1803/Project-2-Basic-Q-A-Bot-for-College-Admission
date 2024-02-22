import nltk
import random
from nltk.stem import PorterStemmer
from fuzzywuzzy import fuzz

nltk.download('punkt')  # Download NLTK punkt tokenizer if not downloaded already
stemmer = PorterStemmer()

welcome_msg = ["Hello! Welcome to college admission Bot. To exit the chatbot you can type 'bye'.", "Wecome to the Q&A Bot. How can I help you? and to exit the chatbot you can type 'bye'."]

farewell_msg = ['Thank you for having me.',"Bye! Thank you for acknowledging me in helping you."]

admission_responses = {
    "What is the admission procedure?": "The admission procedure involves filling out an application form, submitting required documents, giving a specific test that belongs to that specific college if they have , and possibly attending an interview.",
    "What are the admission requirements from the candidates?": "To apply for admission, you typically need to provide your academic transcripts, letters of recommendation, standardized test scores, and a personal statement.",
    "When is the deadline for admission?": "Admission deadlines vary by college and program. It's important to check the specific deadlines for the colleges you're interested in.",
    "Should we apply early for college admission?" : "Applying early can get complicated. There are several categories of early admission: Early Decision, Early Action, and Restricted Early Action.",
    "How do colleges evaluate the application?" : "Most colleges use a holistic review process. This means they consider your test scores, GPA, grade trend, strength of schedule, extracurricular participation, essays, letters of recommendation, etc.",
    "How can I make my application stand out?" : "As cliché as it may sound, the best way to make your application stand out is to be yourself.",
    "What are the benefits of applying to a college instead of a university?" : "Colleges offer you the shortest route to quality employment, and often the cost of a bachelor’s degree is less than that of the same program when applied at a university.",
    "How can I apply for scholarships?"  : "Many colleges offer scholarships for deserving students at the time of application. These scholarships are available for application right before the term begins.",
    "Will I have to undergo ragging in college as a fresher?" : "No. Almost all colleges around the world have strict guidelines concerning ragging.",
    "What will my campus life be like at college?" : "When you are in college, the campus life is fun and vibrant. You get to meet people from different cultural backgrounds.",
    "Can I change my major?" : "Yes. Most colleges provide you with the flexibility to change your principal if you are genuinely not performing well or feel that it is not the right fit for you.",
    "Can I apply for exchange programs?"  : "Yes. Many colleges have exchange programs, ranging from a week to an entire academic year."
}


# Memory to store context
context_memory = {
    "last_question": "",
    "last_response": ""
}

# Main interaction loop
def chat():
    print(random.choice(welcome_msg))
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(random.choice(farewell_msg))
            break
        response = responses(user_input)
        print("Bot:", response)



def responses(input_text):
    global context_memory
    input_text = input_text.lower()
    max_similarity = 0
    best_response = ""
    if fuzz.partial_ratio(input_text, context_memory["last_question"].lower()) > 70:
        return context_memory["last_response"]
    
    for question, answer in admission_responses.items():
        similarity = fuzz.partial_ratio(input_text, question.lower())
        if similarity > max_similarity:
            max_similarity = similarity
            best_response = answer
    if max_similarity > 70:  # Adjust threshold as needed
        context_memory["last_question"] = list(admission_responses.keys())[list(admission_responses.values()).index(best_response)]
        context_memory["last_response"] = best_response
        return best_response
    else:
        return "Sorry! I don't have this information. You can further check this query on a college portal."
    

# Run the chatbot
if __name__ == "__main__":
    chat()
