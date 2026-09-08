from deepeval import assert_test
from deepeval.metrics import HallucinationMetric
from deepeval.test_case import LLMTestCase
from helpers.llm_client import ask_llm
from helpers.test_utils import (get_judge_model, build_context_prompt,)

def test_hallucination_company():

    context = [
        "The company was founded in 2015.",
    ]

    input_text = "When was the company founded?"

    prompt = build_context_prompt(
        input_text,
        context,
    )

    actual_output = ask_llm(prompt)

    test_case=LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        context=context,
    )

    judge_model=get_judge_model()

    hallucination_metric=HallucinationMetric(
        threshold=0.7,
        model=judge_model,
    )

    assert_test(
        test_case=test_case,
        metrics=[hallucination_metric],
    )

def test_hallucination_how_much_employers():

    context=["The company has 500 employees."]

    input_text="How many employees does the company have?"

    prompt=build_context_prompt(input_text, context)

    actual_output=ask_llm(prompt)

    test_case=LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        context=context,
    )

    judge_model=get_judge_model()

    hallucination_metric=HallucinationMetric(
        threshold=0.7,
        model=judge_model,
    )

    assert_test(
        test_case=test_case,
        metrics=[hallucination_metric],
    )

def test_hallucination_company_location():

    context=["Company is located in Berlin"]

    input_text="Where is the company located?"

    prompt=build_context_prompt(input_text, context)

    actual_output=ask_llm(prompt)

    test_case=LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        context=context,
    )

    judge_model=get_judge_model()

    hallucination_metric=HallucinationMetric(
        threshold=0.7,
        model=judge_model,
    )

    assert_test(
        test_case=test_case,
        metrics=[hallucination_metric],
    )