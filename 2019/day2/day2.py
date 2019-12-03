def run_program(code):
    """
    Run the intcode program.

    Args:
        code: intcode program, a list of ints

    Returns:
        Processed intcode program

    """
    i = 0
    while True:
        instruction = code[i]
        if instruction == 99:
            break
        elif instruction == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
        elif instruction == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
        else:
            raise RuntimeError("Unknown instruction code")
        i += 4
    return code


def main():
    """Open input and run program."""
    original = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,1,9,23,27,2,27,9,31,1,31,5,35,2,35,9,39,1,39,10,43,2,43,13,47,1,47,6,51,2,51,10,55,1,9,55,59,2,6,59,63,1,63,6,67,1,67,10,71,1,71,10,75,2,9,75,79,1,5,79,83,2,9,83,87,1,87,9,91,2,91,13,95,1,95,9,99,1,99,6,103,2,103,6,107,1,107,5,111,1,13,111,115,2,115,6,119,1,119,5,123,1,2,123,127,1,6,127,0,99,2,14,0,0"
    for i in range(99):
        for j in range(99):
            code = [int(i) for i in original.split(',')]
            code[1] = i
            code[2] = j
            if run_program(code)[0] == 19690720:
                print(i, j)
                break


if __name__ == "__main__":
    main()
