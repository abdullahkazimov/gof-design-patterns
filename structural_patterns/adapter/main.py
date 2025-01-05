from adapter import JSONFormatter, CSVFormatter, CSVToJSONAdapter

json_formatter = JSONFormatter()

csv_formatter = CSVFormatter()

print("This is not JSON formatting of CSV:")
print(csv_formatter.get_csv())

adapter = CSVToJSONAdapter()

print("But this is adapted version for CSV:")
print(adapter.get_json())