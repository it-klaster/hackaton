var Firebird = require('node-firebird');
var options = {};
options.host = '185.233.119.144'; // Адрес Fb сервера
options.port = 3050;
options.database = 'NODEBOT';	// Имя базы
options.user = 'SYSDBA';
options.password = 'masterkey';
options.lowercase_keys = false; // Значения по умолчанию
options.role = null;            // 
options.pageSize = 4096;        //


const Agent = require('socks5-https-client/lib/Agent');

// const BOT_TOKEN = '801626409:AAEZgD5oVdkk2nKVcSl79eSStelL9pCp-Q0'
const BOT_TOKEN = process.env.BOT_TOKEN;
const Telegraf = require('telegraf')
const Composer = require('telegraf/composer')
const session = require('telegraf/session')
const Stage = require('telegraf/stage')
const Markup = require('telegraf/markup')
const WizardScene = require('telegraf/scenes/wizard')
const stepHandler = new Composer()
var usrmsg = '_';
const test_setup = new WizardScene('test_setup_2',
    function (ctx) {
        ctx.reply('Пожалуйста введите адрес в формате |название улицы|пробел|номер дома|')
        ctx.wizard.next()
    },
    function (ctx) {
        console.log(ctx.message.text)
        usrmsg = ctx.message.text;
        var sqlstring = "select wplan from ZELENOGORSK where NAME LIKE '%" + usrmsg.substr(1) + "'"
        Firebird.attach(options, function (err, db) {
            if (err)
                throw err;
            db.execute(sqlstring, function (err, result) {
                console.log(result);
                console.log(err);
                newresult = String(JSON.stringify(result[0]));
                if (newresult != 'undefined') {
                    newresult = newresult.replace('[[', '');
                    newresult = newresult.replace(']]', '');
                    newresult = newresult.substr(2);
                    newresult = newresult.slice(0, -2);
                    ctx.reply('На данный адрес назначены следующие события: \n' + newresult);
                    //ctx.reply(newresult);
                    ctx.reply('Укажите новое событие. Напишите текст оповещения, не забудьте указать время начала и продолжительность события.')
                    ctx.wizard.next()
                }
                else {
                    ctx.reply('Нам не удалось понять, что вы хотели. Пожалуйста введите адрес в формате |название улицы|пробел|номер дома|');
                }
                //        db.detach();
            });
        });

    },
    function (ctx) {
        console.log(ctx.message.text)
        //var usrmsg=ctx.message.text;
        var sqlstring2 = "select id from ZELENOGORSK where NAME LIKE '%" + usrmsg.substr(1) + "'"
        Firebird.attach(options, function (err, db) {
            if (err)
                throw err;
            db.execute(sqlstring2, function (err, result) {
                console.log(result);
                console.log(err);
                newresult = String(JSON.stringify(result[0]));
                if (newresult != 'undefined') {
                    newresult = newresult.replace('[[', '');
                    newresult = newresult.replace(']]', '');
                    newresult = newresult.substr(2);
                    newresult = newresult.slice(0, -2);
                    var sqlstring3 = "Update ZELENOGORSK set wplan='" + ctx.message.text + "'where id=" + newresult
                    console.log(sqlstring3)
                    Firebird.attach(options, function (err, db) {
                        if (err)
                            throw err;
                        db.execute(sqlstring3, function (err, result) {
                            console.log(result);
                            console.log(err);
                        });
                    });
                    ctx.wizard.next()
                }
                else {
                    ctx.reply('Нам не удалось понять, что вы хотели. Пожалуйста введите адрес в формате |название улицы|пробел|номер дома|');
                }
                //        db.detach();
            });
        });
        ctx.wizard.next();
        ctx.wizard.steps[ctx.wizard.cursor](ctx);
    },
    function (ctx) {
        ctx.reply('Успешно');
        ctx.wizard.next();
    }
);

const bot = new Telegraf(BOT_TOKEN,
    {
        telegram: {
            agent: new Agent({
                socksHost: process.env.SOCS_PROXY,
                socksPort: process.env.SOCS_PORT
            })
        }
    })

const stage = new Stage([test_setup], { default: 'test_setup_2' })
bot.use(session())
bot.use(stage.middleware())
bot.launch()