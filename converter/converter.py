import argparse
import re
from chardet.universaldetector import UniversalDetector


class XmlToStlConverter:
    def __init__(self, column_name):
        self.data = dict()
        self.column_name = column_name

    def detect_encoding(self, path_dir):
        with open(file=path_dir, mode='rb') as temp_xml:
            detector = UniversalDetector()
            for line in temp_xml.readlines():
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            encoding = detector.result['encoding']
                    
        self.data['encoding'] = encoding

        with open(file=f"{self.data['name_out_csv_file']}", mode='a', encoding=self.data['encoding']) as temp_csv:
            temp_csv.write(self.data['name_in_xml_file'] + ';')

    def arguments_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(dest='path_dir', type=str, help='path of the input file')
        args = parser.parse_args()
        path_dir = args.path_dir
        self.data['path_dir'] = path_dir
        pattern = r'(?<=\/)(.+)(?<=\.xml)'
        name_in_xml_file = re.findall(pattern, path_dir)[0]
        self.data['name_in_xml_file'] = name_in_xml_file
        pattern = r'(?<=\/)(.+)(?=\.xml)'
        name_out_csv_file = re.findall(pattern, path_dir)[0]
        self.data['name_out_csv_file'] = name_out_csv_file + '.csv'
        
        return path_dir

    def recursive_scanner(self):
        row_count = 0
        
        with open(file=self.data['path_dir'], mode='r', encoding=self.data['encoding']) as temp_xml:
            count_column_name = len(self.column_name) + 1
            for line in temp_xml.readlines():
                for column_count, pattern in enumerate(self.column_name.values()):
                    answer_regular = re.findall(pattern, line)
                    if answer_regular:
                        with open(file=f"xml/{self.data['name_out_csv_file']}", mode='a', encoding=self.data['encoding']) as temp_csv:
                            if row_count == 0:
                                if column_count + 2 < count_column_name:
                                    end_text = ';'
                                else:
                                    end_text = '\n'
                            temp_csv.write(';;')
                            text = f"{answer_regular[0][1]}{end_text}"
                            temp_csv.write(text)
                        row_count += 1   
                    else:
                        pass
            else:
                row_count = 0


