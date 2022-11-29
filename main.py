import argparse
import re


class XmlToStlConverter:
    def __init__(self):
        self.data = dict()

    def detect_encoding(self, path_dir):
        pattern = r'(?<=encoding=")(.*)("\?\>)'
        with open(file=path_dir, mode='r', encoding='windows-1251') as temp_xml:
            searching_line = temp_xml.readline()
            answer_re = re.search(pattern, searching_line)
            encoding = answer_re[1]


        self.data['encoding'] = encoding

    def arguments_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(dest='path_dir', type=str, help='path of the input file')
        args = parser.parse_args()
        path_dir = args.path_dir
        self.data['path_dir'] = path_dir
        
        return path_dir

    def recursive_scanner(self):
        with open(file=self.data['path_dir'], mode='r', encoding=self.data['encoding']) as temp_xml:
            for line in temp_xml.readlines():
                print(line)


if __name__ == '__main__':
    main_converter = XmlToStlConverter()
    path_dir = main_converter.arguments_parser()
    main_converter.detect_encoding(path_dir)

    print(main_converter.data['encoding'])
    print(main_converter.data['path_dir'])
    main_converter.recursive_scanner()

    