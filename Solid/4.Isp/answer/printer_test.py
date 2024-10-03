import unittest
from unittest.mock import patch, call
from printer import OldFashionedPrinter, NewFashionedPrinter

class TestPrinters(unittest.TestCase):

    @patch('builtins.print')
    def test_old_fashioned_printer(self, mock_print):
        printer = OldFashionedPrinter()
        printer.print("Test Document")
        
        mock_print.assert_called_once_with("Printing document: Test Document")

    @patch('builtins.print')
    def test_new_fashioned_printer_print(self, mock_print):
        printer = NewFashionedPrinter()
        printer.print("Test Document")
        
        mock_print.assert_called_once_with("Printing document: Test Document")

    @patch('builtins.print')
    def test_new_fashioned_printer_scan(self, mock_print):
        printer = NewFashionedPrinter()
        printer.scan("Test Document")
        
        mock_print.assert_called_once_with("Scanning document: Test Document")

    @patch('builtins.print')
    def test_new_fashioned_printer_fax(self, mock_print):
        printer = NewFashionedPrinter()
        printer.fax("Test Document")
        
        mock_print.assert_called_once_with("Faxing document: Test Document")

if __name__ == "__main__":
    unittest.main()
