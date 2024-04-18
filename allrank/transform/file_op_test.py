import unittest
import pandas as pd
from io import StringIO
import os
from file_op import subset_csv_file

class TestSubsetCSVFile(unittest.TestCase):
    def setUp(self):
        # Setup a temporary CSV file to use as input
        self.input_csv = 'temp_input.csv'
        self.output_csv = 'temp_output.csv'
        data = """A\tB\tC
1\t2\t3
4\t5\t6
7\t8\t9
10\t11\t12"""
        with open(self.input_csv, 'w') as f:
            f.write(data)

    def tearDown(self):
        # Remove temporary files after tests
        os.remove(self.input_csv)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)

    def test_correct_subset_length(self):
        # Test if the output file has the correct subset length
        subset_csv_file(self.input_csv, self.output_csv, 2)
        output_df = pd.read_csv(self.output_csv, sep='\t')
        self.assertEqual(len(output_df), 2)

    def test_zero_subset_length(self):
        # Test the function with subset_length set to zero
        subset_csv_file(self.input_csv, self.output_csv, 0)
        output_df = pd.read_csv(self.output_csv, sep='\t')
        self.assertEqual(len(output_df), 0)

    def test_large_subset_length(self):
        # Test the function with subset_length larger than the number of rows in the file
        subset_csv_file(self.input_csv, self.output_csv, 10)
        output_df = pd.read_csv(self.output_csv, sep='\t')
        self.assertEqual(len(output_df), 4)  # Only 4 rows are available

    def test_file_not_found_error(self):
        # Test the function with a non-existent input path
        with self.assertRaises(FileNotFoundError):
            subset_csv_file('non_existent_file.csv', self.output_csv, 2)

if __name__ == "__main__":
    unittest.main()


