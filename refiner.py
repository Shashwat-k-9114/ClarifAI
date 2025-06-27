def generate_refined_prompt(intent, entities):
    if intent == "create_documentation":
        project_name = entities.get("project_name", "your project")
        file_name = entities.get("file_name", "README.md")
        content_hint = entities.get("content", "")

        return (
            f"Write a comprehensive and professional `{file_name}` file for a project named '{project_name}'. "
            f"The documentation should follow best practices for open-source projects and be written in Markdown. "
            f"Include sections like:\n"
            f"- Project overview\n"
            f"- Features and functionality\n"
            f"- Installation instructions\n"
            f"- Usage examples\n"
            f"- Technologies used\n\n"
            f"{'Here’s a summary of the content: ' + content_hint if content_hint else ''}"
        )

    # Add more intent handlers as needed

    return f"Perform the task '{intent}' using the following context: {entities}"
