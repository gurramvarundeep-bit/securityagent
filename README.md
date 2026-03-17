# Security Agent

A security event analysis agent that classifies threats, gathers intel, recommends responses, and produces refined reports.

## Setup

1. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

```bash
python cli.py "suspicious login attempt from unknown IP"
# or
python -m cli "suspicious login attempt from unknown IP"
```
