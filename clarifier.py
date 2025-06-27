# clarifier.py

REQUIRED_FIELDS = {
    "build_bot": ["platform", "type", "content", "frequency"],
    "create_script": ["functionality", "schedule"],
    "build_web_app": ["functionality", "style"],
    "send_email": ["recipient", "subject", "content"]
}


SUGGESTIONS = {
    "platform": ["telegram", "discord", "whatsapp"],
    "type": ["reminder", "alert", "chatbot"],
    "content": ["drink water", "stand up", "stretch"],
    "frequency": ["hourly", "daily", "weekly"],
    "recipient": ["boss", "manager", "team"],
    "subject": ["Project update", "Request for leave", "Meeting follow-up"]
}



def get_missing_fields(task, parsed_data):
    required = REQUIRED_FIELDS.get(task, [])
    missing = []
    for field in required:
        if field not in parsed_data:
            missing.append(field)
    return missing

def clarify_with_user(task, parsed_data):
    missing = get_missing_fields(task, parsed_data)
    if not missing:
        return parsed_data

    print("\n🤖 I need a bit more information:")
    for field in missing:
        suggested = f" (e.g. {', '.join(SUGGESTIONS.get(field, []))})" if field in SUGGESTIONS else ""
        value = input(f"Please specify the '{field}'{suggested}: ").strip()
        parsed_data[field] = value

    return parsed_data
