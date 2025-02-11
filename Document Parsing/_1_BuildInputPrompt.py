def get_json_prompt():
    return """
Analyze this document and return a JSON object. Ensure each response has
    -A detailed level of information
    -Is as long as it can possibly without sacrificing quality and relevance
    -A professional tone and style
    -Provides an important understanding of the topic and is relatable via examples and explanations where relevant
Make sure each response is as follows
{
    "1 basic document details": {
        "title": {
            "field description": "The main title or heading of the document",
            "value": ""
        },
        "authors": {
            "field description": "Names of the author(s) or contributors",
            "value": []
        },
        "date": {
            "field description": "Date of publication or creation",
            "value": ""
        },
        "document type": {
            "field description": "Report, article, research paper, email, contract, etc",
            "value": ""
        }
    },
    "2 Key Content Elements": {
        "Summary": {
            "field description": "A brief synopsis of the document’s content",
            "value": ""
        },
        "Main Topics": {
            "field description": "The core subjects discussed in the document",
            "value": ""
        },
        "Key Insights & Takeaways": {
            "field description": "The so what, important conclusions, findings, or recommendations. Make each takeaway numbered",
            "value": ""
        },
        "Keywords & Phrases": {
            "field description": "Frequently mentioned terms that define the document’s scope",
            "value": ""
        },
        "Sentiment Analysis": {
            "field description": "The overall tone (positive, neutral, negative)",
            "value": ""
        },
        "How can I use this document to make further downstream judgements and opionions on the subject matter at hand that will demonstrate to a wider audience that I have subject matter expertise": {
            "field description": "Provide an overreaching view of what next based on this document?",
            "value": ""
        }
    },
    "3 Entities": {
        "People": {
            "field description": "Individuals mentioned in the document",
            "value": []
        },
        "Organizations": {
            "field description": "Companies, institutions, or groups referenced",
            "value": []
        },
        "Locations": {
            "field description": "Cities, countries, addresses, or geographical places",
            "value": []
        },
        "Dates & Time References": {
            "field description": "Specific days, months, years, or time ranges",
            "value": []
        },
        "Events": {
            "field description": "Conferences, historical events, meetings, or project names",
            "value": []
        }
    },    
    "4 Structured Data": {
        "Numbers & Statistics": {
            "field description": "Financial figures, research data, percentages, etc.",
            "value": ""
        },
        "Monetary Values": {
            "field description": "Prices, budgets, revenues, expenses, etc.",
            "value": ""
        },
        "Measurements": {
            "field description": "Units of weight, distance, volume, speed, etc.",
            "value": ""
        },
        "Legal References": {
            "field description": "Laws, regulations, contracts, compliance terms, etc.",
            "value": ""
        }
    },
    "5 Actionable Elements": {
        "decisions recommendations": {
            "field description": "Key choices or actions suggested in the document",
            "value": ""
        },
        "action items next steps": {
            "field description": "Specific tasks or follow-ups required",
            "value": ""
        },
        "questions raised": {
            "field description": "Unanswered questions or topics that need further discussion",
            "value": ""
        }
    },
    "6 Contextual Insights": {
        "comparisons contrasts": {
            "field description": "Differences and similarities between subjects",
            "value": ""
        },
        "citations references": {
            "field description": "Other sources, studies, or documents mentioned",
            "value": ""
        },
        "implications consequences": {
            "field description": "Effects of the information presented",
            "value": ""
        }
    },
    "7 Structural Formatting": {
        "headings subheadings": {
            "field description": "Sections and organization of content",
            "value": ""
        },
        "bullet points lists": {
            "field description": "Key enumerations or structured points",
            "value": ""
        },
        "tables charts": {
            "field description": "Data representations and visual elements",
            "value": ""
        }
    },
    "8 Document Metadata": {
        "file type format": {
            "field description": "PDF, DOCX, TXT, HTML, etc.",
            "value": ""
        },
        "word count page count": {
            "field description": "Document length",
            "value": ""
        },
        "readability score": {
            "field description": "Complexity of the language used",
            "value": ""
        },
        "language detection": {
            "field description": "Language(s) in the document",
            "value": ""
        }
    },
    "9 Advanced Context": {
        "underlying themes motifs": {
            "field description": "Recurring ideas or metaphors throughout the document",
            "value": ""
        },
        "hidden agendas bias": {
            "field description": "Implicit perspectives or biases",
            "value": ""
        },
        "contradictions inconsistencies": {
            "field description": "Points or claims that do not align",
            "value": ""
        },
        "intent purpose detection": {
            "field description": "Whether the document is informative, persuasive, misleading, etc.",
            "value": ""
        },
        "explicit vs implicit claims": {
            "field description": "What is directly stated versus what is implied",
            "value": ""
        }
    },
    "10 Social Cultural Elements": {
        "cultural references": {
            "field description": "Mentions of cultural, religious, or historical elements",
            "value": ""
        },
        "idioms figurative language": {
            "field description": "Metaphors, analogies, and unique phrasing",
            "value": ""
        },
        "socioeconomic impact": {
            "field description": "Impact of the document on different social groups",
            "value": ""
        },
        "ethical moral considerations": {
            "field description": "Discussions on ethics, fairness, or societal impact",
            "value": ""
        }
    },
    "11 Deep Entity Recognition": {
        "connections between people": {
            "field description": "Mapping relationships between individuals or organizations",
            "value": ""
        },
        "hierarchy organizational structure": {
            "field description": "Roles, reporting lines, and influence structures",
            "value": ""
        },
        "industry sector classification": {
            "field description": "Identifying relevant business or academic sectors",
            "value": ""
        },
        "geopolitical relevance": {
            "field description": "Regional or global impact of the content",
            "value": ""
        },
        "intellectual property mentions": {
            "field description": "Patents, copyrights, trademarks, etc.",
            "value": ""
        }
    },
    "12 Sentiment Emotional Tone": {
        "emotion detection": {
            "field description": "Identifying emotions like excitement, urgency, or frustration",
            "value": ""
        },
        "persuasive techniques": {
            "field description": "Use of emotional appeals, arguments, or rhetorical devices",
            "value": ""
        },
        "public perception impact": {
            "field description": "Potential influence on opinions or trends",
            "value": ""
        },
        "trustworthiness credibility score": {
            "field description": "Evaluation of source reliability and factual accuracy",
            "value": ""
        }
    },
    "13 Advanced Data Analysis": {
        "trend extraction": {
            "field description": "Identifying patterns over time within the document",
            "value": ""
        },
        "predictive insights": {
            "field description": "Forecasting potential future implications based on current data",
            "value": ""
        },
        "financial implications": {
            "field description": "Assessing economic impact from the data provided",
            "value": ""
        },
        "time sensitive information": {
            "field description": "Data that might change over time (e.g., forecasts, stock prices)",
            "value": ""
        }
    },
    "14 Legal Compliance": {
        "legal liabilities risks": {
            "field description": "Potential legal consequences mentioned in the text",
            "value": ""
        },
        "compliance issues": {
            "field description": "How well the content aligns with relevant regulations",
            "value": ""
        },
        "cybersecurity data sensitivity": {
            "field description": "Concerns regarding data security and privacy",
            "value": ""
        },
        "contractual obligations": {
            "field description": "Binding clauses, warranties, or contractual terms",
            "value": ""
        },
        "regulatory references": {
            "field description": "Mentions of laws, industry rules, or government policies",
            "value": ""
        }
    },
    "15 Media Content Integrity": {
        "fact checking needs": {
            "field description": "Statements or claims that require verification",
            "value": ""
        },
        "misinformation propaganda indicators": {
            "field description": "Indications of bias or misleading data",
            "value": ""
        },
        "plagiarism originality": {
            "field description": "Assessment of content originality relative to external sources",
            "value": ""
        },
        "fake reviews testimonials": {
            "field description": "Detection of misleading endorsements or reviews",
            "value": ""
        }
    },
    "16 Usability Accessibility": {
        "readability complexity": {
            "field description": "Evaluating ease of understanding (e.g., Flesch-Kincaid score)",
            "value": ""
        },
        "intended audience matching": {
            "field description": "Alignment with the target readership's knowledge level",
            "value": ""
        },
        "jargon vs layman terms": {
            "field description": "Balance between technical language and plain communication",
            "value": ""
        },
        "translation localization challenges": {
            "field description": "Barriers to efficient translation or localization",
            "value": ""
        }
    },
    "17 Influence Impact Detection": {
        "virality potential": {
            "field description": "Likelihood of the document being widely circulated",
            "value": ""
        },
        "market industry disruption": {
            "field description": "Potential to impact business or industry trends",
            "value": ""
        },
        "political societal influence": {
            "field description": "Effect on policies, activism, or public opinion",
            "value": ""
        },
        "competitive intelligence": {
            "field description": "How the document positions itself compared to competitors",
            "value": ""
        }
    }
}
"""