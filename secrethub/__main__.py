if __name__ == '__main__': # pragma: no cover
    from os import getenv
    from sys import argv
    from secrethub.secrets import Secret


    color = {
        'error': '\033[1;41m ',
        'warning': '\033[1;43m ',
        'success': '\033[1;42m '
    }
    reset = ' \033[m'
    help_text = """

How to use:
python -m secrethub [option]

Options:
new                 Generate new cryptographic key.
encrypt [message]   Encrypt message
decrypt [key]       Decrypt key
hash [password]
verify [hash] [password]
    """

    if not getenv('SECRET'):
        print(
            color['warning'] +\
            'Environment variable \"SECRET\" not found!' +\
            reset
        )
        gen_new_key = input(
            'Do you want to create new key? [Y/n]'
        )
        if gen_new_key == '' or \
            gen_new_key.upper() == 'y' or \
                gen_new_key.lower() == 'yes':
            new_key = Secret.new()
            print(
                color['success'] + f'New key: { new_key }' + reset
            )
            secret = Secret(
                new_key
            )
    else:
        secret = Secret(key=getenv('SECRET'))
    if len(argv) > 1:
        match argv[1]:
            case 'new':
                print(Secret.new())
            case 'encrypt':
                try:
                    print(
                        secret.encrypt(
                            argv[2]
                        )
                    )
                except IndexError:
                    print(
                        color['error'] + 'There is no message to encrypt,' + reset
                    )
            case 'decrypt':
                try:
                    print(
                        secret.decrypt(
                            argv[2]
                        )
                    )
                except IndexError:
                    print(
                        color['error'] + 'There is no message to encrypt,' + reset
                    )
                except ValueError:
                    print(
                        color['error'] + 'Wrong cryptographic message.' + reset
                    )
            case 'hash':
                try:
                    print(
                        secret.hash(
                            argv[2]
                        )
                    )
                except IndexError:
                    print(
                        color['error'] +\
                            'There is no message to hash,' +\
                            reset +\
                            help_text
                    )
            case 'verify':
                if len(argv) >= 4:
                    try:
                        print(
                            color['success'] +\
                                str(
                                    secret.verify(
                                        argv[2], argv[3]
                                    )
                                ) +\
                                reset
                        )
                    except VerifyMismatchError:
                        print(
                            color['error'] +\
                                'Verify mismatch error.' +\
                                reset +\
                                help_text
                        )
                else:
                    print(
                        color['error'] +\
                            'You need to pass hash and password as arguments.' +\
                            reset +\
                            help_text
                    )
            case _:
                print(
                    color['error'] +\
                        f'Command { argv[1] } not found!' +\
                        reset +\
                        help_text
                )
    else:
        print(help_text)
