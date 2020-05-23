{
    "views": {
       "lowIncomeHouseholds": {
            "map": "function(doc) {emit(doc.properties.lga_code, doc.properties.combined_strs_2_denom);}",
            "reduce": "_sum"
        }
    }
}