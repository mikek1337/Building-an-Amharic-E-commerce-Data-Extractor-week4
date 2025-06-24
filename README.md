# Building an Amharic E-commerce Data Extractor

This project focuses on fine-tuning  LLM’s for Amharic Named Entity Recognition (NER) system that extracts key business entities such as product names, prices, and Locations, from text, images, and documents shared across these Telegram channels. The extracted data will be used to populate EthioMart's centralised database, making it a comprehensive e-commerce hub.

# Amharic E-commerce Data Extractor

This project extracts, preprocesses, and analyzes Amharic e-commerce data from Telegram channels. It is designed to help collect and clean data for downstream analysis and machine learning tasks.

## Project Structure

```
.
├── .env
├── .gitignore
├── channel_scraper.session
├── channels.txt
├── labeled_data.txt
├── README.md
├── data/
│   ├── cleaned_messages.csv
│   ├── message_tokens.txt
│   └── messages.csv
├── notebooks/
│   ├── __init__.py
│   ├── channel_scraper.session
│   ├── inital_analysis.ipynb
│   └── README.md
├── scripts/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── README.md
│   ├── scrapy.py
│   └── __pycache__/
│       └── preprocess.cpython-313.pyc
├── src/
├── tests/
│   ├── __init__.py
│   └── test_preprocess.py
└── .github/
    └── workflows/
        └── ci.yml
```

- [`scripts/scrapy.py`](scripts/scrapy.py): Scrapes messages from Telegram channels and saves them to `data/messages.csv`.
- [`scripts/preprocess.py`](scripts/preprocess.py): Provides text preprocessing utilities for cleaning and normalizing messages.
- [`notebooks/inital_analysis.ipynb`](notebooks/inital_analysis.ipynb): Jupyter notebook for data exploration and further processing.
- `channels.txt`: List of Telegram channel usernames to scrape.
- `.env`: Environment variables for Telegram API credentials.

## Setup

1. **Install dependencies**  
   Make sure you have Python 3.10+ and pip installed. Then run:
   ```sh
   pip install -r requirements.txt
   ```

2. **Configure environment variables**  
   Create a `.env` file in the project root with your Telegram API credentials:
   ```
   APP_KEY=your_telegram_api_hash
   APP_ID=your_telegram_api_id
   PHONE=your_phone_number
   ```

3. **Add Telegram channels**  
   List the Telegram channels you want to scrape in [`channels.txt`](channels.txt), one per line (e.g., `@ZemenExpress`).

## Usage

To scrape messages from the listed channels and save them to `data/messages.csv`, run:

```sh
python scripts/scrapy.py
```

## DVC Setup with Google Drive

To version and share your data and models, this project uses [DVC](https://dvc.org/) with Google Drive as remote storage.

### Steps:

1. **Install DVC with Google Drive support:**
    ```sh
    pip install dvc[gdrive]
    ```

2. **Initialize DVC in your project (if not already done):**
    ```sh
    dvc init
    ```

3. **Add your data files to DVC tracking:**
    ```sh
    dvc add ../data/messages.csv
    dvc add ../data/cleaned_messages.csv
    dvc add ../data/message_tokens.txt
    ```

4. **Configure Google Drive as a remote:**
    ```sh
    dvc remote add -d gdrive_remote gdrive://1ExRdlctDJAd7ajYCv0DnbxWODZVeaybf 
    ```

5. **Push your data to Google Drive:**
    ```sh
    dvc push
    ```

6. **To pull data on another machine:**
    ```sh
    dvc pull
    ```

> **Note:**  
> The first time you push or pull, DVC will prompt you to authenticate with Google Drive.


This will:
- Connect to Telegram using your credentials.
- Fetch messages from each channel in `channels.txt`.
- Save the combined messages to `data/messages.csv`.

## Preprocessing & Analysis

- Use [`scripts/preprocess.py`](scripts/preprocess.py) for text cleaning and language processing.
- See [`notebooks/inital_analysis.ipynb`](notebooks/inital_analysis.ipynb) for data exploration, cleaning, and further processing steps.

## Notes

- Ensure your Telegram API credentials are correct.
- The first run may prompt you for Telegram login/verification.
- Data files are saved in the `data/` directory.
- For custom preprocessing, modify or extend the functions in [`scripts/preprocess.py`](scripts/preprocess.py).

## Testing

Unit tests for preprocessing are in [`tests/test_preprocess.py`](tests/test_preprocess.py). Run them with:

```sh
pytest
```

## License

See [LICENSE](LICENSE) for