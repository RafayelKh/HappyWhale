const express = require('express');
const apiController = require('../controllers/apiController.js')
const router = express.Router();
const bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: true });


router.post('/checkConn', urlencodedParser, apiController.apiCheck)

router.post('/createConn', urlencodedParser, apiController.apiCreate)

router.post('/updateInfo', urlencodedParser, apiController.apiUpdate)


module.exports = router