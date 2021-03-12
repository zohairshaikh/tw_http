from tw_services import get_challenge_meta, send_solution


def solve_challenge():
    challenge_meta = get_challenge_meta()

    # Goal is to count sentences in the given string
    s = challenge_meta['text']
    solution = 0
    sentences_ending_with_fs = s.split('. ')
    solution += sentences_ending_with_fs[:len(sentences_ending_with_fs) - 1].__len__()

    sentences_ending_with_qm = s.split('? ')
    solution += sentences_ending_with_qm[:len(sentences_ending_with_qm) - 1].__len__()

    solution += 1  # all books have a final sentence xd
    send_solution({
        "output": {
            "sentenceCount": solution
        }
    })


if __name__ == '__main__':
    solve_challenge()
