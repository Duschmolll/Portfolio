def arithmetic_arranger(*problemsArray):
    import re

    arranged_problems = ""
    firstLine = ""
    secondLine = ""
    thirdLine = ""
    fourthLine = ""
    result = None

    # Looping through all the problems to resolve.
    for i in range(len(problemsArray[0])):
        problem = ""
        diverder = ""
        upSpacer = 0
        downSpacer = 0
        spacer = 0
        result = None

        # Checking is result need to be calculated.
        try:
            if isinstance(problemsArray[1], bool) is True and problemsArray[1] is True:
                problem = problemsArray[0][i].split()
                result = eval(
                    problem[0] + problem[1] + problem[2], {"__builtins__": None}
                )
            elif (
                isinstance(problemsArray[1], bool) is True and problemsArray[1] is False
            ):
                problem = problemsArray[0][i].split()
        except IndexError:
            problem = problemsArray[0][i].split()

        # Checking if inputs are valid.
        if (
            len(re.findall("[^0-9]", problem[0])) != 0
            or len(re.findall("[^0-9]", problem[2])) != 0
        ):
            return "Error: Numbers must only contain digits."
        elif len(problemsArray[0]) >= 6:
            return "Error: Too many problems."
        elif len(re.findall("[^+-]", problem[1])) != 0:
            return "Error: Operator must be '+' or '-'."
        elif len(problem[0]) >= 5 or len(problem[2]) >= 5:
            return "Error: Numbers cannot be more than four digits."

        # Adding space between problems.
        if i > 0:
            spacer = 4

        # Getting the value for formatting answer.
        if len(problem[0]) < len(problem[2]):
            upSpacer = len(problem[2]) + 2 + spacer
            downSpacer = len(problem[2]) + 1
            for x in range(len(problem[2]) + 2):
                diverder += "-"
        else:
            upSpacer = len(problem[0]) + 2 + spacer
            downSpacer = len(problem[0]) + 1
            for x in range(len(problem[0]) + 2):
                diverder += "-"

        # Formatting the answers.
        firstLine += "{:>{x}}".format(problem[0], x=upSpacer)
        secondLine += "{:>{y}}{:>{x}}".format(
            problem[1], problem[2], x=downSpacer, y=spacer + 1
        )
        thirdLine += "{:>{x}}".format(diverder, x=spacer + len(diverder))
        fourthLine += "{:>{x}}".format(str(result), x=upSpacer)

    # Putting all together and return the value.
    if result is not None:
        arranged_problems = (
            firstLine + "\n" + secondLine + "\n" + thirdLine + "\n" + fourthLine
        )
    else:
        arranged_problems = firstLine + "\n" + secondLine + "\n" + thirdLine
    return arranged_problems
