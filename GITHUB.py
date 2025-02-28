import requests
from datetime import datetime
import base64

def getTime():
	now = datetime.now()
	return now.strftime("%Y/%m/%d %H:%M:%S")

class GITHUB:
	def __init__(self, GITHUB_TOKEN, USERNAME, REPO):
		self.GITHUB_TOKEN = GITHUB_TOKEN
		self.USERNAME = USERNAME
		self.REPO = REPO

	def createIssue(self):
		url = f"https://api.github.com/repos/{self.USERNAME}/{self.REPO}/issues"
		data = {
			"title": "ContributeBot",
			"body": getTime(),
		}
		headers = {
			"Authorization": f"Bearer {self.GITHUB_TOKEN}",
			"Accept": "application/vnd.github.v3+json"
		}
		
		return requests.post(url, json=data, headers=headers).json()
		
		
	def commentIssue(self, issue_number):
		url = f"https://api.github.com/repos/{self.USERNAME}/{self.REPO}/issues/{issue_number}/comments"
		data = {
			"body": getTime(),
		}
		headers = {
			"Authorization": f"Bearer {self.GITHUB_TOKEN}",
			"Accept": "application/vnd.github.v3+json"
		}
		
		return requests.post(url, json=data, headers=headers).json()

	def delCommentIssue(self, comment_id):
		url = f"https://api.github.com/repos/{self.USERNAME}/{self.REPO}/issues/comments/{comment_id}"

		headers = {
			"Authorization": f"Bearer {self.GITHUB_TOKEN}",
			"Accept": "application/vnd.github.v3+json"
		}
		
		return requests.delete(url, headers=headers)
		
	def closeIssue(self, issue_number):
		url = f"https://api.github.com/repos/{self.USERNAME}/{self.REPO}/issues/{issue_number}"
		data = {
			"state": "closed"
		}
		headers = {
			"Authorization": f"Bearer {self.GITHUB_TOKEN}",
			"Accept": "application/vnd.github.v3+json"
		}
		
		return requests.patch(url, json=data, headers=headers).json()
	
	def getFileSha(self, path):
		url = f"https://api.github.com/repos/{self.USERNAME}/{self.REPO}/contents/{path}"
		headers = {
			"Authorization": f"Bearer {self.GITHUB_TOKEN}",
			"Accept": "application/vnd.github.v3+json"
		}
		res = requests.get(url, headers=headers).json()
		return res["sha"]
		

	def updateFile(self, path):
		url = f"https://api.github.com/repos/{self.USERNAME}/{self.REPO}/contents/{path}"
		sha = self.getFileSha(path)
		newContent = getTime()
		data = {
			"message": getTime(),
            "content": base64.b64encode(newContent.encode('utf-8')),
            "sha": sha
		}
		headers = {
			"Authorization": f"Bearer {self.GITHUB_TOKEN}",
			"Accept": "application/vnd.github.v3+json"
		}
		
		return requests.put(url, json=data, headers=headers).json()
	
