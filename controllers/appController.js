const fs = require('fs');
const sqlite3 = require('sqlite3').verbose();
const sha1 = require('sha1')
const alert = require('alert')


const appIndex = (req, res) => {
    if(req.cookies.check == 'true'){
        let db = new sqlite3.Database('./db/main.db');
        
        // let sql = `SELECT * FROM users`;

        // db.all(sql, [], (err, rows) => {
        //     if (err) {
        //         throw err;
        //     }
        //     rows.forEach((row) => {
        //         console.log(row.name);
        //     });
        // });
        
        res.render('app/index');
    }else{
        res.render('app/login')
    }
  
}

// const helperStringSlicer = (string, charCount) => {
//     return string.substring(0, charCount) + '...'
// }


const appExitAcc = (req, res) => {
    res.clearCookie('check').redirect('/')
}

const appLoginUser = (req, res) => {
    let db = new sqlite3.Database('./db/main.db');

    let username = req.body.username
    let password = sha1(`${req.body.pass}`)
    let sql = `SELECT * FROM users WHERE username = "${username}" AND password = "${password}"`;

    db.all(sql, [], (err, rows) => {

        if (err) {
            throw err;
        }
        if(rows[0] == undefined){
            res.cookie('check', 'false', {
                expires: new Date(Date.now() + 2 * 3600000)
              }).redirect(req.get('referer'));
            alert('Username or password is incorrect.')
        }else{
            res.cookie('check', 'true', {
                expires: new Date(Date.now() + 2 * 3600000)
              }).redirect('/')
        }
    });

}

const appLogin = (req, res) => {
    res.render('app/login');
}

const appList = async (req, res) => {
    if(req.cookies.check == 'true'){
        let db = new sqlite3.Database('./db/main.db');
        let sql = `SELECT * FROM bots`;

        await db.all(sql, [], (err, rows) => {
            if (err) {
                throw err;
            }
            var responseData = []

            rows.forEach((row) => {
                responseData.push(row)
            });

            res.render('app/list', { data: responseData });
        });
    }else{
        res.render('app/login')
    }
}

module.exports = {
    appIndex,
    appLogin,
    appList,
    appLoginUser,
    appExitAcc
}