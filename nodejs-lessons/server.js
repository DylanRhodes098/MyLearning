//inject the express library
let express = require("express")
//identify the express library
const app = express()
//Define the port/route
const port = 3000;
//Trigger the ability to use json. Use of middleware. 
app.use(express.json())

//handle a get request that sends a string that express is working
app.get("/", (req,res) => {
    res.send("Using express")
});

//handle a post request that echos back the json sent in the get request
app.post ("/echo", (req,res) => {
    res.json({message:req.body})
});

//catch all undefined requests (safety net), that catches any missed messages and sends a 404 error to the user
app.all("*", (req,res) => {
res.status(404).send("error")
});

//Creates a listener that allows the above requests to function smoothly. 
app.listen(port, (req,res) => {
res.log(`you are using http://localhost:${port}`)
});