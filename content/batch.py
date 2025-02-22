
import notion.get_post as notn

PAGE_ID = "1a1e46d2882f807f9ec5ff4514a2e0c1"

do_dict = notn.main(PAGE_ID)

#print(do_dict["JR"])

for key, value in do_dict.items():
    print(f"{key}: {value}")


keyword = "how to get a post from notion via python api"
