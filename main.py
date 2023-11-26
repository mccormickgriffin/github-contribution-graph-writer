import subprocess
import os
from datetime import datetime, timedelta
from graph_word import GraphWord

SATURDAY = 5
SUNDAY = 6

COMMIT_FILE = "commit.md"

def get_full_weeks(year):
    # Find first Sunday
    start_date = datetime(year, 1, 1)
    while start_date.weekday() != SUNDAY:
        start_date += timedelta(days=1)

    # Find last Saturday
    end_date = datetime(year, 12, 31)
    while end_date.weekday() != SATURDAY: 
        end_date -= timedelta(days=1)
    
    days_count = (end_date - start_date).days + 1

    return int(days_count / 7)

def make_git_commit(commit_date):
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    with open(COMMIT_FILE, 'w') as file:
        file.write(formatted_date)
    os.environ['GIT_COMMITTER_DATE'] = formatted_date
    os.environ['GIT_AUTHOR_DATE'] = formatted_date
    subprocess.run(["git", "add", COMMIT_FILE, "-f"])
    subprocess.run(["git", "commit", "--date", f'"{formatted_date}"', "-m", f'"Commit for {formatted_date}"'])

def main():
    # Get user input for what word they want to write on what years contribution graph
    year = int(input("What year would you like to write on? "))
    word = input("What would you like to write? ")
    graph_word = GraphWord(word)

    # Create new folder for generated git repo
    folder_name = f"gcgw-{year}-{word}"
    create_folder_command = f"mkdir {folder_name}"
    process = subprocess.Popen(create_folder_command,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    output, error = process.communicate()
    print(output)

    if process.returncode == 0:
        os.chdir(folder_name)
        subprocess.run(["git", "init"])
        with open(COMMIT_FILE, 'w'):
            pass

        start_date = datetime(year, 1, 1, 12, 0, 0)
        end_date = datetime(year, 12, 31, 12, 0, 0)
        current_date = start_date
        while current_date <= end_date:
            make_git_commit(current_date)
            current_date += timedelta(days=1)
    else:
        print(f"Error creating folder: {error}")

if __name__ == "__main__":
    main()