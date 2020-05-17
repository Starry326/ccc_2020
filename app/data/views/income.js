{
    "views": {
        "mean": {
            "map": "function(doc) {emit(doc.properties.gcc_name16, doc.properties.mean_aud);}"
        },
        "median": {
            "map": "function(doc) {emit(doc.properties.gcc_name16, doc.properties.median_aud);}"
        }
    }
}