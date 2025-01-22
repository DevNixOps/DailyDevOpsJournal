Azure DevOps Pipeline Trigger Script

This Python script allows you to automate triggering pipelines in Azure DevOps for specific branches using a CSV file as input.

Features
	•	Fetch pipeline IDs dynamically based on their names.
	•	Trigger pipelines for specified branches.
	•	Process multiple pipelines and branches from a CSV file.
	•	Includes error handling for failed pipeline triggers and missing files.

 Requirements
	•	Python 3.x
	•	Libraries:
	•	requests
	•	base64
	•	csv
	•	time
	•	sys

You can install the required libraries using:
```pip install requests```
