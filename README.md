# MovieLens-Analysis

## 📌 Project Overview

The **MovieLens-Analysis** project is designed to perform exploratory data analysis and data cleaning on the **MovieLens** dataset. This dataset contains information on movies, user ratings, tags assigned to movies, and links to IMDb and TMDb. The goal of this project is to clean, organize, and prepare the data for further analysis, addressing issues such as poor column names, missing data, outliers, and incorrect data types. Additionally, the data will be reformatted for better visualization and analysis.

Through **data cleaning** and **data analysis** techniques, the project generates detailed reports that provide valuable insights into the dataset, such as ratings distributions and movie popularity.

---

## 🗂️ Project Structure

The project is organized into the following directories:


MovieLens-Analysis/ 
│ ├── data/ # Raw CSV data files (movies.csv, ratings.csv, etc.) 
│ ├── notebooks/ # Jupyter notebook for data exploration (exploration.ipynb) 
│ ├── reports/ # Analysis reports and outputs (reports.txt) 
│ ├── scripts/ # Scripts for data cleaning and analysis (data_cleaning.py, data_analysis.py) 
│ └── README.md # This file with project details


### 🔍 Descriptions of directories:

- **data/**: Contains the original raw data in CSV format, including `movies.csv`, `ratings.csv`, `tags.csv`, and `links.csv`.
- **notebooks/**: Contains Jupyter notebooks for interactive data exploration. For example, `exploration.ipynb` allows you to explore the dataset visually.
- **reports/**: Stores analysis results and reports, such as `reports.txt`, which includes insights and analysis of ratings, movie popularity, and other aspects of the dataset.
- **scripts/**: Includes Python scripts for data cleaning and analysis:
  - `data_cleaning.py`: Prepares and cleans the data.
  - `data_analysis.py`: Performs analysis and generates reports.
  
---

## 🛠️ Features

The project performs the following tasks:

### 1. **Data Cleaning**:
   - **Renaming Columns**: Simplifying and clarifying column names.
   - **Handling Missing Data**: Identifying and managing missing or null values.
   - **Outlier Detection**: Identifying and removing outliers from the data.
   - **Data Type Conversion**: Converting columns to appropriate data types, such as converting Unix timestamps to human-readable dates.
   - **Formatting Timestamps**: Transforming Unix timestamps into readable date and time formats.

### 2. **Data Analysis**:
   - **Exploratory Data Analysis (EDA)**: Examining rating distributions, movie popularity, and tag frequencies.
   - **Reports Generation**: Producing detailed reports, including insights on the structure and content of the data.
   - **Visualization**: Creating graphs and plots for trends and patterns in the dataset.

---

## 🚀 How to Run the Project

### Step-by-Step Guide:

1. **Install Dependencies**:
   - First, create a virtual environment and install the necessary dependencies using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt


Run the Data Cleaning Script:

The data_cleaning.py script performs the cleaning tasks (e.g., renaming columns, handling missing data, etc.):

python scripts/data_cleaning.py

Run the Data Analysis Script:

After cleaning the data, run data_analysis.py to perform the analysis and generate reports:

python scripts/data_analysis.py

Interactive Data Exploration with Jupyter:

The exploration.ipynb notebook provides an interactive environment to explore the data. Open it in Jupyter for dynamic analysis:

jupyter notebook notebooks/exploration.ipynb

📊 Technologies Used
Python: Programming language used for data processing and analysis.
Pandas: Powerful library for data manipulation and analysis.
Matplotlib and Seaborn: Libraries for data visualization and creating plots.
Jupyter Notebook: Environment for interactive data analysis and visualization.
NumPy: Library for numerical computations.
Scikit-learn: Potentially for future applications in machine learning (e.g., movie recommendation systems).
📝 Report Generation
The project generates a detailed report, which can be found in the reports/ folder. This report includes:

Overview of data exploration and analysis.
Insights into rating distributions, movie tags, and trends.
Outlier and missing data analysis.
Reports are saved in text format (reports.txt) and can be further divided into multiple files for easier reading if necessary.

👨‍💻 Author
Enzo Brito
Student of Computer Engineering


⚙️ Future Improvements
This project lays the foundation for further analysis and model-building, such as:

Movie recommendation systems using collaborative filtering or content-based filtering.
Sentiment analysis of user tags.
Improved data visualizations with interactive dashboards (e.g., using Plotly or Dash).

🏁 Conclusion
The MovieLens-Analysis project provides valuable insights into the MovieLens dataset by performing thorough data cleaning and analysis. The project prepares the dataset for further exploration and model development, with a strong focus on data quality and ease of interpretation. By cleaning, exploring, and analyzing the data, this project demonstrates how raw datasets can be transformed into actionable insights.
