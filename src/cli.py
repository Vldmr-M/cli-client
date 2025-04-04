import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sender", required=True)
    parser.add_argument('-r', '--recipient', required=True)
    parser.add_argument('-m', '--message', required=True)

    args = parser.parse_args()
    return args.sender, args.recipient, args.message
