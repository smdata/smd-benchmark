import argparse
import json
import hashlib

def load_smd(data_path):

    print('data path: {}'.format(data_path))
    with open(data_path) as fi:
        smd_str = fi.read()

    smd_hash_val = hashlib.md5(smd_str).hexdigest()
    print('smd hash value: {}'.format(smd_hash_val))
    smd = json.loads(smd_str)

    return smd

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--data_path',dest='data_path')
    args = parser.parse_args()

    smd = load_smd(args.data_path)
    return smd

if __name__ == '__main__':
    smd = main()
