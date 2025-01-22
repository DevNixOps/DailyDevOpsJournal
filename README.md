# Azure DevOps Pipeline Trigger Script

A Python script to automate the process of triggering Azure DevOps pipelines for specific branches using a CSV file as input.

## Features

- Dynamically fetch pipeline IDs based on their names.
- Trigger pipelines for specified branches.
- Process multiple pipelines and branches from a CSV file.
- Includes error handling for missing pipelines, API failures, and file errors.

---

## Prerequisites

- **Python 3.x**
- Required Python Libraries:
  - `requests`
  - `base64`
  - `csv`
  - `time`
  - `sys`

Install the required libraries using the following command:

```bash
pip install requests
```


## Setup

1. **Clone or Download**  
   Clone this repository to your local system or download the script file.

2. **Configure the Script**  
   Open the script and set the following parameters:
   - `organization`: Your Azure DevOps organization name.
   - `project`: Your Azure DevOps project name.
   - `personal_access_token`: Your Azure DevOps Personal Access Token (PAT).

   Example configuration in the script:

   ```python
   organization = "my-organization"
   project = "my-project"
   personal_access_token = "your_personal_access_token"
   ```
   


## Script Workflow

1. **Fetch Pipeline IDs**  
   The script uses the Azure DevOps REST API to fetch the pipeline ID based on its name.

2. **Trigger Pipelines**  
   For each pipeline listed in the CSV file, it triggers a build for the specified branch.

3. **Error Handling**  
   If a pipeline is not found or triggering fails, the script logs the error and proceeds to the next entry.
