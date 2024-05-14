const express = require('express');
const app = express();
const port = 3001;

app.use(express.json());

app.post('/scan', (req, res) => {
    const { device, file_type } = req.body;
    const recoverable_files = [`${file_type}_file_1.txt`, `${file_type}_file_2.txt`, `${file_type}_file_3.txt`, `${file_type}_file_4.txt`, `${file_type}_file_5.txt`];
    res.json(recoverable_files);
});

app.post('/recover', (req, res) => {
    const { files } = req.body;
    const recovered_files = files;
    res.json({ recovered_files });
});

app.listen(port, () => {
    console.log(`Backend listening at http://localhost:${port}`);
});
