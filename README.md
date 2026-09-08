# Automated LLM Testing with DeepEval

## Project Description

This project demonstrates automated testing of a Large Language Model (LLM) using DeepEval, Pytest, and a locally running Ollama model.

The project evaluates the quality of LLM responses across several dimensions:

- Accuracy & Correctness
- Answer Relevancy
- Hallucination Detection
- Toxicity Testing
- Bias Detection

The LLM used for testing is DeepSeek-R1 1.5B running locally through Ollama.

## Technologies

- Python 3.12
- Pytest
- DeepEval
- Ollama
- DeepSeek-R1 1.5B
- Requests
- GitHub Actions

## Project Structure

llm-testing-deepeval/
├── tests/
│   ├── test_accuracy.py
│   ├── test_relevancy.py
│   ├── test_hallucination.py
│   ├── test_toxicity.py
│   └── test_bias.py
├── helpers/
│   ├── llm_client.py
│   └── test_utils.py
├── .github/
│   └── workflows/
│       └── test.yml
├── .gitignore
├── requirements.txt
└── README.md

## Requirements

Before running the project, make sure the following software is installed:

- Python 3.12 or higher
- Ollama
- Git

The required Python dependencies are listed in `requirements.txt`.

## Installation

### 1. Clone the repository

```powershell
git clone https://github.com/Tima6767/llm-testing-deepeval.git
cd llm-testing-deepeval
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Python dependencies

```powershell
pip install -r requirements.txt
```

### 5. Install and configure Ollama

Install Ollama on your machine and make sure it is running.

Download the required DeepSeek model:

```powershell
ollama pull deepseek-r1:1.5b
```

Configure DeepEval to use the local Ollama model:

```powershell
deepeval set-ollama --model=deepseek-r1:1.5b
```

## Running Tests

Run all tests:

```powershell
pytest
```

Run tests with detailed output:

```powershell
pytest -v
```

Run a specific test category:

```powershell
pytest tests/test_accuracy.py -v
```

For example:

```powershell
pytest tests/test_hallucination.py -v
```

## Test Coverage

The project contains 13 automated LLM test cases divided into five quality dimensions.

| Category | Number of Tests | Metric |
|---|---:|---|
| Accuracy & Correctness | 3 | GEval |
| Answer Relevancy | 3 | AnswerRelevancyMetric |
| Hallucination Detection | 3 | HallucinationMetric |
| Toxicity Testing | 2 | ToxicityMetric |
| Bias Detection | 2 | BiasMetric |
| **Total** | **13** | |

## DeepEval Metrics

### GEval

Used to evaluate the accuracy and correctness of the LLM response against an expected answer.

### AnswerRelevancyMetric

Evaluates whether the generated answer is relevant to the user's input and does not contain unnecessary information.

### HallucinationMetric

Evaluates whether the generated response contains information that is not supported by the provided context.

### ToxicityMetric

Evaluates whether the generated response contains toxic or harmful language.

### BiasMetric

Evaluates whether the generated response contains biased statements related to areas such as gender, politics, ethnicity, or geography.

The metrics use a threshold of `0.7`.

## Test Case Structure

Each test creates an `LLMTestCase` containing the information required by the selected metric.

Depending on the metric, a test case can contain:

- `input`
- `actual_output`
- `expected_output`
- `context`

The `actual_output` is generated dynamically by the local LLM.

## Local LLM Architecture

The project uses Ollama as a local LLM runtime.

The general test flow is:

```text
Test Input
    ↓
Ollama / DeepSeek-R1 1.5B
    ↓
Actual Output
    ↓
DeepEval Metric
    ↓
Local Judge Model
    ↓
PASS / FAIL
```

## Report Generation

Tests can be executed with Pytest's verbose output:

```powershell
pytest -v
```

The test results are displayed directly in the terminal.

## Continuous Integration

The project uses GitHub Actions to automatically run the test suite on repository events.

The workflow is located at:

```text
.github/workflows/test.yml
```

Secrets required by the CI pipeline are stored securely in GitHub repository settings and are not committed to the repository.

## Notes

The project uses a local DeepSeek-R1 1.5B model both for generating test responses and for evaluating them through DeepEval.

Because the model is relatively small, LLM-as-a-judge metrics can occasionally produce inconsistent evaluations. Test prompts and evaluation criteria are therefore designed to make the expected behavior as clear as possible.
