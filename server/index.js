const express = require('express');

const app = express();

const port = 3000;

const server = app.listen(port);

app.use(express.static('public'));