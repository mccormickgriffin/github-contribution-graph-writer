import math
from graph_word import GraphWord
from year_details import YearDetails
from folder_manager import FolderManager
from graph_word_commit_writer import GraphWordCommitWriter

def get_confirmation(word, year):
    while True:
        user_input = input(f"Do you want to write {word} on {year}? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def get_year_details_and_graph_word():
    while True:
        year = int(input("What year would you like to write on? ").strip())
        year_details = YearDetails(year)
        word = input("What would you like to write? ").strip()
        graph_word = GraphWord(word.upper())

        if  graph_word.width > year_details.full_weeks:
            print(f"Your message is too long for the space in {year}")
            print(f"{year_details.full_weeks} full weeks available. {graph_word.width} required for {word}")
        else:
            print("Preview: ")
            graph_word.print_graph()
            confirmation = get_confirmation(word, year)
            if confirmation:
                break
            else:
                continue
    
    return year_details, graph_word

def main():
    # Get user input    
    yd, gw = get_year_details_and_graph_word()

    # Center graph word
    extra_spaces = yd.full_weeks - gw.width
    front_spaces = math.floor(extra_spaces / 2)
    back_spaces = math.ceil(extra_spaces / 2)
    gw.pad_front(front_spaces)
    gw.pad_back(back_spaces)

    # Create folder based on user input and navigate into it
    fm = FolderManager()
    folder_name = f"gcgw-{yd.year}-{gw.word}"
    fm.create_and_open_folder(folder_name)

    # Generate all commits to spell word on Github's contribution graph
    gwcw = GraphWordCommitWriter(gw, yd)
    gwcw.write_word()
    
if __name__ == "__main__":
    main()