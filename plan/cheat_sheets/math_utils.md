# math_utils.py Cheat Sheet

## Module Information

- **Module**: math_utils.py
- **Path**: /home/cplan/dev/The-Digital-Hamlet/plan/autogen/math_utils.py

## Description

The `math_utils.py` module provides functions for solving math problems and evaluating math responses.

## Functions

### solve_problem(problem: str, **config) -> str

- **Description**: Solves the math problem.
- **Parameters**:
  - `problem` (str): The problem statement.
  - `config` (dict, optional): The configuration for the API call. Defaults to an empty dictionary.
- **Returns**: The solution to the problem.

### get_answer(solution: Optional[str]) -> Optional[str]

- **Description**: Extracts the answer from the solution string.
- **Parameters**:
  - `solution` (str, optional): The solution string. Defaults to None.
- **Returns**: The answer string.

### is_equiv(str1: Optional[str], str2: Optional[str]) -> float

- **Description**: Checks if two math strings are equivalent.
- **Parameters**:
  - `str1` (str, optional): The first math string.
  - `str2` (str, optional): The second math string.
- **Returns**: A float value indicating the equivalence.

### is_equiv_chain_of_thought(str1: str, str2: str) -> float

- **Description**: Checks if two math strings are equivalent after stripping the solution.
- **Parameters**:
  - `str1` (str): The first math string.
  - `str2` (str): The second math string.
- **Returns**: A float value indicating the equivalence.

### voting_counts(responses)

- **Description**: Counts the votes for each response.
- **Parameters**:
  - `responses` (list): The list of responses.
- **Returns**: A dictionary containing the vote counts for each response.

### eval_math_responses(responses, solution=None, **args)

- **Description**: Evaluates the math responses and calculates success metrics.
- **Parameters**:
  - `responses` (list): The list of responses.
  - `solution` (str, optional): The canonical solution. Defaults to None.
- **Returns**: A dictionary containing the success metrics.

## Constants

### _MATH_PROMPT

- **Description**: The prompt for solving a math problem.

### _MATH_CONFIG

- **Description**: The configuration for solving a math problem.

### _STRIP_STRING_FUNCTIONS

- **Description**: A list of helper functions for stripping math strings.

## Helper Functions

The `math_utils.py` module also includes several helper functions for manipulating math strings. These functions are used internally and may not be directly called by the user.

