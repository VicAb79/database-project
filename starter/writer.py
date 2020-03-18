from enum import Enum
import csv

class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """
    display = 'display'
    csv_file = 'csv_file'

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported output formatting options.
    """

    def __init__(self):
        # TODO: How can we use the OutputFormat in the NEOWriter?
        pass

    def write(self, format, data, **kwargs):
        """
        Generic write interface that, depending on the OutputFormat selected calls the
        appropriate instance write function

        :param format: str representing the OutputFormat
        :param data: collection of NearEarthObject or OrbitPath results
        :param kwargs: Additional attributes used for formatting output e.g. filename
        :return: bool representing if write successful or not
        """
        # TODO: Using the OutputFormat, how can we organize our 'write' logic for output to stdout vs to csvfile
        # TODO: into instance methods for NEOWriter? Write instance methods that write() can call to do the necessary
        # TODO: output format.
        if format == OutputFormat.display.value:
            print("OK")
            value = list(data[0].__dict__.keys())
            print (*value, sep=('     :    '))
            for d in data:
                print(*d.__dict__.values(), sep=(':    '))
            return True

        if format == OutputFormat.csv_file.value:
            print("Writing to csv file ....")
            keys = list(data[0].__dict__.keys())
            with open('output.csv', 'w') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                for d in data:
                    writer.writerow(d.__dict__)
            return True