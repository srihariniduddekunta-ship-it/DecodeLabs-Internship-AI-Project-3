courses = {
    "c": {
        "beginner": ["C Basics", "Variables and Data Types", "Operators in C"],
        "intermediate": ["Functions in C", "Arrays and Strings", "Pointers in C"],
        "advanced": ["Data Structures in C", "File Handling in C", "Dynamic Memory Allocation"]
    },

    "python": {
        "beginner": ["Python Basics", "Control Statements", "Functions in Python"],
        "intermediate": ["OOP in Python", "File Handling", "Python Projects"],
        "advanced": ["Django", "Flask", "Machine Learning with Python"]
    },
    "java": {
        "beginner": ["Core Java", "Variables and Loops", "Methods"],
        "intermediate": ["OOP in Java", "Collections Framework", "Exception Handling"],
        "advanced": ["Spring Boot", "JDBC", "Microservices"]
    },

    "data science": {
        "beginner": ["Data Science Basics", "Statistics Fundamentals"],
        "intermediate": ["Data Analysis with Python", "Data Visualization"],
        "advanced": ["Big Data Analytics", "Predictive Modeling"]
    }
}
topic = input("Enter topic: ").lower()
level = input("Enter level (beginner/intermediate/advanced): ").lower()

if topic in courses and level in courses[topic]:
    print("\nRecommended Courses:")
    for i, course in enumerate(courses[topic][level], start=1):
        print(f"{i}. {course}")
else:
    print("Sorry! No recommendations found.")