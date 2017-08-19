def stories_file():
    return "stories.csv"


def write_to_file(form):
    filename = stories_file()
    headers = ["title", "story", "criteria", "business_value", "estimation", "status"]
    with open(filename, "a") as stories:
        for i in headers:
            for key, value in form.items():
                print(value)
                if i == key:
                    stories.write(value + ";")
        stories.write("\n")
    return


def get_story():
    filename = stories_file()
    with open(filename, "r") as stories:
        lines = stories.readlines()
    print(lines)
    all_story = [element.replace("\n", "").split(";") for element in lines]
    return all_story
