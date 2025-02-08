def get_json_prompt():
    return """
Analyze this document and return a JSON object with the following structured analysis:
{
    "basic_document_details": {
        "title": {
            "field_description": "The main title or heading of the document",
            "value": ""
        },
        "authors": {
            "field_description": "Names of the author(s) or contributors",
            "value": []
        },
        "date": {
            "field_description": "Date of publication or creation",
            "value": ""
        },
        "document_type": {
            "field_description": "Report, article, research paper, email, contract, etc",
            "value": ""
        }
    },
    "key_content_elements": {
        "Summary": {
            "field_description": "A brief synopsis of the document’s content",
            "value": ""
        },
        "Main Topics": {
            "field_description": "The core subjects discussed in the document",
            "value": ""
        },
        "Key Insights & Takeaways": {
            "field_description": "Important conclusions, findings, or recommendations",
            "value": ""
        },
        "Keywords & Phrases": {
            "field_description": "Frequently mentioned terms that define the document’s scope",
            "value": ""
        },
        "Sentiment Analysis": {
            "field_description": "The overall tone (positive, neutral, negative)",
            "value": ""
        }
    },
    "entities": {
        "People": {
            "field_description": "Individuals mentioned in the document",
            "value": []
        },
        "Organizations": {
            "field_description": "Companies, institutions, or groups referenced",
            "value": []
        },
        "Locations": {
            "field_description": "Cities, countries, addresses, or geographical places",
            "value": []
        },
        "Dates & Time References": {
            "field_description": "Specific days, months, years, or time ranges",
            "value": []
        },
        "Events": {
            "field_description": "Conferences, historical events, meetings, or project names",
            "value": []
        }
    },    
    "structured_data": {
        "Numbers & Statistics": {
            "field_description": "Financial figures, research data, percentages, etc.",
            "value": ""
        },
        "Monetary Values": {
            "field_description": "Prices, budgets, revenues, expenses, etc.",
            "value": ""
        },
        "Measurements": {
            "field_description": "Units of weight, distance, volume, speed, etc.",
            "value": ""
        },
        "Legal References": {
            "field_description": "Laws, regulations, contracts, compliance terms, etc.",
            "value": ""
        }
    }
}
"""




