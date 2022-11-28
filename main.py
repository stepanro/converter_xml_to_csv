import argparse
import re


class Parser:
    def __init__(self):
        data = dict()

    def detect_uncoding(self, input_obj):
        pattern = r'(?<=encoding=")(.*)("\?\>)'
        searching_line = input_obj.readline()
        answer_re = re.search(pattern, searching_line)

        return answer_re[1]

    def arguments_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(dest='path_dir', type=str, help='path of the input file')

        return parser






if __name__ == '__main__':
    main_parser = Parser()

    parser = arguments_parser()
    args = parser.parse_args()
    path_dir = args.path_dir

    with open(file=path_dir, mode='r') as temp_xml:
        uncoding = detect_uncoding(temp_xml)
        print(uncoding)
