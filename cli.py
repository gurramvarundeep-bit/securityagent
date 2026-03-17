import os

from dotenv import load_dotenv

load_dotenv()
# Support CHATOPENAI_API_KEY as fallback for OPENAI_API_KEY
if not os.getenv("OPENAI_API_KEY") and os.getenv("CHATOPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = os.getenv("CHATOPENAI_API_KEY")

import typer
from workflow import run_security_analysis

app = typer.Typer()

@app.command()
def analyze(event: str):
    """
    Analyze a security event
    """
    result = run_security_analysis(event)
    print(result)

if __name__ == "__main__":
    app()