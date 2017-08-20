import csv


def stories_file():
    return "stories.csv"


def write_to_file(all_story):
    filename = stories_file()
    with open(filename, "w") as stories:
        for record in all_story:
            row = ",".join(record)
            stories.write(row + "\n")
    return


def get_story():
    filename = stories_file()
    all_story = [[story.strip() for story in stories.rstrip('\n').split(',')] for stories in open(filename)]
    return all_story


def make_list_from_form(dictionary):
    table_heads = ["title", "story", "criteria", "business_value", "estimation", "status"]
    story_list = []
    for key in table_heads:
        story_list.append(dictionary[key])
    return story_list


def save_story(new_story):
    all_story = get_story()
    new_story = make_list_from_form(new_story)
    all_story.append(new_story)
    write_to_file(all_story)
