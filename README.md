> _This repository contains data engineering and data science projects and exercises using open data sources as part of the [AMSE](https://oss.cs.fau.de/teaching/specific/amse/)/[SAKI](https://oss.cs.fau.de/teaching/specific/saki/) course, taught by the [FAU Chair for Open-Source Software (OSS)](https://oss.cs.fau.de/) in the Winter 23 24semester. This repo is forked from [Data Engineering FAU](https://github.com/jvalue/2023-amse-template)._

# Analyzing the Relationship Between Age Demographics and Crime Trends in Berlin Neighborhoods

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The project, titled "Analyzing the Relationship Between Age Demographics and Crime Trends in Berlin Neighborhoods," is a data science initiative aimed at uncovering the intricate connection between age demographics and crime patterns within the diverse neighborhoods of Berlin from 2012 to 2019.

This endeavor is motivated by a dual purpose: First, to contribute to the well-being of Berlin's residents by providing evidence-based insights to enhance public safety, urban planning, and social welfare efforts. Second, to empower local authorities, law enforcement, and policymakers with a data-driven framework for informed decision-making.

To accomplish this, we collect and integrate two pivotal datasets – one detailing the age distribution in various Berlin neighborhoods and another outlining crime incidents spanning seven years. Our data engineering efforts encompassbuilding  data pipeline for automated collecting, storing, cleaning, transformation, and analysis of the data. 

The main question we seek to answer is: "How do age demographics within Berlin's population correlate with and influence crime trends across the city's neighborhoods?" By exploring this question, we aim to uncover patterns, trends, and dependencies that can guide targeted interventions for crime prevention, urban development, and social programs.

Ultimately, this project serves as a valuable resource for both researchers and decision-makers, contributing to evidence-based practices that enhance the quality of life in Berlin's diverse communities.

## Running the project
1. Clone the repository using command 'git clone git@github.com:ishmam367/made-template.git'
2. Run the following command to install the dependencies specified in the requirements.txt file
: pip install -r requirements.txt
3. to execute the pipeline, run the following command from the root directory `./project.pipeline.sh`
4. to execute all the test run the following command from the root directory `./project.tests.sh`


## Project Structure: ETL pipeline 
The project follows a structured ETL (Extract, Transform, Load) pipeline approach, encompassing various directories and modules with specific functionalities. The `pipeline.sh` file in the project folder serves as the entry point for running the pipeline using the command `./project.pipeline.sh` from the made_template folder, resulting in the generation of the final dataset stored in an SQLite database as my_database.sqlite in the data directory.

```bash
project/                       
│                    
├── pipelines/                  # Data pipeline modules
│   ├── __init__.py
│   └── pipeline.py             # ETL data pipeline implementation
├── tests/                      # Test modules
│   ├── __init__.py
│   ├── pipilinetest.py         # Test cases for component and system testing
├── __init__.py.                   
├── final_report.ipynb          # Notebook for final project report
├── pipeline.sh                 # main file to run the ETL pipeline
├── project-plan.md             # Project plan and documentation
└── run_pipeline.py             # defining the databases and calling the pipelines
├── tests.sh                    # file to run all the tests.
```

## Continuous Integration Pipeline using GitHub Action:
A Continuous Integration pipeline has been implemented using a GitHub action defined in [.github/workflows/ci-tests.yml](.github/workflows/Project_CI_Test.yml). This pipeline is triggered whenever changes are made to the `project/` directory  and pushed to the GitHub repository, or when a pull request is created and merged into the `main` branch. It Installs the required Python packages listed in requirements.txt using pip, Creates a kaggle.json file with credentials stored in a GitHub secret (KAGGLE) using jsdaniell/create-json@v1.2.2.
Grants execution permissions to a test script (tests.sh) and runs it to execute the project's tests.
This workflow is designed to automate the testing process upon code pushes, ensuring the project dependencies are installed and tests are run.

## Project Report
See the final [Project report](project/report.ipynb) to see the analysis
