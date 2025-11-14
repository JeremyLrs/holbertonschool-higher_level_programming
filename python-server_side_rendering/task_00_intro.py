def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected a string, got {type(template)}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected a list of dictionaries, got {type(attendees)}.")
        return
    if not template.strip():
        print("Template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, person in enumerate(attendees, start=1):
        content = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{i}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Generated: {filename}")

        except Exception as e:
            print(f"Error wrting {filename}: {e}")

