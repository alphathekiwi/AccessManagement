import pymongo
import pprint

client = pymongo.MongoClient(
    'mongodb+srv://alpha:00Root00@bestmovies-fs4uc.mongodb.net/test?retryWrites=true')
db = client['AccessManagement']
collection = db['DigitalResources']

queries = [
    {'Category': 'Arts'},
    {'Name': {'$regex': '.*Mona.*'}},
]

for q in queries:
    print('\n################################\n#### ' + str(q)
          + ' ####\n################################\n')
    for x in collection.find(q):
        pprint.pprint(x)

collection.insert_one({'Category': 'Technology', 'Type': 'Programming', 'Name': 'Pascal',
                                   'About': 'Pascal is an imperative and procedural programming language, which Niklaus Wirth designed in 1968–69 and published in 1970, as a small, efficient language intended to encourage good programming practices using structured programming and data structuring.',
                                   'Designed': 'Niklaus Wirth'})

collection.update_one({'Name': 'Claude Monet'}, {
    '$set': {'Born': '1841', 'Died': '1927'}})

collection.delete_one({'Type': 'Painting'})

print('\n################################\n#### SHOW ALL IN DATABASE'
      + ' ####\n################################\n')
for x in collection.find():
    pprint.pprint(x)

# Readd Mona Lisa for future testing
collection.insert_one({'Category': 'Arts', 'Type': 'Painting', 'Name': 'Mona Lisa', 'About': '\'The Mona Lisa is a half-length portrait painting by the Italian Renaissance artist Leonardo da Vinci that has been described as \'\'the best known, the most visited, the most written about, the most sung about, the most parodied work of art in the world\'\'. The Mona Lisa is also one of the most valuable paintings in the world. It holds the Guinness World Record for the highest known insurance valuation in history at $100 million in 1962, which is worth nearly $800 million in 2017.\'',
                                   'Year': '1503-1506', 'Medium': 'Oil on poplar panel', 'Dimensions': '77cm x53 cm', 'Location': 'Musee du Louvre, Paris'}
                      )

# print(client.list_database_names())
# print(db.list_collection_names())
