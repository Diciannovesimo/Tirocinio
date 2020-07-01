const spawn = require('child_process');

const process = spawn('Python 3.8.3', ['./test.py']);

process.stdout.on('data', data => {
  console.log(data.toString());
});
