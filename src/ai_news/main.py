#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from ai_news.crew import AiNews

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'giraffas'
    }

    AiNews().crew().kickoff(inputs=inputs)

run()
