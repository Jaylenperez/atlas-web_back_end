const redis = require('redis');

const newClient = redis.createClient();

newClient.on('connect', () => {
  console.log('Redis client connected to the server');
});
newClient.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function createHash() {
  newClient.hset('HolbertonSchools', 'Portland', 50, redis.print);
  newClient.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  newClient.hset('HolbertonSchools', 'New York', 20, redis.print);
  newClient.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  newClient.hset('HolbertonSchools', 'Cali', 40, redis.print);
  newClient.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

function displayHash() {
  newClient.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.log('Error retrieving hash: ' + err);
    } else {
      console.log(reply);
    }
  });
}

createHash();
displayHash();