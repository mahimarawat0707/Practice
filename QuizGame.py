questions = [
    ("What is the capital of India?", "Delhi"),
    ("Which language is used for web development?", "Python"),
    ("2 + 2 =", "4")
]

score = 0
for ques, ans in questions:
    user_ans = input(ques + " ")
    if user_ans.lower() == ans.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {ans}\n")

print(f"🏁 You scored {score}/{len(questions)}")
