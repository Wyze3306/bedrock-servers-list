# Minecraft Bedrock Server List

An open, community-maintained list of **Minecraft Bedrock Edition** servers (mobile, console, Windows 10/11).
Every server has an IP, a port, a description and a language, and most have a logo, a cover picture and a few more pictures in [`art/`](art).

- Ready-to-use data: [`servers.json`](servers.json) and [`servers.csv`](servers.csv)
- One JSON file per server in [`servers/`](servers)
- Contributions welcome: add or fix a server with a pull request, see [CONTRIBUTING.md](CONTRIBUTING.md)

The list is kept clean on purpose: only servers on the default port `19132` and reachable through a domain name are listed (no numeric IP addresses), and names are cleaned of versions, links and decorative symbols.

> The initial list was imported from [minecraftpocket-servers.com](https://minecraftpocket-servers.com/). Each imported entry keeps a `source` link to its original page. The language does not exist on the original site, so it was guessed automatically (description first, then country): feel free to fix it. Server descriptions are kept in their original language, given by the `lang` field.

## Add or edit a server

1. Fork this repository.
2. Create or edit `servers/<server-name>.json`:

```json
{
  "name": "My Server",
  "ip": "play.myserver.net",
  "port": 19132,
  "description": "Survival, minigames and weekly events.",
  "lang": "en",
  "image": "https://example.com/banner.png",
  "logo": "https://raw.githubusercontent.com/Wyze3306/bedrock-servers-list/main/art/logos/my-server.png",
  "cover": "https://raw.githubusercontent.com/Wyze3306/bedrock-servers-list/main/art/covers/my-server.jpg",
  "gallery": ["https://raw.githubusercontent.com/Wyze3306/bedrock-servers-list/main/art/gallery/my-server-0.jpg"],
  "country": "United States of America",
  "version": "1.21",
  "website": "https://myserver.net",
  "discord": "https://discord.gg/xxxx",
  "tags": ["Survival", "Minigames"]
}
```

3. Open a pull request. The CI validates the format automatically. Do not edit `servers.json`, `servers.csv` or the table below: they are regenerated after the merge.

Required fields: `name`, `ip`, `port`, `description`, `lang`. All others are optional.

## Use the data

```bash
curl -s https://raw.githubusercontent.com/Wyze3306/bedrock-servers-list/main/servers.json
```

## Server list

<!-- SERVERS:START -->
**660 servers** · languages: `en` 393, `fr` 46, `id` 39, `tr` 38, `es` 32, `de` 28, `pt-BR` 22, `ru` 17, `zh` 10, `vi` 6, `pl` 6, `ja` 4

| Server | IP | Port | Lang | Description |
|---|---|---|---|---|
| [2 Oyun Modu](https://granosnetwork.com) | `oyna.granosnetwork.com` | `19132` | tr | Sunucumuzda eyalet sistemi var townyden farklı olarak kendi kasabanı falan kurma gibi bir şey yok. Hazırda 5 tane eya... |
| [2b2e](https://ign.gg) | `2b2e.org` | `19132` | en | 2b2e is a Minecraft Bedrock Edition anarchy server founded on the 25th of March 2020. 2b2e is one of the oldest anarc... |
| [2b2t](https://ign.gg) | `play.2b2t.be` | `19132` | en | 2B2TBE is a Cross Platform Server built upon an Anarchy Society where players can expect absolute freedom.  This will... |
| [2b2tjb](https://2b2tjb.jp/) | `2b2tjb.jp` | `19132` | ja | JEでもBEでも入れる 2B2T サーバーです。  ルールはありません。  何かしたからといってBANなどはしません。  ※Servercrusherを作る人は対象外です(BANします)  チート, PK などなんでもOK。  BE版... |
| 2b2tmcpe | `2b2tmcpe.org` | `19132` | en | 2b2tmcpe.org Minecraft Bedrock Edition anarchy server  No rules \| Hacking allowed \| 350k+ unique players \| Join th... |
| [2b2tpe](https://ign.gg) | `2b2tpe.org` | `19132` | en | 2b2tPE.org (also 2b2tBE.org) is the unofficial pocket (or bedrock) edition of the java 2b2t.org for mobile and window... |
| 2b2w | `2b2w.org` | `19132` | en | Vanilla Survival/Anarchy server.   IP: 2b2w.org  Port: 19132  World was created 3/23/2021 and is now over 4 years old... |
| 3b3tpe | `3b3tpe.org` | `19132` | en | 3b3tpe — Bedrock Anarchy  3b3tpe is a Minecraft survival server for bedrock players in a free for all no rules enviro... |
| 404servernotfound | `play.404servernotfound.net` | `19132` | en | 404 // SERVER NOT FOUND – Faction PvP with 1.8 PvP (old combat, no attack cooldown). Java & Bedrock cross-play.  Clai... |
| [424friends](https://424friends.net/) | `play.424friends.net` | `19132` | en | The official 424Friends cross-platform (java / bedrock) SMP Minecraft server! 424Friends is a UK and Western Europe G... |
| [4blocks](https://4blocks.gg) | `4blocks.gg` | `19132` | en | 4BlocksRP is a German-speaking city roleplay server, and Bedrock players are welcome. Join from phone, tablet or cons... |
| [6b6t](https://www.6b6t.org) | `bedrock.6b6t.org` | `19132` | en | 6b6t is a Minecraft anarchy server with no rules, where over 150 players come daily to play, build, raid, and explore... |
| [A Girls-Only Server](http://pin.ngel.ru) | `pin.ngel.ru` | `19132` | en | All girls are invited to join the ultimate community!  Unleash girls' power without any nasty or violent boys!  Towny... |
| ADSLabs MC Server | `bedrock.adslabs.dev` | `19132` | en | ADSLabs SMP: Bedrock Survival  A survival multiplayer server for Minecraft Bedrock Edition. Play from Windows, Xbox, ... |
| [Advancius Network](https://www.advancius.net/) | `mc.advancius.net` | `19132` | en | 🌟 JOIN TODAY FOR A FREE RANK 🌟Tired of pay-to-win servers? Check out our 100+ FREE ranks on our 20+ gamemodes includi... |
| [AdventureCraft](https://advcraft.gg) | `advcraft.gg` | `19132` | en | *** $200 BUILD CONTEST - runs until 10/31/26 ***  THEME: design our next SPAWN CASTLE + TOWN. Build it on your own cr... |
| [Aenat](http://aenat.net) | `mc.aenat.net` | `19132` | vi | AENAT là một máy chủ Minecraft được xây dựng theo định hướng Survival RPG, nơi mỗi người chơi đều có thể bắt đầu từ c... |
| [AetheriumNetwork](https://www.aetheriummc.xyz) | `play.aetheriummc.xyz` | `19132` | es | Welcome to **AetheriumMC Network**, where survival becomes an unforgettable adventure.  Discover a carefully crafted ... |
| [AkumaMC](https://akumamc.net/) | `bedrock.akumamc.net` | `19132` | en | AkumaMC - Best Minecraft Prisons, Skyblock, Survival, Gens & Cobblemon Server 2026  IP: play.akumamc.net  Discord: di... |
| [AlamNusa](https://store.alamnusa.net/) | `mc.alamnusa.net` | `19132` | id | 🍃 AlamNusa \| RPG & Adventure Server 🍃  Masuki dunia di mana petualanganmu menentukan segalanya. Hadapi bos epik, tem... |
| [Alannetwork](http://alannw.com) | `play.alannw.com` | `19132` | tr | 🚀 ALAN NETWORK \| 1.21.x & Bedrock Sürümünün En Efsane Adresi!  Büyük maceraya hazır mısın? play.alannw.com adresinde... |
| Aloi | `mc.aloi.si` | `19132` | de | PietSmiet Community :) |
| [Aloo SMP](https://site.aloosmp.fun) | `play.aloosmp.fun` | `19132` | en | 🥔 ALOO SMP 🥔  The Ultimate 24/7 Public Survival, PvP & Mini-Games Experience!  ⚡ OVERVIEW ⚡  Welcome to Aloo SMP, the... |
| [Anarchadia](https://anarchadia.org) | `bedrock.anarchadia.org` | `19132` | en | Welcome to Anarchadia – an anarchy server where Minecraft stays true to its block game roots. Established on January ... |
| [Anarchy Survival](https://anarchy.ac) | `mc.anarchy.ac` | `19132` | en | Anarchy is a vanilla Minecraft server running since 23rd of June 2024, offering the ultimate freedom to play Minecraf... |
| AngelzMC | `hub.angelzmc.com` | `19132` | en | Welcome to AngelzMC we are a new modern SMP server with a cozy chill vibe!  Relax, explore, build. A laid-back surviv... |
| [AnyCraft](https://www.anycraft.org) | `www.anycraft.org` | `19132` | en | Welcome to AnyCraft, a free, public, and semi-vanilla multiplayer Minecraft server available for everyone to play! Pl... |
| Aogire | `aogiremc.duckdns.org` | `19132` | en | AogireMC (MCPE 0.14.x & 0.15.10) |
| [Apeiron Craft](http://discord.apeironcraft.id) | `mps.apeironcraft.id` | `19132` | id | Apeiron Craft: Survival santai bareng temen 🇮🇩  Server Minecraft Indonesia, host di Singapore jadi ping aman buat pem... |
| [ApoloMC Network](https://shadownmc-store.tebex.io/) | `play.shadownmc.lol` | `19132` | es | EL MEJOR SERVER SMP con muy buena comunidad, para todo tipo de jugadores. Contamos conn nuestra modalidad estrella; S... |
| [Appleks](https://appleks.ru/) | `appleks.ru` | `19132` | ru | Добро пожаловать на сервер appleks, где твоё мастерство выживать и находчивость будут подвержены настоящей проверке! ... |
| [APPLEMC The Fruitiest Network](https://applemc.fun/) | `play.applemc.fun` | `19132` | en | [Version 1.18 - 1.19] AppleMC is 1 of the largest servers that hosts major events weekly and performs daily updates. ... |
| [AppleSMP](https://minecraftservers-list.com/) | `play.applesmp.org` | `19132` | en | Every active Java and Bedrock server, ranked by player votes and updated daily — Survival, SkyBlock, Factions, Prison... |
| [Aqualand](http://aqualand.u3002.com) | `play.u3002.com` | `19132` | en | Aqualand is a simple cross platform survival server  < Basic rules >  - Respect Others. Respect Yourself.  - Do not G... |
| [ArabSkills](http://www.arabskills.net) | `arabskills.net` | `19132` | en | 🎮 Step into ArabSkills Network, the ultimate Arabic Minecraft experience!  Join one of the fastest-growing communitie... |
| [ARC Server](https://atherices.com) | `play.atherices.com` | `19132` | tr | SkyBlock and more! |
| [Arden Network](https://store.ardennetwork.net/) | `play.ardennetwork.net` | `19132` | id | No description provided. |
| [Arenahub Mumbai](https://arenahub.pro/) | `play.arenahub.pro` | `19132` | en | Welcome to ArenaHub Mumbai! The best Indian server for Mobile and PC players featuring OneBlock, Lifesteal, Custom Cr... |
| Arona Network | `arona.asia` | `19132` | en | Minecraft Bedrock PvP Practice Server located in China  Focused on Duels, FFA, and competitive PvP gameplay.  Train y... |
| [ArosMC](http://www.alacanetwork.com) | `oyna.alacanetwork.com` | `19132` | tr | ? ALACANETWORK SKYBLOCK  Gökyüzünde yalnızsın… Ta ki kendi krallığını kurana kadar! ☁️?  Sıfırdan başla, adanı büyüt,... |
| [Arsyanet](https://arsyanet.site) | `arsyanet.my.id` | `19132` | id | 🌟 ArsyaNet adalah server Minecraft Bedrock bertema Survival RPG dengan berbagai fitur custom, gameplay yang menarik, ... |
| Artelia | `artelia.mcbe.fr` | `19132` | fr | ⛓️・ARTELIA PRISON 💎  🔮 Bienvenue à Artelia, une prison pas comme les autres…  ⛏️ Mine. 💰 Gagne. 📈 Progresse. 👑 Domine... |
| ArtMine | `artminepe.ru` | `19132` | ru | Э |
| Arvee Prison | `play.arvee.world` | `19132` | en | Looking for more than ordinary Minecraft survival? Welcome to Arvee Survival!  ⚔️ EliteMobs RPG — fight dangerous eli... |
| Asagiri Realms | `asagirirealms.mcserver.us` | `19132` | en | Welcome to Asagiri Realms — a modded Bedrock survival server for explorers, builders, and boss hunters.  Jump into an... |
| AsiaPots | `asiapots.club` | `19132` | en | Best PotPvP server for Asian |
| [AspiredMC](https://www.aspiredmc.net) | `play.aspiredmc.net` | `19132` | en | AspiredMC is a minecraft network that holds plans to provide a top of the line experience to all players, with our ma... |
| AsteriaMC | `play.asteriamc.my.id` | `19132` | id | No description provided. |
| AsterMC | `play.astermc.org` | `19132` | en | AsterMC is a BRAND NEW, Space-themed survival server with factions, economy, OP-enchants, custom skins, custom plugin... |
| [Asteron SMP](http://overclocksmp.com) | `play.overclocksmp.com` | `19132` | en | A minecraft bedrock public economy server using Blurry's Java PvP. Team with other players and become the richest pla... |
| [Astra x](http://astramcpe.vercel.app) | `astramcpe.sytes.net` | `19132` | en | Server 24/7 Minigames & PvP |
| [Astrid Cloud](https://discord.gg/6wck37kJgg) | `play.astridcloud.xyz` | `19132` | en | Welcome to ASTRIDCLOUD!  Embark on an immersive Minecraft RPG adventure in a world designed for thrill-seekers and ch... |
| [AstroNovaMC](https://astronovamc.it) | `play.astronovamc.it` | `19132` | it | AstroNova MC è un server Minecraft italiano a tema cosmico. Java e Bedrock entrano sullo stesso indirizzo: play.astro... |
| [Asts](https://asts.tw/?lang=auto) | `mc.asts.tw` | `19132` | zh | Discord: https://go.asts.tw/dc |
| [AT Hub Server](https://at-hub.net) | `play.at-hub.net` | `19132` | en | A Minecraft Bedrock server that brings together building, exploration, and competition within a welcoming community f... |
| [AtlantikMC](https://atlantikmc.com) | `oyna.atlantikmc.com.tr` | `19132` | pt | AtlantikMC, Gelişmiş Sistemlere sahip bir Survival sunucusudur.  Bedrock (Mobil) giriş mevcuttur.  IP: oyna.atlantikm... |
| [AuraLife](https://auralife.uz) | `auralife.uz` | `19132` | en | AuraLife — O‘zbekiston Minecraft Bedrock survival serveri. Iqtisod, clanlar, PvP, duellar, eventlar va o‘zbek/rus til... |
| [Aussie Gamers MC](https://aussiegamers.com.au/) | `play.aussiegamers.com.au` | `19132` | en | G'day, mate! Come build with us.  Aussie Gamers MC is a cozy, community-run network hosted in Sydney, so Aussie and K... |
| [Avenian Network](https://jaystechvault.craftingstore.net/) | `play.jaystechvault.com` | `19132` | en | Just a Survival SMP with an Economy.  Youtube: youtube.com/c/Avient  Rank store: https://jaystechvault.craftingstore.... |
| Avorium | `avorium.org` | `19132` | en | A Community based Server, with the Best Combat Style on every Server. We make Games for our Community. |
| Axolotl-PM Server | `foxymc.de` | `19132` | en | FoxyMC is a brandnew Minecraft Bedrock server currently in beta - join now and be part of our community!  Dive into A... |
| Azure Craft | `play.herozdev.net` | `19132` | en | Heroz Network is three gamemodes built from scratch, each with custom 3D models, animations and its own resource pack... |
| [BagelSMP](https://bagelsmp.com/?ip=mps) | `mps.bagelsmp.com` | `19132` | en | BagelSMP is a competitive Minecraft server where you grind for loot and fight other players to climb to the top. Join... |
| [Bagelton Network](http://bagelton.com) | `bagelton.com` | `19132` | en | The Bagelton Network is a server that me and some friends have been working on with creative, minigames, survival, an... |
| [Balikbayan SMP](https://discord.gg/hZSqUQ7VYc) | `balikbayan.minecraft.best` | `19132` | en | Our server aims to be a peaceful place to unwind after a long day at school or work—a world where you can relax, have... |
| [BananaSMP](https://store.blockfun.gg/) | `play.blockfun.store` | `19132` | en | Blockfun is a brand new SMP Network! We plan on becoming a one-stop network for all and any SMP gameplay desires! Her... |
| [BCraft](https://bcraft.cl) | `jugar.bcraft.cl` | `19132` | es | ¡Aventura, libertad y diversión te esperan en BCraft! Explora un mundo lleno de posibilidades, construye tu hogar, pr... |
| [Bedrock Zenvairo](https://skycloud.es) | `mc.skycloud.es` | `19132` | es | Una network en español ideal para:  - Jugar a las aventuras en solitario o acompañado: Tenemos varios modos de juego ... |
| [Bedrockanarchy](http://bedrockanarchy.org) | `bedrockanarchy.org` | `19132` | en | BedrockAnarchy is a vanilla anarchy server for bedrock edition with a map that never resets. There are no set rules s... |
| [Bedrockia](https://bedrockia.net) | `bedrockia.net` | `19132` | de | # Bedrockia – Erbaue eine gemeinsame Welt  Bedrockia ist ein deutschsprachiger Minecraft-Server für kreative Spieler,... |
| [Bedwars & New Game](https://www.cubecraft.net/) | `play.cubecraft.net` | `19132` | en | CubeCraft Games is one of the largest and longest-running Minecraft networks, offering a wide selection of multiplaye... |
| [Belsarun Network](https://belsarun.tebex.io/) | `belsarun.net` | `19132` | es | Belsarun Network \| Survival Semi-Custom  Una nueva aventura comienza aquí. Explora Dungeons, descubre minas llenas d... |
| [Benwyw](https://www.benwyw.com) | `mc.benwyw.com` | `19132` | en | 🎮 Welcome to Ben’s Minecraft Server!  Looking for a fresh, lag-free Survival experience? Whether you’re on PC, Mobile... |
| [BerrySMP](https://store.berrysmp.net) | `pe.berrysmp.net` | `19132` | en | Welcome to BerrySMP!  Our community is super friendly and we all love to play on BerrySMP: a java + bedrock crossplay... |
| [BestPE](https://bestpe.pl) | `bestpe.pl` | `19132` | pl | Naszym celem nie jest tworzenie przesadnie skomplikowanego serwera pełnego niepotrzebnych systemów. Stawiamy na przyj... |
| [Betafied](https://www.betafied.net) | `play.betafied.net` | `19132` | en | BETAFIED: MINECRAFT BETA 1.7.3 FOR BEDROCK  Betafied brings Minecraft Java Beta 1.7.3 gameplay to Bedrock Edition.  C... |
| [Block Party](https://t.me/blockparty_pe) | `block-party.ru` | `19132` | en | Do you like variety?Then this server is for you.  We have the following mini games:  BedWars, BlockParty, SpeedBuilde... |
| [Blockpate](http://blockpate.de) | `play.blockpate.de` | `19132` | de | 🔥 BLOCKPATE.DE 🔥  🎮 Ein modernes Minecraft-Netzwerk mit eigenen Spielwelten, Systemen und jeder Menge Möglichkeiten! ... |
| [Blocktopia](http://linktr.ee/mineportal) | `jogar.blocktopiamp.com` | `19132` | pt-BR | Bem-vindo ao Blocktopia! Somos conhecidos por ser um servidor vanilla+ com plugins, itens exclusivos, lore envolvente... |
| [BlockyMC](http://store.blockymc.org) | `play.blockymc.org` | `19132` | en | BlockyMC delivers an exciting OneBlock SkyBlock experience! Progress through over 30 unique phases as you break block... |
| [Bloom Prisons](https://bloomprisons.buycraft.net/) | `bloomprisons.net` | `19132` | en | **Bloom Prisons** is a **Minecraft Bedrock Edition ONLY** prisons server. Bloom brings back the **classic prisons exp... |
| Blossomcraft | `play.blossomcraft.org` | `19132` | en | A mini restoration program in conjunction with building the brand allows you to reduce commissions or limitations. Th... |
| Bloxblast | `play.bloxblast.net` | `19132` | en | BloxBlast SMP Your Survival Adventure  Welcome to BloxBlast SMP, a Minecraft survival server where you can explore, b... |
| [Bloxr Survival](https://bloxr.co.uk/) | `join.bloxr.co.uk` | `19132` | en | BLOXR — FREE-TO-PLAY JAVA + BEDROCK SURVIVAL  Build a home worth coming back to. Find your spot, protect your land an... |
| [Bluegs](http://www.bluegs.xyz) | `play.bluegs.xyz` | `19132` | en | Enjoy a new experience in mcpe!, BlueGames takes inspiration entirely from HypixelPE and have created a perfect found... |
| [Blurkit](https://www.blurkit.net/) | `bedrock.blurkit.net` | `19132` | es | Blurkit es un Servidor de Minecraft que durante años nos hemos esforzado por brindar una buena experiencia a todos aq... |
| [Bluxmann](http://bluxmann.com) | `bluxmann.com` | `19132` | en | Shane and I are excited to share that we’ve set up a Bedrock Minecraft server just for our kids! This new server is a... |
| [Bobbacraft](https://www.bobbacraft.net) | `jogar.bobbacraft.net` | `19132` | pt-BR | O Bobbacraft é um servidor de Minecraft brasileiro focado em survival multiplayer (SMP), com estilo semi-vanilla e co... |
| [Bosscraft](http://www.bosscraft.net) | `bedrock.bosscraft.net` | `19132` | en | Add BOSSCRAFT2025 as a friend to join!  Bosscraft offers Prison, Skyblock and Survival (SMP) on Minecraft Version 1.2... |
| [BoxMC](https://store.boxmc.net) | `boxmc.net` | `19132` | en | BoxMC.net is the true BoxSMP Challenge experience, with exclusive and super fun powers for Java and Bedrock players. ... |
| [Boxrealm](https://store.boxrealm.net/) | `play.boxrealm.net` | `19132` | en | BoxRealm is the #1 BoxSMP Server welcoming all players on both Java and Bedrock. Join the rest of our incredible comm... |
| [BrasilCraftPE](http://www.brasilcraft.net) | `jogarbrasilcraft.com` | `19132` | pt-BR | 🔴▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔴 🌺 BrasilCraft 🌺 🔴▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔴  🌟 IP: jogarbrasilcraft.com  🌟 Versão do servidor: 1.8x - 26.2x... |
| [BreadixWorld](http://play.breadixpe.net) | `play.breadixpe.ru` | `19132` | ru | Welcome to BreadixWorld with a lot of minigames like  Arcade, Skywars,Survival Games, Bedwars, Duel, Survival, Murder... |
| [Breeze SMP](https://store.breezesmp.com) | `mps.breezesmp.com` | `19132` | en | [BEDROCK SUPPORT] Welcome to Breeze SMP! We are a BRAND NEW SERVER and offer a fun 1.21 Survival experience for all t... |
| [Britania](http://britania-mc.com) | `play.britania-mc.com` | `19132` | fr | Britania : Un serveur ou règne la joie de vivre! Rejoignez un serveur Freebuild où règne la bonne humeur ! Nous avons... |
| [Bumblecraft](http://Bumblecraft.net) | `play.bumblecraft.net` | `19132` | en | No description provided. |
| [Cake SMP](https://cakesmp.tebex.io/) | `cakesmp.com` | `19132` | en | Looking for a survival experience that's a piece of CAKE?!   CakeSMP is a community-driven SMP focused on chill vibes... |
| Caraillenoir | `caraillenoir.com` | `19132` | fr | No description provided. |
| [Catcraft Survival](https://catcraft.net) | `bedrock.catcraft.net` | `19132` | en | 🌟Welcome to CatCraft! Enjoy instant tree chopping🌳 & veinmining ores⛏️, engage in a player-driven diamond economy💎, a... |
| [Catlix Network](https://catlix.net) | `play.catlix.net` | `19132` | ro | No description provided. |
| [Celestia Kitmap](http://celestiamc.fr) | `play.celestiamc.fr` | `19132` | fr | Célestia KitMap V1 |
| [CerberuscraftMC](https://www.cerberusgamingnetwork.co.uk/?i=2) | `cerberusmc.my.pebble.host` | `19132` | en | Compatibility: ALL Versions, Java & Bedrock! See /discord for support.  **Player Cosmetics! Custom Timed Events and W... |
| [CeresMC Minigames](http://ceresmc.com.br) | `ceresmc.com.br` | `19132` | pt-BR | 🌟 CeresMC — Servidor Brasileiro de Minecraft Bedrock Edition 🌟  Seja bem-vindo ao CeresMC, um servidor feito para que... |
| [ChampionsMC](https://championsmc.us) | `play.championsmc.us` | `19132` | en | Welcome to the ChampionsMC Network!  The network revolves around Minecraft, and consists of many social media platfor... |
| CherryMC | `cherrymc.asia` | `19132` | vi | CherryMC.asia tự hào giới thiệu 3 cụm máy chủ SMP, Skyblock và RPG – nơi hội tụ những trải nghiệm Minecraft hấp dẫn n... |
| [ChillSMP](https://shop.chillsmp.org/) | `op.chillsmp.org` | `19132` | en | Welcome to ChillSMP. Our server has the friendliest community on Minecraft.  We're always innovating and pushing to i... |
| [ChocoHills](https://chocohills.com) | `play.chocohills.com` | `19132` | en | No description provided. |
| [Chronos SMP](https://caldronsmp.online) | `play.caldronsmp.online` | `19132` | id | No description provided. |
| [Civilization](https://wasteland7912.uk/apply/play?utm_source=minecraftpocket&utm_medium=listing&utm_campaign=free_20261019) | `minecraft.wasteland7912.uk` | `19132` | en | Join for free right now — no sign-up required! Civilization is a Hard Survival server for Minecraft Bedrock with an i... |
| Cl0cker | `cl0cker.jp` | `19132` | ja | A Simple PvP Practice Server. |
| [Clarity Network](https://store.clarity-id.net/) | `play.clarity-id.net` | `19132` | id | No description provided. |
| [ClarityMC Network](https://claritymc.net) | `play.claritymc.net` | `19132` | es | ⚔️ CLARITYMC NETWORK · Servidor de Minecraft Bedrock y Java en español (LATAM)  ¡Juega desde el CELULAR, consola o PC... |
| [Clary MC Factions](https://tienda-clarymc.tebex.io/) | `clarymc.xyz` | `19132` | es | ──────────═─━✧❀✧━─═──────────  # ClaryMc Factions  # ¿Qué ofrecemos?  > ➤ Soporte  > ➤ Alianzas  > ➤ Staffs no corrup... |
| [ClassicVanilla](https://classicvanilla.org) | `mc.classicvanilla.org` | `19132` | en | [Java/Bedrock] A Minecraft server with classic vanilla experience and the latest version!  • We respect the work of o... |
| [CloneArmyMC](http://clonearmymc.net) | `play.clonearmymc.net` | `19132` | en | Clone Army MC is a Star Wars Minecraft Bedrock Edition server where players can join the Clone Army and become a clon... |
| [Cloud SMP](https://store.cloudsmp.xyz) | `cloudsmp.xyz` | `19132` | id | Cloud SMP adalah sebuah server minecraft yang berdiri sejak 2021. Cloud SMP pertama kali di rilis oleh Chairawan Chan... |
| CloudMC Network | `pe.cloudsmp.asia` | `19132` | vi | Server Smp viet nam tuyet voi |
| [Cobblemon Bedrock](https://cobblemonbedrock.com) | `play.cobblemonbedrock.com` | `19132` | en | Cobblemon for Bedrock and Java players: catch, train and battle Pokémon together!  Note: This is not a Bedrock port. ... |
| [Collapse](https://collapsemc.com/) | `clps.gg` | `19132` | ru | Collapse Practice — Твое главное место для PvP в Minecraft Bedrock!  Ищешь сервер с отзывчивой регистрацией ударов, к... |
| [Complex Gaming](https://www.mc-complex.com/) | `mps.mc-complex.com` | `19132` | en | Complex Gaming is one of the best Minecraft Bedrock and MCPE servers, a friendly crossplay network where Bedrock (MCP... |
| [Cookie Build](https://www.cookie-build.com) | `pe.cookie-build.com` | `19132` | en | Cookie Build is a Minecraft Pocket Edition minigame server. There is only SkyWars, MicroBattles, Build Battle and Tur... |
| Cora | `cora.land` | `19132` | en | No description provided. |
| CosmicMC | `play.cosmicmc.lol` | `19132` | en | Servidor Factions |
| [CosmicPE](https://shop.cosmicpe.me) | `play.cosmicpe.me` | `19132` | en | CosmicPE is a space-age Minecraft: Bedrock Edition Factions server that has lived amongst the stars for the past 5-6 ... |
| [CosmicX](https://cosmicx.net) | `play.cosmicx.net` | `19132` | en | 🌟 Welcome to CosmicX🌟  CosmicX is the perfect server for builders who want complete freedom and no limits getting in ... |
| [CosmosMC](https://cosmosmc.org) | `gems.cosmosmc.org` | `19132` | en | Welcome to CosmosMC. Our server has the friendliest community on Minecraft. We're a Network that offers the best of t... |
| [Cowgl](https://cowgl.tech) | `cowgl.tech` | `19132` | zh | 歡迎來到牛牛的草原！我們是一個提供多款刺激有趣的Minecraft小遊戲伺服器，包括TNTRun、跑酷、SMP、捉迷藏、空島生存、床戰等。我們的伺服器致力於提供一個優質的遊戲環境和社群平台，讓玩家可以輕鬆交友、與其他玩家互動並一起探索... |
| CowsSMP | `cows.info.gf` | `19132` | en | 🐄 The Moo-st Vanilla Survival Server  Pure vanilla survival Minecraft — no mods, no plugins, no udder nonsense. Just ... |
| [Cozy Realms](https://store.cozyrealms.us/) | `play.cozyrealms.us` | `19132` | en | 🌟 A peaceful, relaxing, and chill place to play Minecraft! Cozy Realms is a family-friendly survival server where pla... |
| [CrabSMP](https://crabsmp.net/) | `play.crabsmp.net` | `19132` | en | CrabSMP is a Minecraft Bedrock server built for players who want proper combat, real events and none of the usual ser... |
| Craft | `craft.pe` | `19132` | en | No description provided. |
| [Craftadia Survival](https://www.cusl.net) | `mci.craftadia.com` | `19132` | en | Casino utan svensk licens erbjuder flera fördelar för spelare som letar efter alternativ utanför den svenska reglerin... |
| [Craftale](https://discord.gg/g934gXnd2E) | `oyna.zeusnw.tr` | `19132` | tr | 🚀 Zeus Network, Türkiyedeki tek ThePit sunucusudur, herkesi bekleriz! |
| [Craftale Network](https://craftalemc.com/) | `oyna.craftalemc.com` | `19132` | tr | No description provided. |
| [Craftavia](https://craftavia.net/) | `play.craftavia.net` | `19132` | tr | Craftavia: Türk Minecraft Sunucusu \| SMP, Towny, Skyblock, BoxPvP, Practice  Craftavia, Java ve Bedrock oyuncularını... |
| [CraftersMC](https://craftersmc.net) | `play.craftersmc.net` | `19132` | en | Explore an MMO SkyBlock server full of adventure. Start your journey now on Minecraft: Bedrock Edition!  ⛰ CraftersMC... |
| [Craftriva](http://www.tekelcraft.net) | `oyna.tekelcraft.net` | `19132` | tr | TekelCraft, kaliteli ve eğlenceli bir SkyBlock deneyimi sunmayı amaçlayan topluluk odaklı bir Minecraft sunucusudur. ... |
| [CraftyWorld](https://craftyworld.fr) | `play.craftyworld.fr` | `19132` | fr | Nous vous souhaitons la bienvenue sur CraftyWorld !  Depuis 2015, CraftyWorld a vécu en tant que serveur PvP-Factions... |
| [Crbe](http://Cristalix.PE) | `cristalix.pe` | `19132` | ru | No description provided. |
| [CreateCraft](https://www.createcraft.eu) | `pe.createcraft.eu` | `19132` | de | 🔥 CreateCraft.eu – Dein neues Minecraft Zuhause! 🔥  ❗ NEU: Battlepass jetzt LIVE auf Citybuild ❗  ⚡ Starte JETZT dein... |
| [Creeper's Lab](https://www.creeperslab.net/) | `play.creeperslab.net` | `19132` | en | You like Minecraft? Want to create awesome builds? Play with friendly people? Get involved in building contests? All ... |
| [Crispy Network](https://crispymc.net/) | `bedrock.crispymc.net` | `19132` | en | Crispy Network is an Indonesian Minecraft server that has been running since 2018. Designed to offer a unique experie... |
| [CrypticMC](https://crypticmc.org) | `bedrock.crypticmc.org` | `19132` | en | CrypticMC is a long-term Minecraft survival server with a world that never resets. No land claims, no rollbacks, and ... |
| [Crystalgemcraft](https://www.crystalgemcraft.com/) | `mc.crystalgemcraft.com` | `19132` | pt | 💎 CRYSTALGEMCRAFT - Máy Chủ Minecraft SMP/RPG Đầy Huyền Thoại! 💎  Bạn đã sẵn sàng bước vào một thế giới SMP nhiều thú... |
| [Cubaris](http://www.cubaris.net) | `cubaris.net` | `19132` | en | 🇩🇪 🌐 Willkommen auf Cubaris.net! 🌐  Trete noch heute dem Cubaris Netzwerk bei. Mit bereits hunderten registrierten Sp... |
| [Cubix-Transfer](https://discord.gg/hydramc) | `cubixstudio.eu` | `19132` | fr | Transfering platform, like BCMain  UseFull transfering platform, while adding "StudioCubix" as friends |
| [Cuborix Network](https://cuborix.com) | `mc.cuborix.com` | `19132` | es | 🚀 ¡Bienvenido a CUBORIX!  El servidor de Minecraft definitivo donde la diversión no tiene límites.  🎮 +20 MODALIDADES... |
| CuteLand | `play.cutelandmc.ir` | `19132` | en | 🎀 Welcome to CuteLand SMP! 🎀  Looking for a friendly Minecraft Bedrock SMP with fun features and an active community?... |
| [Cyan Realms](http://cyanrealms.com) | `play.cyanrealms.com` | `19132` | en | Embark on a journey through a vast, procedurally generated world where you can level up a wide array of skills and st... |
| [Daedric](https://daedric.gg) | `br.daedric.gg` | `19132` | en | Discover Daedric, a Minecraft: Java and Bedrock Survival server where your adventure begins.  Explore a world full of... |
| [DarkGames Network](http://darkgames.club) | `play.darkgames.club` | `19132` | es | ¡Tu próxima aventura comienza aquí! Explora nuestros modos, juega con amigos y construye tu historia.  🌳 Survival: cr... |
| [Dcfac](https://discord.gg/4ryeb2DTvA) | `dcfac.net` | `19132` | en | Server based around Minecraft (Bedrock Edition) Network such as OP Factions and other upcoming gamemode(s) with Compe... |
| [Deadland](https://www.deadland.org) | `mps.deadland.org` | `19132` | fr | No description provided. |
| Deadray | `deadray.org` | `19132` | en | Small community-based survival server running the same map since at least 2016.  Join us on Discord |
| Deadzonev2 | `play.deadzone.online` | `19132` | fr | ☣️ DEADZONE V2 ​☣️  Survivras-tu ?  ​Plonge dans un univers post-apocalyptique impitoyable sur Minecraft Bedrock.  ​🧟... |
| [Deathzone Network](https://foro.deathzone.net/) | `deathzone.net` | `19132` | es | 🌟 ¿BUSCANDO UN SERVIDOR QUE MEJORE TU CONEXIÓN Y FPS? DEATHZONE NETWORK 🌟  » Survival 1.19 [1.7x - 1.19x]  » Survival... |
| [Demo](https://worldpe.rf.gd) | `worldpe.ddns.net` | `19132` | en | A server on which you can fight, survive, feel nostalgic and much more! Come on in, it's always fun here! |
| [Democraft](https://democraft/fr) | `play.democraft.fr` | `19132` | fr | DEMOCRAFT - Mini Jeux Java & Bedrock !  Vous cherchez un serveur Minecraft amusant et convivial pour jouer avec vos a... |
| [DemonHCF Network](https://discord.gg/demonhcf) | `play.demonhcf.rip` | `19132` | en | Server HCF Minecraft bedrock. |
| [Diamondbyte](https://diamondbyte.org/servers/) | `server.diamondbyte.org` | `19132` | en | No description provided. |
| Dincraft | `mc.dincraft.no` | `19132` | tr | This is a Norwegian Minecraft server where we mostly speak Norwegian. We do welcome our international friends but kee... |
| [Divinity](https://divinitymc.org) | `divinitymc.org` | `19132` | en | Divinity |
| [DM Летний Вайп](https://doshik.trademc.org) | `play.doshik.ru` | `19132` | ru | Грифер сервер для MCPE |
| [DonutSMP](https://store.donutsmp.net/) | `donutsmp.net` | `19132` | en | DonutSMP is one of the largest and most popular Minecraft Bedrock servers, a crossplay network with Skyblock, Prison,... |
| [Dqanarquia](https://www.dqanarquia.com) | `dqanarquia.com` | `19132` | pt-BR | O DQAnarquia é um servidor de Minecraft anárquico brasileiro para Java e Bedrock, em atividade desde 2022.  A propost... |
| [Dragon Standart](http://pay.dragon-pe.com) | `mon.dragon-pe.com` | `19132` | en | This is a Bedrock edition-only server. We have thousands of mobile players. Join us in a LifeSteal SMP Dragon PE .  m... |
| [DragonEmpire](https://shop.dragon-empire.ru/) | `dragon-empire.ru` | `19132` | en | Welcome to the unique hottest friendly and epic project MCBE DragonEmpire DragonEmpire - Your Home!  🐉Ip: Dragon-empi... |
| DreamWorld | `dwpe.ddns.net` | `19132` | en | DreamWorld is a server that features the craziest ideas and mechanics you've only seen in newer versions of Minecraft... |
| [Drweabo Lounge](https://drweabo.web.id/) | `play.drweabo.web.id` | `19132` | id | DRWEABO LOUNGE - SURVIVAL ECONOMY!  Selamat datang di server minecraft DRWEABO LOUNGE, di mana server survival multip... |
| [Dungeons Fusion](https://dungeonvn.com) | `play.dungeonvn.com` | `19132` | en | ⚔️ DUNGEONS FUSION • SURVIVAL RPG VIỆT NAM ⚔️  The Dungeons. The Challenges. Greater Power. Endless Evolution!  Bạn c... |
| [Dupywars](https://forum.dupywars.xyz) | `dupywars.dedyn.io` | `19132` | en | **Follow the guides on the signs (You will see them once you join) to get started. **  Basic Commands:  - /dupe - Dup... |
| Dynv6 | `diwie.dynv6.net` | `19132` | de | No description provided. |
| Earena | `play.earena.cn` | `19132` | en | ElysianArena - Modern Proxy Architecture · Multi-Minigames · Smooth & Stable Experience  📋 Server Basic Information  ... |
| [Earthreborn](https://earthreborn.fr/) | `play.earthreborn.fr` | `19132` | fr | EarthReborn est un serveur Minecraft Bedrock Earth où chaque joueur peut créer sa nation, développer son économie, no... |
| [EarthVision](https://www.earthvision.eu) | `bedrock.earthvision.eu` | `19132` | en | EarthVision - Minecraft Earth Server (English)  EarthVision is an international server, based on a map of the earth (... |
| [EaseCation CH EC BUILD BATTLES EC](http://www.easecation.net) | `asia.easecation.net` | `19132` | en | ! NOTICE: We are the official partner of Minecraft Chinese Edition (Agent of NetEase).  Due to NetEase's regulations,... |
| [EcoCityCraft](https://www.ecocitycraft.com/economy/) | `mps.ecc.eco` | `19132` | en | BEDROCK PLAYERS: Join mps.ecc.eco on port 19132.  EcoCityCraft is a Minecraft economy community with history since 20... |
| [EienMC](https://eienmc.net) | `play.eienmc.net` | `19132` | tr | 𝗘𝗶𝗲𝗻𝗠𝗖 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗦𝗲𝗿𝘃𝗲𝗿  2017 yılında ilk temelleri atılan, günümüzde HUB sunucusu olarak hizmet veren Sky... |
| Eldenspire | `play.eldenspire.net` | `19132` | en | Eldenspire is a survival economy server based around unique jobs which help the entire community.  We are a new serve... |
| [Eldersea Network](https://eldersea.fun/) | `mc.eldersea.fun` | `19132` | id | Eldersea Network  The Next Generation Minecraft Server  Rasakan keseruan survival faction dengan rpg items, cosmetics... |
| [EldersMC Network](https://eldersmc.top/) | `mc.eldersmc.top` | `19132` | pt-BR | 🌲 Survival com uma experiência verdadeiramente única, criado para quem busca comunidade, evolução e identidade própri... |
| ElectroBlocks | `electroblocks.net` | `19132` | en | I've just started ElectroBlocks - a vanilla anarchy server on bedrock edition. I wanted to create a genuine bedrock e... |
| [Emirycraft](http://emirycraft.denince.biz/) | `emirycraft.keyubu.net` | `19132` | tr | 🟢 EmiryCraft Survival  Klasik Survival'ın sevilen yapısını koruyan, geliştirilmiş ve emek odaklı Türk Minecraft sunuc... |
| EnderArmySMP | `enderarmysmp.dedimc.io` | `19132` | en | Welcome to EnderArmySMP! Enjoy a Bedrock survival server packed with features: a custom GUI, warps, homes, TPA, PvP, ... |
| [Enderpearl](https://enderpearl.de) | `enderpearl.de` | `19132` | de | Enderpearl.de \| Deutscher Crossplay Server seit 2021  Auf Enderpearl.de spielen Bedrock und Java zusammen auf densel... |
| [Endionium](https://discord.gg/7Y6PTsNnaS) | `endionium.mcbe.fr` | `19132` | fr | No description provided. |
| [Endstone Server](http://tofusmp.carrd.co) | `tofusmp.my.id` | `19132` | en | Welcome to TofuSMP, a simple yet enjoyable Minecraft Survival Multiplayer server based in Indonesia. Our goal is to p... |
| Endzone | `aurorapvp.club` | `19132` | en | Aurora PvP is a Bedrock and Java Crossplay PvP Server |
| [Entra Ya](https://discord.com/invite/rmufJbWQC7) | `mc.superdou.net` | `19132` | es | \|\|\|\|\|\| JAVA EDITION y BEDROCK Edition, IP: mc.superdou.net \| Puerto para jugadores de bedrock: 19132. \|\|\|\|... |
| [EpikLava](https://www.epiklava.com) | `mcpe.epiklava.com` | `19132` | tr | No description provided. |
| [Erilanetwork](https://www.erilanetwork.com) | `oyna.erilanetwork.com` | `19132` | tr | 🎮 Erila Network Minecraft Bedrock Türkiye'nin en iyi sunucusu!  2024 yılında Minecraft Bedrock oyuncuları için kurula... |
| Errcity Fr | `serv.errcity.org` | `19132` | fr | Le serveur ErrCity te propose du multi-jeux dans un univers de ville.  Nous proposons du PvP, du parkour, du créatif ... |
| [ErrorSMP](https://discord.com/invite/errorsmp) | `errorsmp.xyz` | `19132` | en | ErrorSMP — Season 9 Diamond SMP  Semi-anarchy SMP with a tight, active community. Griefing allowed — no hacks, X-ray ... |
| [Esn SMP](https://esnoffical.com) | `play.esnoffical.com` | `19132` | en | ESN SMP is a survival SMP with an RPG twist, running on our own custom ESN plugin. Java and Bedrock players play toge... |
| [Etercube](https://etercube.fr) | `mc.etercube.fr` | `19132` | fr | EterCube est un serveur Minecraft Faction dont le but est d'unir les communautés Java et Bedrock sur un environnement... |
| [Evopixel](https://www.evopixel.id/) | `evopixel.id` | `19132` | en | EVO PIXEL  Join EVO PIXEL, an exciting Minecraft server where you can enjoy a variety of fun features and game modes ... |
| [EvoraNetwork](https://evoranetwork.xyz) | `play.evoranetwork.xyz` | `19132` | id | EvoraNetwork adalah server Minecraft Indonesia bertema Eco Crystal PvP yang menghadirkan pengalaman bermain survival ... |
| [Extalia](https://discord.gg/extaliafr) | `extalia.mcbe.fr` | `19132` | fr | # ✨ **__ Extalia - Kitmap ! __** ✨  ═══════════════════  > Extalia un KitMap pas comme les autres qui redéfinit Minec... |
| F8 Lobby World | `royale.f8studios.net` | `19132` | en | RoyaleMC KitPvP from F8 Network!  Fight other players in our rotating arenas!  Boss Fights, Sumo, and many other even... |
| [FadeCloud GENS RELEASE IN NOW](http://fadecloud.com/) | `mp.fadecloud.com` | `19132` | en | FadeCloud Network Gens \| Prison \| Dungeons \| Survival \| Tower Defence  Hosting the BEST grinding and tycoon custo... |
| [FadeMC](https://fademc.gg) | `fademc.gg` | `19132` | en | Welcome to FadeMC — a never-resetting survival world where your builds, loot, and legacy are permanent. We blend clas... |
| [Faderealms Network](https://www.minespice.net/) | `pe.minespice.net` | `19132` | en | MineSpice Network [1.13-1.21]  The Best Minecraft Network for JAVA and BEDROCK versions! Experience the best with ZER... |
| [Faith Avenue](http://faithavenue.org) | `faithavenue.host` | `19132` | en | Welcome to your new paradise!  FaithAvenue is Christian faith focused family friendly city themed network. Our server... |
| [FallenTech](http://shop.fallentech.tk) | `fallentech.tk` | `19132` | en | No description provided. |
| FamSMP | `famsmp.com` | `19132` | en | Welcome to FamSMP — the family-friendly Bedrock survival server!  We're a brand-new community server built around one... |
| [Fapixel](http://www.fapixel.com) | `mc.fapixel.cn` | `19132` | zh | FAPIXEL小游戏服务器（简称FAP，全名FunnyArenaPixel，曾用名FillAmeaPixel）创立于2018年，致力于让国内玩家玩到低延迟、环境友好、玩法丰富的小游戏服务器，我们拥有自主研发的高性能反作弊，独创玩法电子... |
| [FatalMC](https://store.fatalmc.org/) | `mc.fatalmc.org` | `19132` | en | FatalMC is a high quality Network. Our main focus is our Lifesteal mode, as well as our FFA Mode. We plan to add addi... |
| [Feplex АНАРХИЯ](https://bungee.host) | `fecraft.ru` | `19132` | ru | ▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧  ✏️ ЗАБИРАЙ СВОИ новогодние ПОДАРКИ от Домера и Пионера - /free  ✏️ ДЕНЬ СКИДОК НА ДОНАТ 90%!  ✏️... |
| [Fewer Network](https://store.fewer.live) | `bedrock.fewer.live` | `19132` | en | Welcome to the Fewer Network! We are an awesome Minecraft server that offers many different gamemodes, such as a Cust... |
| [Firestarter](https://firestartermc.com) | `mc.firestartermc.com` | `19132` | en | Firestarter is the simple yet exciting community Minecraft experience you’ve been looking for! Whether you just love ... |
| Firevanilla | `firevanilla.net` | `19132` | en | Box pvp |
| [Firewall MC](https://linktr.ee/firewallmc) | `fire.blazebr.com` | `19132` | pt-BR | 🔥 FirewallMC 🔥   ✨ Servidor Bedrock com economia, eventos e sistemas únicos ✨   🛡️ Comunidade ativa e diversão garant... |
| FirstMC | `firstmc.de` | `19132` | de | Willkommen auf FirstMC – Deinem neuen Minecraft-Zuhause!  FirstMC ist kein gewöhnlicher Minecraft-Server – hier geht ... |
| [FlexPlex](http://flexplex.fi) | `bedrock.flexplex.fi` | `19132` | en | No description provided. |
| FlyPVP | `flypvp.pl` | `19132` | pl | No description provided. |
| [FMine](https://top-minecrafter.com/en/) | `be.fmine.su` | `19132` | en | Top Minecrafter is your gateway to discovering the best Minecraft servers, carefully selected and verified by Alexand... |
| [Forgewell Factions](https://forgewellfactions.com/) | `play.forgewellfactions.com` | `19132` | en | FORGEWELL FACTIONS  A Minecraft Bedrock factions server where there's always something to fight for.  Tired of surviv... |
| [FossilSMP](https://fossilsmp.de/#/) | `pe.fossilsmp.de` | `19132` | de | FossilSMP – Survival trifft auf die Welt der Dinosaurier!  Willkommen auf FossilSMP, einem besonderen Minecraft-SMP, ... |
| [Foxy Network](https://discord.gg/JZRqhmyFnh) | `foxynetwork.eu` | `19132` | fr | Serveur UHC et mini jeux Minecraft Bedrock |
| [FreeAttack](https://freeattack.net) | `freeattack.net` | `19132` | en | FreeAttack – dein deutscher Minecraft Bedrock Server  FreeAttack is a German-language Bedrock network with multiple s... |
| [FreeLands](http://karakalov.ru) | `oga-pogrom.org` | `19132` | ru | Один из старейших серверов анархии открытый в 2016 году, который ранее был приватным проектом!  FurryBlock.ru  ------... |
| [Frontier](http://thefrontiermc.net) | `play.thefrontiermc.net` | `19132` | en | Build nations, forge alliances, wage war, and govern your own citizens. Rules are primarily enforced by players, mean... |
| [FrydeMC](https://fryde.org) | `mc.fryde.org` | `19132` | en | FrydeMC Network is a Minecraft server supporting versions 1.7 to the latest.  You can play Survival, OneBlock, and ta... |
| [FueguitoMc Network](https://fueguitomc.com/) | `mc.fueguitomc.com` | `19132` | es | 🔥 ¡Bienvenido a FueguitoMC! 🔥  La network de Minecraft donde la diversión nunca se apaga.  🌍 IP: fueguitomc.com  📌 Ve... |
| [Futonium](http://futonium.eu) | `play.futonium.eu` | `19132` | fr | FUTONIUM est un serveur Faction pour Minecraft Bedrock. Ouverture officielle le 21 octobre à 18 h.  Tu pars de zéro d... |
| FuziVel 1 Jogos 0 | `memorial.ddnsfree.com` | `19132` | pt-BR | Uma história que não pode acabar |
| GameLand | `gameland.mcbe.fr` | `19132` | fr | 🇫🇷 : Le mini-jeu de retour en France ! 🇫🇷  GameLand est un serveur de mini-jeux qui en propose plusieurs : le Hikabra... |
| GamePE | `gamepe.ru` | `19132` | ru | Server MCPE Survival worldwide free without a regular account can join 1.16+ to 1.21.2+ |
| [GearsMC Skyblock](http://www.gearsmc.org) | `oyna.gearsmc.org` | `19132` | tr | ɢᴇᴀʀꜱᴍᴄ ᴛᴜʀᴋɪʏᴇ – ᴇᴍᴇᴋ ꜱᴋʏʙʟᴏᴄᴋ  Dengeli ekonomi, adil rekabet ve kesintisiz macera!  🚀 Sunucu Hakkında  GearsMC; eme... |
| [Geonations](https://geonations.org) | `geonations.org` | `19132` | en | GeoNations is a nations SMP where the map is the politics.  Claim land, found a nation, and go to war over it. Every ... |
| Germanycraft | `germanycraft.de` | `19132` | de | Über GermanyCraft – Mehr als nur ein ServerGermanyCraft ist mehr als nur ein Server — es ist eine kleinere Community.... |
| [Gewie SMP](http://discord.gg/parrotpals) | `parrotpals.net` | `19132` | en | Welcome to ParrotPals, a community-driven Survival Minecraft server where you can build, explore, and team up with ot... |
| Ghostbedrockserver | `play.ghostbedrockserver.com` | `19132` | en | minecraft bedrock with addons and maybe plugins lol   sorry for banner it ai gen because im not good with art stuff a... |
| [GoFight Network](http://gofight.xyz) | `play.gofight.xyz` | `19132` | en | ⚔️ GoFight Network \| Minecraft Bedrock Minigames  Ready to jump into the action? Welcome to GoFight, a Minecraft Bed... |
| GoldCraft | `gocr.cc` | `19132` | en | Minecraft Bedrock Server  - Battle (FFA) \| (Midfight) \| (SumoArena} \| (Duels}... And more!  - MiniGames Spleef \| ... |
| GoldUHCS-UHC MEETUP | `golduhcs.sytes.net` | `19132` | en | Best server UHC and meetup events |
| [GolemSMP](https://golemsmp.net/) | `mc.golemsmp.net` | `19132` | en | IP:  Java  golemsmp.net  Bedrock  mc.golemsmp.net  Bedrock Port: 19132  Max Players: 300 (aiming to grow)  A custom s... |
| [Goodlucky](https://www.goodlucky.io?utm_source=minecraftpocket-servers&utm_medium=info&utm_campaign=mc_server_list) | `goodlucky.io` | `19132` | ko | GoodLucky Server |
| [GrieferGames](https://griefergames.de/) | `griefergames.net` | `19132` | de | Herzlich willkommen auf GrieferGames.net!  Bis zu 22 verschiedenen Citybuilds hast Du die Möglichkeit allein oder mit... |
| [Grow With Us](https://pixelgrew.com) | `play.pixelgrew.net` | `19132` | en | Ultimate SMP |
| [Halloween](https://wertzuigames.net) | `wertzuigames.net` | `19132` | en | Hello, Halloween! 🧛 🌧️ Explore our spooky map variants 🧟, find the 7 hidden pumpkins 🎃, grab some ghoulish cosmetics ... |
| [HanedanMC](http://www.hanedanmc.com) | `play.hanedanmc.com` | `19132` | tr | Tüm Platfromlardan Girebileceğiniz Minecraft Sunucumuz 4 yıldır aktif ve sıfırlanmama garantisi sunuyor.  Towny & Sky... |
| Hanzu Network | `hanzumc.com` | `19132` | en | HANZU MC - Vietnamese Minecraft network for Bedrock & Java  HANZU MC is a Vietnamese Minecraft network that welcomes ... |
| [HappyBedrock](https://happybedrock.org) | `play.happybedrock.org` | `19132` | en | HappyBedrock - a Bedrock minigame network  Join on play.happybedrock.org (port 19132) from any Bedrock device, Minecr... |
| Hashiras Craft | `hashiras.net` | `19132` | pt-BR | Servidor de Minecraft bedrock Semi anarquia |
| [Haven SMP](http://web.peacefulhaven.lol) | `play.peacefulhaven.lol` | `19132` | en | 🌿Haven SMP - A Calm Survival Experience  Looking for a peaceful Minecraft server where you can build, explore, and pl... |
| [Havoc Games](https://havoc.games/) | `pocket.havoc.games` | `19132` | en | 🔫GUNS IN MINECRAFT!!🔫 Fight off zombies and players alike in our fully custom gamemodes!  🧟THE MINING DEAD:  In this ... |
| [Haylazoyuncu](https://www.haylazoyuncu.com) | `play.haylazoyuncu.com` | `19132` | tr | Haylaz Oyuncu 1.16.5 - 23.1.2 sürümleriyle giriş yapılabilen hub sunucudur açılış yakın zamanda! |
| [HeartSMP](https://heartsmp.net/?utm_source=MinecraftPocket-Servers.com) | `lifestealsmp.serverpit.com` | `19132` | en | 🔗 IP: mps.heartsmp.net, Bedrock port: 19132 HIRING STAFF!  🎮 Version: 1.7 - Latest  Welcome to HeartSMP - The Ultimat... |
| HellFireSMP PE | `play.hfsmppe.com` | `19132` | en | Do you want to re-experience nostalgic Minecraft just like it was back in 2013?  Look no further — we’ve got you cove... |
| [HerGert](https://hergert.sbs) | `mc.hergert.sbs` | `19132` | pt-BR | O HerGert é um servidor de sobrevivência brasileiro, feito pra jogar com calma e construir sua cidade com a galera.  ... |
| [Heroxwar](https://www.heroxwar.com) | `play.heroxwar.com` | `19132` | en | ~~~~ ＨｅｒｏｘＷａｒ Network ~~~~   International Minecraft CROSS platform Server  Telegram: https://t.me/HeroxWar  Site: ht... |
| [Hesu](https://hesu.org/store) | `hesu.org` | `19132` | en | Hesu is the next-gen PvP Practice network.  We're available on Windows, iOS, Android, PlayStation, Xbox, Nintendo Swi... |
| [Heveen](https://www.heveen.fr) | `play.heveen.fr` | `19132` | fr | HEVEEN KITMAP  ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  Heveen fait son grand retour.  Apparu pour la première fois en 2022, Heveen KitMap re... |
| [Hexaris](https://store.hexaris.cc) | `hexaris.cc` | `19132` | en | 💚 Hexaris is a claims-based Survival SMP built for all players with just enough risk to keep things interesting. 💚  ⭐... |
| [HexedMC](https://www.hexedmc.net/) | `mps.hexedmc.net` | `19132` | en | Welcome to HexedMC!  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  HexedMC is a Minecraft network filled w... |
| HeXHub | `hexhub.net` | `19132` | de | HeXHub.net  HeXHub.net ist ein kleiner Server welchen ich privat nebenbei betreibe und weiter ausbaue. Der Server läu... |
| [Hill MC Server](https://hillsmp.com) | `play.hillsmp.com` | `19132` | en | Hill SMP Minecraft server 🌳 Survival & 💀 Lifesteal • 💰 Economy • ⚔ PvP & Events • 🛡 Friendly Staff • Build, trade, an... |
| [HimbeerCraftPE](https://play.himbeer.me) | `play.himbeer.me` | `19132` | en | A simple Server with creative-plots, built by lots of talented players.  This is the reloaded version of the old Himb... |
| [Histeria](https://histeria.fr) | `play.histeria.fr` | `19132` | fr | Serveur Minecraft PvP-Faction !   (English version below)   Chers joueurs,   Permettez-moi de te présenter Histeria !... |
| [Hive-o-ween](https://playhive.com/) | `hivebedrock.network` | `19132` | en | The Hive is a large Minecraft Bedrock Edition minigame network offering a wide variety of fast-paced multiplayer expe... |
| [Homeless Shelter](https://playsheltr.pages.dev) | `sheltr.duckdns.org` | `19132` | en | HALLOWEEN NIGHT V3: Saturday 31 October (Halloween), 4pm UK time.  A one-night server event, back for a third round w... |
| [HomeTown](https://hometownmc.com/) | `smp.hometownmc.com` | `19132` | en | We are a no grief semi-vanilla survival server with a focus on a strong community. Play minecraft the way it was made... |
| Hotspotkita MC | `mmc.hotspotkita96.my.id` | `19132` | id | No description provided. |
| [Huarizoland](https://huarizoland-tienda.tebex.io/) | `play.huarizoland.com` | `19132` | es | ⚡Servidor Factions, Economía, Minas con Pvp, Nether, End, Bosses, Crates y mucho más. |
| HUB NationsGlory | `bedrock.nationsglory.fr` | `19132` | fr | c'est un serveur mec, rien de plus |
| [HUB Server](https://vatonage.com/) | `mc.vatonage.com` | `19132` | en | The Vatonage Network is a modded Minecraft Bedrock server with multiple game modes to choose from, including Cobblemo... |
| [HuntMC](https://orbitmc.club) | `orbitmc.club` | `19132` | en | OrbitMC  OrbitMC is a Brazilian PvP and Practice server with Java and Bedrock crossplay. Fight in competitive duels a... |
| [Hydrahcf](https://dc.gg/hydrahcf) | `hydrahcf.net` | `19132` | es | SERVIDOR HCF  PARECIDO A SOLOLEGENDS ( EvilHCF)  INSPURADO en CorHCF  GANA DINERO REAL 💲💸  PROLEAGUE 🏆   en la prolea... |
| [HypeGO](http://shop.hypego.ru) | `hypego.ru` | `19132` | ru | No description provided. |
| [HyperionsMC](https://hyperionsmc.com) | `hyperionsmc.com` | `19132` | es | HYPERIONS MC — Survival con raids de verdad  JAVA + BEDROCK · Entra desde PC o móvil, con cuenta original o sin ella.... |
| [Hyping](https://playhyping.com) | `play.playhyping.net` | `19132` | fr | Hyping est une référence incontournable des serveurs Minecraft en 2025 grâce à son écoute active de sa communauté et ... |
| i Survival | `mysticraft.org` | `19132` | es | 🌌 Mysticraft \| Survival Único para Java y Bedrock  ¿Buscas un servidor donde realmente valga la pena empezar desde c... |
| [IAcraft](https://iacraft.net/) | `play.iacraft.net` | `19132` | es | ⚡ ¿Y si tu servidor tuviera una IA de verdad jugando contigo? ⚡  En IAcraft no hablas con menús: hablas con una IA VI... |
| [iAkunaMC](https://discord.iakunamc.com) | `iakunamc.com` | `19132` | en | ✨ iAkunaMC — YOUR NEW DESTINATION!  - Looking for a competitive, stable server with an active community?   - Discover... |
| [IditiSMP](https://store.iditismp.net/) | `play.iditismp.net` | `19132` | en | Welcome to IditiSMP, the ultimate Shop Survival experience built for action and progression! Battle it out in our hig... |
| Ign | `cpe.ign.gg` | `19132` | en | cpe.ign.gg Minecraft Bedrock Edition anarchy server  No rules \| Hacking allowed \| 350k+ unique players \| Join the ... |
| [ii BloodMine ii](https://bloodmine-pe.ru) | `bmpe.pw` | `19132` | ru | Вам достаточно просто посетить сервер, немного освоиться на нем и практически сразу вам что-то да и понравится. Средн... |
| ii GREENWIX ii | `play.greenwix.fun` | `19132` | en | No description provided. |
| ii MINELUX ii BETA | `minelux.eu` | `19132` | fr | - Minelux est un serveur PvP/Faction qui à ouvert ses portes en 2021 pour la Beta, qui nous prépare à une magnifique ... |
| [ImpendMC](https://store.impendmc.net) | `play.impendmc.net` | `19132` | en | We’re a Minecraft network where you can meet new people in the PvP community and just have fun. We’ve got Random Kit,... |
| [Imperiolatino](https://imperiolatino.tebex.store/) | `play.imperiolatino.online` | `19132` | es | ¡EL SERVIDOR DE MINECRAFT #1 DE TODA LATINOAMÉRICA! 🎮🔥  👑 IMPERIOLATINO 👑  Nuestro servidor está dedicado para toda l... |
| [ImperiumMC](https://imperiummc.net/) | `play.imperiummc.net` | `19132` | en | ImperiumMC - Rome-Themed OP Prison  Step into the Roman Empire and build your legacy. Mine your way through 100 ranks... |
| [Inacraft](http://www.inacraft.my.id) | `play.inacraft.my.id` | `19132` | id | INACRAFT  Minecraft Server Indonesia yang memiliki banyak gameplay seperti  - SKYBLOCK custom  - SURVIVAL  - RPG-DUNG... |
| [InertiaMC](https://inertiamc.net) | `mps.inertiamc.net` | `19132` | en | InertiaMC mixes classic LifeSteal combat with a custom generator economy. Every fight matters here because winning st... |
| [Infection Network](https://tienda.infection.fun/) | `infection.fun` | `19132` | es | Infection Network es un servidor donde siempre escuchamos a la comunidad y hacemos lo mejor para mejorar día a día, c... |
| [Infinite Games](http://shop.skyblockpe.com) | `play.skyblockpe.com` | `19132` | en | Welcome to SkyBlockPE  We are an amazing Skyblock server with awesome people like you! Join today and build your own ... |
| [InsanityCraft](https://www.insanitycraft.net/) | `mps.insanitycraft.net` | `19132` | en | [1.21] InsanityCraft is one of the oldest networks in the world with the most popular game modes! With over a decade ... |
| [InstaCraft Survival](https://www.myinstacraft.com/) | `mc.myinstacraft.com` | `19132` | en | 🌿 InstaCraft Survival — friendly, no-grief community since March 2020.  ⚙️ Java-style survival mechanics with Java + ... |
| [Invalid Server](http://www.capenw.org) | `bedrock.capenw.org` | `19132` | tr | Cape Network Türkiyenin Java - Bedrock Sunucusu!  Girişler: Java & Bedrock  Version: 1.16.5+ Java Sürümleri & Tüm Bed... |
| [Ioncraft Slimefun RPG](https://linktr.ee/ioncraft) | `play.ioncraft.my.id` | `19132` | id | Rekomendasi Versi Client Minecraft 1.21.*  𝗜𝗣 𝗝𝗔𝗩𝗔 & 𝗕𝗘𝗗𝗥𝗢𝗖𝗞 = play.ioncraft.my.id  BEDROCK PORT = 19132  𝗙𝗶𝘁𝘂𝗿 𝗙𝗶𝘁𝘂𝗿... |
| [JackpotMC](https://www.jackpotmc.com) | `bedrock.jackpotmc.com` | `19132` | en | JackpotMC is a server focused on PvP game modes, with our latest game mode being Lifesteal SMP. This is a one of kind... |
| [Jawanese](https://chat.whatsapp.com/BtkV2gBlO4CJJRyvT6evtQ?s=cl&p=a&mlu=4&amv=0) | `play.jawanese.xyz` | `19132` | id | Server minecraft bedrock bertemakan Ekonomi Anarkis dengan fitur simpel dan mudah cocok untuk pemula |
| [JD Bros](https://www.jdbros.de/startseite) | `play.jdbros.de` | `19132` | de | Wir bieten dir ein unverwechselbares Erlebnis auf unserem Citybuild Server exklusiv für die Bedrock Edition!  Mit eig... |
| [Join today](https://ecpe.network) | `play.ecpe.network` | `19132` | en | OP Factions  Team up with your friends to fight for /f top on our OP Factions gamemode! Whether you want to lead your... |
| [Jonarchy](https://www.jonarchy.com) | `jonarchy.com` | `19132` | en | Jonarchy. Try out now! 1.5.2 - 26.3 \|   We got blocked by Microsoft use our mod: https://github.com/1x09lol/Jonarchy... |
| [JonGames denMS](https://jongames.com/minecraft) | `bedrock.jongames.com` | `19132` | en | JonGames Minecraft 1.14.4 Server (1.9 - 1.18 clients supported)  Peaceful Guilds with land claiming and Economy game-... |
| Juko's Minecraftparadise | `mc.futro.dns64.de` | `19132` | de | ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  JUKO'S MINECRAFTPARADISE  Bedrock SMP · 10 Plätze  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  Ke... |
| [Kaario Network](https://www.kaario.net) | `oyna.kaario.net` | `19132` | tr | Sunucumuzda Bulabileceğiniz Oyun Modları:  • Survival  • BoxPvP  • Creative  • Bedwars  • Pratik & FFA  • Daireden So... |
| [Kaboom](https://kaboom.pw) | `play.kaboom.pw` | `19132` | en | Kaboom is a Minecraft multiplayer server that combines free OP with anarchy. Use powerful operator commands to push t... |
| [Kaizen Network](https://kaizenmc.id/) | `mps.kaizenmc.id` | `19132` | id | Kaizen Network adalah server Minecraft Indonesia yang menghadirkan pengalaman bermain terbaik untuk semua pemain.  De... |
| Kandang Alwi | `kalwi.id` | `19132` | id | Don't cheat |
| KASTW-幻月殤恆伺服器 | `ser.kastw.cc` | `19132` | zh | 這個嘛... 地圖雖然還在，但有些隨著更新有點...壞掉。  期待有緣人一同更新啦~ |
| KatipunanSMP | `play.katipunansmp.com` | `19132` | en | Katipunan SMP  Joining Information  Java: katipunansmp.ddns.net  Bedrock: katipunansmp.ddns.net  Port: 19132  Version... |
| [KawaiSMP](https://www.kawaismp.net) | `play.kawaismp.net` | `19132` | id | No description provided. |
| [Kblk MC](https://kblk.space) | `mc.kblk.space` | `19132` | ro | KBLK MC - server Minecraft de survival românesc, fără pay-to-win, pentru Java (1.20 – 26.3) și Bedrock (26.30 – 26.52... |
| [KingdomCraft-S13](https://kingdomcraft.co.nz) | `server.kingdomcraft.co.nz` | `19132` | en | Kingdomcraft SMP is a Kingdoms Server, we have created our own User Interface so server moderation with staff is not ... |
| KingSMP | `kingsmp.net` | `19132` | vi | Đây là máy chủ sinh tồn   Không toxic   Không scam |
| [Kita Network](http://www.kitasmp.com) | `play.kitasmp.com` | `19132` | en | Kita SMP — Survival Economy Bedrock Indonesia 🌊  A fun and active Indonesian Minecraft Bedrock server with economy, l... |
| Kitmap Olympia | `play.olympiamcbe.com` | `19132` | fr | No description provided. |
| [Kitsue](http://mc.kitsue.net) | `play.kitsue.net` | `19132` | vi | máy chủ minecraft java hỗ trợ bedrock |
| [KittiMC Server](https://www.facebook.com/kittimcminecraftszerver/) | `kittimc.serveminecraft.net` | `19132` | hu | ●➤ Non-Stop Fut (0/30)  ●●➤ Verzió: 1.13.0  ●●●➤ WHITELIST SZERVER!!!  ●●●●➤ Jelentkezni Discord csatornánkon lehet! ... |
| [Knight Network](https://knightnw.com) | `bedrock.knightnw.com` | `19132` | tr | ⚔️ KnightNW (Knight Network) — 2018'den beri açık Türk Minecraft sunucusu  KnightNW, Skyblock, Survival SMP ve Factio... |
| [KnightHC](http://www.knighthc.pl) | `knighthc.pl` | `19132` | pl | KnightHC.pl – Survival + Gildie na Minecraft Bedrock  KnightHC.pl to polski serwer Minecraft Bedrock Edition, który ł... |
| [KoalaServers](https://www.koalaservers.net) | `play.koalaservers.net` | `19132` | en | Our aim is for a close to vanilla taste, but with the added flavor of jobs, economy, player ran shops, and warps. We ... |
| [Kolosok Survival](http://roulette77.in/live-roulette) | `kolosok.xyz` | `19132` | en | I am searching for a low-latency Minecraft server that doesn't have an overwhelming amount of custom plugins. Most of... |
| [KretMC](https://www.kretmc.pl) | `play.kretmc.pl` | `19132` | pl | KretMC.pl - Najlepszy serwer Minecraft!  Minecraft Bedrock: play.kretmc.pl port: 19132  Wersja: 1.8-1.20  Ilosc sloto... |
| Kro | `bunnyf.kro.kr` | `19132` | ko | Minecraft MineFarm Server [BunnyFarm]  마인크래프트 마인팜 서버 바니팜입니다! |
| [Kuschlige Herbststimmung auf Blockstal](http://www.blockstal.de) | `blockstal.de` | `19132` | de | Blockstal ist eine kleine, gemütliche und familiäre Community. Wir gehen alle friedlich und freundlich miteinander um... |
| [Lamanitas Crew](http://www.laub.cl) | `play.laub.cl` | `19132` | es | 🌿 LAMANITAS — Survival tranquilo, casi vanilla  Un servidor para vivir y construir a tu ritmo, sin presión.  Aquí no ... |
| Landazia | `landazia.fr` | `19132` | fr | # _**LANDAZIA KITMAP OG**_  ------------------------------------  **Landazia** est un serveur Minecraft Bedrock innov... |
| [Lanf Countries Earth](http://minecraft.bald1nh0.net) | `minecraft.bald1nh0.net` | `19132` | en | Small family-friendly Bedrock server focused on building and exploring. Adventure/Creative style gameplay, relaxed an... |
| [Lava](http://Lvbe.ir) | `play.lvbe.ir` | `19132` | ar | به دنیای Lava Land خوش آمدید!  Lava Land یک سرور ماینکرفت بدراک با هدف ایجاد یک تجربه جذاب و متفاوت برای بازیکنان است... |
| [LEATplex](http://leatplex.net) | `mc.leatplex.net` | `19132` | en | POTSHOT: MAGIC AND MAYHEM UPDATE!  LEATplex is a Minecraft minigames server. We currently support Bedrock Edition 26.... |
| [Legax](http://site.legax.net) | `legax.net` | `19132` | pt-BR | Seja bem-vindo(a) à LEGAX Network, a rede brasileira de servidores de Minecraft Bedrock!  🇧🇷 PING BR: Nossos servidor... |
| Legendsmpr | `legendsmpr.exaroton.me` | `19132` | it | ⚔️ Un nuovo mondo, una nuova era!  Ciao a tutti ragazzi! 👋  Abbiamo aperto un nuovo server Minecraft Survival GDR isp... |
| [LegionMC](https://store.legionmc.uk/) | `play.legionmc.uk` | `19132` | en | Legion Network is a friendly and fun-loving community with Gamemodes for everyone to play! We support both Java and B... |
| [Lemon Network](http://store.lemoncraft.fun) | `play.lemoncraft.fun` | `19132` | en | 🌿 Survival SMP (Chill or Competitive — Your Choice)  Jump into our Survival SMP where you can play your way:  PvP wit... |
| [Lemon Slime](https://lemon-slime.com) | `play.lemon-slime.com` | `19132` | en | Crafter's Guild is a one-of-a-kind Minecraft: Bedrock Edition server founded on a simple, powerful idea: what if the ... |
| [LemonCloud](https://lemoncloud.org) | `mps.lemoncloud.net` | `19132` | en | Welcome to LemonCloud! Our awesome gamemodes:  Prison  Factions  Skyblock  Creative  KitPvP  Survival  Join now! @  I... |
| LemonSMP | `play.lemonsmp.org` | `19132` | en | LemonSMP is a feature-rich Survival SMP running on Minecraft 1.21.11 with Simple Voice Chat and with a fully custom e... |
| [Leone Network](http://shop.leonemc.net) | `bedrock.leonemc.net` | `19132` | en | IP: LeoneMC.net \| Java & Bedrock Compatible  Game Modes (8+ and counting):  - Lifesteal SMP – Steal hearts, dominate... |
| [Lets](https://discord.gg/8T6G8HgM8u) | `survival.lets.game` | `19132` | ro | No description provided. |
| [Liebe auf den ersten Block](https://InfinityCraft.de) | `infinitycraft.de` | `19132` | en | 🇩🇪 Deutsch 🇩🇪  InfinityCraft - Liebe auf den ersten Block  Herzlich willkommen auf InfinityCraft, deinem Citybuild-, ... |
| [Lifeblock](https://shop.lifeblock.network) | `lifeblock.network` | `19132` | en | Lifeblock Network   We are a Minecraft Bedrock Edition Network featuring our newly released gamemode Apocalypse and P... |
| [LifeMC](http://Store.LifeMC.net) | `lifemc.net` | `19132` | en | Welcome to LifeMC, a highly competitive, feature-rich Minecraft survival experience where every decision matters, eve... |
| [Lifesteal SMP](https://store.lifestealsmp.com) | `mps.lifestealsmp.com` | `19132` | en | We are a semi-vanilla Minecraft server with a unique feature where you can steal hearts from other players. PvP is al... |
| Lime Kitmap | `lime-mc.eu` | `19132` | fr | No description provided. |
| [Linesia](https://www.linesia.net/) | `play.linesia.net` | `19132` | fr | Linesia est un serveur Minecraft Mcpe/Bedrock axé sur le mode de jeu KitMap, une expérience divertissante riche en Pv... |
| [LivaMC Network](https://livamc.com/) | `bedrock.livamc.com` | `19132` | tr | LivaMC — Türk Minecraft Sunucusu: SMP, SkyBlock, Towny ve BoxPvP  📱 Bedrock IP: bedrock.livamc.com (port 19132) \| 🌐 ... |
| [Longplay](https://longplay.sk) | `longplay.sk` | `19132` | cs | Pripoj sa na náš Discord a všetko sa tam dozvieš...  ale RPG Survival, ranky, čarovne chestky a množstvo iných veci ť... |
| [Loot](https://loot.team) | `loot.team` | `19132` | en | Semi-vanilla Minecraft server with PvP and a minimal set of QoL features: /home, /tpa, /spawn and private messages. N... |
| LootMC | `lootmc.com` | `19132` | en | §3Noonmc |
| [Lordscraft](https://lordscraftofc.servegame.com/) | `lordscraftofc.servegame.com` | `19132` | pt-BR | Bem-vindo ao Lordscraft!  Aqui, a prioridade é oferecer uma experiência única, com foco em jogabilidade, estabilidade... |
| [Lunamoon SMP](http://discord.gg/lunamoonsmp) | `lunamoonsmp.com` | `19132` | en | ⋆.˚ LUNAMOON SMP 🌙 .⭒˚  JOIN LUNAMOON TO MAKE FRIENDS AND MORE!! |
| [Lunex SMP](http://lunexsmp.vercel.app) | `play.lunexsmp.my.id` | `19132` | id | Selamat datang di LUNEXSMP, sebuah server Minecraft Survival EcoPvP bertema DonutSMP tempat petualangan tanpa batas d... |
| [Lungo Blue](https://lungo.blue) | `lungo.blue` | `19132` | en | Lungo Café [Vanilla] [LGBTQ+] [26.2]  Server Name: Lungo Café  Server Address: lungo.blue  Version: Bedrock / Java 26... |
| [LydoxMC](http://lydoxmc.net) | `lydoxmc.net` | `19132` | en | Welcome to LydoxMC!   What is LydoxMC?   LydoxMC is a competitive Minecraft Bedrock minigames network.   Play excitin... |
| [Lyno Kitmap](http://lyno.tebex.io) | `play.lynokitmap.com` | `19132` | fr | **__LYNO KITMAP V2.5__**  ═════════════════════  **Lyno** fait son retour le **__VENDREDI 14 AOÛT À 18H30__** () avec... |
| [LysaMC](https://store.lysamc.net) | `play.lysamc.net` | `19132` | en | Welcome to LysaMC - A Minecraft Network for Everyone  Something for every player. Multiple game modes, active communi... |
| Làng Băng Vn | `pe.langbangvn.net` | `19132` | en | \|==== Server🚫 ====\|  1.0 ： Không đốt rừng ( vi phạm ban 7 ngày - vĩnh viễn )  1.1 ： Không sử dụng các loại phần mềm... |
| [MagmaMC](https://www.magmamc.net/) | `bedrock.magmamc.net` | `19132` | en | MagmaMC 💎 \| Java and Bedrock support - Survival Minecraft Server  IP: play.magmamc.net  Version: 26.1.2  Website: ht... |
| Make Waves | `play.eyserver.com` | `19132` | en | Welcome my dear player!  Hope you'll have fun in our new server!  -Ancient Piggy Official |
| [ManaCube Bedrock](https://manacube.com) | `bedrock.manacube.com` | `19132` | en | ManaCube is a flourishing minecraft community renowned for its wide variety of engaging Minecraft servers. Our unique... |
| [Mariscolandia](https://discord.gg/YsbAxH3c4) | `mc.mariscolandia.com` | `19132` | es | 🌌 Mariscolandia es un servidor de Minecraft con supervivencia, economía, rangos, eventos, misiones y una comunidad en... |
| [MasterCraft RankUP OP](https://redemaster.net/) | `pe.redemaster.net` | `19132` | es | MasterCraft foi fundado em 2016 por Jheyson Henrique por puro Hobby e hoje somos juntamente com nossos jogadores um d... |
| [Mc4fun](http://www.mc4fun.net) | `bedrock.mc4fun.net` | `19132` | tr | MC4FUN - Türkiye'nin En İyi Minecraft Sunucusu \| Turkey's Best Minecraft Server  IP: mc.mc4fun.net  Website: https:/... |
| [MCBE](https://meow.nfs.tw/) | `meow.mcbe.tw` | `19132` | ja | [NFS.TW]喵喵經典生存伺服器 - 致力於台灣MCBE  ==========【伺服器資訊】=========  《伺服器官網：http://meow.nfs.tw》  -伺服器相關資訊，贊助皆在此-  《服主》夜喵   - Fa... |
| [McbePVP](https://mcbepvp.club) | `mcbepvp.club` | `19132` | en | No description provided. |
| [MCC Network](https://discord.gg/dB2ZJVp) | `mccnetwork.uk` | `19132` | en | Welcome to MCC Network   We are a friendly, feature-rich Minecraft Bedrock server network established in 2016 offerin... |
| [Mcfallout](http://mcfallout.net) | `bedrock.mcfallout.net` | `19132` | zh | 廢土伺服器是目前台港澳最大的生存伺服器，共有超過20萬玩家加入，尖峰時段線上人數超過1500人、每個月有10,000名玩家保持活躍的伺服器。 #minecraft  享受Minecraft，工廠、農場、紅石、水流，盡量發揮你的創意。 ... |
| [MCHub](https://mchub.com) | `mps.mchub.com` | `19132` | en | Welcome to McHub - Your Ultimate Minecraft Adventure!  Dive into a world of endless possibilities on McHub, where thr... |
| Mcsh | `macemc.mcsh.gg` | `19132` | en | A mace smp inspired server for mcpe players only for better experience  Duping/X ray is allowed but using pvp cheats ... |
| [Mcsm](https://mcsm.cc) | `mcsm.cc` | `19132` | zh | No description provided. |
| [MCZone](http://mc-zone.org) | `mc-zone.org` | `19132` | en | Your world. Your adventures! 🚀  Welcome to MCZone—a Minecraft Bedrock server featuring survival, anarchy, and SkyWars... |
| [MeadowSMP](https://store.meadowsmp.com/) | `play.meadowsmp.com` | `19132` | en | 🌷 Welcome to Meadow SMP  Meadow SMP is a friendly, cross-platform Minecraft server for players who love survival, bui... |
| MementoMC | `play.mementomc.com` | `19132` | en | MementoMC is a Hardcore server where if you die, you're banned forever. This is your one life. No resets, no respawns... |
| [Meow](https://www.mineverso.com/) | `mc.mineverso.com` | `19132` | es | Servidor actualizado y optimizado por profesionales para que puedas disfrutar de una buena experiencia sin latencia (... |
| [MigosMc](https://migosmc.net) | `mc.migosmc.net` | `19132` | ru | Начните играть в MigosMc прямо сейчас!  Голосование награда /бонус набор |
| [Mine-Forge](http://www.mine-forge.net) | `minecraft.mine-forge.net` | `19132` | en | A series of Servers, offering Survival Multiplayer worlds. Cooperative, SMP. Active Community, and lots of support |
| Minearg!!! Network | `b.minearg.net` | `19132` | es | ¡Disfruta del mejor servidor survival custom! Con muchísimo contenido, actualizaciones y soporte activo las 24hs!   ➠... |
| [Minecity](https://minecity.at/) | `mc.minecity.at` | `19132` | de | WILLKOMMEN IN MINECITY  Eine Stadt. Ein Server. Deine Geschichte.  MineCity verbindet modernes CityBuild mit eigenen ... |
| [Minecraft](https://minecraft.si/) | `play.minecraft.si` | `19132` | en | Slovenski Minecraft Network  Sedaj tudi na mobilnih napravah. |
| Minecraft BD | `pe.minecraftbd.org` | `19132` | en | ⭐ Welcome to MinecraftBD! 🇧🇩  Join the Bangladeshi Minecraft community and experience a friendly survival adventure w... |
| [Minecraft EvoPixel](https://minecraft.evopixel.ro) | `mc.evopixel.ro` | `19132` | en | Minecraft EvoPixel is a high-performance Minecraft server designed for a seamless and immersive gaming experience. Wi... |
| [Minehut](https://sites.google.com/view/drevil) | `bedrock.minehut.com` | `19132` | en | mine until you can't no more on mcpe.  Guide To Join  Join Server IP:bedrock.minehut.com Port:19132 once you join the... |
| Mineidhost | `palley.mineidhost.com` | `19132` | id | AZURE CRAFT!  Selamat datang di Azure Survival, server Minecraft bertema Fantasy RPG Survival dengan sistem ekonomi d... |
| [Minekube](http://gymben.eu.cc) | `play.gymben.eu.cc` | `19132` | de | ???? GymbenMC \| Kleiner Citybuild mit RIESEN-Community-Feeling \| Jetzt Clan gründen & Teil der Familie werden!  ???... |
| [MineOre](http://mineore.org) | `mineore.org` | `19132` | en | Your new Minecraft BE adventure begins here! 😎 Build, explore the world, and grow alongside your friends on our survi... |
| [Mineplex Games](https://www.mineplex.com/) | `play.mineplex.com` | `19132` | en | THE RETURN OF MINEPLEX   Hello everyone!  A few years ago, Mineplex shut down with a promise that it would return. To... |
| [Minesive](http://store.minesive.com) | `be.minesive.com` | `19132` | id | Minesive New Era |
| [MineSpazio](https://tienda.minespazio.com/) | `db.minespazio.com` | `19132` | en | No description provided. |
| [MineSuperior TOWNY SKYBLOCK SURVIVAL](https://store.minesuperior.net/) | `br.mcs.gg` | `19132` | en | Discover MineSuperior – your ultimate 1.21 Minecraft: Java Edition destination, meticulously curated by a seasoned ma... |
| [Minezinho](https://minezinho.com/) | `jogar.minezinho.com` | `19132` | pt-BR | Seja parte do maior e mais acolhedor servidor de Minecraft da comunidade brasileira! No Minezinho, oferecemos uma exp... |
| MioMC | `miomc.top` | `19132` | zh | No description provided. |
| [ModsCraft](https://craft.pe/) | `play.modscraft.net` | `19132` | ru | :: ModsCraft :: 1.1-1.20 . |
| MomentumMC | `cp.momentummc.ca` | `19132` | en | MomentumMC  Survival /SMP Server  Java/Bedrock Supported  Usually Current Version!  Featuring an amazing community bu... |
| Monsters Anarchy | `monstersanarchy.verixen.net` | `19132` | en | -Monsters Anarchy- (BEDROCK)  -18,800+ Days Played  -The server has no resets! The world is over two years old (start... |
| [Motaz](https://discord.gg/motaz) | `motazmc.fr` | `19132` | fr | 🏰 - Voici **Motaz KitMap**  > 🔥 - Des **interfaces uniques** aux serveur  > ⚒️ - Un serveur **entièrement fait à la m... |
| [MRGNetwork](http://store.playmrg.net) | `playmrg.net` | `19132` | en | Welcome to MystrickGames, a premium Minecraft Bedrock Edition minigame network! We are dedicated to bringing you the ... |
| Multiserver | `multiserver.webhop.me` | `19132` | en | Welcome to Ultragys's Multiserver! You can chill at this server, hang out with others, mine, roleplay, and do some Pv... |
| [MY Global Creative Network](https://www.mychunk.org) | `mychunk.org` | `19132` | ko | 🚀 MyChunk.org : Global Minecraft Creative Server  Experience the ultimate freedom of a server where your imagination ... |
| Myno | `myno.mclobby.fr` | `19132` | fr | ** # Myno Network **   *Myno est un Network créé en 2026, avec pour but de révolutionner MCBE avec plusieurs mode de ... |
| [MysticMeadow Network](http://mysticmeadow.eu) | `malls-sandwich.tun.ply.gg` | `19132` | en | # 🌿 MysticMeadow \| Your Next Survival Adventure! ✨  **🌍 Explore. Build. Survive. Thrive.**  Welcome to **MysticMeado... |
| [Mythblock](https://mythblock.me) | `mythblock.me` | `19132` | en | MythBlock  A OneBlock server that goes far beyond one block  Java: mythblock.me \| Bedrock: mythblock.me, Port 19132 ... |
| Nasty God | `nasty-god.duckdns.org` | `19132` | en | Smp.pvp.rpg |
| NationMC Earth | `nationmc.net` | `19132` | en | NationMC is a next-generation Earth SMP running on a custom 1:500 Earth world, where you and your friends can build r... |
| NauticMC Bedrock | `bedrock.nauticmc.net` | `19132` | en | Server for Minecraft 1.19.80 Active HCF |
| Navalia | `navaliamc.fr` | `19132` | fr | Un très bon serveur KitMines (mélange de KitMap et KitMines) |
| [Neolya PvP Faction](https://neolya.ddns.net) | `neolya.ddns.net` | `19132` | fr | Neolya est un serveur PvP Faction dont le but est de dominer le serveur! |
| NeonCraft SMP | `play.neoncraft.org` | `19132` | en | Hi! Take a moment to read what our server is about ;   ► SMP with landclaim and economy  ► Playable on Java AND Bedro... |
| [Nethergames](https://nethergames.org) | `play.nethergames.org` | `19132` | en | Welcome to the NetherGames Network!  We're a friendly community-based Minecraft Bedrock Edition server network (and a... |
| [Netherite](http://netherite.gg) | `mps.netherite.gg` | `19132` | en | Netherite is an innovative, qualitative, and unique Minecraft Network focused on the game modes SMP, Lifesteal, and S... |
| [NetherixMC](https://netherixmc.net) | `oyna.netherixmc.net` | `19132` | tr | 🔥 NETHERIXMC – FACTION Dünyasına Hoş Geldin! 🔥  Olağanüstü bir Faction deneyimi seni bekliyor! Strateji, takım savaşı... |
| [New Game Blasterwars](http://Galaxite.net) | `play.galaxite.net` | `19132` | en | Galaxite is a featured Bedrock Edition Minecraft Server, made by Blockception.  Players can choose 6 game modes to pl... |
| [Newwind](https://newwindserver.com) | `craft.newwindserver.com` | `19132` | en | Minecraft survival with clans, dungeons, quests, PVP, events, and hundreds of custom items, all while preserving the ... |
| NexusPE OP Factions | `play.nexuspe.net` | `19132` | en | No description provided. |
| [Nitrogen Survival](https://linktr.ee/nitro.net) | `play.nitrogen.zone` | `19132` | en | Welcome to Nitrogen. Our server has the most loyal community in Minecraft. We're a Network that offers Skyblock, Surv... |
| [NixxoSMP](https://www.nixxosmp.lat/?s=lst-mcpocket) | `nixxosmp.lat` | `19132` | es | ⚔️ NIXXOSMP — Survival PvP estilo DonutSMP en español  Economía entre jugadores, PvP de verdad y duelos al instante. ... |
| No Gods Only Blocks | `ngob.org` | `19132` | de | ❌NO RULES – Grief, raid, hack, PvP – anything goes  ❌ NO RESETS – This world stays forever  ❌ NO PAY-TO-WIN – No rank... |
| [No Totem Hardcore](https://www.nototem.net/) | `nototem.net` | `19132` | en | [h5][size=36px]IP: [color=#3598db]nototem.net[/color][/size]  [size=36px]Discord: discord.gg/jhG2E6yAW[/size]  [size=... |
| [Noblerealms](https://store.noblerealms.com) | `play.noblerealms.com` | `19132` | en | Java IP: play.noblerealms.com  Bedrock IP: play.noblerealms.com Port: 19132  Discord: discord.gg/noblerealms  Join th... |
| Nodowa | `mi.nodowa.lat` | `19132` | en | Un servidor vanilla bedrock |
| [Noesantara Network](https://store.noesantara.id/) | `noesantara.id` | `19132` | id | Noesantara Network — Di Mana Mimpi Menjadi Nyata  Server Noesantara Network Yang Dahulu Dikenal Dengan Nama Aetherium... |
| NORD FJELL One world. One history | `mc.nord-fjell.com` | `19132` | en | Breathing the gentle warm breeze sweeping across ancient Burkina Faso, taking time to enjoy top-tier gaming on my han... |
| [NordikMC](http://nordikmc.com) | `play.nordikmc.com` | `19132` | en | YOU GET PAID FROM THE SECOND YOU LOG IN  No sign-up. No menu. No class to pick.  Mine a block, get paid. Chop a tree,... |
| [NoteLand](https://noteland.de) | `play.noteland.de` | `19132` | de | NoteLand.de  Minecraft Bedrock Edition Netzwerk  Dein Land für dich und deine Freunde!   Was bieten wir?  Wir betreib... |
| [NovaPrime](https://npbe.net) | `play.npbe.net` | `19132` | en | No description provided. |
| [NuansaCraft Survival Economy](https://nuansacraft.com) | `play.nuansacraft.com` | `19132` | en | NuansaCraft is a survival multiplayer server made for Indonesian players who want more than just another vanilla worl... |
| [NullMC](https://nullmc.net) | `play.nullmc.net` | `19132` | en | NullMC Network  A competitive Minecraft network built for players who enjoy survival, strategy, and large-scale PvP. ... |
| [Nusantarabatu](https://linktr.ee/nusantarabatu) | `nusantarabatu.id` | `19132` | id | NusantaraBatu \| 1.20 - Latest  Survival -New Gamemode Coming soon  Ip Java : nusantarabatu.id  IP Bedrock : nusantar... |
| [Nutellaserv](https://www.nutellaserv.fr) | `play.nutellaserv.fr` | `19132` | fr | NutellaServ.fr ❀ Mini-Jeux  Nous sommes un serveur Mini-Jeux reprenant l'interface de la version Java, avec des fonct... |
| Néphelia | `nephelia.fr` | `19132` | fr | Néphelia est un serveur Minecraft Bedrock français : KitMap, faction, skyblock et PvP, avec des îles de faction à déf... |
| [OasysPE](https://oasys-pe.com) | `oasys-pe.com` | `19132` | en | Bester Play2Earn-Server für Minecraft: Bedrock Edition. Jetzt beitreten!  Server mit einem Klick hinzufügen -> https:... |
| [ObiSky](https://discord.gg/VtA2sRrQ9f) | `play.obisky.com` | `19132` | en | Welcome to ObiSky!  ObiSky is an upcoming community-based Minecraft: Bedrock Edition server! Our goal is to create a ... |
| [OG Network](https://og-network.net) | `og-network.net` | `19132` | en | The OG Network is a minecraft server dedicated to reviving the old style minecraft experience. We are not pay2win, an... |
| [Og SMP](https://www.og-network.net/) | `og-smp.net` | `19132` | en | This server aims to bring back the old style of Minecraft without Pay2Win garbage.  You can expect a vanilla experien... |
| Ogfactions | `play.ogfactions.ro` | `19132` | ro | ⚔️ OG FACTIONS \| Construiește. Distruge. Domină. ⚔️  Bun venit pe OG Factions, locul unde readucem la viață adevărat... |
| [OHO Network](http://www.ohoth.com) | `play.ohoth.com` | `19132` | th | OHOTH is a Thai-themed Survival SMP that you can play on both Java and Bedrock (PC, mobile and console) with the same... |
| [Old's Cool FreeBuild & Survival](http://pldm.ml) | `pldm.ml` | `19132` | pl | No description provided. |
| OmegaServ | `omegaserv.fr` | `19132` | fr | 🌌 L'ÉVEIL D'OMEGASERV : LA PHASE DE TEST EST LÀ ! 🌌  L'attente touche à sa fin. Prévu initialement en 2020, forgé dan... |
| [Oneblocky](https://store.oneblocky.com) | `mine.oneblocky.com` | `19132` | en | Oneblocky is the ultimate Oneblock SkyBlock adventure! 🌍 Break your way through 30+ phases and build the island of yo... |
| [OPBlocks](https://opblocks.com) | `bedrock.opblocks.com` | `19132` | en | OPBlocks is a high-quality Minecraft Prison, Survival SMP, and Skyblock server featuring unique content and an amazin... |
| [Opsucht](https://www.opsucht.net) | `opsucht.net` | `19132` | de | Herzlich willkommen auf der Vote-Seite von OPSUCHT.NET!  OPSUCHT.NET ist am 23.10.2025 sieben Jahre alt geworden.  Du... |
| [OraclePVP](https://store.oraclepvp.net/) | `oraclepvp.net` | `19132` | en | Play the on the #1 ONECHUNK MINECRAFT SERVER, which offers chunk teams, chunk upgrades, weekly competion and 7 PVE lo... |
| [OrderSMP](https://www.ordersmp.net/) | `ordersmp.net` | `19132` | en | Welcome, citizen. OrderSMP is a free survival server run by the Order: a calm, slightly too organized administration ... |
| [OreoMC](https://store.oreo.gg/) | `play.oreo.gg` | `19132` | en | OreoMC is a Java and Bedrock Survival + Lifesteal SMP! Designed from the ground up with custom content in mind. If yo... |
| Orien | `orienmc.xyz` | `19132` | en | ⚔️ OrienMC is a Minecraft Bedrock server built for PvP! Battle in SkyWars, The Bridge, Duels, and FFA, join events, a... |
| [Origins Rebirth](https://originsrebirth.com) | `play.originsreborn.org` | `19132` | en | Embark on an extraordinary Minecraft journey with Origins Rebirth (Formally Origins Reborn), where the immersive Orig... |
| [OverBlast Network](http://overblast.eu) | `play.overblast.eu` | `19132` | fr | Découvrez un serveur Minecraft unique, spécialisé dans le OneBlock et le SkyBlock, pensé pour offrir une expérience c... |
| [Overy Network](https://overymc.fr/) | `play.overymc.fr` | `19132` | fr | Certains serveurs passent. D'autres marquent toute une génération.  Overy, c'est bien plus qu'un simple serveur Minec... |
| [OxinTowny](http://map.hbmc.net) | `oxin.hbmc.net` | `19132` | tr | 🇹🇷 OXINTOWNY \| BEDROCK TOWNY   Kendi kasabanı kur, topraklarını genişlet, ekonomini geliştir ve diğer oyuncularla bi... |
| [PaffMC](https://paffmc.net) | `play.paffmc.net` | `19132` | en | French Bedrock PvP server: ranked duels with Elo, FFA, KOTH, loot zones and world bosses. Free, no pay-to-win. Join: ... |
| [Paladium](https://paladium-pvp.fr/) | `play.paladium-bedrock.fr` | `19132` | fr | No description provided. |
| [Pantrysrealm](https://wiki.pantrysrealm.net) | `pantrysrealm.net` | `19132` | en | pantry's realm is a semi-vanilla Minecraft Bedrock survival server with achievements on, Hard mode, and a true foreve... |
| [Parucraft](https://parucraft.net/) | `play.parucraft.net` | `19132` | en | Step into a cozy community driven world where you can kick back, create, and truly feel at home. KeepInventory is on,... |
| [pAttack On Titan](http://AttackMC.ir) | `play.attackmc.ir` | `19132` | en | Minecraft server with Skymine Attack on Titan and Survival game modes |
| [PELAR Bedrockis](http://pelar.ee) | `mc.pelar.ee` | `19132` | en | Pelar on kõige vanem tegutsev Minecrafti server Eestis!   Meid tuntakse kogenud meeskonna, mõnusa mängijaskonna ja hu... |
| [pGrieferKing](https://www.grieferking.de/) | `play.grieferking.de` | `19132` | de | ✨ Features im Überblick:  Crossplay-Unterstützung: Spiele gemeinsam mit deinen Freunden, egal ob sie auf Java oder Be... |
| [Pigraid](http://pigraid.gg) | `pigraid.gg` | `19132` | en | One of the original Minecraft Bedrock Edition servers, we offer a rich KitPvP experience which is not Pay2Win, you ca... |
| [Pillars](http://Newcitymc.site) | `play.newcitymc.site` | `19132` | en | No description provided. |
| [PinnaMC PRISON SAISON 1](https://pinnamc.com) | `play.pinnamc.com` | `19132` | en | PinnaMC is a Prison OP server you can play in your own language: English, Français, Español, Deutsch, Português, Ital... |
| [Planet Beacon](https://planetbeacon.minesite.org/) | `planetbeacon.ddns.net` | `19132` | en | This is a new and improved [26.3] Planet Beacon server as a new legacy! This server has SKYBLOCK, CREATIVE PLOTS, SUR... |
| [Plasmodia](http://plasmodia.org) | `play.plasmodia.org` | `19132` | en | Chill SMP \| Land Claiming \| Jobs \| No Resets \| Optional PvP  We are a community-focused Minecraft server built fo... |
| [Playblocks](https://store.playblocks.net) | `pe.playblocks.net` | `19132` | en | Playblocks  Here is a list of features for everyone to look forward to:  ■ POWER SMP REALM: BECOME A SUPER HERO! Choo... |
| PlayNova RenasBey ve Pikachu ü bıraktı | `playnova.best` | `19132` | en | This server is a very nice and carefully prepared global server with language support. |
| Ploto | `play.ploto.fr` | `19132` | fr | Le meilleur kitmap français inspiré du serveur Paladium pour son Clicker et de Plutonium pour sa Boule de Neige infin... |
| [Plutonium](https://www.plutonium.best/) | `mcpe.plutonium.best` | `19132` | fr | Plutonium : L'Expérience PvP Faction incontournable   Plutonium s'est imposé comme une référence historique parmi les... |
| [PocketMobs](https://store.pocketmobs.com) | `play.pocketmobs.com` | `19132` | en | PocketMobs is a Pokémon server for Minecraft Bedrock, on phone, Xbox, PlayStation, Switch and PC.  Season 1 is live: ... |
| [PokeBedrock](http://pokebedrock.com) | `play.pokebedrock.com` | `19132` | en | In the first time ever, anyone can play Pokemon on Minecraft Bedrock. Our servers are running at highest speed so you... |
| [PokéFind](https://www.pokefind.co/) | `play.pokefind.co` | `19132` | en | Join thousands of Trainers on our New Server, PokeFind! PokeFind is a combination of Pokemon Games and some Pokemon G... |
| [Pokémania](https://pokemania.cc/) | `pokemania.cc` | `19132` | fr | POKÉMANIA SAISON 1 — L’AVENTURE COMMENCE !  Tu rêves de devenir le meilleur dresseur Pokemon ?  Alors prépare-toi à d... |
| Polis | `hitlermc.com` | `19132` | en | 100% Vanilla MCBE server, no grif no stealing  discord.gg/6ZMJ6zXsKw |
| [PortalWix](https://portalwix.com/) | `portalwix.com` | `19132` | en | No description provided. |
| [Practice](https://discord.gg/D6SAb3jcSE) | `practice.mcpe.fr` | `19132` | fr | Volcasia Practice est un serveur Minecraft Bedrock dédié au PvP compétitif et à l’entraînement. Affrontez d’autres jo... |
| PreyxStudios | `play.preyxstudios.net` | `19132` | de | PreyxStudios – dein deutsches Netzwerk für Java und Bedrock  Ob Handy, Konsole, Windows oder Java: Bei uns spielen al... |
| [Projects](https://projects.gg) | `play.projects.gg` | `19132` | tr | 🗺️ 1.16.5-26.2 Survival & Skyblock & Hunger Games (26.2 Tabanlı)  🔹 IP: mc.projects.gg / Site: https://projects.gg/  ... |
| [Provanas](https://www.provanas.com) | `mobil.provanas.com` | `19132` | tr | Survival Vadi \| SkyBlock Aincrad \| BoxPvp \| SMP  Serüvenimize 2014 yılında survival ile başlamış olmaktan gurur du... |
| [Prownetwork](https://prownetwork.net/) | `be.prownetwork.net` | `19132` | id | ProwNetwork adalah server Minecraft Indonesia yang berdiri sejak tahun 2020. Selama bertahun-tahun, ProwNetwork telah... |
| [Pumkincraft](https://pumkincraft.com/) | `oyna.pumkincraft.com` | `19132` | tr | Sizlere müjdeli bir haberimiz var! Yepyeni bir Towny sunucu açıyoruz ve bu epik macerada sizinle birlikte olmak için ... |
| PvPCraft MG | `play.pvpcraft.ru` | `19132` | en | Pvp |
| [PvpSMP](https://www.pvpsmp.com) | `mcps.pvpsmp.net` | `19132` | en | PVPSMP is a dual-mode server network with one shared economy and a ton of great features. Players can choose and easi... |
| [qHash](https://hashcube.net) | `oyna.hashcube.net` | `19132` | tr | 2016'dan bu yana Minecraft: Bedrock Edition sürümünde Türkiye'nin en büyük sunucusu olan HashCube, günümüzde SkyBlock... |
| Ragemine | `tpm.ragemine.net` | `19132` | es | Accesibilidad Atlética Total La profunda devoción por la actividad física que define el carácter del ciudadano venezo... |
| Raidlands | `raidlands.org` | `19132` | en | Welcome to Raid Lands, in the server you must protect your base to prevent players from raiding and destroying your b... |
| [RainyPvP](https://rainypvp.net) | `play.rainypvp.net` | `19132` | en | RainyPvP  Looking for a Bedrock Server with multiple features and creative ideas? We got all of that!  It Contains:  ... |
| [RayBigWorld](https://map.raybigworld.duckdns.org/) | `raybigworld.duckdns.org` | `19132` | en | RayBigWorld is a cross-play survival SMP that connects Java and Bedrock players on a single shared world. Built for f... |
| [ReallyWorld](http://reallyworld.ru) | `mc.reallyworld.ru` | `19132` | ru | Grief server |
| [Rede Revo](https://rederevo.com) | `jogar.rederevo.com` | `19132` | pt-BR | Bem-Vindos a Rede Revo, a rede de servidores mais incrível que você já encontrou.  Aceitamos jogadores da 1.12 até a ... |
| [Redestar](https://loja.redestars.com) | `redestars.com` | `19132` | pt-BR | Servidor de sobrevivencia JAVA & BEDROCK |
| Reinos Perdidos | `bedrock.reinosperdidos.com` | `19132` | pt-BR | Reinosejurfhhheiwiiwjsjdjdsjjeejjejejwueue |
| [RelxMC](https://relxmc.com/) | `be.relxmc.com` | `19132` | id | No description provided. |
| [Renderycrafty 2026](http://renderycrafty.pages.dev) | `erci.ilkom.tech` | `19132` | en | RenderyCrafty Server  Survival Multiplayer  RenderyCrafty, also known as RC Server, is a survival Minecraft server lo... |
| [RESTLESS Network](https://restlessmc.net/join/) | `play.restlessmc.net` | `19132` | en | Restless MC is a Java + Bedrock network built around three different experiences: Kingdom SMP, Heartfall Lifesteal, a... |
| [RetireX Online](https://cybox.kr) | `cybox.kr` | `19132` | en | RETIREX ONLINE  Drift through corners. Boost down the straight. Race inside Minecraft.  RetireX Online is a custom ka... |
| Retronix | `retronix.club` | `19132` | en | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐑𝐞𝐭𝐫𝐨𝐧𝐢𝐱 — 𝐁𝐫𝐢𝐧𝐠𝐢𝐧𝐠 𝐁𝐚𝐜𝐤 𝐏𝐯𝐏 𝐢𝐧 𝟐𝟎𝟐𝟔!  𝐖𝐡𝐚𝐭 𝐢𝐬 𝐑𝐞𝐭𝐫𝐨𝐧𝐢𝐱..?  Retronix is a Minecraft: Pocket Edition (MCPE)... |
| [RevivalSMP](https://revivalsmp.net) | `revivalsmp.net` | `19132` | en | RevivalSMP — Lifesteal Survival   Steal hearts. Survive the competition. Become a legend.   What We Offer:   • Lifest... |
| [RevolutionWorlds](http://revolutionworlds.xyz) | `revolutionworlds.xyz` | `19132` | pt-BR | Servidor de MiniGames Versão Bedrock e Java  TNTRUN  PARKOUR  FACTIONS  PVP  SKYWARS  BEDWARS  BUILDBATTLE  HIDE AND ... |
| [RevonicMC](https://store.revonicmc.com) | `play.revonicmc.com` | `19132` | en | Welcome to RevonicMC – your gateway to boundless adventure!  BEDROCK SUPPORTED  Stay Connected:  • IP: play.revonicmc... |
| [RezzCraft pull up a chair](https://www.rezzcraft.us/) | `bedrock.rezzcraft.us` | `19132` | en | [Bedrock & Java] RezzCraft - Friendly Survival SMP \| Land Claims, Player Shops, Daily Quests  Looking for a long-ter... |
| [RiverSMP](https://store.rivernetwork.net) | `rivernetwork.net` | `19132` | en | 🌊 RiverNetwork SMP – The Best SMP Experience! 🌊  RiverNetwork SMP isn’t just another Minecraft server – it’s the best... |
| [RolePlay](http://axiomlandpe.ir) | `play.axiomland.ir` | `19132` | en | rubika : @AxiomLand |
| [Roshercraft](https://roshercraft.com.tr/) | `play.roshercraft.com.tr` | `19132` | tr | RosherCraft oyuncularına kaliteli ve eşsiz bir deneyim sunan minecraft oyun sunucusudur. |
| [RuinSpirit Server Network](https://ruinspirit.net) | `mc.ruinspirit.net` | `19132` | de | Willkommen auf RuinSpirit – Dein neues Minecraft-Heim!  Java: mc.ruinspirit.net  Bedrock: mc.ruinspirit.net:19132  Ha... |
| [Ruinwake](https://ruinwake.com/) | `bedrockruinwake.playit.plus` | `19132` | en | # RUINWAKE \| JAVA & BEDROCK ANARCHY  Welcome to **Ruinwake**, a persistent Minecraft anarchy server inspired by 2b2t... |
| RulerMC | `play.rulermc.com` | `19132` | en | 🌍 SMP  A fresh survival world built for long-term play:  • Teams: build a crew and fight for the top  • Skills, level... |
| Sa Crafters Network | `mc.playmc.co.za` | `19132` | en | Welcome to SA Crafters! SA's best Minecraft server.  Join IP: playmc.co.za  Bedrock IP: mc.playmc.co.za  Bedrock Port... |
| [SABATO alle 18](http://titanet.it) | `mc.titanet.it` | `19132` | it | Un NUOVO modo di giocare a Minecraft ⚡  Survival+ ⚡ una Survival Earth Moddata MA SENZA MOD! Mappa del Mondo Reale!  ... |
| [Sakura Realms](https://store.sakurarealms.net) | `mp.sakurarealms.net` | `19132` | en | Sakura Realms ｡･::･ﾟ★ - an enhanced vanilla smp server! [​Latest Version]  Ever wish Mojang would add simple things t... |
| SakuraLand Practice | `prac.sakuraland.net` | `19132` | zh | 0.14.3-0.15.10 MCPE pvp server |
| [Saloon Network Minecraft Sunucuları](https://saloonnetwork.com) | `play.saloonnetwork.com` | `19132` | tr | ŞİMDİ YENİ OYUN CAPTIVE (BOXED) DE SİZLERLE! DÜNYADA İLK DEFA SALOON NETWORK'TE!  Saloon Network 2018 yılında temelle... |
| [San PE](http://pay.san-pe.fun) | `san-pe.fun` | `19132` | tr | No description provided. |
| Saturnian Wolves | `play.saturnianwolves.xyz` | `19132` | en | Saturnian Wolves SMP  Fresh Java + Bedrock Crossplay Survival  Saturnian Wolves SMP is a fresh survival server built ... |
| [SB Network Hub](http://sbpvp.com) | `play.sbpvp.com` | `19132` | en | SB Network is a Minecraft Bedrock network built around competitive PvP and a high-quality multiplayer experience.  ⚔️... |
| Scannerplay | `s1.minecraft-be.scannerplay.com` | `19132` | en | Latest version |
| SchlaflosGames | `schlaflosgames.de` | `19132` | de | Du suchst ein Server auf dem Freundlichkeit, Hilfsbereitschaft und Spaß an erster Stelle stehen?  Dann bist Du bei un... |
| [Schradernator SMP Survival](https://mc.schradernator.com/?src=smp-list-mcps) | `play.schradernator.com` | `19132` | en | Schradernator SMP is a free Minecraft Bedrock server that opened in October 2026.  HOW TO JOIN  Address: play.schrade... |
| [Scmain](https://ldp.scmain.com/) | `ldp.scmain.com` | `19132` | en | LDP SMP is no wiping server*, where you earn ≈3$ by play**.  Dynamic prices ingame shop(items growing and falling lik... |
| [Sdt-x](http://www.sdt-x.top) | `mc.sdt-x.top` | `19132` | zh | 𝓜𝓲𝓷𝓮𝓬𝓻𝓪𝓯𝓽 𝓑𝓮𝓭𝓻𝓸𝓬𝓴 𝓢𝓓𝓣-𝓧 𝐒𝐤𝐲𝐁𝐋𝐨𝐜𝐤 𝓢𝓮𝓻𝓿𝓮𝓻  ✨ 我們是 純基岩版 海島生存 伺服器  🎉 更多資訊請關注我們的官方平台 🎉  🌟 遊戲特色 🌟  🔹 遊戲幣VIP、地圖: 玩家可於遊戲內賺取 "金... |
| Seas | `seasia.fun` | `19132` | id | No description provided. |
| [Season 10](https://store.zeqa.net/) | `zeqa.net` | `19132` | en | Welcome to Zeqa  What is Zeqa?  Zeqa is the largest non-featured Bedrock PvP server in the world.  You can play with ... |
| [Sega](http://cora.land) | `segamc.net` | `19132` | en | No description provided. |
| SekaiSMP | `sekai.hopto.org` | `19132` | id | No description provided. |
| [SeliBox Ждет именно тебя](https://t.me/seliboxpvp) | `selibox.minerent.io` | `19132` | en | No description provided. |
| [SemiSurvivalCraft](https://www.semisurvivalcraft.com) | `mp.semisurvivalcraft.com` | `19132` | en | SemiSurvivalCraft  Welcome to SemiSurvivalCraft! We're a Cross Platform Semi Vanilla Survival Minecraft server with a... |
| Sempie | `mc.sempie.nl` | `19132` | en | Sempie Craft is a friendly vanilla survival server where Bedrock and Java players play together on one world.  🏡 Land... |
| [Sentouki](https://www.sentouki.net/) | `sentouki.net` | `19132` | en | If you are looking for chill community, with all kind of players from all over the world, to make memories with. Then... |
| [Sera](http://www.seramc.top) | `play.seramc.top` | `19132` | id | 🌍 SERA MC — Minecraft Survival Indonesia  Bosen main survival yang itu-itu aja?  Yuk cobain SERA MC! ✨  🎮 Support Jav... |
| [Serb-craft](https://www.serb-craft.com) | `pe.serb-craft.com` | `19132` | en | Welcome to SERB-CRAFT! Balkan server with its own AntiCheat!  We offer a wide variety of fun servers ranging from Sur... |
| [Server is online](https://miranasmp.com) | `play.miranasmp.com` | `19132` | en | MiranaSMP is a bedrock survival server hosted in Singapore, with low ping for players in the Singapore, Malaysia, Ind... |
| [Server online](http://Forum.glmidnight.co.uk) | `play.glmidnight.co.uk` | `19132` | en | GL Midnight's SMP offers you:  - 24/7!  - Infraction History (Web)  - TPA system  - Unlimited homes  - Discord Server... |
| [Server Unreachable](https://craftbit.net) | `play.craftbit.net` | `19132` | en | We're a new and upcoming Minecraft server that supports both Java and Bedrock edition. Our server is aiming to give a... |
| [Servicraft](http://servicraft.org) | `servicraft.org` | `19132` | es | Bienvenido a Servicraft  ¡Te damos la bienvenida a Servicraft, un servidor de Minecraft que te ofrece una experiencia... |
| [Servidor Oficial Premium Mundo-Minecraft](https://www.mundo-minecraft.com/) | `server.mundo-minecraft.com` | `19132` | es | 🎉 Mundo-Minecraft.com – Servidor Premium de Construcción desde 2010 🎉  ¡Bienvenido a Mundo-Minecraft.com, una comunid... |
| [Sezon 2! Baw się dobrze](https://astoria.studio) | `mc.astoria.studio` | `19132` | pl | Tworzymy własne rozwiązania, dla wygody graczy obsługujemy wiele platform , w tym Windows, Android, iOS, Java, Xbox. ... |
| [Shadowyn](https://www.shadowyn.id/) | `shadowyn.id` | `19132` | id | No description provided. |
| [SheepSMP](https://sheepsurvival.tebex.io) | `sheepsmp.com` | `19132` | en | A survival server that's totally "ewe"-nique!  Join the flock on a server where the fun never *shears* out! With cust... |
| [Shulkerboxes](http://chukerboxes.com) | `ivanos-076802.bedrock.shulkerboxes.com` | `19132` | pt-BR | Um mundo normal de survival.  Aviso: você nasce em um deserto |
| [Silvavita Smp](http://web.silvavita.id) | `silvavita.id` | `19132` | id | No description provided. |
| [Simplex SMP](https://discord.gg/2gAsymnXfd) | `simplexsmp.eu` | `19132` | en | ⛏️ Welcome to SimplexSMP – Your Chill Survival Escape! 🌿  No Pay-to-Win. No confusing systems.  Just pure survival, g... |
| SiphonMC | `play.siphonmc.net` | `19132` | en | Bedrock Server IP: Play.SiphonMC.net  Bedrock Server Port: 19132  -Leveling system, Skilling system, Player reward sy... |
| [Si̇mi̇tSMP](http://www.simitsmp.com) | `oyna.simitsmp.com` | `19132` | tr | Özel simit tarifleri, dengeli ₺ ve Simit Coin ekonomisi, ayrı Lobi ve Survival dünyaları, kasalar ve hilesiz rekabetl... |
| [Sky X Network](https://skyxnetwork.net/) | `skyxnetwork.net` | `19132` | en | SkyXNetwork is a Minecraft server with Survival, Mining Tycoon and Skygen. Survival is the main mode, so if you just ... |
| [Skybars](https://skybars.me) | `mps.skybars.me` | `19132` | en | SkyBars - free Minecraft server for phone and PC. Bedrock (MCPE) and Java crossplay, versions 1.8 up to the latest.  ... |
| Skyblocktr | `play.skyblocktr.com` | `19132` | en | SkyblockTR, Skyblock'a yeni başlayanların da rahatça ilerleyebildiği Türkçe bir sunucudur. Kurallar, menüler ve tüm s... |
| [Skycrafters](http://skycraftermc.net) | `play.skycraftersmc.net` | `19132` | en | Skycrafters is a crossplay Minecraft network where Java and Bedrock players build side by side. Hosted in an Australi... |
| [SkyHold](https://skyhold.in) | `skyhold.in` | `19132` | en | Welcome to SkyHold, a skyblock server for Minecraft Bedrock Edition. Start on a block of grass over the void and grow... |
| Slayne MCPE | `slayne-mcpe.fr` | `19132` | fr | No description provided. |
| [Smilemorecraft New Dungeons Soon](https://www.smilemorecraft.com/) | `mc.smilemorecraft.com` | `19132` | en | Come join the fastest growing SMP on Minecraft! 💖 SmileMoreCraft is a 1.21+ Survival Server that NEVER WIPES! We have... |
| [SMP Server](https://www.astrocraft.org) | `mcps.astrocraft.org` | `19132` | en | 🌌 Astro SMP – Where the Entire Server Shapes the World  The world doesn't start infinite... you unlock it together.  ... |
| [Snug SMP](https://store.snugsmp.com) | `mc.snugsmp.com` | `19132` | en | SnugSMP has been running for around eight months and regularly has 20 to 50 players online, so there is almost always... |
| Soki Network | `play.petradox.xyz` | `19132` | id | Survival RPG Server with many Features! |
| SolCraft SMP disc meta returns | `sol-craft.xyz` | `19132` | en | Java & bedrock! Voice chat support  No grief  Very few commands and economy can be entirely ignored!  Great hardware ... |
| Solstad | `solstad.kildal.net` | `19132` | en | Vanilla bedrock server, restarted every night @4 CET for backup and upgrade build. Has been running from about Bedroc... |
| SoLuna SMP | `solunasmp.ddns.net` | `19132` | th | SoLuna SMP — Premier Minecraft 26.3 Crossplay Survival RPG Server (Java & Bedrock)  Looking for the best Minecraft 26... |
| Some Might Say | `seaberria.cloud-ip.cc` | `19132` | en | Seaberria is a semi-vanilla server (vanilla with quality of life plugins) for both Java and Bedrock players.  It was ... |
| [Something smells fishy](https://discord.fishy.gg) | `smp.fishy.gg` | `19132` | en | 🎣 Fishy SMP — Java + Bedrock Cross-Play Survival  Cast your line, stay a while.  One world, every platform. Join from... |
| Sonaba | `sonaba.net` | `19132` | en | Welcome to Sonaba Network.  The first and ever practice server to support 1.18+ bedrock versions with tons of default... |
| [SoulCraft транспорт](http://soulcraft-pe.ru) | `soulcraft-pe.ru` | `19132` | en | Start playing SoulCraft now!   Vote Reward /kit bonus  INFO =) For playing get into the portal!  1 portal= Server Sur... |
| [SparklyPower](https://sparklypower.net/) | `ps.sparklypower.net` | `19132` | pt-BR | SparklyPower, o melhor servidor de Minecraft Survival brasileiro, com crossplay PC e celular. Desde 2014 trazendo Sur... |
| [SplitCraft SMP](https://splitcraft.net/) | `mc.splitcraft.net` | `19132` | en | 🌸 SplitCraft 🌸  Build under the starry sky  splitcraft.net • Java + Bedrock, consoles too  Survival, but it actually ... |
| [Spot](https://spotgames.net/) | `mobile.spotgames.net` | `19132` | pt-BR | Já estamos aqui há mais de 12 anos fazendo modos divertidos para todo mundo. Sempre colocamos coisas novas e melhoram... |
| Squidnetwork | `play.squidnetwork.my.id` | `19132` | id | Welcome To SquidNetwork!!   IP JAVA : play.squidnetwork.my.id:25625  IP BEDROCK : play.squidnetwork.my.id  PORT BEDRO... |
| [Stableblocks SMP](http://store.stableblocks.net) | `stableblocks.net` | `19132` | en | Welcome to an adventurous and engaging economy based anti grief SMP!  - Take part in an awesome friendly community.  ... |
| StablePVP | `voidsmp.me` | `19132` | en | **Void SMP** (BLISS PLUGIN)  JAVA AND BEDROCK CAN JOIN   BLISS PLUGIN  No Crystal / Anchor PVP  EU Region  Weekly Eve... |
| [Stacksanarchy](https://discord.gg/T8TvHmvSN) | `stacksanarchy.mcserv.me` | `19132` | en | StacksAnarchy is a fun anarchy server that anyone can play!  Have fun doing whatever you want. You can be a builder, ... |
| [Starken's Dev](https://mc.starken.dev/) | `mc.starken.dev` | `19132` | ru | Хүн бүрт нээлттэй, найдвартай тоглох тоглоомын сервер!  Өмнө нь Nexus, Animax, NXS сервер дээр хөгжүүлэгчээр ажиллаж ... |
| [StarLight Network OPEN BACK](http://starlightmc.net) | `play.starlightmc.net` | `19132` | en | ✨ WELCOME TO STARLIGHT NETWORK ✨  The Most Aesthetic & Premium Minecraft Bedrock Experience  Why play on StarLight? S... |
| [Starmcvn](http://starmcvn.com/) | `pe.starmcvn.com` | `19132` | en | STARMCVN NETWORK [1.16.5 - 1.19+]  Discord: starmcvn.com/discord  Đây là server chơi chung giữ mcpc và mcbe  Server k... |
| [StormyLand 101 Anarchy](https://stormyland.org) | `anarchy.stormyland.org` | `19132` | en | StormyLand Network is a Bedrock/Java crossplay anarchy network with no rules, make friends, gather resources, and hav... |
| [StormyLand Survival](https://stormyland.org) | `survival.stormyland.org` | `19132` | en | NOTE: This is a Whitelisted Server, you need to join the StormyLand Discord, and either message me or submit your Gam... |
| [Strike Ffa](https://blog.inpvp.net/) | `play.inpvp.net` | `19132` | en | InPvP is a Minecraft Bedrock Edition network operating several multiplayer servers and experiences across mobile devi... |
| [SunRealms](https://sunrealms.net) | `mps.sunrealms.net` | `19132` | en | SunRealms - Best Minecraft Gens, Prison, Skyblock, Survival, Dungeons & Cobblemon Server 2026  IP: mps.sunrealms.net ... |
| [SuomiCraft PE](https://suomicraftpe.ddns.net/) | `suomicraftpe.ddns.net` | `19132` | en | SuomiCraft PE is a Finnish Minecraft Bedrock Edition server featuring various minigames and gamemodes.  We have on th... |
| [SuperCraft Network](https://tienda.supercraft.es/) | `bedrock.supercraft.es` | `19132` | es | Servidor Java & Bedrock No Premium & Premium  IP: mc.supercraft.es  Puerto para Bedrock: 19132  Reglas  https://www.s... |
| [Survival Mewtype SMP](http://mewtype.my.id) | `iftecen.my.id` | `19132` | id | 🐱 MEWTYPE — MCPE SERVER   ━━━━━━━━━━━━━━━━━━   Welcome to MewType!  Server Minecraft Bedrock buat kamu yang mau mabar... |
| [Survival no rules](http://shifttech.us.to) | `shifttech.us.to` | `19132` | en | its a realm in survival don't be mean and don't steel other then that make friends and have fun |
| [sVanilla Survival](http://corn.gg) | `corn.gg` | `19132` | en | sVanilla Survival goes back to the roots of what a Semi-Vanilla SMP should be. Vanilla, with few quality of life modi... |
| [SwiftServers](https://samplecraft.net) | `pixelattack.swiftservers.org` | `19132` | de | **Willkommen auf unserem Minecraft‑SMP!**   Unser Server bietet dir ein Survival‑Erlebnis, das deutlich über das hina... |
| [TalonMC](https://www.talonmc.net) | `bedrock.talonmc.net` | `19132` | en | TalonMC is the ultimate Minecraft Prison & Skyblock experience, built BY the community, FOR the community! We offer a... |
| [Tavern](https://tavernmc.net) | `tavernmc.net` | `19132` | en | Dive into a unique survival experience where PVPers and PVErs thrive! Level up your skills, battle epic bosses, conqu... |
| [TB craft the best server](https://tbstudio.be/en-US/Minecraft/TBCraft/Home) | `play.tbstudio.be` | `19132` | en | TB Craft  Step into the world of TB Craft, the ultimate survival & community server for Minecraft Bedrock Edition!  P... |
| [TerminaMC](https://TerminaMC.com) | `terminamc.com` | `19132` | en | 🏰 WILL YOU BE THE HERO OR THE VILLAIN? 🔥  The world of Termina is yours to shape. Will you build a thriving town and ... |
| [TerraeMC](https://terraemc.net) | `play.terraemc.net` | `19132` | en | Looking for a Minecraft server that offers a unique and exciting survival experience on both Bedrock and Java edition... |
| The Best SMP Ever | `kiwismp.fun` | `19132` | en | No description provided. |
| [The Cavern](https://thecavern.net) | `mc.thecavern.net` | `19132` | en | The Cavern is a peaceful 1.21 economy based Survival Towny server, with the sole purpose of providing a unique experi... |
| The heavan Reborn | `rth2.ddns.net` | `19132` | zh | 此房為重度模組房 怪物已不同以往請特別小心 (此房僅使用市集模組）  新增了數種別具風格的強大boss  還有新礦洞 新結構 新生態  各個模組細節都在開局說明書裡 請找個地方保留好 以備不時之需  後期有到下界推薦先挖石英 可合成強... |
| [The original Peaceful Vanilla Club](https://www.peacefulvanilla.club) | `bedrock.peacefulvanilla.club` | `19132` | en | ✅ No Fast Travel: Wander and Explore!  Say goodbye to teleportation on this semi-vanilla server. No /tp, /tpa, or /wa... |
| The Server Of Pupperzak | `bsf1.exaroton.me` | `19132` | en | No description provided. |
| Themclife SMP | `themclifesmp.com` | `19132` | en | Hey! We're THEMCLIFE SMP, a small, friendly Towny survival server that Java and Bedrock players share.  **What you'll... |
| [TheNRK](https://nrkcraft.enjin.com) | `play.thenrk.net` | `19132` | en | TheNRKNetwork (1.7 - 1.16)About the server:TheNRK is the server that offers something that no other server brings, bu... |
| [Thouthmine](http://thouthmine.ru) | `play.thouthmine.ru` | `19132` | en | Thouthmine takes you back to a world where every adventure begins with the first tree you chop down. Build a place to... |
| [Tidal](https://store.tidalpvp.com) | `tidalpvp.com` | `19132` | en | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐓𝐢𝐝𝐚𝐥 - 𝐓𝐡𝐞 #𝟏 𝐬𝐩𝐨𝐭 𝐟𝐨𝐫 𝐞𝐯𝐞𝐫𝐲𝐭𝐡𝐢𝐧𝐠 𝐏𝐯𝐏  “𝐖𝐡𝐚𝐭 𝐢𝐬 𝐓𝐢𝐝𝐚𝐥..?”  Tidal is a fresh and upcoming Minecraft: Bedro... |
| [Timelapse PvP](https://discord.gg/FqQduhw33S) | `timelapsepvp.verixen.net` | `19132` | en | > Looking for a Bedrock Blurry’s Java PvP Server without all the clutter?   >   > Timelapse Network delivers smooth p... |
| [Titan MC](http://titansmp.myftp.biz) | `titansmp.myftp.biz` | `19132` | en | No description provided. |
| [ToastyCraft Survival](http://toastycraft.com) | `play.toastycraft.com` | `19132` | en | 🍞 TOASTYCRAFT  Welcome to ToastyCraft, a cozy Minecraft survival server for Java players!  Build a cottage, open a sh... |
| [TopLand](https://toplandmc.ir) | `play.toplandmc.ir` | `19132` | en | Website » http://toplandmc.ir  Telegram » https://t.me/TopLandMc  Rubika » https://rubika.ir/TopLandMc |
| [TorchCraft](https://www.torchcraft.nl/) | `play.torchcraft.nl` | `19132` | tr | TorchCraft is de gezelligste server van Nederland. Naast veel gezelligheid hebben we leuke (en unieke) gamemodes, sne... |
| [Toxichemicals](http://toxichemicals.loseyourip.com) | `toxichemicals.loseyourip.com` | `19132` | en | A simple anarchy server I host for the general public on my own hardware. |
| [ToxMania](https://www.toxmania.net) | `toxmania.net` | `19132` | en | ToxMania – player-driven Survival SMP for Bedrock & Java  Join: toxmania.net · Port 19132  Claims that really protect... |
| TR Survival KLANLAR | `oyna.trsurvival.com.tr` | `19132` | tr | -Seviye ve rütbe sistemi  -Meslek Sistemi  -Hikaye Modu  -Kazgeliş  -Görevler |
| [TrashMCPE](http://discord.trashmcpe.com) | `play.trashmcpe.in` | `19132` | en | ENGLISH:  Hey you, do you know Trash MCPE? Let me introduce it to you :exclamation:  Trash MCPE is a India 1st Only M... |
| [Traycraft](https://traytoven.com) | `play.traytovenmusic.com` | `19132` | en | 🎮 TrayCraft: Crossplay Survival, Modded Feel, No Mods Needed  Java or Bedrock, PC, phone, or console: everyone plays ... |
| [Trinityindonesia](https://store.trinityindonesia.cc) | `trinityindonesia.cc` | `19132` | id | 🇮🇩  Selamat datang di Trinity Indonesia, server Anarchy RPG mendebarkan yang menawarkan pengalaman bermain penuh kebe... |
| TropicMine | `tropicmine.net` | `19132` | de | TropicMine 🌴 – Dein Crossplay City-Build-Server für Java & Bedrock!  Baue deine Träume, verdiene Geld im Farmer-Shop,... |
| [Tularia](https://tularia.fr/) | `play.tularia.fr` | `19132` | fr | Tularia est un serveur mcpe qui vous propose plusieurs modes de jeu avec pleins de nouveautés et d'ajout pour plaire ... |
| [Turkskyblock](https://turkskyblock.com) | `play.turkskyblock.com` | `19132` | en | TürkSkyblock, gökyüzündeki küçük bir adadan başlayıp kendi ekonomini kurduğun Türkçe bir Minecraft Skyblock sunucusud... |
| Turtlesshell | `play.turtlesshell.me` | `19132` | en | # 🐢 TURTLESHELL SMP 🌍  ### ⚔️ SURVIVE • BUILD • EXPLORE • CONQUER ⚔️  **Welcome to TurtlesShell SMP**, where every ad... |
| [TwendyMC](https://shop.twendymc.net) | `pe.twendymc.net` | `19132` | de | - Herzlich willkommen auf der Vote-Seite von -  TwendyMC.net  ⭐Dein Minecraft Crossplay Netzwerk ⭐  Pocket/Bedrock-IP... |
| [Twerion](https://www.twerion.net) | `bedrock.twerion.net` | `19132` | en | 🔹 Our Game Modes at a Glance:  ⚔️ BedWars  Play action-packed team battles where you must protect your bed and destro... |
| [Twilightshollow](https://twilightshollow.org) | `twilightshollow.org` | `19132` | en | Twilight's Hollow is a small SMP built on community values. We started as a small friend group tired of power abuse a... |
| [UltraMine !! Lobby](http://ultramine.net) | `ultramine.net` | `19132` | ru | ⚡ UltraMine — это уникальные Minecraft Pocket Edition сервера, созданные для комфортной игры и приятного времяпровожд... |
| [uMineQ](http://dc.mineq.net/) | `mineq.net` | `19132` | es | Bienvenidos a MINEQ, servidor de Minecraft Bedrock donde si te gusta el PvP ¡este es el lugar perfecto para ti!  Pero... |
| [Under Construction](http://mc.waystonenetwork.com) | `mc.waystonenetwork.com` | `19132` | en | ⚠️ WAYSTONE NETWORK IS IN ACTIVE DEVELOPMENT  The network is open while under construction. Expect bugs, frequent cha... |
| [Unilands](https://unilands.club/) | `unilands.club` | `19132` | en | bedwars bridge ffa duels private games custom maps |
| [UniMC Network](https://www.unimc.vn) | `global.unimc.vn` | `19132` | vi | 🌟 UniMC Network - unimc.vn 🌟  Máy chủ Minecraft Việt Nam 2026  Tham gia để trải nghiệm ngay những tính năng  độc đáo ... |
| Unix | `unix.f5.si` | `19132` | ja | Ranked Duels, UnRanked Duels, FFA |
| [UnrealTactical Network](https://www.youtube.com/channel/UCvQ6SLBfeclQq3j3BMgDQLQ) | `unrealtactical.com` | `19132` | en | Unrealtactical is a family-friendly survival/Smp server offering a variety of exciting features, including free items... |
| [Ussr Space](https://t.me/UssrSpace) | `mc.ussr.space` | `19132` | ru | 🚀 USSR SPACE — Выживание нового поколения!  🎮 ПОДДЕРЖКА ВСЕХ УСТРОЙСТВ  • Java Edition (ПК) — порт 25565  • Bedrock E... |
| [Utopiverse](https://www.utopiverse.net) | `play.utopiverse.net` | `19132` | en | ADD "Utopiverse" AS A FRIEND!  Who are we?  We are an extensive Minecraft network that offers players a unique gamepl... |
| ValenNW | `valennw.club` | `19132` | tr | No description provided. |
| Valeryan | `valeryan.my.id` | `19132` | id | VALERYAN ANARCHY ECO  Server Anarchy Eco Minecraft Bedrock.  Fitur utama  Bounty & PvP, duel dan PvP Arena  Ekonomi l... |
| [ValorMC](https://valormc.net/) | `bedrock.valormc.net` | `19132` | en | Claim your land, pick a job and earn. ValorMC is a brand new Survival SMP for Java and Bedrock!  ValorMC is the survi... |
| [Vanilla Europa](http://store.vanillaeuropa.com/) | `play.vanillaeuropa.com` | `19132` | en | Server IP: play.vanillaeuropa.com  Discord: https://discord.gg/mcstmJK  The Best European Survival Minecraft Server. ... |
| [Vanta Network](https://store.vanta-network.net/) | `vanta-network.net` | `19132` | en | Welcome to Vanta Network! We are a crossplay (Java & Bedrock) PvP and nations server.  We focus on sword, spear, and ... |
| [Vantage](https://vantagesmp.xyz) | `vantagesmp.xyz` | `19132` | en | Geyser/Floodgate crossplay, Folia 26.2, no whitelist, shard economy, lobby safe / wilds PvP-grief, no land claims |
| [Varilx](https://veylor.net) | `veylor.net` | `19132` | de | Veylor.NET ist ein deutscher Survival Minecraft Server auf Version 26.3 für Java und Bedrock. Beide Editionen spielen... |
| [Vayland](https://vayland.net/) | `mc.vayland.net` | `19132` | en | ❤️Welcome to the game project VayLand⚡.  We took the best, discarded the unnecessary and made interesting. Always up ... |
| Vegeance | `vegeance.com` | `19132` | pt-BR | No description provided. |
| [Veltrix](http://veltrixmc.eu) | `veltrixmc.fr` | `19132` | fr | No description provided. |
| [Venity Network](https://www.venitymc.com) | `play.venitymc.com` | `19132` | en | Venity Network is a Minecraft Bedrock server network that features multiple game modes, including BedWars, SkyWars, T... |
| [Ventureland](http://www.ventureland.net) | `bedrock.ventureland.net` | `19132` | en | A unique gamemode in minecraft  ► A large hand-built open world map  ► 8 different classes, each with unique abilitie... |
| [Versai Network](http://store.versai.pro) | `versai.pro` | `19132` | en | Versai.pro is a competitive practice PvP server with lots of features to offer:  Mace  Elytra Mace  NethPot  Crystal ... |
| VerseMC | `play.versemc.it` | `19132` | it | Server Totalmente Italiano.   Per cercare di ricostruire la community con un progetto serio e duraturo nel tempo!  Ti... |
| [Viciante Survival Brasileiro](https://www.viciante.com.br/) | `jogar.viciante.com.br` | `19132` | pt-BR | 🎮 O Viciante é um dos melhores servidores de Minecraft Survival brasileiro com economia, focado em conteúdo exclusivo... |
| [VisionHQ](http://visionpvp.com) | `caldera.visionpvp.com` | `19132` | en | 🌌VisionHQ \| Minecraft Bedrock 🌌  VisionHQ has been in development for about 5 years, it is a custom OP Factions and ... |
| [Voice Chat Games](https://coreygames.com) | `coreygames.net` | `19132` | en | Corey Games is a Minecraft network streamed live on YouTube & Twitch, with Voice Chat and VR supported. Send 300+ com... |
| [Voidhaven](http://www.vhaven.xyz) | `play.vhaven.xyz` | `19132` | id | VOIDHAVEN SMP  Semi-Anarchy Survival Indonesia.  ⚔️ Free PvP • 💰 Player Economy • 🏪 Player Shops • 🛡️ Expensive Land ... |
| Voidrush | `play.voidrush.org` | `19132` | en | ⚔️ VOIDRUSH — A CUSTOM RPG ADVENTURE IN THE VOID ⚔️  📱 Play on phone, tablet, console or PC. Bedrock and Java players... |
| VoidSMP | `voidmc.mcserver.us` | `19132` | en | WELCOME TO VOIDMC SURVIVAL!   Build your empire, explore the world, make friends, become rich, or start a war — the c... |
| [VolexMC Beta](http://www.volexmc.net) | `play.volexmc.net` | `19132` | tr | VolexMC - Gelişmiş Factions, yeni ve ileri seviye özel sistemler,mobil destekli arayüzler ve daha fazlası... |
| Volt | `volt.mcbe.fr` | `19132` | fr | Le meilleur kitmap en 2026 ! |
| [VolteraMC](http://www.volteramc.net) | `play.volteramc.net` | `19132` | id | No description provided. |
| [Voltraz](https://discord.voltraz.xyz) | `voltraz.xyz` | `19132` | id | *🌍 Selamat Datang di Voltraz MC*  Selamat datang di Voltraz MC, server Minecraft semi-RPG yang penuh petualangan, fit... |
| [Vortex Network](https://vortexnetwork.net) | `bedrock.vortexnetwork.net` | `19132` | en | Vortex Network is a space-themed Minecraft server featuring popular game modes such as Prison, Skyblock, Survival and... |
| [Waffle](http://wafflesonne.com/) | `wafflesonne.com` | `19132` | tr | waffle&sonne minecraft  Sunucu Türü: Survival  IP: wafflesonne.com  Sunucu Sürümü: 1.19.2 Java (1.9+ java ve son suru... |
| [Waria Roleplay](https://waria.eu/rp) | `mc.waria.eu` | `19132` | fr | Waria RolePlay est un serveur mcpe roleplay qui existe depuis 2020.  Dans la ville de Waria, vous pouvez  - Crée votr... |
| Wartungsarbeiten | `magmamc.de` | `19132` | de | Magmamc.de ist ein Free-to-Play Minecraft-Server für Java und Bedrock von Version 1.8 bis 1.21.11 (der Server läuft a... |
| [WaterdogPE](http://slmc.ir) | `play.slmc.ir` | `19132` | en | SkyLine, a PocketMine Minecraft Bedrock server. Experience a fusion of strategic Bedwars competition and a deep, inte... |
| Waves Gamer | `play.mc.wavesgamer.com` | `19132` | en | Waves Gamer is a small, UK-hosted Minecraft network built around one idea: everything you get here, you earn by playi... |
| WehaveTrees | `mps.wehavetrees.gg` | `19132` | en | 🌲 Welcome to WeHaveTrees – Survival with a Fresh Twist! 🌲  ✅ Java & Bedrock Support \| 📌 IP: wehavetrees.gg \| 🔗 Disc... |
| Wertie3020 | `wertie3020.duckdns.org` | `19132` | en | this server is a old anarcy server with a lot of history   most players stop playing becos the world was coruped for ... |
| [Wildphire](http://wildphire.net) | `play.wildphire.net` | `19132` | en | Wildphire is a talented and passionate team dedicated to creating top-tier content for the Minecraft Marketplace. Fro... |
| [Willow Haven](https://www.kingdomscalling.com/) | `enter.kingdomscalling.com` | `19132` | en | 🗺️Introducing the WORLD OF ANCALADORE🗺️  Join with: enter.kingdomscalling.com Bedrock Port 19132  NEW Worlds  * Ancal... |
| [WindPvP](https://windpvp.com/wiki/welcome) | `mps.windpvp.com` | `19132` | en | Hello everyone!  I've been working on a Minecraft server that is very different from most of the ones you see.  Inste... |
| [WorthyDeath](https://worthydeath.com) | `domination-brooks.tun.ply.gg` | `19132` | en | 🎮 WORTHY: Bedrock Edition is welcome!  Play on phone, tablet, Xbox, PlayStation, Switch or Windows together with Java... |
| [WoutWoot](https://woutwoot.com) | `bedrock.woutwoot.com` | `19132` | en | WoutWoot is pseudo-anarchy survival with a real player-driven economy.  ⚔ No claims. Anything can be raided. Hide you... |
| [xACE MC](http://acemc.co) | `mp.acemc.co` | `19132` | en | 🌟 Welcome to our BRAND NEW 1.20 Survival Server! BEDROCK COMPATIBLE! It's just been released, and we couldn't be more... |
| [Xgames](https://x.com/mcmenearth?s=21) | `men-earth.xgames.jp` | `19132` | en | # Join Men Earth!  Men Earth is a new Earth server created in October 2025.  The world is made at a 1:4000 scale, so ... |
| [Xorek](https://my.aezamine.com) | `aezamine.com` | `19132` | en | Tired of crashes and cheating on servers? Go to the reliable AézaMine server.  Join the best! |
| [YaskoMC](https://yasko-mc.rf.gd/) | `play.yasko-mc.rf.gd` | `19132` | tr | 🇹🇷 YaskoMC — Türkiye Haritalı SMP  Gerçek Türkiye'de Minecraft oynamaya hazır mısın?  YaskoMC'nin haritası gerçek uyd... |
| [YourSMP](https://yoursmp.net) | `yoursmp.net` | `19132` | en | Welcome to YourSMP.net — The Ultimate Crossplay SMP Experience!  Looking for a friendly, modern, and engaging Surviva... |
| [YummyMC SMP](https://store.yummymc.net/) | `mpc.yummymc.net` | `19132` | en | A food-themed Survival SMP with a friendly, grief-free community! Custom Jobs, Fishing, Farming, Land Claims & weekly... |
| [ZedMC](https://zdmc.ir) | `play.zdmc.ir` | `19132` | en | ZedMC is an Iranian Minecraft server featuring Java & Bedrock cross-play, SMP survival, and a free-to-play experience... |
| [ZenPvP](http://www.zenpvp.net) | `br.zenpvp.net` | `19132` | en | ZenPvP Network  Prison \| Skyblock \| Factions \| Survival \| Gens  We stride to provide the "Ultimate Experience" to... |
| [ZenyLand](https://zenyland.com) | `play.zenyland.com` | `19132` | id | 🌏 ZenyLand merupakan sebuah server Minecraft yang support semua platform. Mulai dari Java, Bedrock, MCPE, Xbox, PS. K... |
| [Zerix Network](https://zerix.ml) | `zerix.ml` | `19132` | en | Zerix Network  is a competitive MCBE PvP server, built with passion since 2018.  MCBEPVP is Zerix’s global Practice P... |
| Üstü Tekno MC Üstü | `oyna.teknomc.net` | `19132` | tr | 🌲Survival🌲  ⚒️MCPE⚒️  🌹Çok güzel sunucu herkesi bekleriz.🌹  📜Bu güzel sunucuyu herkese tanıtmak için açtım hesapı.📜 |
| [ʚ ESKMC NETWORK ɞ](https://tienda.eskmc.net/) | `eskmc.net` | `19132` | es | Servidor de BoxPvP con una gran variedad, entra y prueba! |
| [ᄽMuzCraftᄿ](https://muzcraft.com/oyna) | `mc.muzcraft.com` | `19132` | pt | Türk Minecraft server ip MC.MUZCRAFT.COM Java ve Pocket/Bedrock Edition sunucumuz sizlere Faction ve SkyBlock oyun mo... |
<!-- SERVERS:END -->

## License

Code and structure: [MIT](LICENSE). Server names, descriptions, logos and images belong to their respective owners. If you own a listed server and want it removed, open an issue or a pull request.
