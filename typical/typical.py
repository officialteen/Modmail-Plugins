import discord
from discord.ext import commands
import random

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="lfg")
    async def lfg(self, ctx):
        urls = [
            "https://tenor.com/view/lets-go-the-rock-rock-go-rock-lets-go-lg-gif-18455293",
            "https://tenor.com/view/wrestler-woo-stoked-crazy-excited-gif-4961243",
            "https://tenor.com/view/tom-brady-lets-go-super-bowl-gif-20640032",
            "https://tenor.com/view/hooray-letsgo-lets-go-gif-18410791",
            "https://tenor.com/view/aruuu-lets-goo-lets-go-hype-reaction-gif-24148009",
            "https://tenor.com/view/1inch-1inch-exchange-1inch-dex-defi-crypto-gif-24853025",
            "https://tenor.com/view/lfg-batman-gif-24589308",
            "https://tenor.com/view/roger-rogerdorn-majorleague-lfg-dorn-gif-18311747",
            "https://tenor.com/view/wheelie-rollin-they-see-me-rollin-jeep-kid-gif-19615923",
            "https://tenor.com/view/lfg-lebron-james-lebron-james-meme-gif-23044761",
            "https://tenor.com/view/orange-kid-letsgooo-orange-kid-danceing-orange-kid-letsgooo-gif-22720050"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="hype")
    async def hype(self, ctx):
        urls = [
            "https://tenor.com/view/toad-hype-overload-overload-gif-7868864",
            "https://tenor.com/view/wassup-dance-lol-hype-gif-14697751",
            "https://tenor.com/view/fist-gif-5303912",
            "https://tenor.com/view/funny-lit-hype-dance-gif-11045431",
            "https://tenor.com/view/dance-happy-food-gettin-it-getting-hype-gif-10970905",
            "https://tenor.com/view/hype-letsgooo-gif-23992999",
            "https://tenor.com/view/yes-ben-man-hype-pumped-gif-9117880",
            "https://tenor.com/view/my-little-pony-hype-train-hype-pinkie-pie-mlp-gif-17722254",
            "https://tenor.com/view/post-malone-hype-excite-lets-go-excitement-gif-21872605",
            "https://tenor.com/view/hga-giraffe-high-giraffe-academy-gif-23886522",
            "https://tenor.com/view/fnaf-all-board-da-hype-train-hype-train-train-hype-gif-17722508",
            "https://tenor.com/view/hyped-happy-yessirr-yes-sir-lets-go-gif-17289987",
            "https://tenor.com/view/territaku-terricord-maisha16-maisha-get-hyped-get-hyped-gif-14996555",
            "https://tenor.com/view/jonah-hill-yay-african-child-screaming-shouting-gif-7212866",
            "https://tenor.com/view/shaquille-o-neal-excited-shaking-gif-10121476",
            "https://tenor.com/view/im-very-excite-borat-sagdiyev-thrilled-happy-excited-gif-16967356"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="seal")
    async def seal(self, ctx):
        urls = [
            "https://tenor.com/view/seal-running-away-cute-weird-animal-gif-17851078",
            "https://tenor.com/view/seal-dgaf-seal-with-it-gif-7886518",
            "https://tenor.com/view/approval-gif-21949773",
            "https://tenor.com/view/turbo-seal-seal-seal-bounce-bounce-ethanol-gif-24368220",
            "https://tenor.com/view/seal-gif-9929469",
            "https://tenor.com/view/seal-sax-spin-cute-gif-8848340",
            "https://tenor.com/view/seal-baikal-seal-nico-toba-head-bang-gif-20734367",
            "https://tenor.com/view/cute-animals-cute-seal-approve-approved-gif-17095963",
            "https://tenor.com/view/baby-seal-cute-animals-gif-16233025",
            "https://tenor.com/view/seal-itchy-cute-cute-seal-animal-gif-17162374"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="incoming")
    async def incoming(self, ctx):
        urls = [
            "https://tenor.com/view/fail-hurricane-ocean-funny-boat-gif-18563156",
            "https://tenor.com/view/funny-animals-i-am-coming-cute-bear-gif-12241903",
            "https://tenor.com/view/incoming-watch-out-duck-down-get-down-explosion-gif-12872772",
            "https://tenor.com/view/banger-incoming-gif-23465008",
            "https://tenor.com/view/dog-coming-in-hot-jet-ski-gif-9915773",
            "https://tenor.com/view/steelerstandard-ivanrapoport-steelers-chat-frank-typing-straight-facts-gif-22556065",
            "https://tenor.com/view/incoming-the-fresh-prince-of-bel-air-carlton-alfonso-ribeiro-here-we-go-gif-14999483"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="gm")
    async def gm(self, ctx):
        urls = [
            "https://tenor.com/view/milk-mocha-milk-and-mocha-bears-morning-mornin-gif-17296004",
            "https://tenor.com/view/tired-sleepy-tomand-jerry-tom-conference-gif-18883074",
            "https://tenor.com/view/taco-taco-tuesday-gm-taco-tribe-good-morning-gif-24554577",
            "https://tenor.com/view/gm-good-morning-generative-gif-23737299",
            "https://tenor.com/view/gm-gm-degen-degen-gif-24444532",
            "https://tenor.com/view/funny-dogs-cute-smile-gif-20846490",
            "https://tenor.com/view/tired-yawn-boring-baby-good-morning-gif-17056340",
            "https://tenor.com/view/monkey-ape-dance-dancing-orangutan-gif-19156402",
            "https://tenor.com/view/anitashaw-runningfast-gif-21383292",
            "https://tenor.com/view/carol-baskin-hey-all-you-cool-cats-and-kittens-tiger-king-gif-16938638"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="gn")
    async def gn(self, ctx):
        urls = [
            "https://tenor.com/view/mmi-morsmutual-gn-good-night-good-night-love-gif-24009700",
            "https://tenor.com/view/puddingdos-bytehomies-byteapp-byte-gif-21368958",
            "https://tenor.com/view/i-love-you-goodnight-love-texting-chatting-gif-14508479",
            "https://tenor.com/view/night-vec50-gif-22243719",
            "https://tenor.com/view/%E3%81%8A%E3%82%84%E3%81%99%E3%81%BF-%E5%AF%9D%E3%82%8B-%E5%B9%B8%E3%81%9B-good-night-sleep-gif-15782424",
            "https://tenor.com/view/night-gif-19086031",
            "https://tenor.com/view/sleep-good-night-cat-gif-24504919",
            "https://tenor.com/view/night-good-night-sleep-tired-collapse-gif-10609182",
            "https://tenor.com/view/gnvibe-gif-22339526"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="sweep")
    async def sweep(self, ctx):
        urls = [
            "https://tenor.com/view/broom-sweep-dirt-gif-4766890",
            "https://tenor.com/view/broom-sweep-patrick-fail-stupid-gif-5417128",
            "https://tenor.com/view/broom-sweep-raccoon-gif-5417118",
            "https://tenor.com/view/cleaning-meltdown-tantrum-baby-broom-gif-15616761",
            "https://tenor.com/view/clean-cleaning-sweep-sweeping-mickey-gif-4550405",
            "https://tenor.com/view/sweeping-charles-barkley-gif-18506616",
            "https://tenor.com/view/sweeping-cleaning-mopping-mr-clean-gif-17663331",
            "https://tenor.com/view/mrs-doubtfire-cleaning-dancing-happy-gif-15445847",
            "https://tenor.com/view/spongebob-sweeping-smiling-gif-11862970",
            "https://tenor.com/view/clean-sweep-gif-22946460",
            "https://tenor.com/view/sweep-the-floor-nft-floor-sweep-nft-sweep-gif-23346840",
            "https://tenor.com/view/yell-yellmagic-sweep-gif-22520056"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="queen")
    async def queen(self, ctx):
        urls = [
            "https://tenor.com/view/rihanna-crown-queen-princess-own-it-gif-4897467",
            "https://tenor.com/view/in-the-house-queen-party-walking-into-the-party-diva-gif-13347653",
            "https://tenor.com/view/crown-crowning-queen-gif-21862956",
            "https://tenor.com/view/queen-elizabeth-the-second-queen-elizabeth-england-canada-canadian-gif-17900765",
            "https://tenor.com/view/yas-queen-yasss-girl-sassy-gif-24235716",
            "https://tenor.com/view/the-outpost-the-outpost-series-thecw-gulman-randall-malin-gif-12842854",
            "https://tenor.com/view/bianca-belair-wwe-nxt-nxt-takeover-wwe-pc-gif-16361723",
            "https://tenor.com/view/katy-perry-queen-crown-proud-classy-gif-12763178",
            "https://tenor.com/view/yas-queen-yass-kid-happy-cheer-gif-4928090"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="tiger")
    async def tiger(self, ctx):
        urls = [
            "https://tenor.com/view/tiger-roar-gif-11804661",
            "https://tenor.com/view/international-tiger-day-tiger-animals-gif-puli-gif-18973976",
            "https://tenor.com/view/tiger-wink-gif-14380645",
            "https://tenor.com/view/cute-heart-love-tigger-gif-15562888",
            "https://tenor.com/view/tiger-tiger-cub-kitty-roaring-kitty-meow-gif-20510735",
            "https://tenor.com/view/tiger-grrr-growl-animal-teeth-gif-16295316",
            "https://tenor.com/view/tiger-dancing-happy-gif-15857023",
            "https://tenor.com/view/pet-tiger-big-cat-tigers-petting-gif-16685132",
            "https://tenor.com/view/tony-the-tiger-dancing-weekend-vibe-gif-13760533",
            "https://tenor.com/view/tiger-licking-dog-this-is-happening-friendly-tiger-animal-friendship-tiger-grooming-dog-gif-18861911",
            "https://tenor.com/view/bathtime-searching-for-the-tigress-secret-life-of-tigers-nat-geo-wild-its-cleaning-time-gif-22410834",
            "https://tenor.com/view/roar-nat-geo-wild-animal-fight-night-growl-outcry-gif-22410524",
            "https://tenor.com/view/scared-tiger-booo-suprised-shocked-gif-17203252",
            "https://tenor.com/view/tiger-jump-wall-gif-18169720",
            "https://tenor.com/view/running-tiger-tigers101-nat-geo-wild-running-fast-gif-22410668",
            "https://tenor.com/view/katy-perry-tiger-dance-dancing-party-hard-celebrate-gif-9565972"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="carole")
    async def carole(self, ctx):
        urls = [
            "https://tenor.com/view/carole-baskin-tiger-king-love-you-blowing-kisses-air-kiss-gif-17797819",
            "https://tenor.com/view/hey-all-you-cool-cats-and-kittens-carole-baskin-cameo-tiger-hey-gif-17759024",
            "https://tenor.com/view/hey-all-you-cool-cats-and-kittens-carol-baskin-tiger-king-gif-16717339",
            "https://tenor.com/view/love-you-carole-baskin-cameo-blow-kiss-ily-gif-17759020",
            "https://tenor.com/view/tiger-king-carole-baskin-whatever-yeah-chill-gif-16889845",
            "https://tenor.com/view/tiger-carole-baskin-cameo-look-back-laugh-gif-17759030"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="dance")
    async def dance(self, ctx):
        urls = [
            "https://tenor.com/view/tiger-dancing-happy-gif-15857023",
            "https://tenor.com/view/tigger-bouncing-dancing-dancing-tiger-dance-gif-18325898",
            "https://tenor.com/view/tony-the-tiger-dancing-weekend-vibe-gif-13760533",
            "https://tenor.com/view/tiger-dance-tiger-belly-sassy-body-paint-gif-15006607",
            "https://tenor.com/view/dance-kid-gif-17962746",
            "https://tenor.com/view/yay-yes-yeahhh-cute-girl-happy-dance-gif-14559695",
            "https://tenor.com/view/happy-dancing-celebrate-excited-gif-13870839",
            "https://tenor.com/view/lfg-patriots-go-gif-15264268",
            "https://tenor.com/view/dance-kid-club-gif-9152583",
            "https://tenor.com/view/crazy-dance-funny-dance-michael-scott-dance-danse-marrante-debile-gif-21385827",
            "https://tenor.com/view/happy-dancing-happy-birthday-to-you-excited-dance-dancing-gif-12195909",
            "https://tenor.com/view/dance-funny-gif-4660204",
            "https://tenor.com/view/dancing-funny-funny-dance-siblings-brothers-gif-16707395"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="vibe")
    async def vibe(self, ctx):
        urls = [
            "https://tenor.com/view/the-simpsons-bart-vibe-groove-dance-gif-5472520",
            "https://tenor.com/view/cat-vibe-153bpm-gif-18260767",
            "https://tenor.com/view/vibby-vibby-vibes-vibes-gif-22617156",
            "https://tenor.com/view/vibe-gif-21932627",
            "https://tenor.com/view/teo-cat-vibe-gif-24184240",
            "https://tenor.com/view/spongebob-dance-vibe-good-mood-gif-4959446",
            "https://tenor.com/view/dancing-dance-weekend-vibe-gif-10208597",
            "https://tenor.com/view/its-a-vibe-alyssa-wallace-its-a-trend-trend-vibe-gif-17352212",
            "https://tenor.com/view/2chainz-its-a-vibe-gif-13619818"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="wagmi")
    async def wagmi(self, ctx):
        urls = [
            "https://tenor.com/view/we-gonna-make-it-david-styles-styles-p-jason-terrance-phillips-jadakiss-gif-21046811",
            "https://tenor.com/view/youre-gonna-make-it-dorinda-medley-cameo-youre-gonna-succeed-youre-gonna-pull-it-off-gif-18537800",
            "https://tenor.com/view/tedlasso-wagmi-ted-lasso-10ktf-gif-24729836",
            "https://tenor.com/view/1inch-1inch-exchange-1inch-dex-defi-crypto-gif-24852799",
            "https://tenor.com/view/remember-wagmi-gif-24067442"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="sold")
    async def sold(self, ctx):
        urls = [
            "https://tenor.com/view/sale-by-jordan-belfort-sale-throw-gif-14812374",
            "https://tenor.com/view/leonardo-dicaprio-sold-gif-gif-20734009",
            "https://tenor.com/view/justmoneytrx-just-money-tron-gif-22331476",
            "https://tenor.com/view/bugs-bunny-looney-tunes-cash-money-counting-money-gif-17544086",
            "https://tenor.com/view/sold-ray-ray-butani-schitts-creek-ep204-gif-20106341",
            "https://tenor.com/view/sold-happy-celebrating-real-estate-gif-14286622",
            "https://tenor.com/view/premiumcars-premiumautomotive-luxurycars-caviarz-cars-gif-19559693"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="welcome")
    async def welcome(self, ctx):
        urls = [
            "https://tenor.com/view/the-god-father-marlon-brando-vito-corleone-talk-to-me-gif-20107028",
            "https://tenor.com/view/forest-gump-welcome-group-gif-18109761",
            "https://tenor.com/view/star-wars-baby-yoda-the-mandalorian-welcome-wave-gif-16179355",
            "https://tenor.com/view/hello-welcome-dr-evil-come-gif-17033528",
            "https://tenor.com/view/dreamteam-gif-20922376",
            "https://tenor.com/view/welcome-welcome-to-the-team-minions-gif-21749603",
            "https://tenor.com/view/spongebob-gif-24426684",
            "https://tenor.com/view/hello-there-private-from-penguins-of-madagascar-hi-wave-hey-there-gif-16043627",
            "https://tenor.com/view/garfield-hi-there-waving-friendly-cats-gif-18946417",
            "https://tenor.com/view/hey-tom-hanks-forrest-gump-gif-5114770",
            "https://tenor.com/view/inside-out-hi-hello-hey-there-hope-all-is-well-gif-21232199",
            "https://tenor.com/view/whats-up-buttercup-the-mandalorian-the-child-hey-there-gif-22217272",
            "https://tenor.com/view/looney-tunes-daffy-duck-hello-greetings-well-hello-there-gif-17075737"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="snipe")
    async def snipe(self, ctx):
        urls = [
            "https://tenor.com/view/sniper-pubg-loading-sniper-reload-gif-15505006",
            "https://tenor.com/view/jason-bourne-matt-damon-sniper-gif-5687676",
            "https://tenor.com/view/family-guy-peter-griffin-gun-point-sniper-rifle-gif-16445332",
            "https://tenor.com/view/donald-trump-president-debate-usa-america-gif-18667551",
            "https://tenor.com/view/sniper-saving-private-ryan-private-jackson-wwii-snipe-gif-21409137",
            "https://tenor.com/view/cats-sniper-gun-shoot-gif-8878036",
            "https://tenor.com/view/american-sniper-chris-kyle-navy-gif-19018265",
            "https://tenor.com/view/sniper-sniping-shooting-guns-shoot-gif-9579894",
            "https://tenor.com/view/sniper-bucky-shooting-shoot-rifle-gif-8772689",
            "https://tenor.com/view/fluen-buster-sniper-scope-gif-16921529"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="wen")
    async def wen(self, ctx):
        urls = [
            "https://tenor.com/view/when-wen-naru-yummi-yummi-universe-gif-23030317",
            "https://tenor.com/view/cnft-nft-wen-when-over-exposed-gif-24787226",
            "https://tenor.com/view/popcat-wen-gif-23885304",
            "https://tenor.com/view/wen-gif-24387044"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="outrageous")
    async def outrageous(self, ctx):
        urls = [
            "https://tenor.com/view/kevin-o-leary-shark-tank-outrageous-absurd-ridiculous-gif-6895750",
            "https://tenor.com/view/mae-do-marco-m%C3%A3e-do-marco-gif-20779134"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="whale")
    async def whale(self, ctx):
        urls = [
            "https://tenor.com/view/mae-do-marco-m%C3%A3e-do-marco-gif-20779134",
            "https://tenor.com/view/whale-hellothere-hello-hi-hey-gif-4505186",
            "https://tenor.com/view/1inch-1inch-exchange-1inch-dex-defi-crypto-gif-24852783",
            "https://tenor.com/view/oh-whale-swim-whale-cartoon-oh-well-gif-15436720",
            "https://tenor.com/view/whale-activity-whale-activity-fatih-kev-gif-24585224",
            "https://tenor.com/view/drink-water-drinking-fish-thirsty-whaleshark-gif-17289007",
            "https://tenor.com/view/unusual-whales-unusual-whales-rain-money-gif-23090764",
            "https://tenor.com/view/underwater-whale-gif-24576671",
            "https://tenor.com/view/whale-swallow-eat-nom-hungry-gif-17097355"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

def setup(bot):
    bot.add_cog(cmd(bot))
