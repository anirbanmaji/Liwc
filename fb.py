import facebook
import json
token = "EAACEdEose0cBABKztQcjQxIUJhgBKRdV9JYGFnWjtFIUIIsmrlXjiSfpREzZCSscWZB0fP7FTB7sZBNWwLUL6uZCPh01MZBaMHpTeBpogKoTAgB7ad6tnKASfGCdwdTqrBrZB24wmZBK42aP8fxc9ZBSLZBFStNXnfjZCc3krdQhSGHO8wqbPJjPJDIrZBPfpZBdSgsZD"
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
posts = graph.get_connections(profile['id'],"posts")

#print(json.dumps(posts['data']))
text_file = open("Output.txt", "w+")
for post in posts['data']:
    id_no = post["id"]
    msg=graph.get_object(id_no)
    print(json.dumps(id_no))
    try:
        text_file.write(msg['message']+" ")
    except:
        try:
            text_file.write(msg['story']+" ")
        except:
            continue
text_file.close()

