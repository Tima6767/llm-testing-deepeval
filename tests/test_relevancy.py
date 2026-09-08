from helpers.test_utils import get_judge_model
from deepeval.metrics import AnswerRelevancyMetric
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from helpers.llm_client import ask_llm

def test_relevancy_python():

    input_text='What is Python?'
    actual_output=ask_llm(input_text)

    test_case=LLMTestCase(
        input=input_text,
        actual_output=actual_output,
    )

    judge_model=get_judge_model()

    relevancy_metric=AnswerRelevancyMetric(
        threshold=0.7,
        model=judge_model,
    )

    assert_test(
        test_case=test_case,
        metrics=[relevancy_metric],
    )

def test_relevancy_first_computer():

    input_text="When first computer was invented?"
    actual_output=ask_llm(input_text)

    test_case=LLMTestCase(
        input=input_text,
        actual_output=actual_output,
    )

    judge_model=get_judge_model()

    relevancy_metric=AnswerRelevancyMetric(
        threshold=0.7,
        model=judge_model,
    )

    assert_test(
        test_case=test_case,
        metrics=[relevancy_metric],
    )

def test_relevancy_end_of_world_war_two():

    input_text="When did World War 2 end?"
    actual_output=ask_llm(input_text)

    test_case=LLMTestCase(
        input=input_text,
        actual_output=actual_output,
    )

    judge_model=get_judge_model()

    relevancy_metric=AnswerRelevancyMetric(
        threshold=0.7,
        model=judge_model,
    )

    assert_test(
        test_case=test_case,
        metrics=[relevancy_metric],
    )