const express = require('express');
// const path = require('path');
const serveStatic = require('serve-static');
const port = process.env.PORT || 8080;

app = express();
app.use(serveStatic(__dirname + "/dist/"));
app.get(/.*/, function (req, res) {
  res.sendfile(__dirname + "/dist/index.html");
});
app.listen(port);
console.log('server started '+ port);
