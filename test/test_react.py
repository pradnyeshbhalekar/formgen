import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from package.react_generator import generate_react_form

schema = [
  {
    "label": "Full Name",
    "type": "text",
    "name": "fullName",
    "placeholder": "Enter your full name",
    "required": True,
    "maxLength": 50
  },
  {
    "label": "Email Address",
    "type": "email",
    "name": "email",
    "placeholder": "Enter your email",
    "required": True
  },
  {
    "label": "Password",
    "type": "password",
    "name": "password",
    "placeholder": "Create a password",
    "required": True,
    "minLength": 8
  },
  {
    "label": "Confirm Password",
    "type": "password",
    "name": "confirmPassword",
    "placeholder": "Re-enter your password",
    "required": True,
    "minLength": 8
  },
  {
    "label": "Age",
    "type": "number",
    "name": "age",
    "min": 16,
    "max": 60,
    "required": True
  },
  {
    "label": "GitHub Profile",
    "type": "url",
    "name": "github",
    "placeholder": "https://github.com/username",
    "required": False
  },
  {
    "label": "Gender",
    "type": "radio",
    "name": "gender",
    "options": ["Male", "Female", "Other"],
    "required": True
  },
  {
    "label": "Dietary Preference",
    "type": "select",
    "name": "diet",
    "options": ["None", "Vegetarian", "Vegan", "Gluten-Free"],
    "required": True
  },
  {
    "label": "Agree to Terms and Conditions",
    "type": "checkbox",
    "name": "terms",
    "required": True
  }
]



# Output path
output_path = "example/GeneratedForm.jsx"
generate_react_form(schema, output_path)
