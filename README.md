## Github-JIRA integration Project

### Overview
This project provides an automated solution to create JIRA tickets from GitHub issues using webhooks. When a user comments "/jira" on a GitHub issue, this application creates a corresponding ticket in JIRA with all relevant information.

### The integration works by:
1. Listening for webhook events from GitHub issues
2. Processing comments containing the trigger command ("/jira")
3. Extracting issue details (title, description, repository info, etc.)
4. Creating a formatted JIRA ticket via the Atlassian REST API

<img width="700" alt="image" src="https://github.com/user-attachments/assets/470c3f85-b809-4d66-bbaa-0318c6c05903">

<img width="700" alt="image" src="https://github.com/user-attachments/assets/d15f4bbb-a70e-48d9-92c1-07b01d0f9152">

### Architecture

1. Backend: Python Flask application
2. Infrastructure: AWS EC2 instance
3. APIs: GitHub Webhooks and JIRA REST API
4. Authentication: JIRA API token-based authentication



