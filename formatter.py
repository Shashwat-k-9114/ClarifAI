def format_prompt(intent, entities):
    if intent == "create_readme" or intent == "create_documentation":
        name = entities.get("project_name", "Unnamed Project")
        parts = [f"**Write a README.md file** for a project named **\"{name}\"**.\nInclude the following sections:\n"]

        if "purpose" in entities:
            parts.append(f"- **Purpose**: {entities['purpose']}")
        if "features" in entities:
            parts.append(f"- **Features**: {entities['features']}")
        if "usage" in entities:
            parts.append(f"- **Usage**: {entities['usage']}")
        if "dependencies" in entities:
            deps = ', '.join(entities["dependencies"])
            parts.append(f"- **Dependencies**: {deps}")

        return "\n".join(parts)

    elif intent == "write_essay":
        topic = entities.get("topic", "some topic")
        return f"Write an essay on the topic: **{topic}**."

    elif intent == "send_email":
        recipient = entities.get("recipient", "someone")
        subject = entities.get("subject", "No Subject")
        content = entities.get("content", "Body of the email")
        return f"""Write an email to **{recipient}**  
**Subject**: {subject}  
**Content**: {content}"""

    else:
        return f"Intent: {intent}\nEntities:\n" + "\n".join(f"- {k}: {v}" for k, v in entities.items())
