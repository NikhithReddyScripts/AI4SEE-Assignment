# AI4SEE-Assignment

This repository contains Python scripts to complete the assignment provided.

## Dataset
The dataset required for the assignment is available in the "files.zip" file, which can be downloaded from the following link: files.zip

The "files.zip" contains 4 sets of CSV files, each consisting of a time series dataset and its corresponding anomaly labels:

* test.csv --> test_label.csv
* smap_test.csv --> smap_test_labels.csv
* msl_test.csv --> msl_test_labels.csv
* psm_test.csv --> psm_test_labels.csv

## Tasks and Python Scripts
The assignment tasks and the corresponding Python scripts are as follows:

1. Read test and label files: ***a_ReadTestLabel.py*** <br />
This script reads the time series data and its corresponding anomaly labels from the CSV files.
2. Draw time series plots with anomaly regions: ***b_TimeSeriesPlots.py*** <br />
This script generates time series plots with highlighted anomaly regions based on the provided labels.
3. Perform EDA and find out root cause: ***c_EdaRootCause.py*** <br />
This script performs exploratory data analysis (EDA) to identify significant variables contributing to anomalies and determines the root cause.
4. Find out the variables which are the root cause for the anomaly: ***d_RootCauseVariables.py*** <br />
This script identifies the variables that are the root cause for anomalies based on the EDA results.

## Instructions
To run the Python scripts, follow these steps:

1. Download the "files.zip" dataset from the provided link. <br />
2. Extract the contents of the zip file. <br />
3. Ensure that Python is installed on your system along with the required libraries (e.g., pandas, matplotlib). <br />
4. Run each Python script using a Python interpreter (e.g., python script_name.py).<br />

