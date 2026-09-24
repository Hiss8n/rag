from crude import get_movies
from crude import movies_coll
from embedding import create_embeddings
from flask import Flask,render_template,request
m_movies=get_movies()
app=Flask(__name__)

""" 

  "mappings": {
    "dynamic": true,
    "fields": {
      "hf_embeddings":{
        "dimensions": 384,
        "similarity": "dotProduct",
        "type": "knnVector"
      }
    }
   
  }
}
 """

@app.route("/",methods=["GET","POST"])
def index():
    results=[]
    query=""

    if request.method=="POST":
        query=request.form["query"]
        query_embedding = create_embeddings(query)

        if hasattr(query_embedding, "tolist"):
            query_embedding = query_embedding.tolist()

        result=movies_coll.aggregate([
                {
                    "$vectorSearch":{
                        "queryVector":query_embedding,
                        "path":"hf_embedded",
                        "numCandidates":100,
                        "limit":5,
                        "index":"default"
                    }
                },
                {
        
                "$project": {
                "_id": 0,
                "title": 1,
                "plot": 1,
                "hf_embedded": {
                "$meta": "vectorSearchScore"
            }
        }}
                
            ])
        results=list(result)
    return render_template(
        "index.html",
        results=results,
        query=query
    )
  
if __name__ == "__main__":
    app.run(debug=True)

""" 
      for docc in collection:
            print(f"movies title:{docc["title"]},\nMovie plot:{docc["plot"]}\n") 
            """









