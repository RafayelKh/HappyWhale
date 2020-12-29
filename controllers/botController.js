const fs = require('fs');
const sqlite3 = require('sqlite3').verbose();
// const sha1 = require('sha1')
// const alert = require('alert')


const botIndex = (req, res) => {
    let ip = req.params.ip
    if(req.cookies.check == 'true'){
        let db = new sqlite3.Database('./db/main.db');
       
        let sql = `SELECT * FROM bots WHERE ip = '${ip}'`;

        db.all(sql, [], (err, rows) => {
            if (err) {
                throw err;
            }

            res.render('bot/profile', { data: rows[0] });
        });
    }else{
        res.render('app/login')
    }
  
}


module.exports = {
    botIndex
}