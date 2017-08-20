import csv


def stories_file():
    return "stories.csv"


def write_to_file(all_story):
    filename = stories_file()
    with open(filename, "w") as stories:
        for story in all_story:
            line = ",".join(story)
            stories.write(line + "\n")
    return


def get_story():
    filename = stories_file()
    all_story = [[story.strip() for story in stories.rstrip('\n').split(',')] for stories in open(filename)]
    return all_story


def make_list_from_form(dictionary):
    table_headers = ["title", "story", "criteria", "business_value", "estimation", "status"]
    story_list = []
    for key in table_headers:
        story_list.append(dictionary[key])
    return story_list


def save_story(new_story):
    all_story = get_story()
    new_story = make_list_from_form(new_story)
    all_story.append(new_story)
    id_=str(len(all_story))
    all_story[-1].insert(0,id_)
    write_to_file(all_story)
