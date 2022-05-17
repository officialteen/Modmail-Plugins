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

    @commands.command(name="ryan")
    async def ryan(self, ctx):
        urls = [
            "https://tenor.com/view/ryan-the-office-howard-gif-9141990",
            "https://tenor.com/view/ryan-sign-ryan-sign-gif-20225832",
            "https://tenor.com/view/ryandance-ryan-giraffe-giraffedance-ryangiraffe-gif-23412810",
            "https://tenor.com/view/milk-milk-and-mocha-ryan-chiaki-gif-20172256",
            "https://tenor.com/view/ryan-run-weird-gif-20236226"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="tt")
    async def tt(self, ctx):
        urls = [
            "https://cdn.discordapp.com/attachments/951136494498754582/958378478091264101/tiger_tuesday.png"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="duck")
    async def duck(self, ctx):
        urls = [
            "https://tenor.com/view/duck-yeah-gif-20435370",
            "https://tenor.com/view/lils-silly-duck-lilsduck-ducky-duck-duck-riri-the-duck-gif-19719423",
            "https://tenor.com/view/bird-dance-duck-happy-smile-gif-15512646",
            "https://tenor.com/view/duck-duckling-adorable-gif-20252450",
            "https://tenor.com/view/dancing-cute-duck-duck-cartoon-gif-21446316",
            "https://tenor.com/view/duck-fall-back-cute-falling-jump-gif-15884158",
            "https://tenor.com/view/followme-duck-duck-go-run-gif-13231144"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="marcus")
    async def marcus(self, ctx):
        urls = [
            "https://tenor.com/view/eartha-kitt-marcus-boomerang-eddie-murphy-gif-9746949g",
            "https://tenor.com/view/marcus-elmo-abcdac-gif-19454874",
            "https://tenor.com/view/little-superstar-marcus-after4ultras-celebration-happy-happy-dancing-gif-15854807",
            "https://tenor.com/view/marcus-side-eye-eyeroll-gif-14312179",
            "https://tenor.com/view/spray-marcus-no-nope-gif-15516439"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="cards")
    async def cards(self, ctx):
        urls = [
            "https://tenor.com/view/poker-face-poker-partypoker-gif-14470006",
            "https://tenor.com/view/mickey-mouse-card-gif-8709513",
            "https://tenor.com/view/ma-vie-cards-shifty-oops-fail-gif-17242923",
            "https://tenor.com/view/card-joker-playing-cards-playing-cards-ladder-cards-joker-wild-card-gif-13866104",
            "https://tenor.com/view/onwaaard-zombie-orpheus-the-gamers-hands-of-fate-tghof-gif-17172280",
            "https://tenor.com/view/bloody-battle-roblox-buzz-buzz-lightyear-magic-cards-gif-22129326"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="cubs")
    async def cubs(self, ctx):
        urls = [
            "https://tenor.com/view/cubs-cub-play-tiger-cub-tiger-gif-14369241",
            "https://tenor.com/view/carrying-cub-tiger-cub-escape-tiger-cub-lets-go-home-gif-22411407",
            "https://tenor.com/view/tiger-tiger-cub-kitty-roaring-kitty-meow-gif-20510735",
            "https://tenor.com/view/tiger-licking-lips-yummy-tasty-tiger-cubs-gif-16527606",
            "https://tenor.com/view/tiger-cub-baby-tiger-rawr-wake-up-tiger-gif-13295121",
            "https://tenor.com/view/tiger-cub-baby-tiger-sneak-tiger-tigers-gif-13295144",
            "https://tenor.com/view/tiger-cub-tiger-cub-escape-tiger-climbing-baby-tiger-gif-22411404",
            "https://tenor.com/view/animals-tiger-cub-play-cute-gif-3309557",
            "https://tenor.com/view/lion-king-simba-roar-cute-lion-cub-gif-17303165"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="moon")
    async def moon(self, ctx):
        urls = [
            "https://tenor.com/view/doge-doge-coin-to-the-moon-crypto-cryptocurrency-gif-14563637",
            "https://tenor.com/view/golden-tiger-goldentiger-coin-goldentiger-crypto-crypto-to-the-moon-golden-tiger-to-the-moon-gif-24440846",
            "https://tenor.com/view/christiangravias-collings-collingsrealestate-collingsnft-crypto-gif-24893289",
            "https://tenor.com/view/dinoswap-dino-matic-poly-quick-gif-23091993",
            "https://tenor.com/view/to-the-moon-elon-musk-gif-21490621",
            "https://tenor.com/view/safemoon-safemoonarmy-gif-22764284",
            "https://tenor.com/view/fly-me-to-the-moon-take-me-to-the-moon-send-me-to-the-moon-lets-go-to-the-moon-launch-me-to-the-moon-gif-17524452"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="baby")
    async def baby(self, ctx):
        urls = [
            "https://tenor.com/view/baby-pose-wink-cute-adorable-gif-14212692",
            "https://tenor.com/view/the-holy-baby-baby-holy-the-holy-cat-the-holy-baby-cult-gif-24153109",
            "https://tenor.com/view/americas-got-talent-agt-happy-smile-excited-gif-14880927",
            "https://tenor.com/view/kiss-day-gif-23596984",
            "https://tenor.com/view/tiger-baby-cute-cub-roar-gif-17763828"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="bands")
    async def bands(self, ctx):
        urls = [
            "https://tenor.com/view/i-want-hella-bands-lil-skies-whoispdp-tokyo-song-i-want-money-gif-23006558",
            "https://tenor.com/view/money-hustling-make-it-rain-gif-7263922",
            "https://tenor.com/view/payday-nicki-minaj-swag-hundreds-dollar-bills-gif-5403748",
            "https://tenor.com/view/two-bands-on-my-feet-on-my-feet-two-bands-bands-money-gif-13095071",
            "https://tenor.com/view/hundred-bands-everytime-hundred-bands-stacks-rich-flex-gif-13769945"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="punk")
    async def punk(self, ctx):
        urls = [
            "https://cdn.discordapp.com/attachments/931612704479793173/959470092255625247/giphy_1.gif",
            "https://cdn.discordapp.com/attachments/931612704479793173/959470092045914122/cat-nodding.gif",
            "https://cdn.discordapp.com/attachments/931612704479793173/959470091802665070/giphy.gif",
            "https://cdn.discordapp.com/attachments/931612704479793173/959470091320315954/giphy_2.gif",
            "https://cdn.discordapp.com/attachments/931612704479793173/959470090749870210/ric-flair.gif",
            "https://cdn.discordapp.com/attachments/931612704479793173/959470090443689994/halloween-skull.gif",
            "https://cdn.discordapp.com/attachments/931612704479793173/959470090238189619/beavis-and-butthead-yes.gif",
            "https://cdn.discordapp.com/attachments/931612704479793173/959470090003312640/punk-punk-is-not-dead.gif"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="bige")
    async def bige(self, ctx):
        urls = [
            "https://tenor.com/view/big-e-wwe-wrestling-25words-or-less-gif-15515016",
            "https://tenor.com/view/weartesters-sniff-sneakerhead-sniffingchris-chrissniff-gif-24057591",
            "https://tenor.com/view/future-gif-9525959",
            "https://tenor.com/view/patrick-star-evil-laugh-fire-flames-burning-gif-24546963"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="sc", aliases=['scott'])
    async def sc(self, ctx):
        urls = [
            "https://c.tenor.com/0R2CGQunyHUAAAAM/the-santa-clause-santa-clause.gif",
            "https://tenor.com/view/santaclause-fat-gif-19409679",
            "https://c.tenor.com/C_VepJ2uqG4AAAAM/santa-claus-belly.gif",
            "https://c.tenor.com/tQHgsditfgAAAAAM/santa-santaclaus.gif",
            "https://tenor.com/view/the-santa-clause-gif-7327123",
            "https://tenor.com/view/docbrown-backtothefuture-greatscott-gif-5445978",
            "https://tenor.com/view/scott-i-like-that-joker-gif-15408598",
            "https://tenor.com/view/groundhog-screaming-yelling-scott-gopher-gif-18829122"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])        
        
    @commands.command(name="jess")
    async def jess(self, ctx):
        urls = [
            "https://tenor.com/view/jessica-fallout-jess-gif-19856774",
            "https://tenor.com/view/free-elf-jess-dobby-gif-18451682",
            "https://tenor.com/view/chessies-chesapeake-shores-jess-sc-heart-home-dirty-dancing-gif-22363558",
            "https://tenor.com/view/its-jess-new-girl-jess-wink-gif-6080121"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])

    @commands.command(name="chef")
    async def chef(self, ctx):
        urls = [
            "https://tenor.com/view/chefs-kiss-french-chef-perfect-dish-excellent-food-perfection-gif-20341505",
            "https://tenor.com/view/master-chef-gordon-ramsey-gif-12002082",
            "https://tenor.com/view/swedish-chef-cooking-muppets-singing-dancing-gif-16637219",
            "https://tenor.com/view/salad-hostile-bitter-mess-messy-gif-9191505",
            "https://tenor.com/view/salt-sprinkle-chef-tada-voila-gif-7639090",
            "https://tenor.com/view/perfecto-perfect-success-aroma-yummy-gif-17840702"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])
        
    @commands.command(name="viral")
    async def viral(self, ctx):
        urls = [
            "https://tenor.com/view/im-viral-will-davis-miles-teller-get-a-job-viral-video-gif-18257614",
            "https://tenor.com/view/its-gone-viral-chicago-pd-viral-it-has-spread-going-viral-gif-20873898",
            "https://tenor.com/view/so-viral-shea-whitney-so-famous-trending-popular-gif-23644999",
            "https://tenor.com/view/young-invent-h-gang-black-spanish-rock-star-rose-hip-hop-gif-22745724",
            "https://tenor.com/view/sunglasses-cant-deal-with-it-gif-5853358",
            "https://tenor.com/view/tigerplayz-tigersir-tigerking-tiger-rgb-gif-22803638"
        ]
        rnd = random.randint(0, len(urls) - 1)
        await ctx.send(urls[rnd])
        
def setup(bot):
    bot.add_cog(cmd(bot))
