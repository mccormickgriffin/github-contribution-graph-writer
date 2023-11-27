from datetime import datetime, timedelta
from git_manager import GitManager
from graph_character import ROW_COUNT

COMMIT_FILE = "commit.md"

class GraphWordCommitWriter:
    _instance = None

    def __new__(self, graph_word, year_details):
        # Singleton Pattern
        if not self._instance:
            self._instance = super(GraphWordCommitWriter, self).__new__(self)
            self.gm = GitManager()
            self.graph_word = graph_word
            self.year_details = year_details
        return self._instance
    
    def write_word(self):
        self.gm.init_repo()

        # Fill partial week in beginning of year
        current_date = datetime(self.year_details.year, 1, 1, 12, 0, 0)
        while current_date < self.year_details.first_sunday:
            self.gm.make_git_commit(current_date)
            current_date += timedelta(days=1)

        # Fill partial week at end of year
        end_date = datetime(self.year_details.year, 12, 31, 12, 0, 0)
        while end_date > self.year_details.last_saturday:
            self.gm.make_git_commit(end_date)
            end_date -= timedelta(days=1)
        
        # Generate commits based on graph_word data
        for column in range(self.graph_word.width):
            print(f"Column: {column}")
            for row in range(ROW_COUNT):
                print(f"Row: {row}")

                num_commits = 5 if self.graph_word.get(row, column) else 1
                for _ in range(num_commits):
                    self.gm.make_git_commit(current_date)
                current_date += timedelta(days=1)

        # Fill in the rest of the full weeks
        while current_date <= end_date:
            self.gm.make_git_commit(current_date)
            current_date += timedelta(days=1)
