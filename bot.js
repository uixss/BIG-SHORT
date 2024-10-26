import { Telegraf } from 'telegraf'; 
import { exec } from 'child_process';

const bot = new Telegraf('');


bot.command('short', (ctx) => {
    const url = ctx.message.text.split(' ')[1];

    if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) {
        ctx.reply("http:// o https://");
        return;
    }
    exec(`python manager.py ${url}`, (error, stdout, stderr) => {
        if (error) {
            ctx.reply(`Error ejecutando el script: ${error.message}`);
            return;
        }

        if (stderr) {
            ctx.reply(`Error en el script: ${stderr}`);
            return;
        }
        ctx.reply(`${stdout}`);
    });
});

bot.launch();
