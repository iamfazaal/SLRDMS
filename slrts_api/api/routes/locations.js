const express = require('express');
const router = express.Router();
var firebase = require('firebase');

firebase.initializeApp({
    serviceAccount: "./slrtsalgo-e12e0831ed43.json",
    databaseURL: "https://slrtsalgo.firebaseio.com"
});

var ref = firebase.database().ref('node-client');
var messageRef = ref.child('locations/namesh');

//Post method.. this one is the useful one.
router.post('/', (req, res, next) => {
    console.log('Locations:\n', req.body);

    messageRef.update({
        lng: req.body[0][0],
        lat: req.body[0][1]
    });

    res.sendStatus(200);
});

module.exports = router;