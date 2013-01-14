*** Settings ***
Test Template     Calculate
Library           CalculatorLibrary

*** Test Cases ***    Expression    Expected
Additions             12 + 2 + 2    16
                      2 + -3        -1

Substractions         12 - 2 - 2    8
                      2 - -3        5

Multiplication        12 * 2 * 2    48
                      2 * -3        -6

Division              12 / 2 / 2    3
                      2 / -3        -1

Calculation error     [Template]    Calculation should fail
                      kekkonen      Invalid button 'k'.
                      ${EMPTY}      Invalid expression.
                      1 / 0         Division by zero.

*** Keywords ***
Calculate
    [Arguments]    ${expression}    ${expected}
    Push buttons    C${expression}=
    Result should be    ${expected}

Calculation should fail
    [Arguments]    ${expression}    ${expected}
    ${error} =    Should fail    C${expression}=
    Should be equal    ${expected}    ${error}
