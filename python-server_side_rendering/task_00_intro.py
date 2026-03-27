#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str):
            err_msg = (
                "Error: Invalid input type for template. "
                f"Expected str, got {type(template).__name__}."
            )
            print(err_msg)
            return

        if not template:
            print("Template is empty, no output files generated.")
            return

        if not isinstance(attendees, list):
            err_msg = (
                "Error: Invalid input type for attendees. "
                f"Expected list, got {type(attendees).__name__}."
            )
            print(err_msg)
            return

        if not attendees:
            print("No data provided, no output files generated.")
            return

        for index, attendee in enumerate(attendees, start=1):
            try:
                if not isinstance(attendee, dict):
                    err_msg = (
                        f"Error: Invalid input type for attendee "
                        f"at index {index - 1}. Expected dict, "
                        f"got {type(attendee).__name__}."
                    )
                    print(err_msg)
                    return

                required_keys = {
                    'name',
                    'event_title',
                    'event_date',
                    'event_location'
                }

                data_dict = {}
                for key in required_keys:
                    if key in attendee and attendee[key] is not None:
                        data_dict[key] = attendee[key]
                    else:
                        data_dict[key] = "N/A"

                invitation_content = template
                invitation_content = invitation_content.replace(
                    '{name}', str(data_dict['name'])
                )
                invitation_content = invitation_content.replace(
                    '{event_title}', str(data_dict['event_title'])
                )
                invitation_content = invitation_content.replace(
                    '{event_date}', str(data_dict['event_date'])
                )
                invitation_content = invitation_content.replace(
                    '{event_location}', str(data_dict['event_location'])
                )

                filename = f"output_{index}.txt"

                if os.path.exists(filename):
                    msg = (
                        f"Warning: File {filename} already exists. "
                        "Overwriting..."
                    )
                    print(msg)

                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(invitation_content)

            except IOError as e:
                err_msg = (
                    f"Error: Failed to write invitation file "
                    f"output_{index}.txt: {e}"
                )
                print(err_msg)
                return
            except Exception as e:
                err_msg = (
                    f"Error: Unexpected error processing attendee "
                    f"at index {index - 1}: {e}"
                )
                print(err_msg)
                return

    except Exception as e:
        err_msg = f"Error: Unexpected error in generate_invitations: {e}"
        print(err_msg)
        return


