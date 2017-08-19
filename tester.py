story = [['1', 'Result page', 'Print out the info from the forms', 'Use a table for the results', '100', '2', 'TODO'], ['2', 'Form page', "Ask the user's name, email address and hair color", 'Only valid email address', '200', '3', 'Planning'], ['3', 'problem', 'need new', 'crit', '500', '2.5', 'Planning']]
edit = dict(([('bis_value', '200'), ('status', 'Review'), ('story_title', 'title'), ('criteria', 'crit'), ('story', 'story'), ('estimation', '4')]))


def make_list_from_form_result(dictionary):
    table_heads = ["story_title", "story", "criteria", "bis_value", "estimation", "status"]
    story_list = []
    for key in table_heads:
        story_list.append(dictionary[key])
    return story_list

with open("stories.csv", "r") as file:
            lines = file.readlines()
print(lines)
all_story=[element.rstrip("\n") for element in lines]
print (all_story[0][6])