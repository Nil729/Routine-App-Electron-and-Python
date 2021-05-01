// Modules to control application life and create native browser window
const {app, BrowserWindow} = require('electron')


// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })

  mainWindow.loadFile('index.html')
  
  mainWindow.on('closed', function () {

    mainWindow = null
  })
}


app.on('activate', function () {
  if (mainWindow === null) {
    createWindow()
  }
})

app.on('window-all-closed', function () {
  app.quit()
})

app.on('ready', createWindow)