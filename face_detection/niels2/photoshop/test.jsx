#target photoshop

current_document = app.activeDocument;
current_layer = current_document.activeLayer;
var clCopy = current_document.activeLayer.copy();

// create temporary doc with selected layer from current document
docHeight = current_document.height;
docWidth = current_document.width;
docResolution = current_document.resolution;
$.writeln("docHeight", docHeight);
tempDoc = app.documents.add( docWidth,docHeight, docResolution, "tempDoc", NewDocumentMode.RGB);
app.activeDocument = tempDoc;
tempDoc.paste();
app.activeDocument = current_document;




// new_width = 200;
//
// current_document.resizeImage(
//   UnitValue(new_width, 'px'),
//   null,
//   null,
//   ResampleMethod.BICUBIC
// );
// http://lacuisine.tech/2018/08/09/execute-python-script-from-photoshop/
fileRef = File("/Users/n/School/MED3/P3/test.png")
outPath = "/Users/n/School/MED3/P3/Code/P3-G306/face_detection/niels2/photoshop/out.jpg"
fileRef = File("/Users/n/School/MED3/P3/Code/P3-G306/face_detection/niels2/photoshop/out.jpg")

docExportOptions = new ExportOptionsSaveForWeb

docExportOptions.format = SaveDocumentType.PNG //-24 //JPEG, COMPUSERVEGIF, PNG-8, BMP
docExportOptions.transparency = true
docExportOptions.blur = 0.0
docExportOptions.includeProfile = false
docExportOptions.interlaced = false
docExportOptions.optimized = true
docExportOptions.quality = 100
docExportOptions.PNG8 = false

current_document.exportDocument(fileRef, ExportType.SAVEFORWEB, docExportOptions)


// Same as before, we gather the information we need
// Get the active document name
var theDoc = app.activeDocument;
// Save the name without fullpath
var docName = theDoc.name.replace(/\..+$/, '');

// we set the path to our temporary .command (Mac equivalent of .bat)
// we use the current date time as string in the filename
var date = Number(new Date());
// https://www.davidebarranca.com/2012/10/scriptui-window-in-photoshop-palette-vs-dialog/--
// var execFilePath = "/Users/n/School/MED3/P3/Code/P3-G306/face_detection/niels2/photoshop/"+ date +".command"
var execFilePath = "/Users/n/School/MED3/P3/Code/P3-G306/face_detection/niels2/photoshop/c.command"

// we create the command file, and setup it before opening it
var execFile = new File(execFilePath);
execFile.encoding = "UTF-8";
execFile.lineFeed = "Unix";
execFile.open("w");

// now we write on the .command file,
// that it's a bash script, calling python with an argument
execFile.write(
  "#!/bin/bash\n\n" +
  "python /Users/n/School/MED3/P3/Code/P3-G306/face_detection/niels2/photoshop/function.py " + outPath);

// you can repeat that command and write many lines instead

// when the file is written, we simply execute it
File(execFilePath).execute();




function W() {
  var w = new Window('dialog', 'Title');
  var b = w.add('button', undefined, 'OK', {
    name: 'ok'
  });
  return w
}
$.setTimeout = function(func, time) {
  $.sleep(time);
  func();
};

$.setTimeout(function() {
  alert("hello world")
}, 1000);
// current_document.// OPTIMIZE:
// var w = W();
// $.writeln(w.show());

maskPath = File("/Users/n/School/MED3/P3/Code/P3-G306/face_detection/niels2/photoshop/canny.jpeg")

var openedMask = open(maskPath)

openedMask.artLayers[0].duplicate(current_document);
openedMask.close();
// app.activeDocument = current_layer;
