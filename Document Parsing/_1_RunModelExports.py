import csv

def export_reponse_model_dump_json(response):
        with open("LLM model_dump_json.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='\\')
            writer.writerow(["LLM model_dump_json"])  # Header row
            writer.writerow([response.model_dump_json])    # Data row
        print("LLM response saved to LLM model_dump_json.csv")

def export_reponse_model_schema(response):
        with open("LLM model_schema.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='\\')
            writer.writerow(["LLM model_schema"])  # Header row
            writer.writerow([response.schema])    # Data row
        print("LLM response saved to LLM model_schema.csv")
