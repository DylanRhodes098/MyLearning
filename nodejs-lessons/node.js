let fs = require("fs")
let path = require("path")

let message = process.argv[2];
console.log("message", process.argv[1]);

if (!message) {
    console.error("error", err); return;
}
console.log("success")

let filePath = path.join(__dirname, "message.txt")

fs.writeFile(filePath, message, (err) => {
    if(err) {
        console.error("error",err); return;
    }
console.log("succes")
});

fs.readFile (filePath, "etf8", (err, data) => {
    if(err) {
        console.error("error",err) 
    }
console.log(data)
});