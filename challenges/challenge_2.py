from tw_services import get_challenge_meta, send_solution


def solve_challenge():
    challenge_meta = get_challenge_meta()

    # Goal is to count words in the given string
    s = challenge_meta['text']
    solution = s.split(' ').__len__()

    send_solution({
        "output": {
            "wordCount": solution
        }
    })


if __name__ == '__main__':
    solve_challenge()
