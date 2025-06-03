#!/usr/bin/env python3
"""
Script to create a new solution file from template.
Usage: python create_solution.py [problem_number] [problem_title] [category] [language]
Example: python create_solution.py 1 "Two Sum" arrays python
"""

import os
import sys
import shutil
from datetime import datetime

# Map of categories to directories
CATEGORIES = {
    'arrays': 'arrays',
    'hashing': 'arrays',  # Both arrays and hashing problems go to arrays/ directory
    'two_pointers': 'two_pointers',
    'sliding_window': 'sliding_window',
    'stack': 'stack',
    'binary_search': 'binary_search',
    'linked_list': 'linked_list',
    'trees': 'trees',
    'tries': 'tries',
    'heap': 'heap_priority_queue',
    'priority_queue': 'heap_priority_queue',
    'backtracking': 'backtracking',
    'graphs': 'graphs',
    'advanced_graphs': 'advanced_graphs',
    'dp_1d': 'dynamic_programming_1d',
    'dp_2d': 'dynamic_programming_2d',
    'greedy': 'greedy',
    'intervals': 'intervals',
    'math': 'math_geometry',
    'geometry': 'math_geometry',
    'bit_manipulation': 'bit_manipulation'
}

# Map of language choices to file extensions
LANGUAGES = {
    'python': '.py',
    'py': '.py',
    'javascript': '.js',
    'js': '.js',
    'java': '.java',
    'cpp': '.cpp',
    'c++': '.cpp'
}

def create_solution_file(problem_number, problem_title, category, language):
    """Create a solution file from template."""
    # Validate category
    if category.lower() not in CATEGORIES:
        print(f"Invalid category: {category}")
        print(f"Available categories: {', '.join(CATEGORIES.keys())}")
        return
    
    # Validate language
    if language.lower() not in LANGUAGES:
        print(f"Invalid language: {language}")
        print(f"Available languages: {', '.join(LANGUAGES.keys())}")
        return
    
    # Get proper directory and file extension
    directory = CATEGORIES[category.lower()]
    extension = LANGUAGES[language.lower()]
    
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Create filename
    filename = f"{problem_number}_{problem_title.lower().replace(' ', '_')}{extension}"
    filepath = os.path.join(directory, filename)
    
    # Check if file already exists
    if os.path.exists(filepath):
        print(f"File already exists: {filepath}")
        overwrite = input("Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            return
    
    # Get template file
    template_file = f"solution_template{extension}"
    if not os.path.exists(template_file):
        print(f"Template file not found: {template_file}")
        return
    
    # Copy template to new file
    shutil.copy(template_file, filepath)
    
    # Update template placeholders
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Convert problem title to slug format
    problem_slug = problem_title.lower().replace(' ', '-')
    
    # Replace placeholders
    content = content.replace('[Problem Number]', str(problem_number))
    content = content.replace('[Problem Title]', problem_title)
    content = content.replace('[problem-slug]', problem_slug)
    
    # Write updated content
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Solution file created: {filepath}")
    
    # Open the file in your preferred editor (optional)
    # Uncomment one of the following lines:
    # os.system(f"code {filepath}")  # VS Code
    # os.system(f"vim {filepath}")   # Vim
    # os.system(f"nano {filepath}")  # Nano

def print_usage():
    """Print usage instructions."""
    print("Usage: python create_solution.py [problem_number] [problem_title] [category] [language]")
    print("Example: python create_solution.py 1 \"Two Sum\" arrays python")
    print(f"\nAvailable categories: {', '.join(CATEGORIES.keys())}")
    print(f"Available languages: {', '.join(LANGUAGES.keys())}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print_usage()
    else:
        problem_number = sys.argv[1]
        problem_title = sys.argv[2]
        category = sys.argv[3]
        language = sys.argv[4]
        create_solution_file(problem_number, problem_title, category, language) 