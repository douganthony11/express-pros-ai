const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.post('/respond', async (req, res) => {
  const message = req.body.transcript?.toLowerCase() || '';
  let response = "I'm not sure how to help with that. Let me transfer you to the office.";

  if (message.includes('pay stub')) {
    response = "You can find your pay stubs on your Express account. Would you like me to text you the link?";
  } else if (message.includes('w2')) {
    response = "You can get your W2 at workforce.expresspros.com/duplicatew2. The password is your full SSN. Should I text this to you?";
  } else if (message.includes('call in') || message.includes('sick')) {
    response = "I'm sorry to hear you're not feeling well. I've marked it down. Feel better soon!";
  }

  res.json({ response });
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
