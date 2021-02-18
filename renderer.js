
function start(){
  const {PythonShell} = require('python-shell');
  var AppDir = document.getElementById("AppDir").value;
  var sec = document.getElementById("sec").value;
  const path = require('path');

  let options = {
    mode: 'text',
    pythonOptions: ['-u'], // get print results in real-time.
    args: [AppDir,sec]
  };

  var t2 = ['h', 't', 't', 'p', 's', ':', '/'];
  var nw1 = [];
  
  for (i = 0; i < 7; i++) {
    AppDirArr = AppDir[i];
    nw1.push(AppDirArr);
  }
  console.log(nw1)
  console.log(t2)

  if (JSON.stringify(nw1) === JSON.stringify(t2)){
    console.log("Es web");
    let Open_Web = path.join(__dirname, '/extraResources/Open_Web.py')

    PythonShell.run(Open_Web, options, function (err, results) { 
      if (err) throw err;
      // Results is an array consisting of messages collected during execution.
      console.log('results: %j', results);
      alert("Temps acavat")
    });
  }else{ 
    console.log("Es dir");
    let Open_App = path.join(__dirname, '/extraResources/Open_App.py')

    PythonShell.run(Open_App.py, options, function (err, results) {
      if (err) throw err;
      // Results is an array consisting of messages collected during execution.
      console.log('results: %j', results);
      alert("Temps acavat") 
    });
  }
}

//-------------------------------------------------Sends the data to the database------------------------------------------------



function InsertTable(){

  const path = require('path');
  let BaseDeDatos = path.join(__dirname, '/extraResources/BaseDeDatos.py')

  const {PythonShell} = require('python-shell');
  var NombreTabla = document.getElementById("CrearTaula").value;

  let options = {
    mode: 'text',
    pythonOptions: ['-u'], 
    args: [NombreTabla]
  };

  PythonShell.run(BaseDeDatos, options, function (err, results) {
    if (err) throw err;

    console.log('results: %j', results);
    alert("Rutina creada")
  });
}

function InsertRowDB(){
  const path = require('path');
  let InsertRow = path.join(__dirname, '/extraResources/InsertRow.py')

  var AppDir = document.getElementById("AppDir").value;
  var sec = document.getElementById("sec").value;
  var min = document.getElementById("min").value;
  var hor = document.getElementById("horas").value;
  var NombreTabla = document.getElementById("CrearTaula").value;

  const {PythonShell} = require('python-shell');

  let options = {
    mode: 'text',
    pythonOptions: ['-u'],
    args: [AppDir,sec,NombreTabla,min,hor]//pass the arguments to python  [1,2,3...]
  };

  PythonShell.run(InsertRow, options, function (err, results) {
    if (err) throw err;

    console.log('results: %j', results);
  });
}

function RunRutina(){

  const path = require('path');
  let Select_DB = path.join(__dirname, '/extraResources/Select_DB.py')

  const {PythonShell} = require('python-shell');
  var NombreTabla = document.getElementById("CrearTaula").value;

  let options = {
    mode:'text',
    pythonOptions: ['-u'],
    args: [NombreTabla]
  };
  PythonShell.run(Select_DB, options, function(err, results) {
    if (err) throw err;

    console.log('Select_DB.py finished.');
    console.log('Select_DB.py', results);
  });

}
