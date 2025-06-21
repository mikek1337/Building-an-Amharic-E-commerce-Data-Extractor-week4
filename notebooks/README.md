# Notebooks Directory

This directory contains Jupyter notebooks for data exploration, cleaning, and analysis related to the Amharic E-commerce Data Extractor project.

## Contents

- **inital_analysis.ipynb**  
  This notebook demonstrates the initial data cleaning and preprocessing steps for messages scraped from Telegram channels.  
  Steps include:
  - Loading raw messages from `../data/messages.csv`
  - Removing missing values
  - Cleaning messages (removing emojis, tabs, and unwanted characters) using `process_text` from the preprocessing script
  - Saving cleaned messages to `../data/cleaned_messages.csv`
  - Tokenizing and processing messages with `process_language`
  - Saving tokens to `../data/message_tokens.txt`

## Usage

1. Ensure you have run the data scraping script and have `../data/messages.csv` available.
2. Open `inital_analysis.ipynb` in Jupyter or VS Code.
3. Run the notebook cells to clean, preprocess, and tokenize the message data.

## Requirements

- Python 3.10+
- pandas
- The preprocessing utilities from `../scripts/preprocess.py`

## Notes

- The notebook expects the data files to be present in the `../data/` directory relative to this folder.
- Modify or extend the notebook for further analysis as