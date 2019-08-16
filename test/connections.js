const mongoose = require('mongoose');

// Connects to the database
mongoose.connect('mongodb://localhost/test');

mongoose.connection.once('open', function(){
    console.log('Connection Successful');

}).on('error', function(error){
    console.log('Connection Error: Error logged', error);
});

