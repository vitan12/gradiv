const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// Creating basic Schema and Model for testing

const testSchema  = new Schema({
    name: String;
    location: String;
    tuition: Number;
    rank: Number; 
});

const testSchool = mongoose.model('testchool', testSchema);

module.exports = testSchool;

var mySchool = new testSchool({});