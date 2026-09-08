from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from helpers.llm_client import ask_llm
from helpers.test_utils import get_judge_model, get_accuracy_metric

def test_accuracy_capital_of_france():

    input_text = "What is the capital of France?"
    expected_output = "The capital of France is Paris."
    actual_output = ask_llm(input_text)

    test_case = LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        expected_output=expected_output,
    )

    judge_model=get_judge_model()

    accuracy_metric=get_accuracy_metric(judge_model)

    assert_test(
        test_case=test_case,
        metrics=[accuracy_metric],
    )


def test_accuracy_water_formula():

    input_text = "What is the chemical formula for water?"
    expected_output = "The chemical formula for water is H2O."
    actual_output = ask_llm(input_text)

    test_case = LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        expected_output=expected_output,
    )

    judge_model=get_judge_model()

    accuracy_metric=get_accuracy_metric(judge_model)

    assert_test(
        test_case=test_case,
        metrics=[accuracy_metric],
    )

def test_accuracy_simple_math():

    input_text='What is 427 plus 573?'
    expected_output='1000'
    actual_output=ask_llm(input_text)

    test_case = LLMTestCase(
        input=input_text,
        actual_output=actual_output,
        expected_output=expected_output,
    )
    
    judge_model=get_judge_model()

    accuracy_metric=get_accuracy_metric(judge_model)

    assert_test(
        test_case=test_case,
        metrics=[accuracy_metric],
    )
    