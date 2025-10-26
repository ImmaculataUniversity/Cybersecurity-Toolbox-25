import ezsheets

# This triggers the OAuth flow and creates token files
ezsheets.init()

# Create a new blank spreadsheet
ss = ezsheets.Spreadsheet()
ss.title = 'My New Sheet'

# Load an existing spreadsheet by URL or ID
ss = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/your_sheet_id')

# Get the first sheet
sheet = ss.sheets[0]

# Read and write individual cells
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
print(sheet['A1'])  # Output: 'Name'

sheet[1, 2] = 'Alice'  # Column 1, Row 2

# Read entire row or column
row = sheet.getRow(2)
column = sheet.getColumn('A')

# Update entire row or column
sheet.updateRow(2, ['Alice', '30'])
sheet.updateColumn('A', ['Name', 'Alice', 'Bob'])

# Upload a local Excel file
ss = ezsheets.upload('my_spreadsheet.xlsx')

# Download as different formats
ss.downloadAsExcel('backup.xlsx')
ss.downloadAsCSV('data.csv')

# Delete a sheet
sheet.delete()

# Clear all data from a sheet
sheet.clear()
