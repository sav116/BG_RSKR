from win32com import client
excel = client.Dispatch("Excel.Application")
word = client.Dispatch("Word.Application")
doc = word.Documents.Open("C:\\Users\\Artem\\PycharmProjects\\RSKR\\for_table1.docx")
book = excel.Workbooks.Open("C:\\Users\\Artem\\PycharmProjects\\RSKR\\table.xlsx")
sheet = book.Worksheets(1)
sheet.Range("A1:H22").Copy()
doc.Content.PasteExcelTable(False,False,False)
# excel.close()
# sheet.Range("A1:D20").Select      # Selected the table I need to copy
# doc.Content.PasteExcelTable(False, False, False)