import random

def quiz():
    score = 0
    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer.strip().lower() == q["answer"].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {q['answer']}")
            score -= 1
    print(f"\n🎉 Quiz Over! You scored {score}/{len(questions)}.")
            
            
print ("If you type correct answer then '+1' and if you type wrong then '-1'\nokay then let's start . ")
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "In which year did India gain independence?", "answer": "1947"},
    {"question": "What is the chemical symbol for Gold?", "answer": "Au"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "How many continents are there?", "answer": "7"},
    {"question": "Who is known as the 'Father of Computers'?", "answer": "Charles Babbage"},
    {"question": "What is the smallest prime number?", "answer": "2"},
]
random.shuffle(questions)
quiz()
