This project analyses the sentiment and relevance of interview answers.

## Requirements

- Python 3.x
- pandas
- plotly
- textblob
- spaCy
- spaCy English model (`en_core_web_sm`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/iABn0rma1/interview-insights.git
    cd interview-insights
    ```

2. Install the required packages:

    ```bash
    pip install pandas plotly textblob spacy
    ```

3. Download the spaCy English model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Output

- `output.csv`: Contains the analyzed results, including sentiment scores, key phrases, and overall quality scores.
- Displays the frequency distribution of the sentiments.
- Final overall score percentage.
