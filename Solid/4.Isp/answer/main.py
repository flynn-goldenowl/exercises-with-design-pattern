from printer import OldFashionedPrinter, NewFashionedPrinter

if __name__ == '__main__':
    old_printer = OldFashionedPrinter()
    old_printer.print('Document 1')
    
    new_printer = NewFashionedPrinter()
    new_printer.print('Document 2')
    new_printer.scan('Document 3')
    new_printer.fax('Document 4')