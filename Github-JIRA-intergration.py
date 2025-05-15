import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://rashikasahu352.atlassian.net/rest/api/3/issue"
    email = "******"
    API_TOKEN = "******"
    auth = HTTPBasicAuth(email, API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    
    requestData = request.json
    issueTitle = requestData["issue"]["title"]
    issueDesc = requestData["issue"]["body"]
    issueRepo = requestData["repository"]["name"]
    issueUser = requestData["comment"]["user"]["login"]
    issueComment = requestData["comment"]["body"]
    issueDescription = f"GitHub Issue Description:\n{issueDesc}\n\nRepository: {issueRepo}\nSubmitted by: {issueUser}"
    print(issueTitle, issueDesc, issueRepo, issueUser, issueComment)
    print(issueDescription)

    if issueComment == "/jira":
        payload = json.dumps( {
        "fields": {
            "description": {
            "content": [
                {
                "content": [
                    {
                    "text": issueDescription,
                    "type": "text"
                    }
                ],
                "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
            },
            "project": {
            "key": "RASHIKA"
            },
            "issuetype": {
            "id": "10009"
            },
            "summary": issueTitle,
        },
        "update": {}
        } )

        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return "Please enter correct comment to create the jira ticket"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



