from behave import given, when, then
import numpy as np

from calc import add_matrices, subtract_matrices, multiply_matrices


@given('a matrix "{matrix}"')
def step_given_matrix(context, matrix):
    context.matrix = np.array(eval(matrix))


@when('I add a matrix "{matrix}"')
def step_when_add_matrices(context, matrix):
    context.solution = add_matrices(context.matrix, np.array(eval(matrix)))


@then('the result of add should be "{matrix}"')
def step_then_add_solution(context, matrix):
    matrix = np.array(eval(matrix))
    np.testing.assert_array_equal(context.solution, matrix, f"Expected {matrix}, but got {context.solution}")


@when('I subtract a matrix "{matrix}"')
def step_when_subtruct_matrices(context, matrix):
    context.solution = subtract_matrices(context.matrix, np.array(eval(matrix)))


@then('the result of subtract should be "{matrix}"')
def step_then_subtruct_solution(context, matrix):
    matrix = np.array(eval(matrix))
    np.testing.assert_array_equal(context.solution, matrix, f"Expected {matrix}, but got {context.solution}")


@when('I multiply a matrix "{matrix}"')
def step_when_multiply_matrices(context, matrix):
    context.solution = multiply_matrices(context.matrix, np.array(eval(matrix)))


@then('the result of multiply should be "{matrix}"')
def step_then_multiply_solution(context, matrix):
    matrix = np.array(eval(matrix))
    np.testing.assert_array_equal(context.solution, matrix, f"Expected {matrix}, but got {context.solution}")
