/*
 * This file is provided for custom JavaScript logic that your HTML files might need.
 * Maqetta includes this JavaScript file by default within HTML pages authored in Maqetta.
 */

updateResultTable = function(value) {
   console.log(value);
}

require(["dojo/ready", "dijit/registry"], function(ready, registry){
     ready(function(){
         var searchName = registry.byId('org_search_name');
         dojo.connect(searchName, "onKeyUp", function(){
           var value = searchName.get("value");
           updateResultTable(value);
         });
         //on(searchName, "change", updateResultTable); 
     });
});
