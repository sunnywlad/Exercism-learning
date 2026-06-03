def reverse(text):
    return ''.join([text[-ind] for ind in range(1, len(text) + 1)])
