
## Project Structure

```
.
├── .env
├── .gitignore
├── channel_scraper.session
├── channels.txt
├── labeled_data.txt
├── README.md
├── requirements.txt
├── data/
│   ├── cleaned_messages.csv
│   ├── cleaned_messages.csv.dvc
│   ├── improved_labeled.txt
│   ├── improved_labeled.txt.dvc
│   ├── labeled_data.txt
│   ├── labeled_data.txt.dvc
│   ├── message_tokens.txt
│   ├── message_tokens.txt.dvc
│   └── ...
├── notebooks/
│   ├── analysis_channels.ipynb
│   ├── finetuning.ipynb
│   ├── inital_analysis.ipynb
│   ├── model.ipynb
│   └── README.md
├── scripts/
│   ├── preprocess.py
│   ├── scrapy.py
│   └── README.md
├── src/
├── tests/
│   └── test_preprocess.py
└── .github/
    └── workflows/
        └── ci.yml
```

> **Reminder:**  
> Before running model fine-tuning, ensure Google Drive is configured and mounted to store trained models and checkpoints. This is required for saving outputs during the fine-tuning process.


- [`scripts/scrapy.py`](scripts/scrapy.py): Scrapes messages from Telegram channels and saves them to `data/messages.csv`.
- [`scripts/preprocess.py`](scripts/preprocess.py): Provides text preprocessing utilities for cleaning and normalizing messages.
- [`notebooks/inital_analysis.ipynb`](notebooks/inital_analysis.ipynb): Data cleaning and preprocessing.
- [`notebooks/analysis_channels.ipynb`](notebooks/analysis_channels.ipynb): Channel-level analysis (posting frequency, views, price extraction, lending score).
- [`notebooks/finetuning.ipynb`](notebooks/finetuning.ipynb): Fine-tuning and evaluating NER models.
- [`notebooks/model.ipynb`](notebooks/model.ipynb): Model loading, splitting, comparison, and explainability (LIME).
- `channels.txt`: List of Telegram channel usernames to scrape.
- `.env`: Environment variables for Telegram API credentials.

---



---

## Usage


### 1. Data Cleaning & Preprocessing

- Use [`scripts/preprocess.py`](scripts/preprocess.py) for text cleaning and language processing.
- Run [`notebooks/inital_analysis.ipynb`](notebooks/inital_analysis.ipynb) to clean, preprocess, and tokenize the message data. This notebook saves cleaned messages to `data/cleaned_messages.csv` and tokens to `data/message_tokens.txt`.

### 2. Channel Analysis

- Use [`notebooks/analysis_channels.ipynb`](notebooks/analysis_channels.ipynb) to analyze channel activity, average views, price extraction, and compute a "lending score" for each channel.

### 3. NER Model Training & Evaluation

- Use [`notebooks/finetuning.ipynb`](notebooks/finetuning.ipynb) and [`notebooks/model.ipynb`](notebooks/model.ipynb) to:
  - Load and split labeled NER data.
  - Fine-tune and compare multiple transformer models (e.g., XLM-RoBERTa, DistilBERT, BERT).
  - Evaluate models using seqeval metrics (precision, recall, F1).
  - Run inference and explain predictions using LIME.

---

## Notes

- Ensure your Telegram API credentials are correct.
- The first run may prompt you for Telegram login/verification.
- Data files are saved in the `data/` directory.
- For custom preprocessing, modify or extend the functions in [`scripts/preprocess.py`](scripts/preprocess.py).
- Notebooks expect data files to be present in the `data/` directory.

## License

See [LICENSE](LICENSE) for details.