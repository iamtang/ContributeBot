import os
from dotenv import load_dotenv
from GITHUB import GITHUB
import random

load_dotenv()
range = os.getenv("RANGE")
github = GITHUB(
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN"),
	USERNAME = os.getenv("USERNAME"),
	REPO = os.getenv("REPO")
)

def main():
    # issueData = github.createIssue()
    # commentData = github.commentIssue(issueData['number'])
    # github.delCommentIssue(commentData['id'])
    # github.closeIssue(issueData['number'])
    # res = github.updateFile('README.md')
    _range = list(map(int, range.split('-')))
    random_number = random.randint(*_range)
    i = 0
    while i < random_number:
        i+=1
        github.updateFile('README.md')

    
if __name__ == '__main__':
    main()