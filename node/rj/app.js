var express = require('express');

var app = express();

app.use('/assets', express.static('assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/rj.html');
});

app.listen(3000);