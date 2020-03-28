const fs = require('fs');
const csvFilePath = './../input/csvToJson.csv';
const csv = require('csvtojson');
 
const jsonArray = csv().fromFile(csvFilePath).then((jsonObj) => {
    console.log(jsonObj);
    var jsonContent = JSON.stringify(jsonObj);
    fs.writeFile("./../output/csvToJsonOutput.json", jsonContent, 'utf8', function (err) {
        if (err) {
            console.log("An error occured while writing JSON Object to File.");
            return console.log(err);
        }
        console.log("JSON file has been saved.");
    });
});