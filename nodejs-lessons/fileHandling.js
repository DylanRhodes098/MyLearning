// file handling 
const fs = require("fs");
const path = require("path");

const message = process.argv[2]
console.log("message", process.argv[1]) 

if (!message) {
    console.error("error", err)
    process.exit[1];
}
console.log("success");

const filePath = path.join(__dirname, "message.txt");

fs.writeFile(filePath, message, (err) => {
    if (err) {
        console.error("error", err); return;
    }
    console.log("success");
})

fs.readFile(filePath, "utf8", (err, data) => {
    if (err) {
        console.error("error", err); return;
    }
    console.log(data);
})