# Define the Hamlet Class, and it's related services, functions, variables, etc
# The hamlet is geographically the parent of all other things in the digital hamlet
# Future ideas to add:
# - I think one day my hamlet might be able to interact with other hamlets
#   Multiple hamlets could in principle become a single regional entity where shared interactions
#   increase the outcomes and prosperity of all hamlets in the regional entity network
# - In principle, regional entities could combine to great larger and larger entities, like
#   cities, states, countries, planets, and beyond.  There would be some safe and logical limitation
#   to the extent of dvisions and mergers.  Alternatively, maybe designing an infrastructure where
#   different entities (hamlets, regions, cities, etc.) could combine to form larger entities infinitelyclass GeoEntity:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location
