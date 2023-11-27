import subprocess
import os
import uuid

COMMIT_FILE = "commit.md"

class GitManager:
    _instance = None

    def __new__(self):
        # Singleton Pattern
        if not self._instance:
            self._instance = super(GitManager, self).__new__(self)
        return self._instance
    
    def init_repo(self):
        subprocess.run(["git", "init"])
    
    def make_git_commit(self, commit_date):
        formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        with open(COMMIT_FILE, 'w') as file:
            file.write(str(uuid.uuid4()))
        os.environ['GIT_COMMITTER_DATE'] = formatted_date
        os.environ['GIT_AUTHOR_DATE'] = formatted_date
        subprocess.run(["git", "add", COMMIT_FILE, "-f"])
        subprocess.run(["git", "commit", "--date", f'"{formatted_date}"', "-m", f'"Commit for {formatted_date}"'])
