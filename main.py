import os
from dotenv import load_dotenv
from GITHUB import GITHUB
import random

load_dotenv()
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
    random_number = random.randint(0, 6)
    i = 0
    while i < random_number:
        i+=1
        github.updateFile('README.md')

    print(random_number)
    
if __name__ == '__main__':
    main()