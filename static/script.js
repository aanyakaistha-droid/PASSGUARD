
const passwordInput = document.getElementById("password");

const toggleButton = document.getElementById("togglePassword");

const strengthText = document.getElementById("strengthText");

const strengthFill = document.getElementById("strengthFill");


// SHOW / HIDE PASSWORD

toggleButton.addEventListener("click", function () {

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleButton.textContent = "HIDE";
    } else {
        passwordInput.type = "password";
        toggleButton.textContent = "SHOW";
    }

});


// CHECK PASSWORD AS USER TYPES

passwordInput.addEventListener("input", function () {

    const password = passwordInput.value;

    let score = 0;

    // Check password requirements

    const checks = [
        [password.length >= 8, "lengthCheck"],
        [/[A-Z]/.test(password), "upperCheck"],
        [/[a-z]/.test(password), "lowerCheck"],
        [/[0-9]/.test(password), "numberCheck"],
        [/[^A-Za-z0-9]/.test(password), "specialCheck"]
    ];

    checks.forEach(function (check) {

        const element = document.getElementById(check[1]);

        if (check[0]) {
            score++;
            element.textContent = "✓ " + element.textContent.substring(2);
            element.classList.add("passed");
        } else {
            element.textContent = "○ " + element.textContent.substring(2);
            element.classList.remove("passed");
        }

    });


    // Display strength

    let strength = "WEAK";
    let percentage = 20;

    if (score >= 5) {
        strength = "STRONG";
        percentage = 100;
    } else if (score >= 3) {
        strength = "MODERATE";
        percentage = 60;
    } else if (score >= 2) {
        percentage = 40;
    }

    if (password.length === 0) {
        strength = "NOT CHECKED";
        percentage = 0;
    }

    strengthText.textContent = strength;
    strengthFill.style.width = percentage + "%";

});

const copyButton = document.getElementById("copyButton");

if (copyButton) {

    copyButton.addEventListener("click", async function () {

        const password = document.getElementById(
            "generatedPassword"
        ).textContent;

        try {
            await navigator.clipboard.writeText(password);
            copyButton.textContent = "COPIED ✓";
        } catch (error) {
            copyButton.textContent = "COPY FAILED";
        }

    });

}


