def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}

    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts[0], parts[1], parts[2]

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(operand1), len(operand2))
        arranged_problems["top"].append(operand1.rjust(max_length + 2))
        arranged_problems["bottom"].append(operator + operand2.rjust(max_length + 1))
        arranged_problems["line"].append("-" * (max_length + 2))

        if display_answers:
            if operator == "+":
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            arranged_problems["result"].append(result.rjust(max_length + 2))

    if display_answers:
        arranged_problems = [
            "    ".join(arranged_problems["top"]),
            "    ".join(arranged_problems["bottom"]),
            "    ".join(arranged_problems["line"]),
            "    ".join(arranged_problems["result"]),
        ]
    else:
        arranged_problems = [
            "    ".join(arranged_problems["top"]),
            "    ".join(arranged_problems["bottom"]),
            "    ".join(arranged_problems["line"]),
        ]

    return "\n".join(arranged_problems)
