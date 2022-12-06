from converter.converter import XmlToStlConverter
from parametrs.parametrs import column_name

if __name__ == '__main__':
    main_converter = XmlToStlConverter(column_name=column_name)
    path_dir = main_converter.arguments_parser()
    main_converter.detect_encoding(path_dir)
    main_converter.scanner()

    