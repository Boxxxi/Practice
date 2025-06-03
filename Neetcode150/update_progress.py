#!/usr/bin/env python3
"""
Script to update the PROGRESS.md file by checking completed problems.
It scans through the directories and marks problems as completed in the PROGRESS.md file.
"""

import os
import re
from collections import defaultdict

# Map of directories to their corresponding sections in PROGRESS.md
DIR_TO_SECTION = {
    'arrays': 'Arrays & Hashing',
    'two_pointers': 'Two Pointers',
    'sliding_window': 'Sliding Window',
    'stack': 'Stack',
    'binary_search': 'Binary Search',
    'linked_list': 'Linked List',
    'trees': 'Trees',
    'tries': 'Tries',
    'heap_priority_queue': 'Heap / Priority Queue',
    'backtracking': 'Backtracking',
    'graphs': 'Graphs',
    'advanced_graphs': 'Advanced Graphs',
    'dynamic_programming_1d': '1-D Dynamic Programming',
    'dynamic_programming_2d': '2-D Dynamic Programming',
    'greedy': 'Greedy',
    'intervals': 'Intervals',
    'math_geometry': 'Math & Geometry',
    'bit_manipulation': 'Bit Manipulation'
}

def extract_problem_number(filename):
    """Extract problem number from file name or content."""
    # First try to get it from the filename
    match = re.search(r'(\d+)[\._-]', filename)
    if match:
        return match.group(1)
    
    # If not found in filename, read the file content
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            content = f.read()
            # Try to find the problem number in the content
            match = re.search(r'Problem:\s*(\d+)', content)
            if match:
                return match.group(1)
    
    return None

def scan_directories():
    """Scan directories for completed problems."""
    completed_problems = defaultdict(list)
    
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    for directory, section in DIR_TO_SECTION.items():
        dir_path = os.path.join(script_dir, directory)
        if os.path.exists(dir_path):
            for filename in os.listdir(dir_path):
                if filename.endswith(('.py', '.js', '.java', '.cpp')):
                    file_path = os.path.join(dir_path, filename)
                    problem_number = extract_problem_number(file_path)
                    if problem_number:
                        completed_problems[section].append(problem_number)
    
    return completed_problems

def update_progress_file(completed_problems):
    """Update the PROGRESS.md file."""
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    progress_file = os.path.join(script_dir, 'PROGRESS.md')
    
    if not os.path.exists(progress_file):
        print("PROGRESS.md file not found.")
        return
    
    with open(progress_file, 'r') as f:
        lines = f.readlines()
    
    updated_lines = []
    current_section = None
    total_completed = 0
    total_problems = 0
    
    for line in lines:
        if line.startswith('## '):
            current_section = line[3:].strip()
            updated_lines.append(line)
        elif line.startswith('- [ ]') and current_section in completed_problems:
            # Extract problem number
            match = re.search(r'- \[ \] (\d+)\.', line)
            if match:
                problem_num = match.group(1)
                total_problems += 1
                if problem_num in completed_problems[current_section]:
                    # Mark as completed
                    updated_line = line.replace('- [ ]', '- [x]')
                    updated_lines.append(updated_line)
                    total_completed += 1
                else:
                    updated_lines.append(line)
            else:
                updated_lines.append(line)
        elif line.startswith('- [x]'):
            total_problems += 1
            total_completed += 1
            updated_lines.append(line)
        elif line.startswith('- [ ]'):
            total_problems += 1
            updated_lines.append(line)
        elif line.startswith('# Total Problems Completed:'):
            updated_lines.append(f"# Total Problems Completed: ({total_completed}/{total_problems})\n")
        elif line.startswith('Progress:'):
            updated_lines.append(f"Progress: {total_completed / total_problems * 100:.1f}% - |{'|' * total_completed}{'.' * (total_problems - total_completed)}|")
        else:
            updated_lines.append(line)
    
    with open(progress_file, 'w') as f:
        f.writelines(updated_lines)
    
    print(f"Progress updated: {total_completed}/{total_problems} problems completed.")

if __name__ == "__main__":
    completed_problems = scan_directories()
    update_progress_file(completed_problems) 