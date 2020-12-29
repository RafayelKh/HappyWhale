// Main Modules connecting
const express = require('express');
const appRoutes = require('./routes/appRoutes.js')
const botRoutes = require('./routes/botRoutes.js')
const apiRoutes = require('./routes/apiRoutes.js')
const cookieParser = require('cookie-parser')
const bodyParser = require('body-parser')
const session = require('express-session')

const SECRET = 'somepass712' 

// Express init
const app = express();
const port = process.env.PORT || 3000;
app.set('view engine', 'ejs');
app.use(cookieParser('login check'))
app.use(express.static('public'));
app.use(session({secret: SECRET}));
app.use(bodyParser.json()); 


app.listen(port, () => {
  console.log(`Example app listening at http://127.0.0.1:${port}`);
})

app.use('/bots', botRoutes);

app.use('/api', apiRoutes);

app.use('/', appRoutes);

// app.use((req, res) => {
//   res.status(404).render('404', { title: 'Error' });
// })
