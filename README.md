
# Selenium Web Scraper for Downloading PDFs from MISTI

This project is a Python script that automates the process of extracting and downloading PDF documents from the [MISTI website](https://www.misti.gov.kh/documents?type=law). The script uses Selenium for web scraping and `requests` to download the PDF files.

## Features
- Scrapes the document list from the MISTI webpage.
- Extracts the URLs of PDFs listed on the page.
- Downloads the PDFs and saves them to a specified directory.

## Prerequisites

1. **Python 3.9+**: Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. **Selenium WebDriver**: You need to install a WebDriver (e.g., ChromeDriver) that matches your Chrome browser version.
   - Download ChromeDriver: https://sites.google.com/chromium.org/driver/
   - Make sure to add it to your system's PATH.

3. **Required Python Packages**:
   - `selenium`
   - `requests`

   You can install them using pip:

   ```bash
   pip install selenium requests
   ```

## Setup and Usage

1. **Clone the Repository** (or create a Python file with the code):
   ```bash
   git clone git@github.com:SB-Menghorng/Test-Scaping.git
   ```

2. **Modify the download path**:
   Edit the `save_path` in the script to set the location where PDFs will be downloaded. For example, in the script:
   ```python
   save_path = os.path.join("D:/Help/Downloads", filename)
   ```
   Replace `D:/Help/Downloads` with your desired download location.

3. **Run the Script**:
   You can run the script using the following command:
   ```bash
   python selenium_script.py
   ```

   This will start the Chrome browser, navigate to the specified URL, scrape the list of documents, and download the PDFs.

## How It Works

- The script navigates to the [MISTI law documents page](https://www.misti.gov.kh/documents?type=law).
- It uses XPath and tag names to find the container holding the document links.
- Each document card is processed to extract the PDF link.
- The script downloads the PDFs using `requests` and saves them in the specified directory.

## Important Notes

- **Wait Time**: The script includes a `time.sleep(15)` to ensure that the browser has enough time to load the page. You can adjust the wait time depending on your internet speed.
- **WebDriver Compatibility**: Ensure your ChromeDriver version matches your Chrome browser version, or the script will fail to run properly.

## Example Output

The script will print out the downloaded PDF's filename:

```
PDF downloaded successfully and saved as document1.pdf
```

## Troubleshooting

1. **ChromeDriver Issues**:
   - If you encounter errors with the WebDriver, ensure that you have the correct version installed and that it is in your system's PATH.

2. **Element Not Found**:
   - If the script cannot find elements on the page, check if the page structure has changed. You may need to adjust the XPath or tag names.

3. **Connection Issues**:
   - If the PDF fails to download, ensure that the website and the link are accessible and that your internet connection is stable.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
