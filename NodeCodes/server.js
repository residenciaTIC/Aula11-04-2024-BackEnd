const http = require('http')
const data = require('./data.json')

const server = http.createServer((_req, res) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
    res.setHeader('Content-Type', 'application/json')
    res.end(JSON.stringify(data))
})

server.listen(3000, '127.0.0.1', () => {
    console.log('Server on')
})