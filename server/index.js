const path = require('path');
const { App, appLog, config } = require('bff-server');

function start() {
    // App
    const app = new App();

    // Routes

    // static files
    app.staticDir(path.join(__dirname, 'public'));
    
    // start
    app.start();
}

// start the app!
start();