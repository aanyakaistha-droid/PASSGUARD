# PASSGUARD — Password Security Analyzer

### Video Demo: <ADD YOUR VIDEO URL HERE>

### Description

PASSGUARD is a web-based password security analyzer developed as my CS50x final project. The goal of this project is to help users understand password security and encourage better password habits through an interactive and easy-to-use interface.

Passwords are an important part of digital security, but many people still use short, predictable, or easily guessed passwords. PASSGUARD addresses this problem by evaluating password strength, identifying missing security requirements, providing improvement suggestions, and offering a password generator to help users create stronger passwords.

The application combines Python and Flask for its backend functionality with HTML, CSS, and JavaScript for its frontend interface. I chose Flask because it is lightweight and beginner-friendly while still allowing me to build a functional web application.

### Features

**1. Password Strength Analysis**

Users can enter a password and analyse its strength. The application checks five basic security requirements:

- Length of at least 8 characters.
- Presence of an uppercase letter.
- Presence of a lowercase letter.
- Presence of a number.
- Presence of a special character.

Each requirement contributes to the password's overall score. Based on the score, the password is classified as Weak, Moderate, or Strong. If requirements are missing, the application displays suggestions to help improve the password.

**2. Live Password Strength Indicator**

PASSGUARD includes a live strength indicator that updates as the user types. JavaScript checks the password against the five requirements and updates the strength label and progress bar without requiring the user to submit the form each time.

A checklist also displays which requirements have been fulfilled, making the evaluation easier to understand.

**3. Show and Hide Password**

The password input includes a show/hide option. This allows users to reveal their password when needed or conceal it while entering it.

**4. Secure Password Generator**

The application also includes a password generator. Users can choose a desired password length, and the application generates a random password using its dedicated Python generator module.

This feature provides an alternative for users who do not want to create their own passwords.

**5. Copy Generated Password**

Users can copy the generated password using a copy button. The application provides feedback when the password has been copied successfully or when copying fails.

### Files and Their Functionality

The project is organised into separate files to keep the code manageable and make each component responsible for a specific task.

- **app.py:** This is the main Flask application. It defines the routes, handles requests from the browser, connects the frontend with the Python modules, and renders the HTML template.

- **checker.py:** Contains the password strength evaluation logic. It checks the password against the five security requirements, calculates a score, determines the strength category, and generates feedback.

- **generator.py:** Contains the password generation functionality. It generates random passwords according to the length selected by the user.

- **templates/index.html:** Contains the structure of the web application. It includes the password input, show/hide control, live strength indicator, checklist, analysis button, and password generator interface.

- **static/style.css:** Controls the visual appearance of PASSGUARD. It defines the dark cyber-inspired theme, colours, typography, spacing, input fields, buttons, cards, and other styling elements.

- **static/script.js:** Handles frontend interactions, including the show/hide password feature, live password evaluation, checklist updates, progress bar, and copying generated passwords.

- **README.md:** Documents the project, its features, structure, and implementation.

### Design Choices

I chose a cyber-security-inspired visual theme to match the purpose of the application. The interface uses a dark background with bright green accents to create a security dashboard aesthetic.

I also decided to separate the backend logic from the frontend interface. Keeping password analysis and generation in separate Python files makes the application easier to understand, maintain, and expand.

JavaScript was used for live feedback because I wanted users to see password requirements being fulfilled as they type instead of receiving feedback only after submitting the form.

Another important design decision was to include a password generator alongside the analyzer. Rather than simply telling users that their passwords are weak, PASSGUARD also provides a way to create a stronger alternative.

### Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

### What I Learned

Building PASSGUARD helped me understand how different parts of a web application work together. I gained experience with Python functions, conditional statements, string operations, Flask routes, HTML templates, CSS styling, and JavaScript event listeners.

I also learned how to organise a project into multiple files and connect frontend interactions with backend functionality.

One of the main challenges was integrating the live strength checker, password analysis, and password generator into one application while keeping the interface consistent.

Overall, PASSGUARD allowed me to apply concepts learned throughout CS50x to build a practical project focused on an everyday cybersecurity problem.
