

dictionary={"story_title":"asd", "story":"kek", "criteria":"lol", "bis_value":"500", "estimation":"2", "status":"TODO"}
table_heads = ["story_title", "story", "criteria", "bis_value", "estimation", "status"]
story_list = []
i=0
for key in table_heads:
    story_list.append(dictionary[key])
    i+=1
print (story_list)