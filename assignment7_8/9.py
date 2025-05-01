import re
token_patterns = {
    "Punctuation": r"[.,!?;(){}[\]<>:\"",
    "Date": r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b",
    "URL": r"\b(?:http://|https://|www\.)[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}\b", 
    "Email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", 
    "Number": r"\b\d{1,3}(?:[,\s]\d{3})*(?:\.\d+)?\b|\b\d{1,3}(?:\/\d{1,3})+\b",
    "Username": r"@\w+",  
    "Word": r"\w+" 
}

def tokenizer(text):
    tokens = []
    combined_pattern = '|'.join(f"(?P<{key}>{pattern})" for key, pattern in token_patterns.items())

    for match in re.finditer(combined_pattern, text):
        for token_type in token_patterns:
            if match.group(token_type):
                tokens.append((token_type, match.group(token_type)))
                break
    
    return tokens

text = "Hello! My name is @user_name. Visit https://www.example.com for more info. Email me at user@example.com. I owe 33,000.00 USD or 313/77 shares."

tokens = tokenizer(text)
for token_type, token_value in tokens:
    print(f"{token_type}: {token_value}")