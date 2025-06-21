# Amharic E-commerce Data Extractor

This project extracts, preprocesses, and analyzes Amharic e-commerce data from Telegram channels.

## Project Structure

- `scripts/`
  - [`scrapy.py`](scripts/scrapy.py): Scrapes messages from Telegram channels and saves them to `data/messages.csv`.
  - [`preprocess.py`](scripts/preprocess.py): Provides text preprocessing utilities.
- `.env`: Environment variables for Telegram API credentials.

## Setup

2. **Configure environment variables** in a `.env` file:
    ```
    APP_KEY=your_telegram_api_hash
    APP_ID=your_telegram_api_id
    PHONE=your_phone_number
    ```

3. **Add Telegram channels** to `channels.txt`, one per line.

## Usage

To scrape messages from the listed channels and save them to `data/messages.csv`, run:

```sh
python scripts/scrapy.py
```

This will:
- Connect to Telegram using your credentials.
- Fetch messages from each channel in `channels.txt`.
- Save the combined messages to `data/messages.csv`.

## Preprocessing & Analysis

- Use [`preprocess.py`](scripts/preprocess.py) for text cleaning and language processing.
- See [`notebooks/inital_analysis.ipynb`](notebooks/inital_analysis.ipynb) for data exploration and further processing steps.

## Notes

- Ensure your Telegram API credentials are correct.
- The first run may prompt you for Telegram login/verification.
- Data files are saved in the `data/` directory.

## License

See [LICENSE](LICENSE) for details.