# Azure DevOps Pipeline Trigger Script

A Python script to automate the process of triggering Azure DevOps pipelines for specific branches using a CSV file as input.

## Features

- Dynamically fetch pipeline IDs based on their names.
- Trigger pipelines for specified branches.
- Process multiple pipelines and branches from a CSV file.
- Includes error handling for missing pipelines, API failures, and file errors.

## Prerequisites

- **Python 3.x**
- Required Python Libraries:
  - `requests`
  - `base64`
  - `csv`
  - `time`
  - `sys`

Install the required libraries using:

```bash
pip install requests
