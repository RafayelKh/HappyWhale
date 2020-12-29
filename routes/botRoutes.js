const express = require('express');
const botController = require('../controllers/botController.js')
const router = express.Router();
const bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: true });


router.get('/:ip', botController.botIndex)


module.exports = router