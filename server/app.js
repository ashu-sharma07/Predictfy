import "dotenv/config";
import express from "express";
import bodyParser from "body-parser";
import mongoose from "mongoose";

// Basic App Set up
const port = 3000;
const app = express();
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

// Handle Get Request

app.get("/", (req, res) => {
  res.send("Hello");
});

app.listen(port, () => {
  console.log(`Application running on port ${port}.`);
});
