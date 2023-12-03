def get_code_gray(vector_size: int) -> list[str]:
    code_gray_ = ["" for _ in range(vector_size)]
    for i in range(vector_size):
        code_gray_[i] = "0" * 2 ** i + "1" * 2 ** i
    for i in range(0, vector_size - 1):
        for _ in range(vector_size - (i + 1)):
            code_gray_[i] += code_gray_[i][::-1]
    code_gray = []
    for i in range(2 ** vector_size):
        code_gray.append("".join([
            code_gray_[index][i]
            for index in range(vector_size)
        ]))
    return code_gray
