var express = require('express');
var bodyparser = require('body-parser');

var app = express();
var urlencoded = bodyparser.urlencoded({extended: false});

robotics = [{name: 'Vyoma', job: ['Coder']},
    {name: 'Jack', job: ['Driver', 'Builder']},
    {name: 'Leo', job: ['Builder', 'Driver']},
    {name: 'Mason', job: ['Builder']},
    {name: 'Joe', job: ['Coder', 'Notebook']}];

app.set('view engine', 'ejs');
app.use('/assets', express.static('assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/sign-up', function(req, res) {
    res.render('sign_up', {qs: req.query});
});

app.post('/sign-up', urlencoded, function(req, res) {
    robotics.push(req.body);
    res.render('sign_up_sucess', {data: req.body});
});

app.get('/profile/:member', function(req, res) {
    var mbrdta = {};
    for(let i = 0; i < robotics.length; i++) {
        if (req.params.member === robotics[i].name) {
            mbrdta = robotics[i];
        }
    }
    res.render('profile', {data: mbrdta});
});

app.get('/404', function(req, res) {
    res.sendFile(__dirname + '/404.html');
});

app.listen(3000);

/*
var http = require('http');
var fs = require('fs');

var server = http.createServer(function(req, res) {
    if(req.url === '/fun-text') {
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end('Funny text.');
    } else if (req.url === '/home' || req.url === '/') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        fs.createReadStream(__dirname + '/index.html', 'utf8').pipe(res);
    } else if (req.url === '/api/robotics') {
        res.writeHead(200, {'Content-Type': 'application/json'});
        robotics = [{'Name': 'Vyoma', Job: 'Coder'},
        {'Name': 'Jack', Job: ['Driver', 'Builder']},
        {'Name': 'Leo', Job: ['Builder', 'Driver']},
        {'Name': 'Mason', Job: 'Builder'},
        {'Name': 'Joe', Job: ['Coder', 'Notebook']}];
        res.end(JSON.stringify(robotics));
    } else if (req.url === '/sign-up') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        fs.createReadStream(__dirname + '/sign_up.html', 'utf8').pipe(res);
    } else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        fs.createReadStream(__dirname + '/404.html', 'utf8').pipe(res);
    }
});

server.listen(3000);*/