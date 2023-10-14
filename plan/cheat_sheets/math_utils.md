# math_utils.py

This module provides functions for solving math problems and evaluating math responses.

## Functions

- `solve_problem(problem: str, **config) -> str`: Solves the math problem.
- `get_answer(solution: Optional[str]) -> Optional[str]`: Extracts the answer from the solution string.
- `is_equiv(str1: Optional[str], str2: Optional[str]) -> float`: Checks if two math strings are equivalent.
- `is_equiv_chain_of_thought(str1: str, str2: str) -> float`: Checks if two math strings are equivalent after stripping the solution.
- `voting_counts(responses)`: Counts the votes for each response.
- `eval_math_responses(responses, solution=None, **args)`: Evaluates the math responses and calculates success metrics.

## Constants

- `_MATH_PROMPT`: The prompt for solving a math problem.
- `_MATH_CONFIG`: The configuration for solving a math problem.
- `_STRIP_STRING_FUNCTIONS`: A list of helper functions for stripping math strings.

