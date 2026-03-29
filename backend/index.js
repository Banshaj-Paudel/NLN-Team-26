const express = require('express');
const app = express();
app.use(express.json());
// Routes will be added by Dev 2
app.get('/', (req, res) => res.json({ status: 'BurnMap backend running' }));
app.listen(3001, () => console.log('Backend running on port 3001'));
