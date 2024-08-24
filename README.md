# SummarEase

**SummarEase** is a text summarization tool that leverages a T5 small base model fine-tuned on the CNN dataset. This tool is designed to provide concise and accurate summaries of large bodies of text, making it easier to digest and understand key points quickly.

## Features

- **Accurate Summarization**: Provides concise summaries of long texts using state-of-the-art NLP techniques.
- **URL Summarization**: Enter a URL, and SummarEase will fetch and summarize the content of the webpage using BeautifulSoup.
- **User-Friendly Interface**: An intuitive frontend that allows users to easily input text or URLs and receive summaries.
- **Customizable**: The project is open-source, allowing contributors to modify and enhance its capabilities.

## Installation

### 1. Clone the Repository

First, clone the SummarEase repository to your local machine:

```bash
git clone https://github.com/yourusername/SummarEase.git
cd SummarEase
```

### 2. Install Dependencies

Next, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

After installing the dependencies, you can run the application with:

```bash
flask run
```

### 4. Access the Application

Open your web browser and go to:

```
http://127.0.0.1:5000/
```

## Usage

### Text Summarization

1. Input the text you want to summarize in the provided text area.
2. Click on the "Summarize" button.
3. The generated summary will appear below the input area.

### URL Summarization

1. Enter the URL of the webpage you want to summarize.
2. Click on the "Summarize" button.
3. The summary of the webpage content will be displayed.

## Contribution Guidelines

We welcome contributions from the community! Here’s how you can contribute:

1. **Fork the Repository**: Click the "Fork" button on the top right of the repository page.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/SummarEase.git
   ```
3. **Create a New Branch**: Create a branch for your feature or bug fix.
   ```bash
   git checkout -b feature-name
   ```
4. **Make Your Changes**: Implement your feature or fix the bug.
5. **Commit and Push**: Commit your changes and push them to your fork.
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature-name
   ```
6. **Submit a Pull Request**: Go to the original repository and click "New Pull Request".
7. ## License

SummarEase © 2024 by Rushab Rasik Karania is licensed under CC BY-NC-SA 4.0.

This means that you are free to share, adapt, and build upon the software non-commercially, as long as you credit the original author and license your new creations under the same terms.

To view a copy of this license, visit [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en).






