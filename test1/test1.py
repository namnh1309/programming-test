#!/usr/bin/env python2
import os
import re


BUFSIZE = 4096


class LagestTrianglePath(object):
    tempfile = "temp.txt"
    outfile = "output.txt"

    def __init__(self, filename, delimiter=" "):
        self.filename = filename
        self.delimiter = delimiter

    def reverse_lines(self, filename, buffsize=BUFSIZE):
        """
        Reading file line by line in reverse order.
        """
        with open(filename, "rb") as f:
            f.seek(0, os.SEEK_END)
            position = f.tell()
            remainder = ""
            while position:
                sz = min(buffsize, position)
                position -= sz
                f.seek(position)
                buff = f.read(sz) + remainder
                try:
                    i = buff.index('\n')
                    for line in buff[i+1:].split("\n")[::-1]:
                        if line:
                            yield line
                    remainder = buff[:i]
                except ValueError:
                    remainder = buff[:i]
            if remainder:
                yield remainder

    def parse_line(self, line):
        """
        Parse line of file in format '1 2 3 4 5'.
        Return list of number.
        """
        return [int(element) for element in re.split(r'\s+', line) if element]

    @staticmethod
    def get_path_for_one_element(curr_line, prev_line, i):
        """
        From an element in line get the element in next line which product
        expensive path.
        """
        if prev_line[i] > prev_line[i+1]:
            return (
                (curr_line[i], i), curr_line[i] + prev_line[i]
                )
        else:
            return (
                (curr_line[i], i + 1), curr_line[i] + prev_line[i+1]
                )

    def get_max_path_line(self, curr_line, prev_line):
        """
        Make expensive path for all elements in line.
        """
        paths = []
        line = []
        for i, num in enumerate(curr_line):
            path, new_element = self.get_path_for_one_element(curr_line,
                                                              prev_line, i)
            paths.append(path)
            line.append(new_element)
        return paths, line

    def get_max_path(self):
        with open(self.tempfile, 'w') as tempfile:
            for i, line in enumerate(self.reverse_lines(self.filename)):
                line = self.parse_line(line)
                if i == 0:
                    prev_line = line
                    continue
                curr_line = line
                path, prev_line = self.get_max_path_line(curr_line, prev_line)
                tempfile.write(
                    ' '.join(["{0},{1}".format(ele, i) for ele, i in path]) +
                    '\n'
                    )

    def parse_result_line(self, line):
        """
        """
        eles = [ele for ele in re.split(r'\s+', line) if ele]
        return [
            (int(ele.split(',')[0]), int(ele.split(',')[1])) for ele in eles
            ]

    def last_line_of_input_file(self):
        inputfile = self.reverse_lines(self.filename)
        last_line_of_input_file = inputfile.next()
        return self.parse_line(last_line_of_input_file)

    def write_results_2_file(self, results):
        with open(self.outfile, 'wb') as f:
            f.write('-'.join(str(num) for num in results))

    def remove_temp_file(self):
        pass

    def compute_max_path(self):
        self.get_max_path()

        last_line_of_input_file = self.last_line_of_input_file()

        tempfile_reverse = self.reverse_lines(self.tempfile)

        path = []
        max_value = 0
        next_num_index = 0

        for result_line in tempfile_reverse:
            results = self.parse_result_line(result_line)
            num, next_num_index = results[next_num_index]
            max_value += num * num
            path.append(num)

        num = last_line_of_input_file[next_num_index]
        max_value += num * num
        path.append(num)

        self.write_results_2_file(path)

        print "find maximun path successful"
        print "path in file output.txt"


class LagestTrianglePathWithNewRulerPath(LagestTrianglePath):
    pass


if __name__ == "__main__":
    import sys
    test = LagestTrianglePath(sys.argv[1])

    # test reverse line
    # for l in test.reverse_lines():
    #     print l

    # test parse line
    # test_line = "  1 2  3  4   5  "
    # print test.parse_line(test_line)

    # test get path method

    # curr_line = [1]
    # prev_line = [3, 4]
    # print test.get_path_for_one_element(curr_line, prev_line, 0)

    # curr_line = [9, 8]
    # prev_line = [5, 2, 9]
    # print test.get_path_for_one_element(curr_line, prev_line, 1)

    # test get max path
    # curr_line = [1]
    # prev_line = [3, 4]
    # print test.get_max_path_line(curr_line, prev_line)

    # curr_line = [9, 8]
    # prev_line = [5, 2, 9]
    # print test.get_max_path_line(curr_line, prev_line)

    # test
    # test.get_max_path()

    # test
    # test_line = "  1,11 2,22  3,33  4,44   5,55  "
    # print test.parse_result_line(test_line)

    # test
    # print test.last_line_of_input_file()

    # test
    test.compute_max_path()
