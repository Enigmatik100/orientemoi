import shortuuid


def gen_question_code(size=6):
    return f"TEAM-{shortuuid.random(size).upper()}"
