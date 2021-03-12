from tw_services import get_challenge_meta, send_solution


def solve_challenge():
    challenge_meta = get_challenge_meta()

    # Goal is to count the vowels in the given string
    s = challenge_meta['text']

    vowels = ['a', 'e', 'i', 'o', 'u']
    solution = {}
    list(map(lambda vowel: solution.update({vowel: s.count(vowel)}), vowels))

    send_solution({
        "output": solution
    })


if __name__ == '__main__':
    solve_challenge()
