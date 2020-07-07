console.log('Integrazione Phyton in javascript');

const spawn = require('child_process').spawn;

const process = spawn('Python', ['CreatoreCVS.py', 5, '2262347']);

process.stdout.on('data', data => {
  console.log(data.toString());
});
