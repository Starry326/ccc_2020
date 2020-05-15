{
    "views": {
        "tweets-count": {
            "map": "function(doc) {emit(doc._id,1);}",
            "reduce": "_count"
        }
    }
}