import streamlit as st
import random
import string
import datetime

# Function to generate random passwords
def generate_password(length, num_passwords):
    today = str(datetime.date.today())

    # Create a list of letters, numbers, and symbols
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Create a list of all the characters
    all_characters = letters_lower + letters_upper + numbers + symbols

    # Create a list of passwords
    passwords = []

    # Create a for loop to generate the passwords
    for _ in range(num_passwords):
        password = "".join(random.sample(all_characters, length))
        passwords.append(password)

    # Save the passwords to a text file
    with open(f"passwords-{today}.txt", "w") as f:
        for password in passwords:
            f.write(password + "\n")

    return passwords

# Function to generate HTML code for the "Copy" button
def copy_button(password):
    return f"""
    <button onclick="copyToClipboard('{password}')">Copy</button>
    <script>
        function copyToClipboard(text) {{
            var textarea = document.createElement("textarea");
            textarea.value = text;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand("copy");
            document.body.removeChild(textarea);
            alert("Password copied to clipboard!");
        }}
    </script>
    """

# Streamlit UI
st.title("Random Password Generator")
st.write("Welcome to the random password generator!")

# Ask user for password length
length = st.slider("Select the password length:", min_value=8, max_value=30, value=12)

# Ask user for the number of passwords
num_passwords = st.slider("Select the number of passwords:", min_value=1, max_value=10, value=5)

# Generate passwords on button click
if st.button("Generate Passwords"):
    generated_passwords = generate_password(length, num_passwords)
    st.success("Passwords generated successfully!")

    # Display the generated passwords with "Copy" button
    st.subheader("Generated Passwords:")
    for password in generated_passwords:
        st.write(password, unsafe_allow_html=True)
        st.markdown(copy_button(password), unsafe_allow_html=True)
