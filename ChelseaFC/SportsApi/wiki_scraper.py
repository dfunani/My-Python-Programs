import wikipediaapi
from models import Club


class Wikipedia():
    def __init__(self):
        self.url = ""

    def GetBio(self, club):
        try:
            wiki_wiki = wikipediaapi.Wikipedia('en')
            if club == "Crystal Palace":
                club += " FC"
            page_py = wiki_wiki.page(club.strip())
            bio = (page_py.text.strip()) + '\n'
            bio = bio[0: 65000]
        except Exception as e:
            bio = f"A biography for {club} was not found on Wikipedia"
        return {"status": "success", "result": bio}

    def GetTrophies(self, club):
        trophies = {
            "epl": 0,
            "faCup": 0,
            "comShield": 0,
            "leagueCup": 0,
        }
        return {"status": "success", "result": trophies}


clubNames = Club().FetchNames()

for names in clubNames['result']:
    result = Wikipedia().GetBio(names)
    print(names, result['result'][0:255],
          end="\n\n", sep="\n")
    Club().UpdateBio(result['result'][0:255], names)
