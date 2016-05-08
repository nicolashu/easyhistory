var fs  = require("fs");

var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('Au99.99.txt')
});

var list = [];
lineReader.on('line', function (line) {
    var array = line.split(/\s+/);
    var date = array[0], open = array[2], high = array[3], low = array[4], close = array[5], volume = '', amount = '';
    if (/\d{4}-\d{2}-\d{2}/.test(date)) {
//        list.push(date + ',' + open + ',' + high + ',' + close + ',' + low + ',' + volume + ',' + amount)
        list.push(date + ',' + close + ',1.0')
    }
});

lineReader.on('close', function() {
    list.push('date,close,factor');
    list = list.reverse();
    fs.appendFileSync("./output.txt", list.join('\n'));
});
