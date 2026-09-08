from deepeval.metrics import GEval
from deepeval.test_case import SingleTurnParams
from deepeval.models import OllamaModel


def get_judge_model():
    return OllamaModel(
        model="deepseek-r1:1.5b",
        base_url="http://localhost:11434",
        temperature=0,
    )


def get_accuracy_metric(judge_model):
    return GEval(
        name="Accuracy",
        evaluation_steps=[
            "Compare the factual answer in the actual output with the expected output.",
            "The actual output passes if it contains the correct answer from the expected output.",
            "Do not penalize additional relevant information.",
            "Penalize only factual errors, contradictions, or an incorrect main answer.",
        ],
        evaluation_params=[
            SingleTurnParams.ACTUAL_OUTPUT,
            SingleTurnParams.EXPECTED_OUTPUT,
        ],
        threshold=0.7,
        model=judge_model,
    )

def build_context_prompt(input_text, context):
    context_text="/n".join(context)

    return f"""

    Context:{context_text}

    Question:{input_text}

    Answer the quistion using only provided information in the context """