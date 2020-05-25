var Client = require('ftp');
var c = new Client();
var connectionProperties = {  //Настройка FTP
    host: "skywalkeradmin.ru",
    user: "matskywalker",
    password: "240580-Aa"
};
c.connect(connectionProperties);
var Firebird = require('node-firebird');
var options = {};
options.host = '185.174.172.61';
options.port = 3050;
options.database = 'NODEBOT';
options.user = 'SYSDBA';
options.password = 'masterkey';
options.lowercase_keys = false; // 
options.role = null;            // 
options.pageSize = 4096;        // 
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
const download = require('download')
var sleep = require('sleep');
var https = require('https');
const fs = require('fs-extra');
const watermark = require('image-watermark');
var caption = require('caption')
//fs.openSync('watermark.jpg', 'a')
const Telegraf = require('telegraf')
const Telegram = require('telegraf/telegram')
var BOT_TOKEN = process.env.BOT_TOKEN ? process.env.BOT_TOKEN : '247414626:AAH-o9OdFJnJITL7-bsDejdAPgtaTxxzF-I'
const bot = new Telegraf(BOT_TOKEN,
  {
    telegram: {
      agent: new Agent({
        socksHost: process.env.SOCS_PROXY,
        socksPort: process.env.SOCS_PORT
      })
    }
  })
const telegram = new Telegram(BOT_TOKEN)
bot.start((ctx) => ctx.reply('Привет! Вы подключились к цифровому Зеленогорску. Для получения информации введите название улицы и номер дома. Для помощи введите /hlp'))
bot.help((ctx) => ctx.reply('Для получения информации введите название улицы и номер дома.'))
bot.on('sticker', (ctx) => ctx.reply('Для получения информации введите название улицы и номер дома.'))
bot.on('photo', (ctx) =>{ 
    telegram.getFileLink(ctx.message.photo[3].file_id).then(url => {
		console.log (url);
		var val = url, split = val.split('/');
		jpegfile=split[split.length-1];
		download(url).then(data => {
			fs.writeFileSync(jpegfile, data);
			var options = {
				'text' : 'Recived by '+ctx.message.from.id;, 
				'dstPath' : jpegfile,
				'align' : 'ttb'
				};			
			watermark.embedWatermark(jpegfile, options)		
		});
one(url).then(() => two()).then(() => three());
	}); 
});
	
/* bot.hears('Мира 1', (ctx) => ctx.reply('Адрес: Мира 1, На сегодня назначено: отключение электричества с 16:00 до 16:30'))
bot.hears('мира 1', (ctx) => ctx.reply('Адрес: Мира 1, На сегодня назначено: отключение электричества с 16:00 до 16:30'))
bot.hears('мира1', (ctx) => ctx.reply('Адрес: Мира 1, На сегодня назначено: отключение электричества с 16:00 до 16:30'))
bot.hears('Мира1', (ctx) => ctx.reply('Адрес: Мира 1, На сегодня назначено: отключение электричества с 16:00 до 16:30'))
bot.hears('ул. Мира 1', (ctx) => ctx.reply('Адрес: Мира 1, На сегодня назначено: отключение электричества с 16:00 до 16:30'))
bot.hears('ул. мира 1', (ctx) => ctx.reply('Адрес: Мира 1, На сегодня назначено: отключение электричества с 16:00 до 16:30')) */
bot.hears('/hlp', (ctx) => ctx.reply('Для получения информации введите название улицы и номер дома в формате |название улицы|пробел|номер дома|'))
bot.hears('/help', (ctx) => ctx.reply('Для получения информации введите название улицы и номер дома в формате |название улицы|пробел|номер дома|'))
bot.on('text',(ctx) =>{
var usrmsg=ctx.message.text;
console.log (ctx.message.from.id)
console.log (ctx.message.text)
var sqlstring="select wplan from ZELENOGORSK where NAME LIKE '%"+usrmsg.substr(1)+"'"
//console.log (sqlstring)
Firebird.attach(options, function(err, db) {
    if (err)
        throw err;
    db.execute(sqlstring, function(err, result) {
        console.log (result);
        console.log (err);
        newresult=String(JSON.stringify(result[0]));
         if (newresult!='undefined') 
         {
        newresult=newresult.replace('[[','');
        newresult=newresult.replace(']]','');
        newresult=newresult.substr(2);
        newresult=newresult.slice(0, -2);
        ctx.reply(newresult);
         }
         else {
           ctx.reply('Нам не удалось понять, что вы хотели. Пожалуйста введите адрес в формате |название улицы|пробел|номер дома|');
         }
//        db.detach();
    });
});
});
bot.launch()
//247414626:AAH-o9OdFJnJITL7-bsDejdAPgtaTxxzF-I fen_x_bot


function one(url) {
  return new Promise(resolve => {	  
	c.on('ready', function() {
    c.put(jpegfile, '/domains/skywalkeradmin.ru/'+jpegfile, function(err) {
      if (err) {
        console.log(err.message);
    } 
    c.end();
    });
  });
  c.connect(connectionProperties);
  resolve();  
  });
}

function two() {
  return new Promise(resolve => {
	  setTimeout(() => {	  
    resolve();
	}, 100);
  });
}

function three(){
var pic_stream = 'http://skywalkeradmin.ru/'+jpegfile
setTimeout(() => {
	msg=telegram.sendPhoto('@MatSkywalker', pic_stream, { caption: ctx.message.text })
	},1000); 
}

function wtmk(watermark_text){
	var options = {
		'text' : watermark_text, 
		'dstPath' : 'watermark.jpg',
		'align' : 'ltr'
		};			
	watermark.embedWatermark('../../home/admin/web/vps26188nl.hyperhost.name/public_html/one.jpg', options)
	

	
	//copyFile ('./watermark.jpg','../../home/admin/web/vps26188nl.hyperhost.name/public_html/watermark.jpg')
};
 
// function sndmsg(){
	// wurl='http://vps26188nl.hyperhost.name/watermark.jpg'
	// console.log(wurl);
	// telegram.sendPhoto(119737966, wurl)
// };

// function copyFile(source, target) {
  // var rd = fs.createReadStream(source);
  // var wr = fs.createWriteStream(target);
  // return new Promise(function(resolve, reject) {
    // rd.on('error', reject);
    // wr.on('error', reject);
    // wr.on('finish', resolve);
    // rd.pipe(wr);
  // }).catch(function(error) {
    // rd.destroy();
    // wr.end();
    // throw error;
  // });
// }
