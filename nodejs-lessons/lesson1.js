const fs = require("fs")
const path = require("path")

let message = process.argv[2]
console.log("message", process.argv[1])

if (!message) {
    console.log("error")
    process.exit[1]
}
console.log("success")
let filePath = path.join(__dir, "index.js")

