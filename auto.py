import os
import csv

# File paths
CSV_FILE = 'data.csv'
BASE_DIR = 'Vulnerabilities'
MAIN_README = 'README.md'

def get_next_id():
    # Check if the CSV file exists
    if not os.path.exists(CSV_FILE):
        return 1  # Start with ID 1 if file does not exist

    max_id = 0
    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            try:
                current_id = int(row[0])
                max_id = max(max_id, current_id)
            except (ValueError, IndexError):
                continue  # Skip rows with invalid IDs
    return max_id + 1

def create_folder_structure(bug_id, title, technique, severity, description, discovery_date, browser, affected_version, bounty, cve, poc_code):
    # Create folder name based on ID
    folder_name = f'bug-{bug_id:03d}'
    folder_path = os.path.join(BASE_DIR, folder_name)
    
    # Create the main folder
    os.makedirs(folder_path, exist_ok=True)

    # Create the bug-XXX.html file with PoC code
    poc_file_path = os.path.join(folder_path, f'bug-{bug_id:03d}.html')
    with open(poc_file_path, 'w') as poc_file:
        poc_file.write(poc_code)

    # Create the README.md file for the individual bug
    readme_file_path = os.path.join(folder_path, 'README.md')
    with open(readme_file_path, 'w') as readme_file:
        readme_file.write(f'# Title: {title}\n\n')
        readme_file.write(f'## Description: \n{description}\n\n')
        readme_file.write(f'## Affected Browser(s): {browser}\n\n')
        readme_file.write(f'## Severity: {severity}\n\n')
        readme_file.write(f'## Spoof Type: {technique}\n\n')
        readme_file.write(f'## POC Photo/Video: {folder_name}.mp4/.mov/.png\n\n')  # Placeholder for PoC links
        readme_file.write(f'## Discovery Date: {discovery_date}\n\n')

    return folder_name

def add_to_csv(bug_id, title, technique, severity, discovery_date, browser, affected_version, bounty, cve):
    # Write the new entry to the CSV file
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header if the file is new
        if file.tell() == 0:
            writer.writerow(['ID', 'Title', 'Technique', 'Severity', 'Discovery Date', 'Browser', 'Affected Version', 'Bounty', 'CVE'])
        # Add the new row
        new_row = [bug_id, title, technique, severity, discovery_date, browser, affected_version, bounty, cve]
        writer.writerow(new_row)

def update_main_readme():
    # Read data from CSV file
    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Generate Markdown table
    table = "| " + " | ".join(rows[0]) + " |\n"  # Header row
    table += "|---" * len(rows[0]) + "|\n"  # Separator row
    for row in rows[1:]:
        table += "| " + " | ".join(row) + " |\n"

    # Update main README.md
    with open(MAIN_README, 'w') as readme_file:
        readme_file.write("# Address_Bar_Spoofing\n")
        readme_file.write("Web Browsers address bar spoofing vulnerabilities\n\n")
        readme_file.write("## Vulnerability Data\n\n")
        readme_file.write(table)

def main():
    # Collect user input for the new entry
    title = input('Title: ')
    technique = input('Technique: ')
    severity = input('Severity: ')
    browser = input('Browser: ')
    affected_version = input('Affected Version: ')
    bounty = input('Bounty: ')
    cve = input('CVE (if any): ')
    discovery_date = input('Discovery Date (YYYY-MM-DD): ')

    print("Enter a long description (press Enter for new line, type 'END' on a new line to finish):")
    description_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        description_lines.append(line)
    description = "\n".join(description_lines)

    print("Enter the PoC code (press Enter for new line, type 'END' on a new line to finish):")
    poc_code_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        poc_code_lines.append(line)
    poc_code = "\n".join(poc_code_lines)

    # Get the next ID
    bug_id = get_next_id()
    
    # Create the folder structure and include details in README.md
    folder_name = create_folder_structure(bug_id, title, technique, severity, description, discovery_date, browser, affected_version, bounty, cve, poc_code)
    print(f'Created folder: {folder_name}')
    
    # Add the new entry to the CSV file
    add_to_csv(bug_id, title, technique, severity, discovery_date, browser, affected_version, bounty, cve)
    print(f'Added entry to CSV: ID {bug_id}')
    
    # Update the main README.md with CSV content
    update_main_readme()
    print("Updated main README.md with current data.")

if __name__ == '__main__':
    main()
