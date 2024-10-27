
# URL Shortener 

This script is a URL shortener that integrates various URL shortening services. It automatically fetches shortened URLs from multiple services and returns them.

## Features ✨

- Shortens URLs using multiple services:
  - [Clck.ru](https://clck.ru)
  - [Feji.io](https://feji.io)
  - [Goo.su](https://goo.su)
  - [RLU.ru](https://rlu.ru)
  - [Shortlink.net](https://shortlink.net)
  - [Surl.li](https://surl.li)
  - [Encurtador.dev](https://encurtador.dev)
  - [Onx.la](https://onx.la)
  - [Shorturl.ru](https://shorturl.ru)
  - [Shorturl.at](https://shorturl.at)
  - [WDurl.ru](https://wdurl.ru)

## How to Use 📖

1. Clone the repository:
   ```bash
   git clone https://github.com/uixss/big-shot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd bit-short
      ```
3. Run the script with a URL as an argument:
   ```bash
   python manager.py https://example.com
   ```

## Requirements 📋

- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `requests_toolbelt`


## Telegram Bot Integration 🚀

This script can also be integrated with a Telegram bot using the following Node.js code:

```javascript
import { Telegraf } from 'telegraf'; 
import { exec } from 'child_process';

const bot = new Telegraf('<BOT_TOKEN>');

bot.command('short', (ctx) => {
    const url = ctx.message.text.split(' ')[1];

    if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) {
        ctx.reply("Please provide a valid URL starting with http:// or https://");
        return;
    }
    exec(`python manager.py ${url}`, (error, stdout, stderr) => {
        if (error) {
            ctx.reply(`Error executing the script: ${error.message}`);
            return;
        }

        if (stderr) {
            ctx.reply(`Script error: ${stderr}`);
            return;
        }
        ctx.reply(`${stdout}`);
    });
});

bot.launch();
```

This code allows users to send a URL to the Telegram bot, which will execute the Python script and return the shortened URL directly in the chat.

## Contributing 🤝

Feel free to submit pull requests or open issues to improve this script!
