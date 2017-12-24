const express = require('express');
const router = express.Router();
const path = __dirname + '/views/';

/* GET home page. */
router.get('/', function (req, res, next) {
    res.sendFile('/views/about.html', { root: './' });
});

module.exports = router;
