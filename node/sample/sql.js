var express = require('express');
var mysql = require('mysql');

var app = express();

var connection = mysql.createPool({
    //connectionLimit is amount of people that can connect at once. Keeps things moving fast for all.
    connectionLimit: 50,
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'sample'
});

app.get('/', function(req, res) {
    //Connect to database.
    connection.getConnection(function(err, tempCont) {
        if (err) {
            tempCont.release();
            throw err;
        }
        console.log('Connected.');
        //Query tempCont.
        tempCont.query('SELECT * FROM sample', function(err, rows, fields) {
            //Release tempCont because no more queries need to be made.
            tempCont.release();
            if (err) {throw err; }
            //Send result of SQL query to user.
            res.json(rows);
        });
    });
});

app.listen(3000);