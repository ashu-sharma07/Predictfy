import "dotenv/config";
import express from "express";
import bodyParser from "body-parser";
import mongoose from "mongoose";
import path from "path";
import bcrypt from "bcrypt";
import { fileURLToPath } from "url";

// dirname

const __filename = fileURLToPath(import.meta.url);

const __dirname = path.dirname(__filename);

// Basic App Set up
const port = 3000;
const saltRounds = 10;
const app = express();
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

// DataBase Integration

const password = process.env.PASSWORD;
mongoose.connect(
  `mongodb+srv://ashusharma07:${password}@cluster0.j5rug.mongodb.net/userDB`
);

const userSchema = new mongoose.Schema({
  userName: String,
  userEmail: String,
  userPassword: String,
});

const User = new mongoose.model("User", userSchema);

// Handle Get Request

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.get("/signup", (req, res) => {
  res.sendFile(__dirname + "/public/signup.html");
});

app.get("/login", (req, res) => {
  res.sendFile(__dirname + "/public/login.html");
});

// Handle Post Request

app.post("/signup", (req, res) => {
  bcrypt.hash(req.body.userPassword, saltRounds, function (err, hash) {
    // Store hash in  password DB.
    const newUser = new User({
      userName: req.body.userName,
      userEmail: req.body.userEmail,
      userPassword: hash,
    });
    newUser.save((err) => {
      if (err) {
        console.log(err);
      } else {
        console.log(newUser);
        res.redirect("/");
      }
    });
  });
});

app.post("/login", (req, res) => {
  const username = req.body.userEmail;
  const password = req.body.userPassword;
  User.findOne({ userEmail: username }, (err, foundUser) => {
    if (err) {
      console.log(err);
    } else {
      console.log("found");
      if (foundUser) {
        bcrypt.compare(password, foundUser.userPassword, (err, result) => {
          if (result === true) {
            res.redirect("/");
          }
        });
      }
    }
  });
});

app.listen(port, () => {
  console.log(`Application running on port ${port}.`);
});
