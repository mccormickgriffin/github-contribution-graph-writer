from datetime import datetime, timedelta
from graph_word import GraphWord
from git_manager import GitManager
from folder_manager import FolderManager

SATURDAY = 5
SUNDAY = 6

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

def get_year_and_graph_word():
    while True:
        year = int(input("What year would you like to write on? "))
        word = input("What would you like to write? ")

        full_weeks_in_year = get_full_weeks(year)
        graph_word = GraphWord(word)
        word_width = graph_word.width() 
        if  word_width > full_weeks_in_year:
            print(f"Your message is too long for the space in {year}")
            print(f"{full_weeks_in_year} full weeks available. {word_width} required for {word}")
        else:
            break
    
    return year, graph_word

def main():
    fm = FolderManager()
    gm = GitManager()

    # Get user input    
    year, word = get_year_and_graph_word()

    folder_name = f"gcgw-{year}-{word}"
    fm.create_and_open_folder(folder_name)
    
    gm.init_repo()
    gm.make_commits_for_enitre_year(year)
    

if __name__ == "__main__":
    main()