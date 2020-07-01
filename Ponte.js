console.log('Integrazione Phyton in javascript');

const spawn = require('child_process').spawn;

const process = spawn('Python', ['./ScriptPH.py', 'William']);

process.stdout.on('data', data => {
  console.log(data.toString());
});
