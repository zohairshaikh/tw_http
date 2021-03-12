from tw_services import get_challenge_meta, send_solution


def solve_challenge():
    challenge_meta = get_challenge_meta()

    # Goal is to count the chars in the given string
    s = challenge_meta['text']
    solution = len(s)

    send_solution({
        "output": {
            "count": solution
        }
    })


if __name__ == '__main__':
    solve_challenge()
