console.log('Integrazione Phyton in javascript');

const spawn = require('child_process').spawn;

const process = spawn('Python', ['CSVcreator.py', 78, '2262347']);

process.stdout.on('data', data => {
  console.log(data.toString());
});
