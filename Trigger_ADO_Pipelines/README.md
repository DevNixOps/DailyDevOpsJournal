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
   
3. **Prepare Input CSV File**
   Create a CSV file that lists pipeline names and branches in the following format:
   ```csv
   pipeline_name,branch_name
   ExamplePipeline,main
   AnotherPipeline,develop
   ```

   Save the file (e.g., pipelines.csv) in the same directory as the script or note its full path.



## Usage

Run the script by providing the path to the CSV file as an argument:
```bash
python trigger_pipelines.py <file_path>
```

## Example Command:
```bash
python trigger_pipelines.py pipelines.csv
```


## Script Workflow

1. **Fetch Pipeline IDs**  
   The script uses the Azure DevOps REST API to fetch the pipeline ID based on its name.

2. **Trigger Pipelines**  
   For each pipeline listed in the CSV file, it triggers a build for the specified branch.

3. **Error Handling**  
   If a pipeline is not found or triggering fails, the script logs the error and proceeds to the next entry.


## Example Output

```bash
Processing pipeline: ExamplePipeline on branch: main
Pipeline 123 triggered successfully for branch 'main'!

Processing pipeline: AnotherPipeline on branch: develop
Pipeline 'AnotherPipeline' not found.
```


## Error Handling

- **File Not Found**  
  Displays an error if the specified CSV file is missing.

- **Pipeline Not Found**  
  Logs a message if the specified pipeline does not exist in Azure DevOps.

- **API Failures**  
  Logs the response from the Azure DevOps API if a request fails.


  ## Notes

- Ensure your Personal Access Token (PAT) has sufficient permissions to:
  - Read pipelines.
  - Trigger builds.
- Keep your PAT secure and do not share it publicly.
- Optionally, modify the script to include a delay between API calls to avoid rate-limiting issues.


## License

This script is licensed under the MIT License. Feel free to use and modify it as needed.
