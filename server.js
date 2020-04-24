var express = require('express');
var app = express();
var path = require('path');
const fs = require('fs');
const spawn  = require('child_process').spawn;
let imagepath= '';
let subprocess;


app.use(express.static(path.join(__dirname, "./views")
));


app.listen(8080,()=>{ console.log("Server is running .. "); });


const multer = require("multer");

const handleError = (err, res) => {
  res
    .status(500)
    .contentType("text/plain")
    .end("Oops! Something went wrong!");
};



const upload = multer({
  dest: 'views/upload'
});


app.get("/",(req,res,next)=>{
    res.sendFile(path.join(__dirname,'/views/index.html'));
  })
app.post("/",upload.single("image-selector"),(req, res) => {
    console.log(req.file.path);
    const tempPath = req.file.path;
    const targetPath = path.join(__dirname, "./views/upload/image.png");
    imagepath = targetPath;
    if (path.extname(req.file.originalname).toLowerCase() === ".png" ||path.extname(req.file.originalname).toLowerCase() === ".jpg" || path.extname(req.file.originalname).toLowerCase() === ".jpeg" ) {
      
      fs.rename(tempPath, targetPath, err => {
        res.redirect("/");
        if (err) return handleError(err, res);
          console.log("Executing python ...")
          console.log("Child Process created ... ");
          subprocess = spawn('python',["./node.py"] ); 
          console.log("Start Processing ... ");
          subprocess.stdout.on('data', function(data) { 
            console.log('Processing Done ...')
            console.log(data.toString());

        });
      });
    } 
    else 
    {
      fs.unlink(tempPath, err => {
        if (err) return handleError(err, res);
  
        res
          .status(403)
          .contentType("text/plain")
          .end("Only .png/jepg/jpg files are allowed!");
      });
    }
  }
);

// app.get('/mypage', (req,res) =>{

//     res.sendFile(path.join(__dirname,"/views/index.html"));
  
//   });