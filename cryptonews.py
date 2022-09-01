import cryptocompare
import nextcord
from nextcord.ext import commands
from nextcord.ext import tasks
from asyncio import sleep

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

async def crypto_price():
    while True:
        btc = cryptocompare.get_price('BTC', currency='USD')
        btcprice = btc['BTC']['USD']

        eth = cryptocompare.get_price('ETH', currency='USD')
        ethprice = eth['ETH']['USD']

        doge = cryptocompare.get_price('DOGE', currency='USD')
        dogeprice = doge['DOGE']['USD']

        lite = cryptocompare.get_price('LTC', currency='USD')
        liteprice = lite['LTC']['USD']

        cardano = cryptocompare.get_price('ADA', currency='USD')
        cardanoprice = cardano['ADA']['USD']

        bnb = cryptocompare.get_price('BNB', currency='USD')
        bnbprice = bnb['BNB']['USD']

        xrp = cryptocompare.get_price('XRP', currency='USD')
        xrpprice = xrp['XRP']['USD']

        shiba = cryptocompare.get_price('SHIB', currency='USD')
        shibaprice = shiba['SHIB']['USD']

        solana = cryptocompare.get_price('SOL', currency='USD')
        solanaprice = solana['SOL']['USD']

        channel = bot.get_channel(1014304744270991440)
        message = await channel.fetch_message(1014684709760016424) # Message ID
        await message.edit(content=f'**BTC:** ${btcprice} | **ETH:** ${ethprice} | **DOGE:** ${dogeprice} | **LTC:** ${liteprice} | **ADA:** ${cardanoprice} | **BNB:** ${bnbprice} | **XRP:** ${xrpprice} | **SHIB:** ${shibaprice} | **SOL:** ${solanaprice}')
        await sleep(30)

@bot.event
async def on_ready():
    print('Bot is ready!')
    bot.loop.create_task(crypto_price())  
@bot.slash_command()
async def price(ctx):
    await ctx.send("Please provide a coin to search for.")

@price.subcommand()
async def bitcoin(ctx):
    price = cryptocompare.get_price("BTC", currency='USD')
    real_price = price["BTC"]['USD'] 
    await ctx.send(f"<:bitcoin:1014676474256699444> is currently worth ${real_price}" ,ephemeral=True)

@price.subcommand()
async def ethereum(ctx):
    price = cryptocompare.get_price("ETH", currency='USD')
    real_price = price["ETH"]['USD'] 
    await ctx.send(f"<:ethereum:1014676476882342029> is currently worth ${real_price}" ,ephemeral=True)

@price.subcommand()
async def dogecoin(ctx):
    price = cryptocompare.get_price("DOGE", currency='USD')
    real_price = price["DOGE"]['USD'] 
    await ctx.send(f"<:dogecoin:1014676475649196054> is currently worth ${real_price}" ,ephemeral=True)

@price.subcommand()
async def litecoin(ctx):
    price = cryptocompare.get_price("LTC", currency='USD')
    real_price = price["LTC"]['USD'] 
    await ctx.send(f"<:litecoin:1014678003617366036> is currently worth ${real_price}" ,ephemeral=True)

@price.subcommand()
async def cardano(ctx):
    price = cryptocompare.get_price("ADA", currency='USD')
    real_price = price["ADA"]['USD'] 
    await ctx.send(f"<:cardano:1014678365971697714> is currently worth ${real_price}" ,ephemeral=True)

@price.subcommand()
async def binancecoin(ctx):
    price = cryptocompare.get_price("BNB", currency='USD')
    real_price = price["BNB"]['USD'] 
    await ctx.send(f"<:binance:1014679168933445693> is currently worth ${real_price}" ,ephemeral=True)

@price.subcommand()
async def xrp(ctx):
    price = cryptocompare.get_price("XRP", currency='USD')
    real_price = price["XRP"]['USD'] 
    await ctx.send(f"<:ripple:1014679168933445693> is currently worth ${real_price}" ,ephemeral=True)

@price.subcommand()
async def shibainu(ctx):
    price = cryptocompare.get_price("SHIB", currency='USD')
    real_price = price["SHIB"]['USD'] 
    await ctx.send(f"<:shiba:1014679973199626312> is currently worth ${real_price}" ,ephemeral=True)

@price.subcommand()
async def solana(ctx):
    price = cryptocompare.get_price("SOL", currency='USD')
    real_price = price["SOL"]['USD'] 
    await ctx.send(f"<:solana:1014680240414523502> is currently worth ${real_price}" ,ephemeral=True)

@bot.command()
async def setup(ctx):
    await ctx.send("Prices are loading...")

bot.run("MTAxNDY2OTQyNTkxNzU1ODk2Nw.GtUA9S.U0SoKpdMbKMzcRMDCcGK5syhNlXzAsZBqJvTPw")    
