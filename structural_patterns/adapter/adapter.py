class JSONFormatter:
    def get_json(self):
        return "JSON"

class CSVFormatter:
    def get_csv(self):
        return "CSV"

class CSVToJSONAdapter(JSONFormatter, CSVFormatter):

    def get_json(self):
        return "data: { " + self.get_csv() + " }"