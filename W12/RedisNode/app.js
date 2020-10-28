var redis = require('redis');


var client = redis.createClient("6379","104.198.244.0"); //creates a new client
//client = redis.createClient();

client.on('connect', function() {
    console.log('connected');

    client.set('framework', 'ReactJS');
});

client.get('framework', function(err, reply) {
    console.log(reply);
});

client.exists('queryDan', function(err, reply) {
    if (reply === 1) {
        console.log('exists');
        client.hgetall('queryDan', function(err, reply) {
            console.log(reply);
        });
    } else {


        console.log('doesn\'t exist');
        client.hmset('queryDan', {'id': 4,'name': 'Daniel'});
    }
});