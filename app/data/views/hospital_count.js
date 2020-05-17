{
    "views": {
        "total": {
            "map": "function(doc) {emit(doc.properties.hospital_name, 1);}",
            "reduce": "_count"
        },
        "public": {
            "map": "function(doc) {if(doc.properties.sector==\"Public\") {emit(doc.properties.hospital_name, 1);}}",
            "reduce": "_count"
        },
        "private": {
            "map": "function(doc) {if(doc.properties.sector==\"Private\") {emit(doc.properties.hospital_name, 1);}}",
            "reduce": "_count"
        },
        "under50": {
            "map": "function(doc) {if(doc.properties.beds==\"<50\") {emit(doc.properties.hospital_name, 1);}}",
            "reduce": "_count"
        },
        "50-99": {
            "map": "function(doc) {if(doc.properties.beds==\"50-99\") {emit(doc.properties.hospital_name, 1);}}",
            "reduce": "_count"
        },
        "100-199": {
            "map": "function(doc) {if(doc.properties.beds==\"100-199\") {emit(doc.properties.hospital_name, 1);}}",
            "reduce": "_count"
        },
        "200-500": {
            "map": "function(doc) {if(doc.properties.beds==\"200-500\") {emit(doc.properties.hospital_name, 1);}}",
            "reduce": "_count"
        },
        "over500": {
            "map": "function(doc) {if(doc.properties.beds==\">500\") {emit(doc.properties.hospital_name, 1);}}",
            "reduce": "_count"
        }
    }
}