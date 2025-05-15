## Github-JIRA integration Project

### Overview
This project provides an automated solution to create JIRA tickets from GitHub issues using webhooks. When a user comments "/jira" on a GitHub issue, this application creates a corresponding ticket in JIRA with all relevant information.

### The integration works by:
1. Listening for webhook events from GitHub issues
2. Processing comments containing the trigger command ("/jira")
3. Extracting issue details (title, description, repository info, etc.)
4. Creating a formatted JIRA ticket via the Atlassian REST API

