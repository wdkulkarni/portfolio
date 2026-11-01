var express = require('express');
var bodyparser = require('body-parser');

var app = express();
var urlencoded = bodyparser.urlencoded({extended: false});
app.set('view engine', 'ejs');

app.use('/assets', express.static('assets'));
data = [];

function nextDate(date, days, rev=false) {
    if (rev === true) {date[1] -= days;
    } else {date[1] += days; }
    if (rev === true) {
        while (date[1] <= 0) {
            date[1] += month_days;
            date[0] -= 1;
        }
        while (date[0] <= 0) {
            date[0] += 12;
            date[2] -= 1;
        }
    } else {
        while (true) {
            var month_days = 0;
            if (date[0] === '1' || date[0] === '3' || date[0] === '5' || date[0] === '7' || date[0] === '8' || date[0] === '10' || date[0] === '12') {
                month_days = 31;
            } else if (date[0] === '4' || date[0] === '6' || date[0] === '9' || date[0] === '11') {
                month_days = 30;
            } else {
                var leaps = ['0', '4', '8', '12', '16', '20', '24', '28', '32', '36', '40', '44', '48'];
                var x = false;
                for (let i = 0; i < leaps.length; i++) {
                    if (leaps[i] === date[2]) {
                        month_days = 29;
                        x = true;
                    }
                }
                if (x === false) {
                    month_days = 28;
                }
            }
            if (date[1] > month_days) {
                date[1] -= month_days;
                date[0] += 1;
            } else {
                break;
            }
        }
        while (date[0] > 12) {
            date[0] -= 12;
            date[2] += 1;
        }
    }
    return date;
}

app.get('/', function(req, res) {
    res.render('index', {data: data});
});

app.post('/', urlencoded, function(req, res) {
    closestWeekend = [1, 1, 0];
    splitDate = req.body.date.split('/');
    splitDate = [parseInt(splitDate[0]), parseInt(splitDate[1]), parseInt(splitDate[2])];
    /*while (true) {
        closestWeekend = nextDate(closestWeekend, 364);
        if (closestWeekend[2] >= splitDate[2]) {
            closestWeekend = nextDate(closestWeekend, 364, rev=true);
            break;
        }
    }
    while (true) {
        closestWeekend = nextDate(closestWeekend, 28);
        if (closestWeekend[0] >= splitDate[0] && closestWeekend[2] >= splitDate[2]) {
            closestWeekend = nextDate(closestWeekend, 28, rev=true);
            break;
        }
    }*/
    while (true) {
        closestWeekend = nextDate(closestWeekend, 7);
        if (closestWeekend[1] >= splitDate[1] && closestWeekend[0] >= splitDate[0] && closestWeekend[2] >= splitDate[2]) {
            closestWeekend = nextDate(closestWeekend, 7, rev=true);
            break;
        }
    }
    console.log(closestWeekend);
    if (splitDate !== closestWeekend) {
        var x = false;
        for (let i = 0; i < data.length; i++) {
            var y = false;
            for(let j = 0; j < data[i].dates.length; j++) {
                if (req.body.date === data[i].dates[j]) {y = true; }
            }
            if (data[i].name === req.body.name && !y) {
                data[i].times += 1;
                data[i].dates.push(req.body.date);
                x = true;
            } else if (y && data[i].name === req.body.name) {x = true; }
        }
        if (x === false) {
            data.push({name: req.body.name, times: 1, dates: [req.body.date]});
        }
    }
    res.json(data);
});

app.get('/:item', function(req, res) {
    data = data.filter(function(item) {
        item = item.times + ' : ' + item.name;
        item = item.replace(/ /g, '-');
        return item.replace(/\//g, '-') !== req.params.item;
    });
    res.json(data);
});

app.listen(3000);