# AI Customer Review Classifier

## Overview

An LLM-powered sentiment classification application built using Python and the Google Gemini API. The project compares zero-shot and few-shot prompting techniques for customer review classification.

## Objectives

- Classify customer reviews as POSITIVE, NEGATIVE, or NEUTRAL.
- Compare zero-shot and few-shot prompting.
- Evaluate classification accuracy and coverage.
- Implement response validation, API error handling, and rate-limit throttling.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- python-dotenv

## Application Workflow

1. Load the labeled test dataset.
2. Generate zero-shot or few-shot prompts.
3. Send prompts to the Gemini API.
4. Normalize and validate model responses.
5. Compare predictions against ground-truth labels.
6. Calculate and display evaluation metrics.

## Installation

Install the required dependencies:

```bash
pip install google-genai python-dotenv
```

Create a `.env` file in the parent directory of `lesson_8`:

```env
GEMINI_API_KEY=your_api_key
```

Run the application:

```bash
python review_classifier.py
```

## Experimental Configuration

- Model: gemini-3.5-flash-lite
- Temperature: 0.0
- Test dataset: 15 customer reviews
- Sentiment classes: Positive, Negative, Neutral
- Request delay: 5 seconds

## Experimental Results

| Metric | Zero-shot | Few-shot |
|---|---:|---:|
| Total reviews | 15 | 15 |
| Correct predictions | 15 | 15 |
| Incorrect predictions | 0 | 0 |
| Invalid outputs | 0 | 0 |
| API errors | 0 | 0 |
| Accuracy | 100% | 100% |
| Coverage | 100% | 100% |

Both prompting techniques achieved identical accuracy on the experimental dataset, including reviews containing sarcasm, negation, mixed sentiment, and implicit criticism.

## Conclusion

Zero-shot prompting is preferable for this experimental dataset because it achieves identical accuracy using a shorter prompt. However, additional evaluation is required before recommending it for production use.

## Limitations

- Small, manually constructed test dataset.
- Limited representation of real-world customer reviews.
- No measured latency or token consumption comparison.
- No automatic retry mechanism for failed API requests.
- Annotation guidelines are not explicitly included in the prompts.

## Future Improvements

- Evaluate on larger, independently labeled datasets.
- Implement precision, recall, F1-score, and confusion matrix calculations.
- Measure token usage, inference costs, and latency.
- Implement retries with exponential backoff.
- Develop a web-based interface for sentiment classification.