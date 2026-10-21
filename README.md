# SpaceX Falcon 9 First-Stage Landing Prediction — EDA

An exploratory data analysis and feature-engineering project that investigates how Falcon 9 launch characteristics relate to first-stage landing outcomes. The notebook uses Python, Pandas, Matplotlib, and Seaborn to explore the dataset and export a one-hot-encoded feature matrix for downstream machine-learning work.

## Project objectives

- Explore landing outcomes by flight number and payload mass.
- Compare outcomes across launch sites and orbit types.
- Calculate and visualize landing success rates by orbit and year.
- Prepare categorical variables with one-hot encoding.
- Export the processed features as a CSV file.

## Repository structure

```text
spacex-falcon9-eda/
├── edadataviz.ipynb       # Clean, locally runnable analysis notebook
├── data/
│   └── .gitkeep           # Generated CSV is created here when the notebook runs
├── images/
│   └── .gitkeep           # Add exported chart screenshots here if desired
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

The notebook reads the CSV dataset from the IBM Skills Network course-hosted source:

`https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv`

An internet connection is required when loading the data. The dataset is not duplicated in this repository. Please check the source's terms and attribution requirements before redistribution or commercial use.

## Tools and libraries

- Python 3.10+
- Jupyter Notebook
- Pandas and NumPy
- Matplotlib and Seaborn

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/spacex-falcon9-eda.git
   cd spacex-falcon9-eda
   ```

2. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Start Jupyter:

   ```bash
   jupyter notebook
   ```

5. Open `edadataviz.ipynb` and run the cells from top to bottom.

The notebook saves the processed feature matrix to `data/dataset_part_3.csv`.

## Analysis workflow

1. Load the dataset and inspect its structure and missing values.
2. Explore relationships between flight number, payload mass, launch site, orbit, and landing outcome.
3. Visualize the yearly landing success trend.
4. Select features and one-hot encode `Orbit`, `LaunchSite`, `LandingPad`, and `Serial`.
5. Convert encoded columns to `float64` and export the resulting feature matrix.

## Important notes

- The target label is `Class` (`1` indicates a successful landing and `0` indicates an unsuccessful landing in the course dataset).
- `Class` is intentionally not included in the exported feature matrix; join it back from the source data when preparing a supervised-learning dataset.
- The notebook provides exploratory analysis, not a validated production prediction model.
- Visual patterns are associations and should not be interpreted as proof of causation.
- The notebook downloads data at runtime, so it needs network access.

## Potential improvements

- Add statistical tests and confidence intervals for success rates.
- Build a scikit-learn classification pipeline with stratified train/test split and cross-validation.
- Compare models with precision, recall, F1-score, ROC-AUC, and a confusion matrix.
- Add interactive Plotly visualizations and a dashboard.
- Add a reproducible data versioning or caching strategy.

## Author

**Your Name** — replace this line with your name and add your GitHub/LinkedIn links.

## Acknowledgements

Dataset source: IBM Skills Network, *SpaceX Falcon 9 First Stage Landing Prediction* learning materials.
