from pymongo import MongoClient
from embedding import create_embeddings
from dotenv import load_dotenv
import os

load_dotenv()

MONDODB_URI = os.getenv("MONGODB_URI")
# Connect
client=MongoClient(MONDODB_URI)

# Database
db=client["sample_mflix"]
# ccollect and print movies to the database:
movies_coll=db["movies"]


""" print(movies_coll) """
# CREATE
def create_movie():
    title = input("Movie title: ")
    year = int(input("Year: "))
    genre = input("Genre: ")
    rating = float(input("Rating: "))

    movie = {
        "title": title,
        "year": year,
        "genre": genre,
        "rating": rating
    }

    result = movies.insert_one(movie)

    print("Movie created:", result.inserted_id)


# READ
def get_movies():
    movies=db.get_collection("movies").find().limit(50)
    print("****************::")

    for movie in movies:
     return movie


# UPDATE
""" def embed_movies():
     movies=movies_coll.find().limit(50)
     for movie in movies:
        embedding=create_embeddings(movie["plot"])
        
        if hasattr(embedding, "tolist"):
            embedding = embedding.tolist()

        result = movies_coll.update_one(
            {"_id": movie["_id"]},
            {"$set": {"hf_embedded": embedding}}
        )

        print("Modified:", result.modified_count)
         """
        
       # movie["hf_embedded"]=embedding

      
        #movies.replace_one({'_id':movie['_id']},movie)
       
      
 

# DELETE
def delete_movie():
    title = input("Movie title to delete: ")
    result = movies.delete_one({"title": title})

    if result.deleted_count > 0:
        print("Movie deleted.")
    else:
        print("Movie not found.")


# MENU
