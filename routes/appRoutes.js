const express = require('express');
const appController = require('../controllers/appController.js')
const router = express.Router();
const bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: true });


router.get('/', appController.appIndex)
router.get('/login', appController.appLogin)
router.get('/list', appController.appList)
router.post('/handle-login', urlencodedParser, appController.appLoginUser)
router.get('/exit', urlencodedParser, appController.appExitAcc)


module.exports = router