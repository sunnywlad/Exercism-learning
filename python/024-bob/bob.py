def is_question(hey_bob):
    return hey_bob.strip()[-1] == '?'

def is_yelling(hey_bob):
    return hey_bob.upper() == hey_bob and any(s.isalpha() for s in hey_bob)

def is_silent(hey_bob):
    return hey_bob.strip() == ''

def response(hey_bob):
    if is_silent(hey_bob):
        return "Fine. Be that way!"
    elif is_question(hey_bob) and is_yelling(hey_bob):
        return "Calm down, I know what I'm doing!"
    elif is_question(hey_bob):
        return "Sure."
    elif is_yelling(hey_bob):
        return "Whoa, chill out!"
    else:
        return "Whatever."
