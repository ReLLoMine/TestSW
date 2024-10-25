Feature: Matrix calculator
    Scenario: Two matrix addition
        Given a matrix "[[1, 2], [3, 4]]"
        When I add a matrix "[[1, 2], [3, 4]]"
        Then the result of add should be "[[2, 4], [6, 8]]"

    Scenario: Two matrix subtraction
        Given a matrix "[[1, 2], [3, 4]]"
        When I subtract a matrix "[[1, 2], [3, 4]]"
        Then the result of subtract should be "[[0, 0], [0, 0]]"

    Scenario: Two matrix multiplication
        Given a matrix "[[1, 2], [3, 4]]"
        When I multiply a matrix "[[1, 2], [3, 4]]"
        Then the result of multiply should be "[[7, 10], [15, 22]]"