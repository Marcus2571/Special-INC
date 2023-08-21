require('dotenv').config();

const http = require('http');
const path = require('path');
const express = require('express');
const tokenGenerator = require('./src/token_generator');

// Create Express webapp
const app = express();

app.use(express.static(path.join(__dirname, 'public')));

// const client = require('twilio')(process.env.TWILIO_ACCOUNT_SID, "6effa1cd46549c0a87799496f4528c47");

// client.video.v1.rooms
//                .create({
//                   statusCallback: 'http://example.org',
//                   type: 'peer-to-peer',
//                   uniqueName: 'SalesMeeting'
//                 })
//                .then(room => console.log(room.sid));

app.get('/', function(request, response) {
  const identity = request.query.identity;
  const room = request.query.room;
  console.log(identity, room);
  response.send(tokenGenerator(identity, room));
});

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  console.trace(err);
  res.status(err.status || 500);
  res.send({
    message: err.message,
    error: {},
  });
});

// Create an http server and run it
const server = http.createServer(app);
const port = process.env.PORT || 3000;
server.listen(port, function() {
  console.log('Express server running on *:' + port);
});