const redis = require('redis');

const newClient = redis.createClient();

newClient.on('connect', () => {
  console.log('Redis client connected to the server');
});
newClient.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

newClient.subscribe('holberton school channel');
newClient.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        newClient.unsubscribe('holberton school channel');
        newClient.quit();
    }
})