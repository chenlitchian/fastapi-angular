//index.js
 
var express = require('express');
 
const app = express();
const port = 8000;
 
app.use(express.static('view'))
 
var http = require('http');
var httpProxy = require('http-proxy');
var proxy = httpProxy.createProxyServer({});
 
proxy.on('proxyReq', function (proxyReq, req) {
    random_options = ['haha','admin','tester']
    const randomElement = random_options[Math.floor(Math.random() * random_options.length)];
    proxyReq.setHeader('X-WEBAUTH-USER', 'admin')
});
 
proxy.on('proxyRes', function (proxyRes, req, res) {
    res.setHeader('Access-Control-Allow-Origin', '*');
});
 
proxy.on('error', function (err, req, res) {
    res.writeHead(500, {'Content-Type': 'text/plain'});
    res.end("An error occured");
});
 
app.all("/*", function (req, res) {
    console.log("Forwarding...")
    proxy.web(req, res, {
        target: 'http://localhost:3000/', // link to our target service
        secure: false
    });
})
 
app.listen(port,
    () => console.log(`Listening on port ${port}!`))