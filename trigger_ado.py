import requests
import base64
import csv
import time
import sys

# Configuration
organization = ""                # Azure DevOps organization name
project = ""                     # Azure DevOps project name
personal_access_token = ""       # Your Azure DevOps PAT

# Encode PAT for Authorization
auth = base64.b64encode(f":{personal_access_token}".encode()).decode()

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {auth}"
}


def get_pipeline_id(pipeline_name):
    """
    Get the pipeline ID from its name.
    """
    url = f"https://dev.azure.com/{organization}/{project}/_apis/pipelines?api-version=6.0-preview.1"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pipelines = response.json().get("value", [])
        for pipeline in pipelines:
            if pipeline.get("name") == pipeline_name:
                return pipeline.get("id")
    else:
        print(f"Failed to fetch pipelines. Status code: {response.status_code}")
        print("Response:", response.text)
        return None


def trigger_pipeline(pipeline_id, branch_name):
    """
    Trigger a pipeline by its ID for a specific branch.
    """
    url = f"https://dev.azure.com/{organization}/{project}/_apis/pipelines/{pipeline_id}/runs?api-version=6.0-preview.1"
    payload = {
        "resources": {
            "repositories": {
                "self": {
                    "refName": f"refs/heads/{branch_name}"  # Branch name (e.g., "refs/heads/main")
                }
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code in [200, 201]:
        print(f"Pipeline {pipeline_id} triggered successfully for branch '{branch_name}'!")
    else:
        print(f"Failed to trigger pipeline {pipeline_id} for branch '{branch_name}'. Status code: {response.status_code}")
        print("Response:", response.text)


def main(file_path):
    """
    Main function to process the input file and trigger pipelines.
    """
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                pipeline_name, branch_name = row
                print(f"Processing pipeline: {pipeline_name} on branch: {branch_name}")
                
                # Get pipeline ID
                pipeline_id = get_pipeline_id(pipeline_name.strip())
                if pipeline_id:
                    trigger_pipeline(pipeline_id, branch_name.strip())
                    # Optional: Add delay to avoid overwhelming the server
                    time.sleep(2)
                else:
                    print(f"Pipeline '{pipeline_name}' not found.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python trigger_pipelines.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
