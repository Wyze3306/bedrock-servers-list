# Liste des serveurs Minecraft Bedrock

Liste ouverte et collaborative des serveurs **Minecraft Bedrock Edition** (mobile, console, Windows 10/11).
Chaque serveur a son IP, son port, une image, une description et une langue.

- Données prêtes à l'emploi : [`servers.json`](servers.json) et [`servers.csv`](servers.csv)
- Une fiche par serveur dans [`servers/`](servers) (un fichier JSON chacun)
- Contributions bienvenues : ajoutez ou corrigez un serveur par pull request, voir [CONTRIBUTING.md](CONTRIBUTING.md)

> La liste initiale a été importée depuis [minecraftpocket-servers.com](https://minecraftpocket-servers.com/). Chaque fiche importée garde un lien `source` vers sa page d'origine. La langue n'existe pas sur le site d'origine, elle a été déduite automatiquement (description, puis pays) : n'hésitez pas à la corriger.

## Ajouter ou modifier un serveur

1. Forkez le dépôt.
2. Créez ou modifiez `servers/<nom-du-serveur>.json` :

```json
{
  "name": "Mon Serveur",
  "ip": "play.monserveur.net",
  "port": 19132,
  "description": "Survie, mini-jeux et événements chaque semaine.",
  "lang": "fr",
  "image": "https://exemple.com/banniere.png",
  "country": "France",
  "version": "1.21",
  "website": "https://monserveur.net",
  "discord": "https://discord.gg/xxxx",
  "tags": ["Survival", "Minigames"]
}
```

3. Ouvrez une pull request. La CI valide automatiquement le format. Ne touchez pas à `servers.json`, `servers.csv` ni au tableau ci-dessous, ils sont régénérés après la fusion.

Champs obligatoires : `name`, `ip`, `port`, `description`, `lang`. Les autres sont facultatifs.

## Utiliser les données

```bash
curl -s https://raw.githubusercontent.com/Wyze3306/bedrock-servers-list/main/servers.json
```

## Liste des serveurs

<!-- SERVERS:START -->
**1042 serveurs** · langues : `en` 653, `id` 65, `fr` 60, `es` 51, `tr` 45, `pt-BR` 39, `de` 33, `ru` 27, `zh` 16, `it` 9, `ja` 8, `vi` 8

| Serveur | IP | Port | Langue | Version | Description |
|---|---|---|---|---|---|
| [! SuperCraft Network [1.8-26.3] ❤ !](https://tienda.supercraft.es/) | `bedrock.supercraft.es` | `19132` | es | 26.63 | Servidor Java & Bedrock No Premium & Premium  IP: mc.supercraft.es  Puerto para Bedrock: 19132  Reglas  https://www.s... |
| !!!MINEARG!!! NETWORK. | `B.MINEARG.NET` | `19132` | es | 26.52 | ¡Disfruta del mejor servidor survival custom! Con muchísimo contenido, actualizaciones y soporte activo las 24hs!   ➠... |
| &amp;aWelcome! 0/70 players online! 0.14.x &amp; 0.15.10 | `bbpe.ddns.net` | `1410` | en | 0.15.10 alpha | Mcpe 0.14.3-0.15.10 MultiVersion based server. |
| [&gt; &gt; &gt; ┃ STARKEN&#039;S DEV ┃ [1.8 - 26.X] ┃ &lt; &lt; &lt;](https://mc.starken.dev/) | `mc.starken.dev` | `19132` | ru | 26.52 | Хүн бүрт нээлттэй, найдвартай тоглох тоглоомын сервер!  Өмнө нь Nexus, Animax, NXS сервер дээр хөгжүүлэгчээр ажиллаж ... |
| [&gt; 26.60 &lt; ATUALIZADO](http://site.legax.net) | `legax.net` | `19132` | pt-BR | 26.60 | Seja bem-vindo(a) à LEGAX Network, a rede brasileira de servidores de Minecraft Bedrock!  🇧🇷 PING BR: Nossos servidor... |
| [&lt;&gt; play.nutellaserv.net &lt;&gt;](https://www.nutellaserv.fr) | `play.nutellaserv.fr` | `19132` | fr | 26.50 | NutellaServ.fr ❀ Mini-Jeux  Nous sommes un serveur Mini-Jeux reprenant l'interface de la version Java, avec des fonct... |
| [&lt;&lt;---------- Cake SMP ----------&gt;&gt;](https://cakesmp.tebex.io/) | `cakesmp.com` | `19132` | en | 26.62 | Looking for a survival experience that's a piece of CAKE?!   CakeSMP is a community-driven SMP focused on chill vibes... |
| [&lt;{Faith Avenue}&gt; Ver 26.2](http://faithavenue.org) | `FaithAvenue.host` | `19132` | en | 26.60 | Welcome to your new paradise!  FaithAvenue is Christian faith focused family friendly city themed network. Our server... |
| [&quot; THE CAVERN [26.2+]n 26.2 Update! /discord&quot;](https://thecavern.net) | `mc.thecavern.net` | `19132` | en | 26.63 | The Cavern is a peaceful 1.21 economy based Survival Towny server, with the sole purpose of providing a unique experi... |
| [&quot;&quot;](http://Bumblecraft.net) | `Play.bumblecraft.net` | `19132` | en | 26.45 | Aucune description. |
| [&quot;A Anarchy Server&quot;](http://toxichemicals.loseyourip.com) | `toxichemicals.loseyourip.com` | `19132` | en | 26.52 | A simple anarchy server I host for the general public on my own hardware. |
| &quot;A Minecraft Server&quot; | `basic-4.alstore.space` | `25710` | en | 26.52 | A mcpe server from indonesia  This server is free for all. |
| &quot;A Minecraft Server&quot; | `starter-4.astrixhost.web.id` | `5038` | id | 26.63 | Sekarang bisa dimainkan di Java dan Bedrock, ini adalah server Survival & Oneblock, kamu dapat menjelajah, membangun,... |
| &quot;A Minecraft Server&quot; | `mc.kenster.uk` | `50272` | en | 26.40 | We are currently a completely vanilla smp server the world may be reset |
| &quot;A Minecraft Server&quot; | `aquasmp.my.id` | `5001` | id | 26.52 | Minecraft Survival Economy Bedrock Servers with Tons of Feature and Events |
| &quot;A Minecraft Server&quot; | `play.blackarchive.fun` | `12009` | ja | 26.60 | ₊˚‧✧︵‿・୨୧・‿︵✧︵‿・୨୧・‿︵✧‧˚₊  ꒰꒰ ୨୧ ˖˚˳⊹ BlackArchive \| Fantasy Roleplay  ╭﹒⊹˚ʚ︰꒷꒦︶︶︶︶︶꒷꒦︶︶︶︶︶꒷꒦︶︶︶︶︶₊˚⊹  The Archive s... |
| &quot;A Minecraft Server&quot; | `skemberdu.playwithbao.com` | `16726` | en | 26.52 | Welcome to Skemberdu, a dedicated survival and economy server built for pure, joyful gameplay! We offer full Java and... |
| &quot;A Minecraft Server&quot; | `play.runichosting.com` | `25566` | en | 26.63 | Welcome to Runic Hearth SMP, a free survival server where Java and Bedrock players can build, explore, and play toget... |
| &quot;A Minecraft Server&quot; | `play.asteriamc.my.id` | `19132` | id | 26.60 | Aucune description. |
| &quot;A Minecraft Server&quot; | `51.222.117.199` | `8131` | en | 26.40 | [size=18]RED REQUEST NETWORK[/size]  NOW RECRUITING FOUNDING STAFF & MODERATORS  Red Request is a high-performance Mi... |
| &quot;a semi-vanilla survival minecraft server, that do not encourage or offer pay to win&quot; | `tissues-clipboard.tun.ply.gg` | `34602` | en | 26.51 | A claim survival server that has modded generation using vanilla block that will let player and you have a unique exp... |
| [&quot;ArosMC&quot;](http://www.alacanetwork.com) | `oyna.alacanetwork.com` | `19132` | tr | 26.62 | ? ALACANETWORK SKYBLOCK  Gökyüzünde yalnızsın… Ta ki kendi krallığını kurana kadar! ☁️?  Sıfırdan başla, adanı büyüt,... |
| [&quot;Bloxr Survival \| NEW \| Java + Bedrock&quot;](https://bloxr.co.uk/) | `join.bloxr.co.uk` | `19132` | en | 26.60 | BLOXR — FREE-TO-PLAY JAVA + BEDROCK SURVIVAL  Build a home worth coming back to. Find your spot, protect your land an... |
| [&quot;Come fall for us through our aethernhttps://discord.gg/AmArDSBfFK&quot;](https://twilightshollow.org) | `twilightshollow.org` | `19132` | en | 26.62 | Twilight's Hollow is a small SMP built on community values. We started as a small friend group tired of power abuse a... |
| [&quot;DonutButBetter&quot;](https://donutbutbetter-website.donutbutbetter.workers.dev) | `76.164.199.237` | `19132` | en | 26.60 | DonutButBetter: everything you liked about DonutSMP, without what you hated.  Live economy: /sell prices follow suppl... |
| &quot;Etheria SMP — Tracez votre histoire, bâtissez votre empire.&quot; | `etheriasmp.apexmc.co` | `25690` | fr | 26.51 | un SMP bedrock et java avec des évents fréquents et des armures et armes moder!!! |
| [&quot;i2b2t: INDONESIA 2 BUILDERS 2 TOOLS&quot;](https://hollowknightttt.github.io/laughing-fiesta/) | `i2b2t.jo3.org` | `46265` | en | 26.63 | I2B2T: Indonesia 2Builders2Tools #RETURN  i2b2t — Pure & Uncensored Minecraft Anarchy  ​Welcome to i2b2t, a raw, lawl... |
| [&quot;IP: mc.benwyw.comnDC: discord.benwyw.com \| Web: www.benwyw.com&quot;](https://www.benwyw.com) | `mc.benwyw.com` | `19132` | en | 26.63 | 🎮 Welcome to Ben’s Minecraft Server!  Looking for a fresh, lag-free Survival experience? Whether you’re on PC, Mobile... |
| &quot;lifesteal&quot; | `170.23.68.81` | `25628` | en | 26.52 | # ⚔️ LastBreath SMP \| Bedrock Hardcore  **ONE WORLD. LIMITED LIVES. PERMANENT CONSEQUENCES.**  Welcome to LastBreath... |
| [&quot;Lordscraft, um lugar para todos&quot;](https://lordscraftofc.servegame.com/) | `lordscraftofc.servegame.com` | `19132` | pt-BR | 26.60 | Bem-vindo ao Lordscraft!  Aqui, a prioridade é oferecer uma experiência única, com foco em jogabilidade, estabilidade... |
| [&quot;Memento Mori - Java + Bedrock Hardcore&quot;](https://oldmannetwork.com/minecraft/hardcore/) | `oldmannetwork.com` | `19136` | en | 26.60 | MEMENTO MORI - ANARCHY HARDCORE  No claims. No rules. One life.  Permanent death. No respawn. PvP enabled everywhere ... |
| [&quot;Mine-Forge&quot;](http://www.mine-forge.net) | `minecraft.mine-forge.net` | `19132` | en | 26.40 | A series of Servers, offering Survival Multiplayer worlds. Cooperative, SMP. Active Community, and lots of support |
| [&quot;Paradigm&quot;](https://hub.playparadigm.online) | `playparadigm.online` | `25597` | en | 26.63 | Visit our website!  https://hub.playparadigm.online  Join our discord!  https://discord.gg/playparadigm  Paradigm is ... |
| [&quot;PMCc013e59c0bdf0ea05c94bead1361c610&quot;](https://discord.gg/6nbxAVD8ud) | `162.220.10.130` | `2043` | en | 26.60 | The Corvian Empire is the dominant power on the continent of Mythros. At the heart of the Corvian Empire lies the nat... |
| &quot;RPG TESTE&quot; | `jersey-unlikely.gl.at.ply.gg` | `54582` | en | 26.51 | Aucune description. |
| [&quot;Ruinwake \| Anarchy Survival&quot;](https://ruinwake.com/) | `bedrockruinwake.playit.plus` | `19132` | en | 26.62 | # RUINWAKE \| JAVA & BEDROCK ANARCHY  Welcome to **Ruinwake**, a persistent Minecraft anarchy server inspired by 2b2t... |
| [&quot;SeliBox Ждет именно тебя!!!&quot;](https://t.me/seliboxpvp) | `selibox.minerent.io` | `19132` | en | 26.60 | Aucune description. |
| &quot;StarBorne Survival Server \| https://dsc.gg/starbornemc&quot; | `starborne.mine.bz` | `2022` | en | 26.51 | After earth slowly destroyed itself from wars, chaos and politics, Project StarBorne was created to gather the last o... |
| [&quot;StormyLand 101 Anarchy&quot;](https://stormyland.org) | `anarchy.stormyland.org` | `19132` | en | 26.63 | StormyLand Network is a Bedrock/Java crossplay anarchy network with no rules, make friends, gather resources, and hav... |
| [&quot;Survival no rules&quot;](http://shifttech.us.to) | `shifttech.us.to` | `19132` | en | 26.52 | its a realm in survival don't be mean and don't steel other then that make friends and have fun |
| [&quot;ToastyCraft Survival&quot;](http://toastycraft.com) | `play.toastycraft.com` | `19132` | en | 26.52 | 🍞 TOASTYCRAFT  Welcome to ToastyCraft, a cozy Minecraft survival server for Java players!  Build a cottage, open a sh... |
| &quot;Towny • Survival • Economy • PvP&quot; | `vatra.dat.gg` | `17743` | en | 26.30 | 🔥 Vatra — a Ukrainian PvP survival server (1.9–26.1.2) with Towny, communities, and city-building!  🧭 Getting started... |
| &quot;Vanilla Plus&quot; | `23.230.3.146` | `25574` | es | 26.52 | Es un servidor con amigos existen addons instalado y para darle mas diversion quiero que entre agan base y los maten ... |
| &quot;« ✪ OGFACTIONS ✪ » - Experienta Supreman ➤ Sisteme Custom ● Open Beta ● ONLINE&quot; | `play.ogfactions.ro` | `19132` | ro | 26.52 | ⚔️ OG FACTIONS \| Construiește. Distruge. Domină. ⚔️  Bun venit pe OG Factions, locul unde readucem la viață adevărat... |
| [- Motaz -](https://discord.gg/motaz) | `motazmc.fr` | `19132` | fr | 26.60 | 🏰 - Voici **Motaz KitMap**  > 🔥 - Des **interfaces uniques** aux serveur  > ⚒️ - Un serveur **entièrement fait à la m... |
| [-- HEXARIS [26.2+] --](https://store.hexaris.cc) | `hexaris.cc` | `19132` | en | 26.60 | 💚 Hexaris is a claims-based Survival SMP built for all players with just enough risk to keep things interesting. 💚  ⭐... |
| [-----&lt; Creeper&#039;s Lab [Java+Bedrock] &gt;-----](https://www.creeperslab.net/) | `play.creeperslab.net` | `19132` | en | 26.60 | You like Minecraft? Want to create awesome builds? Play with friendly people? Get involved in building contests? All ... |
| ------- StikSMP 1.21.11-26.X ------- | `bplay.stiksmc.us` | `443` | en | 26.60 | Join StikSMP 1.21.11-26.X — A Fair, Feature-Rich - Minecraft Server Experience!  Server IP: play.stiksmc.us  Bedrock ... |
| [-------- PCC Rebuilt [1.21.10 - 26.3] -------- Creative Minigames Oneblock AND Racing](https://pccrebuilt.wixsite.com/pccr) | `mc.PocketCreative5.club` | `8027` | en | 26.51 | Pocket Creative Club is back! Now branded as PCC Rebuilt (or PCCR), this is a new server dedicated to the Minecraft c... |
| [---------- DungeonMC s1 ----------](https://discord.gg/dun) | `dunmc.us` | `20015` | en | 26.51 | Aucune description. |
| -----------[ PVP S1 ]----------- | `Router.shulker.xyz` | `27239` | pt-BR | 26.63 | Aucune description. |
| [----❤-☠---RustCraft---☠-❤----](https://rustcraft.aclclouds.online/) | `rustcraft.aclclouds.online` | `1188` | ar | 26.52 | اولین سرور ماینکرافت راست ایران |
| [---[- mc.crystalgemcraft.com -]---](https://www.crystalgemcraft.com/) | `mc.crystalgemcraft.com` | `19132` | pt | 26.60 | 💎 CRYSTALGEMCRAFT - Máy Chủ Minecraft SMP/RPG Đầy Huyền Thoại! 💎  Bạn đã sẵn sàng bước vào một thế giới SMP nhiều thú... |
| --= Aogire =-- ( 0.14.x, 0.15.10 ) | `aogiremc.duckdns.org` | `19132` | en | 0.15.10 alpha | AogireMC (MCPE 0.14.x & 0.15.10) |
| [-/ VORTEX NETWORK -/](https://vortexnetwork.net) | `bedrock.vortexnetwork.net` | `19132` | en | 26.52 | Vortex Network is a space-themed Minecraft server featuring popular game modes such as Prison, Skyblock, Survival and... |
| 1.20 üsᴛü ᴛᴇᴋɴᴏ ᴍᴄ 1.20 üsᴛü | `Oyna.teknomc.net` | `19132` | tr | 26.51 | 🌲Survival🌲  ⚒️MCPE⚒️  🌹Çok güzel sunucu herkesi bekleriz.🌹  📜Bu güzel sunucuyu herkese tanıtmak için açtım hesapı.📜 |
| 1.9.X——26.X 生存服\| 拓展内容已更新到1.21.11 | `mc.9666.fun` | `22148` | zh | 26.63 | \| 建造梦想基地 \| 领地系统保护你的家，圈地后无人可破坏 \|  \| 探索世界 \| `/rtp` 随机传送，发现新地形新冒险 \|  \| 刷怪战斗 \| 怪物穿戴附魔装备，下界合金级怪物0掉落，挑战感拉满 \|  \| 经... |
| 138.201.48.55 | `138.201.48.55` | `25782` | en | 26.52 | Coremademc S-3 is started join now this server for mcpe 0.14.3-0.15.10 join now » MiNi games etc and a simple LifeSte... |
| 1B1T Bedrock Anarchy | `144.217.224.171` | `25609` | en | 26.63 | 1B1T is a fully vanilla, hack-free anarchy server. Originally a realm, we recently moved to a server as our community... |
| 2b2w.org | `2b2w.org` | `19132` | en | 26.63 | Vanilla Survival/Anarchy server.   IP: 2b2w.org  Port: 19132  World was created 3/23/2021 and is now over 4 years old... |
| 3b3tpe [1.21.11] | `3b3tpe.org` | `19132` | en | 26.63 | 3b3tpe — Bedrock Anarchy  3b3tpe is a Minecraft survival server for bedrock players in a free for all no rules enviro... |
| 404 \| Faction-PvP - Java + Bedrock | `play.404servernotfound.net` | `19132` | en | 26.51 | 404 // SERVER NOT FOUND – Faction PvP with 1.8 PvP (old combat, no attack cooldown). Java & Bedrock cross-play.  Clai... |
| [4BLOCKS ◆ CITY ROLEPLAY](https://4blocks.gg) | `4blocks.gg` | `19132` | en | 26.60 | 4BlocksRP is a German-speaking city roleplay server, and Bedrock players are welcome. Join from phone, tablet or cons... |
| :: ArtMine.me :: Survival, Dupe, Grief, Anarchy | `artminepe.ru` | `19132` | ru | 26.60 | Э |
| [::TRAYCRAFT:: NOVEMBER UPDATE](https://traytoven.com) | `play.traytovenmusic.com` | `19132` | en | 26.60 | 🎮 TrayCraft: Crossplay Survival, Modded Feel, No Mods Needed  Java or Bedrock, PC, phone, or console: everyone plays ... |
| [=== Cyan Realms v1.21 ===](http://cyanrealms.com) | `play.cyanrealms.com` | `19132` | en | 26.62 | Embark on a journey through a vast, procedurally generated world where you can level up a wide array of skills and st... |
| [==============ILLUSIVEMC============== 26.2 Survival!!!! \| Welcome! \| Unique Experience!!! !](https://web.illusivemc.com/) | `IllusiveMC.com` | `25581` | en | Minecraft Java | IllusiveMC is a Non-Vanilla Minecraft SMP Server, where the fun never ends! Our server boasts a treasure trove of fea... |
| [=======[SURVIVAL MEWTYPE SMP ]==========](http://mewtype.my.id) | `Iftecen.my.id` | `19132` | id | 26.60 | 🐱 MEWTYPE — MCPE SERVER   ━━━━━━━━━━━━━━━━━━   Welcome to MewType!  Server Minecraft Bedrock buat kamu yang mau mabar... |
| [==UNDER CONSTRUCTION==](http://mc.waystonenetwork.com) | `mc.waystonenetwork.com` | `19132` | en | 26.60 | ⚠️ WAYSTONE NETWORK IS IN ACTIVE DEVELOPMENT  The network is open while under construction. Expect bugs, frequent cha... |
| [?l?w[?pAttack On Titan?f]?c Sv Annime...](http://AttackMC.ir) | `Play.AttackMC.ir` | `19132` | en | 1.21.100 | Minecraft server with Skymine Attack on Titan and Survival game modes |
| [[ Mineplex Games ]](https://www.mineplex.com/) | `play.mineplex.com` | `19132` | en | 26.52 | THE RETURN OF MINEPLEX   Hello everyone!  A few years ago, Mineplex shut down with a promise that it would return. To... |
| [!] SkyMC : NETWORK [!] Actualizacion: Medieval Duelo - UHC | `49.12.82.39` | `25599` | tr | 0.15.10 alpha | Bedrocksmp ev yapabilirsiniz ne isterseniz yapabilirsiniz |
| [[$] --- EcoCityCraft - Since 2011 --- [$]](https://www.ecocitycraft.com/economy/) | `mps.ecc.eco` | `19132` | en | 26.63 | BEDROCK PLAYERS: Join mps.ecc.eco on port 19132.  EcoCityCraft is a Minecraft economy community with history since 20... |
| [[...] HypeGO](http://shop.hypego.ru) | `hypego.ru` | `19132` | ru | 26.60 | Aucune description. |
| [02:37:39] Welcome to your server! [0/50] | `SavanaWix.minecraft.pe` | `24251` | id | 0.15.10 alpha | Welcome to SavanaWix!  Server multiplayer dari indonesia yang di khususkan untuk player mcpe/craftsman 0.14.3 × 0.15.... |
| [[ASTS]Allen跨平台插件伺服器](https://asts.tw/?lang=auto) | `mc.asts.tw` | `19132` | zh | 26.63 | Discord: https://go.asts.tw/dc |
| [block/pink_petals] Soki Network \| 1.21.4 - 26.3 [item/nether_star@items] | `play.petradox.xyz` | `19132` | id | 26.62 | Survival RPG Server with many Features! |
| [[FreeAttack] Lobby \| 0/100 online · 0 im Netzwerk](https://freeattack.net) | `freeattack.net` | `19132` | en | 26.60 | FreeAttack – dein deutscher Minecraft Bedrock Server  FreeAttack is a German-language Bedrock network with multiple s... |
| [[hud/heart/frozen_hardcore_full@gui] ʜᴇʀᴏxᴡᴀʀ [hud/heart/frozen_hardcore_full@gui] [1.8 - 26.x] [rea](https://www.heroxwar.com) | `play.heroxwar.com` | `19132` | en | 26.63 | ~~~~ ＨｅｒｏｘＷａｒ Network ~~~~   International Minecraft CROSS platform Server  Telegram: https://t.me/HeroxWar  Site: ht... |
| [[item/bone@items] FossilSMP [item/bone@items]](https://fossilsmp.de/#/) | `pe.fossilsmp.de` | `19132` | de | 26.60 | FossilSMP – Survival trifft auf die Welt der Dinosaurier!  Willkommen auf FossilSMP, einem besonderen Minecraft-SMP, ... |
| [[NFS.TW]喵喵經典生存伺服器 - 致力於台灣MCBE](https://meow.nfs.tw/) | `meow.mcbe.tw` | `19132` | ja | 1.20.30 | [NFS.TW]喵喵經典生存伺服器 - 致力於台灣MCBE  ==========【伺服器資訊】=========  《伺服器官網：http://meow.nfs.tw》  -伺服器相關資訊，贊助皆在此-  《服主》夜喵   - Fa... |
| [[NoteLand]](https://noteland.de) | `play.noteland.de` | `19132` | de | 26.60 | NoteLand.de  Minecraft Bedrock Edition Netzwerk  Dein Land für dich und deine Freunde!   Was bieten wir?  Wir betreib... |
| [OmegaServ] SkyBlock | `omegaserv.fr` | `19132` | fr | 26.60 | 🌌 L'ÉVEIL D'OMEGASERV : LA PHASE DE TEST EST LÀ ! 🌌  L'attente touche à sa fin. Prévu initialement en 2020, forgé dan... |
| [PvP Update + UI + Fast Mode6] LightWix | `lwpe.duckdns.org` | `2816` | en | 0.15.10 alpha | Welcome to LightWix!  The first ever server to have a anime based game in craftsman! Enjoy. |
| [SSMPS5] New Events Started | `Strengthsmp.okzk.com` | `10017` | en | 0.15.10 alpha | 0.14x0.15 multiversion Lifesteal server |
| [바니팜] 전체 접속자: 99명 | `bunnyf.kro.kr` | `19132` | ko | 26.60 | Minecraft MineFarm Server [BunnyFarm]  마인크래프트 마인팜 서버 바니팜입니다! |
| [_ᐅᐅᐅLongPlay.skᐊᐊᐊ_](https://longplay.sk) | `longplay.sk` | `19132` | cs | 26.51 | Pripoj sa na náš Discord a všetko sa tam dozvieš...  ale RPG Survival, ranky, čarovne chestky a množstvo iných veci ť... |
| [A Girls-Only Server](http://pin.ngel.ru) | `pin.ngel.ru` | `19132` | en | 26.45 | All girls are invited to join the ultimate community!  Unleash girls' power without any nasty or violent boys!  Towny... |
| A Minecraft Server | `mi.nodowa.lat` | `19132` | en | 26.63 | Un servidor vanilla bedrock |
| A Minecraft server | `eyyooo.joinmc.world` | `35828` | tr | 26.63 | gelmenizi öneririm çünkü kasılıyoz eyleniyoz şu an genellikle 2 kişi oynuyoruz bizim dışımızda gelen ilk kişiye hediy... |
| A Minecraft server | `stablearch.joinmc.world` | `47481` | en | 26.63 | This is vannila server. The perfect server to play on after a rough day. to avoid getting lost type /sethome at your ... |
| A Minecraft server | `skymon.joinmc.world` | `20176` | en | 26.63 | Pokemon ( cobblemon) server for minecraft bedrock |
| A Minecraft Server | `macemc.mcsh.gg` | `19132` | en | 26.63 | A mace smp inspired server for mcpe players only for better experience  Duping/X ray is allowed but using pvp cheats ... |
| A Minecraft Server | `noblesmc.xyz` | `19024` | en | Minecraft Java | Server Information  Welcome to NOBLES MC, a semi-vanilla survival server for players who enjoy a relaxed, slow-paced ... |
| A Minecraft server | `a38z23.joinmc.world` | `42068` | en | 26.63 | Aucune description. |
| [A Minecraft Server mcjp-yiynut8x8a](https://x.com/mcmenearth?s=21) | `men-earth.xgames.jp` | `19132` | en | 26.63 | # Join Men Earth!  Men Earth is a new Earth server created in October 2025.  The world is made at a 1:4000 scale, so ... |
| [A Velocity Server](https://store.melonmc.org) | `mps.melonmc.org` | `25565` | en | Minecraft Java | Discover MelonMC, a welcoming survival server built around community, creativity, and fun.  Play Minecraft the way yo... |
| ADSLabs MC Server | `bedrock.adslabs.dev` | `19132` | en | 26.63 | ADSLabs SMP: Bedrock Survival  A survival multiplayer server for Minecraft Bedrock Edition. Play from Windows, Xbox, ... |
| Advancius Network | `play.advancius.net` | `19132` | en | 26.60 | Aucune description. |
| [Advancius Network](https://www.advancius.net/) | `mc.advancius.net` | `19132` | en | 26.60 | 🌟 JOIN TODAY FOR A FREE RANK 🌟Tired of pay-to-win servers? Check out our 100+ FREE ranks on our 20+ gamemodes includi... |
| [AdventureCraft - an ocelot runs the black market](https://advcraft.gg) | `advcraft.gg` | `19132` | en | 26.45 | *** $200 BUILD CONTEST - runs until 10/31/26 ***  THEME: design our next SPAWN CASTLE + TOWN. Build it on your own cr... |
| [AetheriumNetwork 🌀 [1.8/26.3]](https://www.aetheriummc.xyz) | `play.aetheriummc.xyz` | `19132` | es | 26.51 | Welcome to **AetheriumMC Network**, where survival becomes an unforgettable adventure.  Discover a carefully crafted ... |
| [AkumaMC](https://akumamc.net/) | `bedrock.akumamc.net` | `19132` | en | 26.60 | AkumaMC - Best Minecraft Prisons, Skyblock, Survival, Gens & Cobblemon Server 2026  IP: play.akumamc.net  Discord: di... |
| [ALAGAD SMP SEASON 2](https://discord.gg/kgKeJKwxA) | `alagadsmp.ultramc.co` | `24026` | en | 26.60 | ★ A GROWING COMMUNITY • JAVA + BEDROCK ★  Economy Survival • MMORPG • Parkour • SMP • PvP  Alagad SMP is your ultimat... |
| [AlamNusa](https://store.alamnusa.net/) | `mc.alamnusa.net` | `19132` | id | 26.62 | 🍃 AlamNusa \| RPG & Adventure Server 🍃  Masuki dunia di mana petualanganmu menentukan segalanya. Hadapi bos epik, tem... |
| Altay Server | `valoriamc.eu` | `19123` | fr | 26.60 | Serveur minecraft bedrock !  Kitmap 400€ Cashprize thème tropicale !  Fondateur : Valr3nz ! |
| Altay Server | `lithium.mcbe.fr` | `19155` | fr | 26.50 | 🔹 Bienvenue sur Lithium — Un serveur Minecraft Bedrock (MCPE) unique et compétitif !   ⚔️ Plonge dans un monde PvP ra... |
| [AlteraHardcore7 \| 0.14.3 - 0.15.10](http://wa.me/6283188454152) | `altera.webhop.me` | `19148` | en |  | The anarchy- and hardcore-themed Minecraft server AlteraHardcore is perfect for you to play on. |
| [Anarchadia.org](https://anarchadia.org) | `bedrock.anarchadia.org` | `19132` | en | 26.63 | Welcome to Anarchadia – an anarchy server where Minecraft stays true to its block game roots. Established on January ... |
| [ANARCHY SURVIVAL 26.2](https://anarchy.ac) | `mc.anarchy.ac` | `19132` | en | 26.60 | Anarchy is a vanilla Minecraft server running since 23rd of June 2024, offering the ultimate freedom to play Minecraf... |
| [ANARCHY \| no queue · no rules · no resets](https://anarchy.tripletai.co.uk) | `roosevelt-decker.tun.ply.gg` | `45753` | en | 26.52 | No queue. You connect and you are in. No login queue, no whitelist, no application.  ANARCHY is a survival-anarchy se... |
| ANGELZMC \| [26.3] | `hub.angelzmc.com` | `19132` | en | 26.62 | Welcome to AngelzMC we are a new modern SMP server with a cozy chill vibe!  Relax, explore, build. A laid-back surviv... |
| [AnyCraft](https://www.anycraft.org) | `www.anycraft.org` | `19132` | en | 26.51 | Welcome to AnyCraft, a free, public, and semi-vanilla multiplayer Minecraft server available for everyone to play! Pl... |
| [Apeiron Craft • MAINTENANCE](http://discord.apeironcraft.id) | `mps.apeironcraft.id` | `19132` | id | 26.52 | Apeiron Craft: Survival santai bareng temen 🇮🇩  Server Minecraft Indonesia, host di Singapore jadi ping aman buat pem... |
| ApexMC §0\| Is on Maintainence | `ApexMC.ddns.net` | `4367` | en | 0.15.10 alpha | Join the ultimate Craftsman 0.15.10 and 0.14.3 server featuring intense LifeSteal UHC PvP, custom Clan Survival, and ... |
| [APOLOMC NETWORK \|\| 1.20.6 ▸ 1.21.+](https://shadownmc-store.tebex.io/) | `play.shadownmc.lol` | `19132` | es | 26.63 | EL MEJOR SERVER SMP con muy buena comunidad, para todo tipo de jugadores. Contamos conn nuestra modalidad estrella; S... |
| [APPLEMC [1.21+] The Fruitiest Network](https://applemc.fun/) | `play.applemc.fun` | `19132` | en | 26.63 | [Version 1.18 - 1.19] AppleMC is 1 of the largest servers that hosts major events weekly and performs daily updates. ... |
| [AppleSMP 🍎 26.1.2 \| discord.gg/applesmp](https://minecraftservers-list.com/) | `play.applesmp.org` | `19132` | en | 26.60 | Every active Java and Bedrock server, ranked by player votes and updated daily — Survival, SkyBlock, Factions, Prison... |
| [AQUALAND \| 26.50+ \| play.u3002.com](http://aqualand.u3002.com) | `play.u3002.com` | `19132` | en | 26.63 | Aqualand is a simple cross platform survival server  < Basic rules >  - Respect Others. Respect Yourself.  - Do not G... |
| [ArabSkills](http://www.arabskills.net) | `arabskills.net` | `19132` | en | 26.60 | 🎮 Step into ArabSkills Network, the ultimate Arabic Minecraft experience!  Join one of the fastest-growing communitie... |
| [ARC Server](https://atherices.com) | `play.atherices.com` | `19132` | tr | 26.60 | SkyBlock and more! |
| [ARCANE REALMS •*❆ ᴅɪsᴄᴏʀᴅ.ɢɢ/ᴀʀᴄᴀɴᴇʀᴇᴀʟᴍs 🗡](https://arcane-realms.org) | `bedrock.arcane-realms.org` | `50944` | en | 26.60 | Arcane Realms is a premier multi-gamemode Minecraft network built for both casual adventurers and competitive players... |
| [Arden Network \| 1.21.x - Latest](https://store.ardennetwork.net/) | `play.ardennetwork.net` | `19132` | id | 26.60 | Aucune description. |
| Arona Network | `arona.asia` | `19132` | en | 26.60 | Minecraft Bedrock PvP Practice Server located in China  Focused on Duels, FFA, and competitive PvP gameplay.  Train y... |
| Asagiri Realms | `asagirirealms.mcserver.us` | `19132` | en | 26.52 | Welcome to Asagiri Realms — a modded Bedrock survival server for explorers, builders, and boss hunters.  Jump into an... |
| AsiaPots | `asiapots.club` | `19132` | en | 26.50 | Best PotPvP server for Asian |
| [Asteron SMP](http://overclocksmp.com) | `play.overclocksmp.com` | `19132` | en | 26.60 | A minecraft bedrock public economy server using Blurry's Java PvP. Team with other players and become the richest pla... |
| [Astra 0.14x - 0.15x Mantenimiento!](http://astramcpe.vercel.app) | `astramcpe.sytes.net` | `19132` | en | 0.15.10 alpha | Server 24/7 Minigames & PvP |
| [AstroNovaMC » Halloween • 31/10 alle 21: giveaway!](https://astronovamc.it) | `play.astronovamc.it` | `19132` | it | 26.60 | AstroNova MC è un server Minecraft italiano a tema cosmico. Java e Bedrock entrano sullo stesso indirizzo: play.astro... |
| [AT Hub Server](https://at-hub.net) | `play.at-hub.net` | `19132` | en | 26.60 | A Minecraft Bedrock server that brings together building, exploration, and competition within a welcoming community f... |
| [AtlantikMC](https://atlantikmc.com) | `oyna.atlantikmc.com.tr` | `19132` | pt | 26.63 | AtlantikMC, Gelişmiş Sistemlere sahip bir Survival sunucusudur.  Bedrock (Mobil) giriş mevcuttur.  IP: oyna.atlantikm... |
| [Aussie Gamers MC](https://aussiegamers.com.au/) | `play.aussiegamers.com.au` | `19132` | en | 26.60 | G'day, mate! Come build with us.  Aussie Gamers MC is a cozy, community-run network hosted in Sydney, so Aussie and K... |
| [Avenian Network - YouTuber Slimefun Modded SMP](https://jaystechvault.craftingstore.net/) | `avn.gg` | `19132` | en | 26.60 | Just a Survival SMP with an Economy.  Youtube: youtube.com/c/Avient  Rank store: https://jaystechvault.craftingstore.... |
| [Avenian Network - YouTuber Slimefun Modded SMP](https://jaystechvault.craftingstore.net/) | `play.jaystechvault.com` | `19132` | en | 26.60 | Just a Survival SMP with an Economy.  Youtube: youtube.com/c/Avient  Rank store: https://jaystechvault.craftingstore.... |
| Axolotl-PM Server | `foxymc.de` | `19132` | en | 26.60 | FoxyMC is a brandnew Minecraft Bedrock server currently in beta - join now and be part of our community!  Dive into A... |
| Azure Craft \| Solo Crafteling \| MineKart | `play.herozdev.net` | `19132` | en | 26.63 | Heroz Network is three gamemodes built from scratch, each with custom 3D models, animations and its own resource pack... |
| [BagelSMP.com](https://bagelsmp.com/?ip=mps) | `mps.bagelsmp.com` | `19132` | en | 26.63 | BagelSMP is a competitive Minecraft server where you grind for loot and fight other players to climb to the top. Join... |
| [Bagelton Network - 1.8+ - Minecraft Tuesdays!](http://bagelton.com) | `bagelton.com` | `19132` | en | 26.62 | The Bagelton Network is a server that me and some friends have been working on with creative, minigames, survival, an... |
| BakaCrew Server | `baka.skyes.me` | `19205` | en | 26.61 | Looking for the ultimate Bedrock survival experience to call home?  Born in Malaysia and built for Bedrock players ev... |
| [Balikbayan SMP \| 1.21.11+ \| Season 2](https://discord.gg/hZSqUQ7VYc) | `balikbayan.minecraft.best` | `19132` | en | 26.60 | Our server aims to be a peaceful place to unwind after a long day at school or work—a world where you can relax, have... |
| [BananaSMP](https://store.blockfun.gg/) | `play.blockfun.store` | `19132` | en | 26.60 | Blockfun is a brand new SMP Network! We plan on becoming a one-stop network for all and any SMP gameplay desires! Her... |
| [BARASMP \| ECONOMIC PVP SURVIVAL](http://store.barasmp.my.id) | `be.barasmp.my.id` | `443` | id | 26.51 | Selamat datang di BARASMP, server Minecraft Survival EcoPVP terbaik dengan gameplay kompetitif dan ekonomi yang dinamis! |
| [BCraft](https://bcraft.cl) | `jugar.bcraft.cl` | `19132` | es | 26.62 | ¡Aventura, libertad y diversión te esperan en BCraft! Explora un mundo lleno de posibilidades, construye tu hogar, pr... |
| Bedrock Anarquia | `gaming-11.bedhosting.com.br` | `25028` | pt-BR | 26.61 | Servidor brasileiro de anarquia pura. Não a regras de duplicações do Item nem de chat pvp livre e destruição também. ... |
| [Bedrock Dedicated Server](https://suprenium.fr/) | `gm6.lordhosting.fr` | `19152` | fr | 26.60 | gfd |
| [Bedrock Dedicated Server](https://linktr.ee/HoshinoSMP) | `basic-1.alstore.space` | `25631` | en | 26.61 | Minecraft Server! Server Theme : Economy & Anarchy  Theme The Season :  1. Season 1 = RPG 🎆  2. Season 2 = Modern 🏦  ... |
| Bedrock Dedicated Server | `moonveilmc.my.id` | `19258` | en | 26.61 | MoonveilMC is an Indonesian survival server with a unique and fun gameplay experience.  Enjoy custom enchantments, ec... |
| [Bedrock Dedicated Server](https://chat.whatsapp.com/BtkV2gBlO4CJJRyvT6evtQ?s=cl&p=a&mlu=4&amv=0) | `play.jawanese.xyz` | `19132` | id | 26.52 | Server minecraft bedrock bertemakan Ekonomi Anarkis dengan fitur simpel dan mudah cocok untuk pemula |
| [Bedrock Dedicated Server](https://discord.gg/mtnAkbWMZ) | `51.81.107.169` | `25937` | es | 26.61 | 🔌Nueva IP De TheArcadeLand🛠️  -------------------------------------------------  🙌Les presentamos TheArcadeLand✨  Ali... |
| Bedrock Dedicated Server | `51.81.243.191` | `25605` | en | 26.61 | Fire SMP is professional server added by MrFireBoii plugin beacon plugin common strike plugin |
| Bedrock Dedicated Server | `hcm-1.heppycloud.id` | `25581` | id | 26.52 | SURVIVAL VANILLA SERVER |
| [Bedrock Dedicated Server](http://Google.com) | `bsc-4.aerocloud.id` | `19267` | id | 26.51 | Hai nma gua ikhwan |
| [Bedrock Dedicated Server](http://sawitanarchy.netlify.app) | `prem-1.aerocloud.id` | `19235` | id | 26.52 | Server anarchy bedrock only |
| Bedrock Dedicated Server | `170.23.68.71` | `25593` | en | 26.52 | Welcome to **KineticSMP**! We offer a unique survival experience packed with custom features including clans, pets, a... |
| Bedrock Dedicated Server | `aeternus.hopto.org` | `25756` | pt-BR | 26.61 | RPG Sobrevivência e PvP, escolha uma raça e uma classe,  MCPE 0.15x  IP: aeternus.hopto.org  Porta: 25756 |
| Bedrock Dedicated Server | `15.235.86.66` | `25573` | en | 26.60 | 🌍✨ PxCraft Bedrock Server ✨🌍  Welcome to PxCraft, a friendly Bedrock Server built for people who love playing togethe... |
| [Bedrock Dedicated Server](https://discord.gg/EQjjXjzZG) | `shulker.wardenservers.com` | `27641` | es | 26.51 | Un servidor con buen hosting y una buena comunidad |
| Bedrock Dedicated Server | `49.12.82.39` | `25711` | en | 26.61 | For Free OP Join This Server |
| Bedrock Dedicated Server | `uriel.minecraftindo.my.id` | `21031` | id | 26.52 | *URIEL SMP*  minecraft bedrock smp bertema lifesteal, rame ramein ja tampung sampe 40 player, ajak temen" klen semua ... |
| Bedrock Dedicated Server | `138.201.48.55` | `25720` | en | 26.62 | A server support minecraft/mastercraft/craftman 0.14.x/0.15.x   The server is fun and you can play with your friends. |
| Bedrock Dedicated Server | `185.29.166.242` | `25000` | en | 26.62 | Amazing server |
| Bedrock Dedicated Server | `basic-8.alstore.space` | `23047` | en | 26.61 | Anarchy, total freedom for every individual |
| [Bedrock Dedicated Server](http://www.mabaryukk.my.id) | `Play.mabaryukk.my.id` | `25551` | id | 26.61 | Server semi vanilla Indonesia |
| [Bedrock Dedicated Server](https://discord.gg/extaliafr) | `extalia.mcbe.fr` | `19132` | fr | 26.52 | # ✨ **__ Extalia - Kitmap ! __** ✨  ═══════════════════  > Extalia un KitMap pas comme les autres qui redéfinit Minec... |
| [Bedrock Zenvairo](https://skycloud.es) | `mc.skycloud.es` | `19132` | es | 26.63 | Una network en español ideal para:  - Jugar a las aventuras en solitario o acompañado: Tenemos varios modos de juego ... |
| [bedrock.6b6t.org](https://www.6b6t.org) | `bedrock.6b6t.org` | `19132` | en | 26.60 | 6b6t is a Minecraft anarchy server with no rules, where over 150 players come daily to play, build, raid, and explore... |
| [BEDROCKIA • Creative RPG](https://bedrockia.net) | `bedrockia.net` | `19132` | de | 26.62 | # Bedrockia – Erbaue eine gemeinsame Welt  Bedrockia ist ein deutschsprachiger Minecraft-Server für kreative Spieler,... |
| [BEDWARS &amp; NEW GAME!](https://www.cubecraft.net/) | `play.cubecraft.net` | `19132` | en | 26.60 | CubeCraft Games is one of the largest and longest-running Minecraft networks, offering a wide selection of multiplaye... |
| [BerrySMP](https://store.berrysmp.net) | `pe.berrysmp.net` | `19132` | en | 26.60 | Welcome to BerrySMP!  Our community is super friendly and we all love to play on BerrySMP: a java + bedrock crossplay... |
| [Betafied - Beta 1.7.3](https://www.betafied.net) | `play.betafied.net` | `19132` | en | 26.60 | BETAFIED: MINECRAFT BETA 1.7.3 FOR BEDROCK  Betafied brings Minecraft Java Beta 1.7.3 gameplay to Bedrock Edition.  C... |
| [Bienvenue sur CraftyWorld !](https://craftyworld.fr) | `play.craftyworld.fr` | `19132` | fr | 26.62 | Nous vous souhaitons la bienvenue sur CraftyWorld !  Depuis 2015, CraftyWorld a vécu en tant que serveur PvP-Factions... |
| BillionLanDD Is BACK! | `BillionLandDD.ddns.net` | `7144` | en | 0.15.10 alpha | Join = Powerfully |
| BlauMC.de | `blaumc.de` | `1032` | de | 26.51 | 💙 Willkommen bei BlauMC.de!  BlauMC ist ein Minecraft-Netzwerk für Java & Bedrock, das aktuell weiter ausgebaut wird.... |
| [BlindMC.fun ⚑](http://store.blindmc.fun) | `blindmc.fun` | `2083` | en | 26.51 | Blind MC Is The Best Nepali Minecraft Server With Lifesteal & Economy. Go Join & Enjoy. This Server is going to chang... |
| [Blocktopia \| O melhor servidor da América Latina!](http://linktr.ee/mineportal) | `jugar.blocktopiamp.com` | `19132` | es | 26.60 | Bienvenidos a Blocktopia, nos caracterizamos por ser un servidor vanilla con plugins, ítems, lore y eventos exclusivo... |
| [Blocktopia \| O melhor servidor da América Latina!](http://linktr.ee/mineportal) | `jogar.blocktopiamp.com` | `19132` | pt-BR | 26.60 | Bem-vindo ao Blocktopia! Somos conhecidos por ser um servidor vanilla+ com plugins, itens exclusivos, lore envolvente... |
| [Bloom Prisons](https://bloomprisons.buycraft.net/) | `bloomprisons.net` | `19132` | en | 26.60 | **Bloom Prisons** is a **Minecraft Bedrock Edition ONLY** prisons server. Bloom brings back the **classic prisons exp... |
| BLOSSOMCRAFT &gt;&gt; Grief Protected [26.2+] | `play.BlossomCraft.org` | `19132` | en | 26.63 | A mini restoration program in conjunction with building the brand allows you to reduce commissions or limitations. Th... |
| [BLURKIT 》 ENTRA YA!](https://www.blurkit.net/) | `bedrock.blurkit.net` | `19132` | es | 26.63 | Blurkit es un Servidor de Minecraft que durante años nos hemos esforzado por brindar una buena experiencia a todos aq... |
| [BLUXMANN.COM](http://bluxmann.com) | `bluxmann.com` | `19132` | en | 26.52 | Shane and I are excited to share that we’ve set up a Bedrock Minecraft server just for our kids! This new server is a... |
| BOXPVP » SKYBLOCK | `play.adacraft.net` | `25828` | tr | 26.51 | ADACRAFT - SMP   [i]Sınırsız özgürlük, tam kontrol, ticaret ve rekket  🔥 Sunucu Özellikleri:  · 🎮 Özel SMP Sistemleri... |
| [BP »BedWars«](https://t.me/blockparty_pe) | `block-party.ru` | `19132` | en | 0.14.3 alpha | Do you like variety?Then this server is for you.  We have the following mini games:  BedWars, BlockParty, SpeedBuilde... |
| [BrasilCraftPE](http://www.brasilcraft.net) | `jogarbrasilcraft.com` | `19132` | pt-BR | 26.60 | 🔴▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔴 🌺 BrasilCraft 🌺 🔴▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔴  🌟 IP: jogarbrasilcraft.com  🌟 Versão do servidor: 1.8x - 26.2x... |
| [BREEZE SMP [26.3]](https://store.breezesmp.com) | `mps.breezesmp.com` | `19132` | en | 26.60 | [BEDROCK SUPPORT] Welcome to Breeze SMP! We are a BRAND NEW SERVER and offer a fun 1.21 Survival experience for all t... |
| [BRIZA : 0.14x 0.15x New Update #Briza](https://dsc.gg/briza) | `BrizaSky.sytes.net` | `26033` | pt-BR | 0.15.10 alpha | A BrizaSky está de volta!! 🚀🔥🎉 |
| [BROTHEHHEHEHHER](https://discord.com/invite/hyperthebandit) | `hyperthebandit.online` | `22515` | en | 26.52 | hyperthebandit.online  Welcome to HyperTheBandit SMP, a community-driven Minecraft Survival server built for players ... |
| [Building Zone - 04](http://buildzone.lol) | `play.buildzone.lol` | `25903` | ru | 1.21.50 | На связи Окси   Сегодня хочу представить вам сервер Building Zone - место, где встречается красота построек и вдохнов... |
| [BURST UPDATE NEW LOBBY SW RANKED](https://burst-network.vercel.app/) | `Burst.ddns.net` | `25590` | tr | 0.15.10 alpha | Olá jogadores da Burst Network! 🎮🔥  Viemos informar a vocês sobre a nova atualização da Burst Network, trazendo muita... |
| [CarrotMC LifeSteal](https://lemehost.com) | `15.235.173.7` | `13974` | en | 0.15.10 alpha | THE LIFESTEAL SERVER FOR MCPE 0.14.3 0.15.10. IP 15.235.173.7 PORT 13964  Have Economy Lifesteal PvP And Many More |
| [CASHPIRE SMP \| ECONOMY &amp; SURVIVAL [1.21.11]](https://cashpiresmp.net/) | `cashpiresmp.usga.me` | `19167` | en | 26.52 | ⚔️ Welcome to Cashpire SMP: Build Your Kingdom. Claim Your Glory. ⚔️  Join an active community of 50+ players every d... |
| CastCraft | `castcraft.duckdns.org` | `28738` | en | 26.61 | An anarchy server for Minecraft Bedrock, frequently updated to the newest versions. |
| [CATCRAFT SURVIVAL [26.3] Join our discord](https://catcraft.net) | `bedrock.catcraft.net` | `19132` | en | 26.60 | 🌟Welcome to CatCraft! Enjoy instant tree chopping🌳 & veinmining ores⛏️, engage in a player-driven diamond economy💎, a... |
| [CELESTIA KITMAP !](http://celestiamc.fr) | `play.celestiamc.fr` | `19132` | fr | 26.60 | Célestia KitMap V1 |
| [CeresMC Minigames](http://ceresmc.com.br) | `ceresmc.com.br` | `19132` | pt-BR | 26.60 | 🌟 CeresMC — Servidor Brasileiro de Minecraft Bedrock Edition 🌟  Seja bem-vindo ao CeresMC, um servidor feito para que... |
| [ChampionsMC S1](https://championsmc.us) | `play.championsmc.us` | `19132` | en | 26.50 | Welcome to the ChampionsMC Network!  The network revolves around Minecraft, and consists of many social media platfor... |
| [CHEESE LEGACY](https://cheeselegacy.craftingstore.net) | `cheeselegacy.ultramc.co` | `19013` | en | 26.60 | Cheese Legacy  After a long break, Cheese Legacy is now open. Get ready for new adventures, fresh builds, and chaos. ... |
| [Cherry Blossom!](https://discord.gg/JkVmvn54CS) | `cherryblossom.apexmc.co` | `25582` | en | 26.20 | 🌸 Cherry Blossom 🌸 is a family friendly(PG) server that was created to give players a feeling of progression and acco... |
| Chiseled Guardian | `play.precisionrtk.uk` | `25575` | en | 26.33 | BattleCore  The Ultimate Military Survival, PvP & Territory Warfare Experience  BattleCore is a next-generation Minec... |
| [ChocoHills \| 1.21+](https://chocohills.com) | `play.chocohills.com` | `19132` | en | 26.62 | Aucune description. |
| [CHRONOS SMP \| CROSSPLAY SERVER](https://caldronsmp.online) | `play.caldronsmp.online` | `19132` | id | 26.51 | Aucune description. |
| [Civilization](https://wasteland7912.uk/apply/play?utm_source=minecraftpocket&utm_medium=listing&utm_campaign=free_20261019) | `minecraft.wasteland7912.uk` | `19132` | en | 26.62 | Join for free right now — no sign-up required! Civilization is a Hard Survival server for Minecraft Bedrock with an i... |
| [CJSV - Hardcore](https://cjsv.tebex.io) | `paloma.hidencloud.com` | `24655` | es | 26.60 | 🌟EL NUEVO SERVIDOR SURVIVAL HARDCORE EXTREMO QUE ESTABAS ESPERANDO! 🌟  ¿Buscas una nueva aventura épica? ¡Únete hoy m... |
| CL0CKER | `cl0cker.jp` | `19132` | ja | 26.60 | A Simple PvP Practice Server. |
| [Clarity Network ( 1.21.11 - 26.3 )](https://store.clarity-id.net/) | `play.clarity-id.net` | `19132` | id | 26.60 | Aucune description. |
| [ClarityMC Network [1.8.x \| 1.21.x]](https://claritymc.net) | `play.claritymc.net` | `19132` | es | 26.60 | ⚔️ CLARITYMC NETWORK · Servidor de Minecraft Bedrock y Java en español (LATAM)  ¡Juega desde el CELULAR, consola o PC... |
| [Clary MC Factions](https://tienda-clarymc.tebex.io/) | `clarymc.xyz` | `19132` | es | 26.60 | ──────────═─━✧❀✧━─═──────────  # ClaryMc Factions  # ¿Qué ofrecemos?  > ➤ Soporte  > ➤ Alianzas  > ➤ Staffs no corrup... |
| [CloneArmyMC: Star Wars RP!](http://clonearmymc.net) | `play.clonearmymc.net` | `19132` | en | 26.60 | Clone Army MC is a Star Wars Minecraft Bedrock Edition server where players can join the Clone Army and become a clon... |
| CLOUDMC NETWORK \| [PC-PE] | `pe.cloudsmp.asia` | `19132` | vi | 26.60 | Server Smp viet nam tuyet voi |
| [CoastalMC Bedrock Network](https://coastalmc.org) | `play.coastalmc.org` | `25727` | en | 26.60 | Coastal Network  A Minecraft Network Built for the Community.  Welcome to Coastal Network, a Minecraft Bedrock networ... |
| [Cobblemon Bedrock](https://cobblemonbedrock.com) | `play.cobblemonbedrock.com` | `19132` | en | 26.60 | Cobblemon for Bedrock and Java players: catch, train and battle Pokémon together!  Note: This is not a Bedrock port. ... |
| CobraSMP | `play.cobrasmp.com` | `25632` | tr | 26.52 | SMP Voting Site Beschrijving  Welkom op de ultieme SMP server voor zowel Java als Bedrock spelers!  Onze server biedt... |
| [Collapse](https://collapsemc.com/) | `clps.gg` | `19132` | ru | 26.60 | Collapse Practice — Твое главное место для PvP в Minecraft Bedrock!  Ищешь сервер с отзывчивой регистрацией ударов, к... |
| [COOKIE BUILD • Java + Bedrock](https://www.cookie-build.com) | `pe.cookie-build.com` | `19132` | en | 26.60 | Cookie Build is a Minecraft Pocket Edition minigame server. There is only SkyWars, MicroBattles, Build Battle and Tur... |
| CopperKeep \| Now Open | `play.copperkeep.org` | `25565` | en | 26.51 | Welcome to CopperKeep SMP, a survival server built around farming, building, and a community that sticks together. We... |
| Corenetwork By CorethonnCorethon Is Real | `bgr-1.anjas.id` | `30093` | id | 26.52 | Aucune description. |
| [CosmicPE - Factions, PvP, and Events](https://shop.cosmicpe.me) | `play.cosmicpe.me` | `19132` | en | 26.60 | CosmicPE is a space-age Minecraft: Bedrock Edition Factions server that has lived amongst the stars for the past 5-6 ... |
| [CosmicX.net 「26.3」](https://cosmicx.net) | `play.cosmicx.net` | `19132` | en | 26.63 | 🌟 Welcome to CosmicX🌟  CosmicX is the perfect server for builders who want complete freedom and no limits getting in ... |
| CouldedSMP :: 0.14.x-0.15.10 | `51.81.107.169` | `25947` | en | 0.15.10 alpha | Aucune description. |
| CowsSMP | `cows.info.gf` | `19132` | en | 26.33 | 🐄 The Moo-st Vanilla Survival Server  Pure vanilla survival Minecraft — no mods, no plugins, no udder nonsense. Just ... |
| [Cozy Realms 1.21](https://store.cozyrealms.us/) | `play.cozyrealms.us` | `19132` | en | 26.60 | 🌟 A peaceful, relaxing, and chill place to play Minecraft! Cozy Realms is a family-friendly survival server where pla... |
| [CrabSMP \| Season X \| v26.60](https://crabsmp.net/) | `play.crabsmp.net` | `19132` | en | 26.60 | CrabSMP is a Minecraft Bedrock server built for players who want proper combat, real events and none of the usual ser... |
| [Craftadia Survival → Version 26.3](https://www.cusl.net) | `mci.craftadia.com` | `19132` | en | 26.62 | Casino utan svensk licens erbjuder flera fördelar för spelare som letar efter alternativ utanför den svenska reglerin... |
| [Craftale Network](https://craftalemc.com/) | `oyna.craftalemc.com` | `19132` | tr | 26.60 | Aucune description. |
| [Craftale \| Skyblock](https://discord.gg/g934gXnd2E) | `oyna.zeusnw.tr` | `19132` | tr | 26.60 | 🚀 Zeus Network, Türkiyedeki tek ThePit sunucusudur, herkesi bekleriz! |
| [CRAFTAVIA 1.15.2 - 26.3](https://turkskyblock.com) | `play.turkskyblock.com` | `19132` | en | 26.63 | TürkSkyblock, gökyüzündeki küçük bir adadan başlayıp kendi ekonomini kurduğun Türkçe bir Minecraft Skyblock sunucusud... |
| CRAFTAVIA 1.15.2 - 26.3 | `play.turkskyblock.net` | `19132` | en | 26.63 | TurkSkyblock Network, etkinliği bol bir Türkçe Skyblock sunucusudur. Bilgisayardan Java ile, telefondan ya da konsold... |
| CRAFTAVIA 1.15.2 - 26.3 | `play.skyblocktr.com` | `19132` | en | 26.63 | SkyblockTR, Skyblock'a yeni başlayanların da rahatça ilerleyebildiği Türkçe bir sunucudur. Kurallar, menüler ve tüm s... |
| [CRAFTAVIA 1.15.2 - 26.3](https://craftavia.net/) | `play.craftavia.net` | `19132` | tr | 26.63 | Craftavia: Türk Minecraft Sunucusu \| SMP, Towny, Skyblock, BoxPvP, Practice  Craftavia, Java ve Bedrock oyuncularını... |
| [CraftersMC ✧ SkyBlock: End § Beyond!](https://craftersmc.net) | `play.craftersmc.net` | `19132` | en | 26.60 | Explore an MMO SkyBlock server full of adventure. Start your journey now on Minecraft: Bedrock Edition!  ⛰ CraftersMC... |
| [CrafterWix : Season: 6 : 0.15 - 0.14 : MiniGames + Survival + PvpModes](http://CrafterWix/s7) | `5.39.63.207` | `6914` | en | 0.15.10 alpha | CrafterWix S7 Owner Dev_GamerYT_11 , YouTube @DevMCPE11 , Discord DevMCPE11 , Instagram DevShakya.official , CrafterW... |
| CrafterWix : Season: 6 : 0.15 - 0.14 : MiniGames + Survival + PvpModes | `CrafterWix.ddns.net` | `6914` | en | 0.15.10 alpha | CrafterWix S7 Owner Dev_GamerYT_11 , YouTube @DevMCPE11 , Discord DevMCPE11 , Instagram DevShakya.official , CrafterW... |
| [CRAFTPORTAL](https://craftportal.net) | `pe.craftportal.net` | `2003` | de | 26.60 | Deine ZUKUNFT beginnt mit EINEM Block!  Seit 2022 steht Craftportal für ein einzigartiges Spielerlebnis, das Kreativi... |
| [CraftyMC](https://www.craftymc.bond/) | `play.craftymc.bond` | `45794` | en | 1.21.100 | 📌 SERVER INFORMATION  Super excited to drop this here. If you're tryna find a wild, fast-paced survival server to gri... |
| [CRBE](http://Cristalix.PE) | `cristalix.pe` | `19132` | ru | 26.60 | Aucune description. |
| [CreateCraft.EU - Network [1.21.9 - 26.3]](https://www.createcraft.eu) | `pe.createcraft.eu` | `19132` | de | 26.60 | 🔥 CreateCraft.eu – Dein neues Minecraft Zuhause! 🔥  ❗ NEU: Battlepass jetzt LIVE auf Citybuild ❗  ⚡ Starte JETZT dein... |
| [CreateMineRepeat \| 1.26.51 vanilla · /go\|/server hub\|survival\|plots\|pvp\|jeu1-4 \| Script API cmr_bp ·](https://createminerepeat.com) | `createminerepeat.playit.plus` | `3223` | en | 26.50 | 🌙 CreateMineRepeat — a server for Minecraft (Bedrock)  A server from Québec, run by a team in Montréal. A dark, alway... |
| CrownSMP : 24/7 Best Lifesteal SMP | `5.39.63.207` | `2943` | en | 0.15.10 alpha | U Can Play Here This Server Has Anti Hitbox, And Many More Plugins, U Can Be Staff Also In Our Dc Server, Link Is In ... |
| [CrypticMC.org](https://crypticmc.org) | `bedrock.crypticmc.org` | `19132` | en | 26.60 | CrypticMC is a long-term Minecraft survival server with a world that never resets. No land claims, no rollbacks, and ... |
| [Cubaris](http://www.cubaris.net) | `Cubaris.net` | `19132` | en | 26.60 | 🇩🇪 🌐 Willkommen auf Cubaris.net! 🌐  Trete noch heute dem Cubaris Netzwerk bei. Mit bereits hunderten registrierten Sp... |
| [Cubix-Transfer](https://discord.gg/hydramc) | `cubixstudio.eu` | `19132` | fr | 26.60 | Transfering platform, like BCMain  UseFull transfering platform, while adding "StudioCubix" as friends |
| [Currently under maintenance](https://arcantianet.work) | `bedrock.arcantianet.work` | `443` | en | 26.51 | Arcantia Network is a Minecraft Java Crossplay Server that specialized in Economy and SlimeFun. Any Java player or Be... |
| Currently under maintenance | `play.voidryn.in` | `25568` | en | 26.51 | Voidryn Survival is a balanced Minecraft server with events, rewards, and a friendly community. Build, explore, and s... |
| [Currently under maintenance](https://relxmc.com/) | `be.relxmc.com` | `19132` | id | 26.60 | Aucune description. |
| [DAEDRIC \| [26.3]](https://daedric.gg) | `br.daedric.gg` | `19132` | en | 26.62 | Discover Daedric, a Minecraft: Java and Bedrock Survival server where your adventure begins.  Explore a world full of... |
| Darguns Dungeon | `74.112.77.132` | `1035` | en | 26.61 | Darguns Dungeon is a massive Minecraft Bedrock RPG adventure that combines the freedom and exploration of The Elder S... |
| [DarkGames Network](http://darkgames.club) | `play.darkgames.club` | `19132` | es | 26.50 | ¡Tu próxima aventura comienza aquí! Explora nuestros modos, juega con amigos y construye tu historia.  🌳 Survival: cr... |
| Darkholm - PVP Factions | `bedrock.darkholm.live` | `8178` | en | 26.63 | Welcome to Darkholm, a medieval Factions realm of raids, rivals and riches.  Everything you own is earned out in the ... |
| [dcfac.net](https://discord.gg/4ryeb2DTvA) | `dcfac.net` | `19132` | en | 26.50 | Server based around Minecraft (Bedrock Edition) Network such as OP Factions and other upcoming gamemode(s) with Compe... |
| [Deadland](https://www.deadland.org) | `mps.deadland.org` | `19132` | fr | 26.60 | Aucune description. |
| Deadray | `deadray.org` | `19132` | en | 26.60 | Small community-based survival server running the same map since at least 2016.  Join us on Discord |
| DEADZONEV2 | `play.deadzone.online` | `19132` | fr | 26.60 | ☣️ DEADZONE V2 ​☣️  Survivras-tu ?  ​Plonge dans un univers post-apocalyptique impitoyable sur Minecraft Bedrock.  ​🧟... |
| DeathZone | `deathzone.mcsrvr.online` | `25842` | en | 26.61 | Zombie Apocalypse Server |
| Dedicated Server | `diwie.dynv6.net` | `19132` | de | 26.52 | Aucune description. |
| [Dedicated Server](https://www.citysim.top/PHP/) | `citysim.top` | `19134` | en | 26.60 | The most professional social simulation server |
| [Dedicated Server](https://lemon-slime.com) | `play.lemon-slime.com` | `19132` | en | 26.52 | Crafter's Guild is a one-of-a-kind Minecraft: Bedrock Edition server founded on a simple, powerful idea: what if the ... |
| [Dedicated Server](https://web.nemicorp.space/) | `smp.triggeredhosts.space` | `9257` | en | 26.51 | JOIN LEAF SMP for Bedrock only gameplay naive support !   includes some quality of life mods |
| Dedicated Server | `nasty-god.duckdns.org` | `19132` | en | 26.45 | Smp.pvp.rpg |
| Dedicated Server | `88.211.228.204` | `25648` | en | 26.63 | BRAND NEW SMP!! END PORTAL OPENING 05/09/2026  JOIN DISCORD BEFORE JOINING SERVER - QeXEgmq8y   PVP AND ECONOMY SERVE... |
| [Dedicated Server](https://wiki.pantrysrealm.net) | `pantrysrealm.net` | `19132` | en | 26.60 | pantry's realm is a semi-vanilla Minecraft Bedrock survival server with achievements on, Hard mode, and a true foreve... |
| Dedicated Server | `play.ghostbedrockserver.com` | `19132` | en | 26.52 | minecraft bedrock with addons and maybe plugins lol   sorry for banner it ai gen because im not good with art stuff a... |
| Dedicated Server | `cairo-organisers.tun.ply.gg` | `47903` | en | 26.52 | ⚔️ Welcome to Stacia ⚔️  Stacia is a progressive dark-fantasy MMORPG built entirely for Minecraft Bedrock! Step into ... |
| Dedicated Server | `Battlescape.mc.gg` | `25565` | en | 26.63 | A KitPvP where every Kit is uniquely created and balanced- each of which have special abilities and promote using a s... |
| Dedicated Server | `198.89.99.144` | `10522` | pt-BR | 26.61 | 🌍 Bem-vindo ao nosso servidor Minecraft!  ⚔️ Uma pequena comunidade, grandes aventuras!  Aqui, cada jogador faz parte... |
| Dedicated Server | `townsendtv.com` | `20004` | en | 1.21.30 | Vanilla survival no rules with hard difficulty. |
| DEEP DIVE – Can you set the record? | `arrowwars.dk` | `10015` | en | 26.52 | Limited oxygen. Infinite depth. Can you set the record?  You wake up on a tiny deserted island with nothing but the o... |
| Demo | `simplesurvival.duckdns.org` | `19133` | en | 0.8.1 alpha | A survival server hosted on MCPE 0.8.1 that uses plugins to simulate an infinite world like newer versions of minecra... |
| [Demo](https://alphastone-mcpe.github.io/) | `alphastone.ddns.net` | `19132` | en | 0.8.1 alpha | AlphaStone is a vanilla server for playing on the old version of Minecraft PE Alpha 0.9.5.  We aim to preserve the at... |
| [Demo](https://nostalgiape.ddns.net/) | `nostalgiape.ddns.net` | `19132` | en | 0.8.1 alpha | NostalgiaPE Classic — a unique server on Minecraft PE Alpha 0.8.1, recreating the atmosphere of 2013. Old world, plug... |
| [Demo](http://thouthmine.ru) | `play.thouthmine.ru` | `19132` | en |  | Thouthmine takes you back to a world where every adventure begins with the first tree you chop down. Build a place to... |
| [Demo](https://worldpe.rf.gd) | `worldpe.ddns.net` | `19132` | en | 0.8.1 alpha | A server on which you can fight, survive, feel nostalgic and much more! Come on in, it's always fun here! |
| [DEMOCRAFT](https://democraft/fr) | `play.democraft.fr` | `19132` | fr | 26.63 | DEMOCRAFT - Mini Jeux Java & Bedrock !  Vous cherchez un serveur Minecraft amusant et convivial pour jouer avec vos a... |
| [DemonHCF Network » HCF](https://discord.gg/demonhcf) | `play.demonhcf.rip` | `19132` | en | 26.60 | Server HCF Minecraft bedrock. |
| [diamondbyte.org Server Network](https://diamondbyte.org/servers/) | `server.diamondbyte.org` | `19132` | en | 26.51 | Aucune description. |
| Dincraft - Siden 2014 | `mc.Dincraft.no` | `19132` | tr | 26.52 | This is a Norwegian Minecraft server where we mostly speak Norwegian. We do welcome our international friends but kee... |
| [discord.bobbacraft.net](https://www.bobbacraft.net) | `jogar.bobbacraft.net` | `19132` | pt-BR | 26.60 | O Bobbacraft é um servidor de Minecraft brasileiro focado em survival multiplayer (SMP), com estilo semi-vanilla e co... |
| [discord.dqanarquia.com](https://www.dqanarquia.com) | `dqanarquia.com` | `19132` | pt-BR | 26.60 | O DQAnarquia é um servidor de Minecraft anárquico brasileiro para Java e Bedrock, em atividade desde 2022.  A propost... |
| [discord.gg/lifeblock](https://shop.lifeblock.network) | `lifeblock.network` | `19132` | en | 1.21.100 | Lifeblock Network   We are a Minecraft Bedrock Edition Network featuring our newly released gamemode Apocalypse and P... |
| [DM Летний Вайп \|](https://doshik.trademc.org) | `play.doshik.ru` | `19132` | ru | 26.60 | Грифер сервер для MCPE |
| [DMZ SMP SEASON 2](https://dmzsmp.netlify.app/) | `dmzsmp.playwithbao.com` | `36824` | en | 26.61 | This is a semi anarchy server that simulates hardcore mode and has been around for 2 years! Join up! |
| [DonutSMP.net](https://store.donutsmp.net/) | `DonutSMP.net` | `19132` | en | 26.63 | DonutSMP is one of the largest and most popular Minecraft Bedrock servers, a crossplay network with Skyblock, Prison,... |
| Dragon SMP! New plugin THOR AXE | `premiumplay.niverahosting.de5.net` | `1402` | en | 0.15.10 alpha | Ye server bohot acha hai aur owners is ko aur acha bnaye ge toh ap log bhi join kro |
| DRAGON SMP! NEW PLUGIN: LIFESTEAL | `play.vyraniumcloud.ccwu.cc` | `19142` | en | 0.15.10 alpha | THIS SERVER IS TOO GOOD JOIN NOW DRAGON SMP! |
| [Dragon Standart](http://pay.dragon-pe.com) | `mon.dragon-pe.com` | `19132` | en | 26.60 | This is a Bedrock edition-only server. We have thousands of mobile players. Join us in a LifeSteal SMP Dragon PE .  m... |
| [DragonEmpire](https://shop.dragon-empire.ru/) | `dragon-empire.ru` | `19132` | en | 26.60 | Welcome to the unique hottest friendly and epic project MCBE DragonEmpire DragonEmpire - Your Home!  🐉Ip: Dragon-empi... |
| dragonzsl | `ultra-05.bedhosting.com.br` | `21192` | pt-BR | 26.51 | 🔥🐉 DRAGON BALL — NOVO SERVIDOR BETA 🐉🔥  Você está pronto para entrar em um universo onde seu poder só depende de você... |
| [DRAKONIA LEGENDS \| Java y Bedrock](https://discord.gg/Ctkqh7dX7) | `drakonialegends.neovex.net` | `25662` | es | 26.60 | [centro]🐉 DRAKONIA LEGENDS 🐉  Servidor latino de Survival con dragones – Java y Bedrock juntos[/centro]  📌 IP Java: u... |
| DreamWorld 0.14-0.15 | `dwpe.ddns.net` | `19132` | en | 0.15.10 alpha | DreamWorld is a server that features the craziest ideas and mechanics you've only seen in newer versions of Minecraft... |
| [DRWEABO LOUNGE](https://drweabo.web.id/) | `play.drweabo.web.id` | `19132` | id | 26.51 | DRWEABO LOUNGE - SURVIVAL ECONOMY!  Selamat datang di server minecraft DRWEABO LOUNGE, di mana server survival multip... |
| [Dungeons Fusion \| Hầm ngục - Thử thách - Sức mạnh](https://dungeonvn.com) | `play.dungeonvn.com` | `19132` | en | 26.63 | ⚔️ DUNGEONS FUSION • SURVIVAL RPG VIỆT NAM ⚔️  The Dungeons. The Challenges. Greater Power. Endless Evolution!  Bạn c... |
| [dupywars.dedyn.io](https://forum.dupywars.xyz) | `dupywars.dedyn.io` | `19132` | en | 26.52 | **Follow the guides on the signs (You will see them once you join) to get started. **  Basic Commands:  - /dupe - Dup... |
| [EarthVision Season 4! - EarthSMP](https://www.earthvision.eu) | `bedrock.earthvision.eu` | `19132` | en | 26.52 | EarthVision - Minecraft Earth Server (English)  EarthVision is an international server, based on a map of the earth (... |
| [EaseCation CH EC BUILD BATTLES EC](http://www.easecation.net) | `asia.easecation.net` | `19132` | en | 1.21.50 | ! NOTICE: We are the official partner of Minecraft Chinese Edition (Agent of NetEase).  Due to NetEase's regulations,... |
| [EienMC ✧ SkyBlock § Factions](https://eienmc.net) | `play.eienmc.net` | `19132` | tr | 26.60 | 𝗘𝗶𝗲𝗻𝗠𝗖 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗦𝗲𝗿𝘃𝗲𝗿  2017 yılında ilk temelleri atılan, günümüzde HUB sunucusu olarak hizmet veren Sky... |
| ELDENSPIRE » Survival Economy [26.2] | `Play.eldenspire.net` | `19132` | en | 26.51 | Eldenspire is a survival economy server based around unique jobs which help the entire community.  We are a new serve... |
| [EldersMC Network ✦ [1.21.6+]](https://eldersmc.top/) | `mc.eldersmc.top` | `19132` | pt-BR | 26.60 | 🌲 Survival com uma experiência verdadeiramente única, criado para quem busca comunidade, evolução e identidade própri... |
| ElectroBlocks | `electroblocks.net` | `19132` | en | 26.60 | I've just started ElectroBlocks - a vanilla anarchy server on bedrock edition. I wanted to create a genuine bedrock e... |
| Elvan SMP » [26.2-1.9] | `play.elvan.space` | `25495` | en | 26.51 | Welcome to the official server page for the Elvyan SMP 1.5 a Bangladeshi YouTuber SMP. This server brings together Ba... |
| EmeraldUHCs | `EmeraldUHCs.ddns.net` | `10252` | en | 0.15.10 alpha | Indian Best Pvp Server |
| [EMIRYCRAFT • Survival](http://emirycraft.denince.biz/) | `emirycraft.keyubu.net` | `19132` | tr | 26.51 | 🟢 EmiryCraft Survival  Klasik Survival'ın sevilen yapısını koruyan, geliştirilmiş ve emek odaklı Türk Minecraft sunuc... |
| EnderArmySMP | `enderarmysmp.dedimc.io` | `19132` | en | 26.60 | Welcome to EnderArmySMP! Enjoy a Bedrock survival server packed with features: a custom GUI, warps, homes, TPA, PvP, ... |
| [Enderpearl.de](https://enderpearl.de) | `enderpearl.de` | `19132` | de | 26.63 | Enderpearl.de \| Deutscher Crossplay Server seit 2021  Auf Enderpearl.de spielen Bedrock und Java zusammen auf densel... |
| [EndFall - Apocalipse Zumbi](https://discord.gg/V59ZpYh4T) | `Endfall.razehost.net` | `25687` | it | 26.60 | ENDFALL \| APOCALIPSE ZUMBI — MINECRAFT BEDROCK  Você está preparado para sobreviver ao fim do mundo?  Bem-vindo ao E... |
| [Endstone Server](http://tofusmp.carrd.co) | `Tofusmp.my.id` | `19132` | en | 26.51 | Welcome to TofuSMP, a simple yet enjoyable Minecraft Survival Multiplayer server based in Indonesia. Our goal is to p... |
| endzone.me - [1.21] | `endzone.me` | `19132` | en | 26.52 | Endzone.me is an active 1.19 Bedrock Anarchy Server. We Provide a Geyser Anarchy Server that brings the best of Anarc... |
| endzone.me - [1.21] | `aurorapvp.club` | `19132` | en | 26.52 | Aurora PvP is a Bedrock and Java Crossplay PvP Server |
| ERRCITY FR | `serv.errcity.org` | `19132` | fr | 26.63 | Le serveur ErrCity te propose du multi-jeux dans un univers de ville.  Nous proposons du PvP, du parkour, du créatif ... |
| [ErrorSMP \| Season X](https://discord.com/invite/errorsmp) | `errorsmp.xyz` | `19132` | en | 26.60 | ErrorSMP — Season 9 Diamond SMP  Semi-anarchy SMP with a tight, active community. Griefing allowed — no hacks, X-ray ... |
| [ESN SMP](https://esnoffical.com) | `play.esnoffical.com` | `19132` | en | 26.60 | ESN SMP is a survival SMP with an RPG twist, running on our own custom ESN plugin. Java and Bedrock players play toge... |
| EternalLand 2b2t | `EternalLand.sytes.net` | `24622` | es | 0.15.10 alpha | servidor 2b2t - Semi anárquico  - tiene totems  - tiene mobs  -Optimizado  - sobre php8  -protección anti ddos  - úni... |
| ETHEREALPE \| Factions + Zones | `glacia.etherealpe.com` | `25503` | en | 26.51 | OPEN BETA!! COME TEST OUR SERVER. REWARDS ARE GAINED EASILY..  https://discord.gg/kTuzBc3SSC |
| [EVOPIXEL [1.21+]](https://www.evopixel.id/) | `evopixel.id` | `19132` | en | 26.60 | EVO PIXEL  Join EVO PIXEL, an exciting Minecraft server where you can enjoy a variety of fun features and game modes ... |
| [EvoraNetwork [Economy CPVP Server]](https://evoranetwork.xyz) | `play.evoranetwork.xyz` | `19132` | id | 26.52 | EvoraNetwork adalah server Minecraft Indonesia bertema Eco Crystal PvP yang menghadirkan pengalaman bermain survival ... |
| F8 Lobby World | `royale.f8studios.net` | `19132` | en | 26.51 | RoyaleMC KitPvP from F8 Network!  Fight other players in our rotating arenas!  Boss Fights, Sumo, and many other even... |
| [Faction / Prison](https://www.aspiredmc.net) | `play.aspiredmc.net` | `19132` | en | 26.60 | AspiredMC is a minecraft network that holds plans to provide a top of the line experience to all players, with our ma... |
| factionary.playit.cafe | `upon-postage.gl.at.ply.gg` | `37314` | en | 26.45 | Aucune description. |
| FACTIONS | `play.cosmicmc.lol` | `19132` | en | 26.50 | Servidor Factions |
| [FadeCloud GENS RELEASE IN NOW](http://fadecloud.com/) | `mp.fadecloud.com` | `19132` | en | 26.60 | FadeCloud Network Gens \| Prison \| Dungeons \| Survival \| Tower Defence  Hosting the BEST grinding and tycoon custo... |
| [FadeMC [1.21.4-26.3]](https://fademc.gg) | `fademc.gg` | `19132` | en | 26.62 | Welcome to FadeMC — a never-resetting survival world where your builds, loot, and legacy are permanent. We blend clas... |
| [FADEREALMS NETWORK](https://www.minespice.net/) | `pe.minespice.net` | `19132` | en | 26.63 | MineSpice Network [1.13-1.21]  The Best Minecraft Network for JAVA and BEDROCK versions! Experience the best with ZER... |
| Falcon Server | `13.140.129.97` | `19133` | en | 26.52 | Aucune description. |
| Falix Limbo | `136.243.13.159` | `20408` | en | 26.60 | Aucune description. |
| [FallenTech](http://shop.fallentech.tk) | `fallentech.tk` | `19132` | en | 26.60 | Aucune description. |
| FamSMP | `famsmp.com` | `19132` | en | 26.36 | Welcome to FamSMP — the family-friendly Bedrock survival server!  We're a brand-new community server built around one... |
| [FAP - SkyPVP](http://www.fapixel.com) | `mc.fapixel.cn` | `19132` | zh | 26.60 | FAPIXEL小游戏服务器（简称FAP，全名FunnyArenaPixel，曾用名FillAmeaPixel）创立于2018年，致力于让国内玩家玩到低延迟、环境友好、玩法丰富的小游戏服务器，我们拥有自主研发的高性能反作弊，独创玩法电子... |
| [FatalMC](https://store.fatalmc.org/) | `mc.fatalmc.org` | `19132` | ja | 26.62 | FatalMC is a high quality Network. Our main focus is our Lifesteal mode, as well as our FFA Mode. We plan to add addi... |
| [Fewer Network](https://store.fewer.live) | `bedrock.fewer.live` | `19132` | en | 26.63 | Welcome to the Fewer Network! We are an awesome Minecraft server that offers many different gamemodes, such as a Cust... |
| [firestarter](https://firestartermc.com) | `mc.firestartermc.com` | `19132` | en | 26.60 | Firestarter is the simple yet exciting community Minecraft experience you’ve been looking for! Whether you just love ... |
| [Firewall MC](https://linktr.ee/firewallmc) | `fire.blazebr.com` | `19132` | pt-BR | 26.60 | 🔥 FirewallMC 🔥   ✨ Servidor Bedrock com economia, eventos e sistemas únicos ✨   🛡️ Comunidade ativa e diversão garant... |
| FirstMC.de | `FirstMC.de` | `19132` | de | 26.62 | Willkommen auf FirstMC – Deinem neuen Minecraft-Zuhause!  FirstMC ist kein gewöhnlicher Minecraft-Server – hier geht ... |
| [FlexPlex &gt;&gt; Nyt taskussasi!](http://flexplex.fi) | `bedrock.flexplex.fi` | `19132` | en | 26.51 | Aucune description. |
| FLYPVP.PL | `flypvp.pl` | `19132` | pl | 26.60 | Aucune description. |
| [FMinе \| Королевская Анархия](https://top-minecrafter.com/en/) | `be.fmine.su` | `19132` | en | 26.60 | Top Minecrafter is your gateway to discovering the best Minecraft servers, carefully selected and verified by Alexand... |
| [ForgeMint SMP - Java + Bedrock Survival](https://forgemintsmp.com) | `play.forgemintsmp.com` | `25615` | en | 26.62 | ForgeMint SMP is a brand new survival economy server for Bedrock AND Java. Earn money and shards, open crates, trade ... |
| [Forgewell Factions](https://forgewellfactions.com/) | `play.forgewellfactions.com` | `19132` | en | 26.60 | FORGEWELL FACTIONS  A Minecraft Bedrock factions server where there's always something to fight for.  Tired of surviv... |
| [Foxy Network](https://discord.gg/JZRqhmyFnh) | `foxynetwork.eu` | `19132` | fr | 26.60 | Serveur UHC et mini jeux Minecraft Bedrock |
| [FreeLands.xyz \|\|\| Анархия FurryBlock.ru](http://site.FreeLands.xyz) | `FreeLands.xyz` | `19132` | ru | 26.63 | «Free Lands» – это сервер Vanilla Bedrock Edition последней версии, на котором есть все игровые механики, включая ред... |
| [FreeLands.xyz \|\|\| Анархия FurryBlock.ru](http://karakalov.ru) | `OGA-Pogrom.org` | `19132` | ru | 26.63 | Один из старейших серверов анархии открытый в 2016 году, который ранее был приватным проектом!  FurryBlock.ru  ------... |
| [FROGGY SMP • 1.21.11-26.1.2](https://roulette77.de/) | `froggysmp.net` | `60403` | de | 26.62 | Ich suche seit Ewigkeiten nach einem vernünftigen Citybuild- oder Survival-Server, der nicht total überladen ist. Übe... |
| [Frontier](http://thefrontiermc.net) | `play.thefrontiermc.net` | `19132` | en | 26.62 | Build nations, forge alliances, wage war, and govern your own citizens. Rules are primarily enforced by players, mean... |
| [FrydeMC \| Survival S3](https://fryde.org) | `mc.fryde.org` | `19132` | en | 26.33 | FrydeMC Network is a Minecraft server supporting versions 1.7 to the latest.  You can play Survival, OneBlock, and ta... |
| [FueguitoMc Network](https://fueguitomc.com/) | `mc.fueguitomc.com` | `19132` | es | 26.51 | 🔥 ¡Bienvenido a FueguitoMC! 🔥  La network de Minecraft donde la diversión nunca se apaga.  🌍 IP: fueguitomc.com  📌 Ve... |
| [FuziVel 1 Jogos 0 &gt; Estamos procurando jogadores. Você foi encontrado. §0 ██](http://u.gy/FuziCraft) | `Fuzivel.ddnsfree.com` | `19132` | pt | 0.15.10 alpha | Servidor para MInecraft, para versões antigas 0.14.x - 0.15.10  O servidor possui 3 idiomas com 95% de todo servidor ... |
| FuziVel 1 Jogos 0 &gt; Fuzivel detectou sua presença. Agora já era. §0 ██ | `memorial.ddnsfree.com` | `19132` | pt-BR | 0.15.10 alpha | Uma história que não pode acabar |
| FuziVel 2 Builders 1 &gt; Mapa download http://memorial.ddnsfree.com:4040 §0 ██ | `memorial.ddnsfree.com` | `19133` | pt-BR | 0.15.10 alpha | Outra história!! |
| [Gamel City](https://youtube.com/@familiagamel?si=6NBfjKcy4s5UWJ3t) | `gamel.bed.net.br` | `9003` | pt-BR | 26.63 | O maior servidor Br de RP e sobrevivência que existe ou vai existir. Bedrock Minecraft! |
| GameLand | `gameland.mcbe.fr` | `19132` | fr | 26.60 | 🇫🇷 : Le mini-jeu de retour en France ! 🇫🇷  GameLand est un serveur de mini-jeux qui en propose plusieurs : le Hikabra... |
| GamePE.me ➧ Survival, Dupe, Grief, Anarchy | `gamepe.ru` | `19132` | ru | 26.60 | Server MCPE Survival worldwide free without a regular account can join 1.16+ to 1.21.2+ |
| [GearsMC Skyblock](http://www.gearsmc.org) | `oyna.gearsmc.org` | `19132` | tr | 26.60 | ɢᴇᴀʀꜱᴍᴄ ᴛᴜʀᴋɪʏᴇ – ᴇᴍᴇᴋ ꜱᴋʏʙʟᴏᴄᴋ  Dengeli ekonomi, adil rekabet ve kesintisiz macera!  🚀 Sunucu Hakkında  GearsMC; eme... |
| [GEONATIONS \| Java + Bedrock SMP](https://geonations.org) | `geonations.org` | `19132` | en | 26.60 | GeoNations is a nations SMP where the map is the politics.  Claim land, found a nation, and go to war over it. Every ... |
| [Gewie SMP](http://discord.gg/parrotpals) | `parrotpals.net` | `19132` | en | 26.51 | Welcome to ParrotPals, a community-driven Survival Minecraft server where you can build, explore, and team up with ot... |
| [Geyser](https://www.sentouki.net/) | `sentouki.net` | `19132` | en | 26.52 | If you are looking for chill community, with all kind of players from all over the world, to make memories with. Then... |
| Geyser | `mc.aloi.si` | `19132` | de | 26.63 | PietSmiet Community :) |
| [Geyser](http://www.ventureland.net) | `bedrock.ventureland.net` | `19132` | en | 1.21.0 | A unique gamemode in minecraft  ► A large hand-built open world map  ► 8 different classes, each with unique abilitie... |
| [Geyser](https://parucraft.net/) | `play.parucraft.net` | `19132` | en | 26.60 | Step into a cozy community driven world where you can kick back, create, and truly feel at home. KeepInventory is on,... |
| [Geyser](https://latechsmp.net) | `play.latechsmp.net` | `50060` | en | 26.52 | Minecraft Java + Bedrock Survival Anarchy Server \| NO RULES!!  - Fight enemy players and build big bases  - join the... |
| Geyser | `moonvalesmp.xyz` | `19013` | en | 26.52 | 🌙 MoonVale SMP — Your Forever Home in the Stars  Not just another server. MoonVale is a cozy Vanilla+ sanctuary where... |
| [Geyser](http://bedrockanarchy.org) | `bedrockanarchy.org` | `19132` | en | 26.60 | BedrockAnarchy is a vanilla anarchy server for bedrock edition with a map that never resets. There are no set rules s... |
| [Geyser](https://discord.gg/8T6G8HgM8u) | `survival.lets.game` | `19132` | ro | 26.51 | Aucune description. |
| Geyser | `skyverse.exaroton.me` | `54101` | en | 26.52 | The Skyverse is a SkyGen based server on minecraft bedrock edition. The Skyverse is polished and while it doesn't hav... |
| [Geyser](https://chat.whatsapp.com/JRNQlG5heOvLflhrpO7zAe?s=cl&p=a&mlu=0&ilr=0) | `lite-2.astrixhost.web.id` | `5026` | en | 26.52 | VortySMP \| A premium Survival Economy server featuring Jobs, Quests, Crates, Auction House, Player Warps, Bank, Vote... |
| [Geyser](https://hyperionsmc.com) | `hyperionsmc.com` | `19132` | es | 26.52 | HYPERIONS MC — Survival con raids de verdad  JAVA + BEDROCK · Entra desde PC o móvil, con cuenta original o sin ella.... |
| Geyser | `play.squidnetwork.my.id` | `19132` | id | 26.62 | Welcome To SquidNetwork!!   IP JAVA : play.squidnetwork.my.id:25625  IP BEDROCK : play.squidnetwork.my.id  PORT BEDRO... |
| Geyser | `Bedrocktogether.exaroton.me` | `21332` | en | 26.52 | Bedrock Together \| Minecraft Bedrock SMP  Welcome to Bedrock Together, a friendly Minecraft Bedrock survival server ... |
| Geyser | `threebthreet.wdn.gg` | `443` | en | 26.60 | NOTE OUR MAIN SERVER LISTING IS ON https://www.planetminecraft.com/server/3b3t-eaglercraft-bedrock-java-1-7-26-3-beta... |
| Geyser | `HOGRAIDS.MC.GG` | `25636` | en | 26.45 | IVE STARTED WORKING ON THIS SIMPLE SURVIVAL SERVER SO PLAYERS HAVE SOME FUN. |
| [Geyser](https://SpillHosting.no) | `node2.spillhosting.no` | `25005` | en | 26.60 | The Mudpit is a Vanilla+ survival server, and Season 2 is now open.  We went back to basics. The economy was rebuilt ... |
| Geyser | `play.mementomc.com` | `19132` | en | 26.60 | MementoMC is a Hardcore server where if you die, you're banned forever. This is your one life. No resets, no respawns... |
| Geyser | `lite-6.astrixhost.web.id` | `5025` | id | 26.60 | Aucune description. |
| Geyser | `Play.Minebloodmc.fun` | `25594` | en | 26.60 | MINEBLOOD NETWORK \| 26.2\| Java & Bedrock   ● Survival   ● Slimefun   ● Lifesteal   Welcome to Mineblood Network   J... |
| Geyser | `listed-completing.gl.at.ply.gg` | `35634` | en | 26.60 | TIDES SMP - Water-World Survival (Bedrock + Java crossplay)  Tides is a survival SMP where the map is mostly ocean an... |
| Geyser | `enx-ext-3.enx.host` | `10158` | en | 26.52 | # 🔥 SURVIVAL ETERNO — SABOR HARDCORE ⛏️  # 🔥 ETERNAL SURVIVAL — HARDCORE FLAVOR ⛏️  🌍 **Servidor de Minecraft Surviva... |
| [Geyser](https://www.gaprok.fun) | `play.gaprok.fun` | `5010` | id | 26.60 | Gaprok Network merupakan server Minecraft Indonesia yang menghadirkan pengalaman bermain Survival SMP bagi siapa saja... |
| Geyser | `play.turtlesshell.me` | `19132` | en | 26.60 | # 🐢 TURTLESHELL SMP 🌍  ### ⚔️ SURVIVE • BUILD • EXPLORE • CONQUER ⚔️  **Welcome to TurtlesShell SMP**, where every ad... |
| Geyser | `mc.sempie.nl` | `19132` | en | 26.60 | Sempie Craft is a friendly vanilla survival server where Bedrock and Java players play together on one world.  🏡 Land... |
| [Geyser](https://discord.gg/mYAPQbsSSD) | `iceandfire.net` | `21476` | en | 26.60 | Looking for a true Game of Thrones roleplay & factions experience where your choices shape history? Ice & Fire is a m... |
| [Geyser](https://424friends.net/) | `play.424friends.net` | `19132` | en | 26.60 | The official 424Friends cross-platform (java / bedrock) SMP Minecraft server! 424Friends is a UK and Western Europe G... |
| GloryMC (Mace) | `5.39.63.207` | `2648` | en | 0.15.10 alpha | PRIME |
| [GO PLAY SURVIVAL SEASON 2 Speed On. Game On.](https://www.goplay.pk/minecraft) | `minecraft.goplay.pk` | `30445` | en | Minecraft Java | Enjoy fast and reliable Minecraft game server hosting with GoPlay PK. Create memorable adventures with stable perform... |
| [GoFight Network](http://gofight.xyz) | `play.gofight.xyz` | `19132` | en | 26.60 | ⚔️ GoFight Network \| Minecraft Bedrock Minigames  Ready to jump into the action? Welcome to GoFight, a Minecraft Bed... |
| GoldCraft | `gocr.cc` | `19132` | en | 26.60 | Minecraft Bedrock Server  - Battle (FFA) \| (Midfight) \| (SumoArena} \| (Duels}... And more!  - MiniGames Spleef \| ... |
| GoldUHCS-UHC MEETUP | `GoldUHCs.sytes.net` | `19132` | en | 0.15.10 alpha | Best server UHC and meetup events |
| [GolemSMP.net](https://golemsmp.net/) | `mc.golemsmp.net` | `19132` | en | 26.63 | IP:  Java  golemsmp.net  Bedrock  mc.golemsmp.net  Bedrock Port: 19132  Max Players: 300 (aiming to grow)  A custom s... |
| [GPORTAL Server - A Minecraft server by g-portal.com](http://Twitch.tv/uktoon) | `45.85.250.177` | `30085` | en | Minecraft Java | Welcome to UKToon's Official Server!  The home for my Twitch community, friends, and fans.  ---  About the Server  Th... |
| Grand Valerius | `mc.grand-valerius.xyz` | `21112` | id | 26.45 | Aucune description. |
| GraveBound | `51.81.107.169` | `25590` | en | 26.63 | Join Minecraft new smp for 0.15.X/0.14.3 only one day event join as indian server |
| [GraveSMP \| 0.15.10x Are Online Now](http://Gravesmp.edgeone.dev) | `Gravesmp.undo.it` | `25569` | id | 0.15.10 alpha | Welcome To GraveSMP  Server Indonesia 0.15.10 yang Online 24 Jam  INFO SERVER  IP : gravesmp.undo.it  Port : 25569  V... |
| Gray School \| SquidGame! | `play.grayschool.my.id` | `10111` | ja | 0.15.10 alpha | Update Squid Game Event! 0.14.3 - 0.15.10 |
| [GreenGold Legacy \| Vanilla с плагинами \| Без вайпов](https://discord.gg/e62TnP33) | `bedrock.greengold.game-serverhosting.com` | `41023` | ru | 26.62 | GreenGold Legacy — русскоязычный Vanilla-сервер с плагинами для Java и Bedrock.  🌍 Один общий мир для Java и Bedrock ... |
| [GrieferGames](https://griefergames.de/) | `griefergames.net` | `19132` | de | 26.60 | Herzlich willkommen auf GrieferGames.net!  Bis zu 22 verschiedenen Citybuilds hast Du die Möglichkeit allein oder mit... |
| [GuaraníCraft](https://redeark.com.br/) | `198.89.99.192` | `19132` | pt-BR | 26.60 | Servidor Semi Anarquia com economia balanceada, eventos diários, sistema de pets, clãs, guerras entre clãs e diversas... |
| [H Y D R A \| Remastered `× Seasson 01 [ Click Enter ] ·](https://dc.gg/hydrahcf) | `HydraHCF.net` | `19132` | es | 0.15.10 alpha | SERVIDOR HCF  PARECIDO A SOLOLEGENDS ( EvilHCF)  INSPURADO en CorHCF  GANA DINERO REAL 💲💸  PROLEAGUE 🏆   en la prolea... |
| HANZU NETWORK 1.8 → 1.21+ | `hanzumc.com` | `19132` | en | 26.60 | HANZU MC - Vietnamese Minecraft network for Bedrock & Java  HANZU MC is a Vietnamese Minecraft network that welcomes ... |
| [HappyBedrock \| New: TNT Wars &amp; Annihilation](https://happybedrock.org) | `play.happybedrock.org` | `19132` | en | 26.60 | HappyBedrock - a Bedrock minigame network  Join on play.happybedrock.org (port 19132) from any Bedrock device, Minecr... |
| HASHIRAS CRAFT │ discord.gg/hashirascraft | `hashiras.net` | `19132` | pt-BR | 26.60 | Servidor de Minecraft bedrock Semi anarquia |
| [HAVEN SMP](http://web.peacefulhaven.lol) | `play.peacefulhaven.lol` | `19132` | en | 26.62 | 🌿Haven SMP - A Calm Survival Experience  Looking for a peaceful Minecraft server where you can build, explore, and pl... |
| [Havoc Games](https://havoc.games/) | `pocket.havoc.games` | `19132` | en | 26.60 | 🔫GUNS IN MINECRAFT!!🔫 Fight off zombies and players alike in our fully custom gamemodes!  🧟THE MINING DEAD:  In this ... |
| [HeadSteal SOON!](https://discord.gg/ckNUnbqR6K) | `HSteal.ddns.net` | `7153` | en | 0.15.10 alpha | New Survival and HeadSteal Server to Play have Fun.  Discord Link: https://discord.gg/xJuMg4VfQN  Join Discord for Rank. |
| [HEARTSMP » LIFESTEAL ❤ &amp; CREATIVE ✎](https://heartsmp.net/?utm_source=Minecraft-Mp.com) | `play.heartsmp.net` | `19132` | en | 26.63 | 🔗 IP: mp.heartsmp.net, Bedrock port: 19132 HIRING STAFF!  🎮 Version: 1.7 - Latest  Welcome to HeartSMP Creative - The... |
| [HEARTSMP » LIFESTEAL ❤ &amp; CREATIVE ✎](https://heartsmp.net/?utm_source=MinecraftPocket-Servers.com) | `lifestealsmp.serverpit.com` | `19132` | en | 26.63 | 🔗 IP: mps.heartsmp.net, Bedrock port: 19132 HIRING STAFF!  🎮 Version: 1.7 - Latest  Welcome to HeartSMP - The Ultimat... |
| HellFireSMP PE | `play.hfsmppe.com` | `19132` | en | 0.8.1 alpha | Do you want to re-experience nostalgic Minecraft just like it was back in 2013?  Look no further — we’ve got you cove... |
| [HerGert](https://hergert.sbs) | `mc.hergert.sbs` | `19132` | pt-BR | 26.60 | O HerGert é um servidor de sobrevivência brasileiro, feito pra jogar com calma e construir sua cidade com a galera.  ... |
| HeroBrineSMP Version v0.14x-v0.15.10 | `185.211.103.141` | `9732` | en | 0.15.10 alpha | A simple Lifesteal smp join now |
| [Heveen discord.gg/heveen](https://www.heveen.fr) | `play.heveen.fr` | `19132` | fr | 26.60 | HEVEEN KITMAP  ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  Heveen fait son grand retour.  Apparu pour la première fois en 2022, Heveen KitMap re... |
| [HexedMC](https://www.hexedmc.net/) | `mps.hexedmc.net` | `19132` | en | 26.60 | Welcome to HexedMC!  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  HexedMC is a Minecraft network filled w... |
| HeXHub.net » Unterstütze uns kostenlos | `hexhub.net` | `19132` | de | 26.63 | HeXHub.net  HeXHub.net ist ein kleiner Server welchen ich privat nebenbei betreibe und weiter ausbaue. Der Server läu... |
| [Hill MC Server](https://hillsmp.com) | `play.hillsmp.com` | `19132` | en | 1.21.100 | Hill SMP Minecraft server 🌳 Survival & 💀 Lifesteal • 💰 Economy • ⚔ PvP & Events • 🛡 Friendly Staff • Build, trade, an... |
| [HIMALCRAFT \| discord.gg/himalcraft](http://store.himalcraft.fun) | `himalcraft.fun` | `25679` | en | 26.51 | HimalCraft is a 24 7 Minecraft server created for players who enjoy Lifesteal survival and competitive Practice PvP. ... |
| [HimbeerCraftPE](https://play.himbeer.me) | `play.himbeer.me` | `19132` | en | 1.21.111 | A simple Server with creative-plots, built by lots of talented players.  This is the reloaded version of the old Himb... |
| [HIVE-O-WEEN \| BEDWARS S5](https://playhive.com/) | `hivebedrock.network` | `19132` | en | 1.0.0 | The Hive is a large Minecraft Bedrock Edition minigame network offering a wide variety of fast-paced multiplayer expe... |
| [Homeless Shelter \| Season 2](https://playsheltr.pages.dev) | `sheltr.duckdns.org` | `19132` | en | 26.60 | HALLOWEEN NIGHT V3: Saturday 31 October (Halloween), 4pm UK time.  A one-night server event, back for a third round w... |
| [HomeTown - A Survival Experience](https://hometownmc.com/) | `smp.hometownmc.com` | `19132` | en | 26.60 | We are a no grief semi-vanilla survival server with a focus on a strong community. Play minecraft the way it was made... |
| HORIZON \| UPDATE! | `Horizon.blazebr.xyz` | `25584` | en | 0.15.10 alpha | Un server de fútbol muy innovador para mcpe 0.15.10 |
| HorizonSMP ◆ [26.2] | `95.217.198.222` | `20292` | en | 26.52 | Builders wanted!  Java + Bedrock crossplay survival server. Custom terrain with big mountains and forests, tons of re... |
| Hotspotkita MC | `mmc.hotspotkita96.my.id` | `19132` | id | 26.63 | Aucune description. |
| Hottes Minecraft server | `130.180.107.105` | `19132` | de | 26.52 | Aucune description. |
| HUB NationsGlory | `be.nationsglory.fr` | `19132` | en | 26.60 | cool serveur |
| HUB NationsGlory | `bedrock.nationsglory.fr` | `19132` | fr | 26.60 | c'est un serveur mec, rien de plus |
| [HUB Server](https://vatonage.com/) | `mc.vatonage.com` | `19132` | en | 26.60 | The Vatonage Network is a modded Minecraft Bedrock server with multiple game modes to choose from, including Cobblemo... |
| HungerMC Atualização!! [0.14.3] §0 ██ | `memorial.ddnsfree.com` | `19135` | pt-BR | 0.15.10 alpha | Uma pequena história |
| [HyperMC \| Explore The New Update! LifeSteal S5 0.14.3-0.15.10](https://discord.gg/S5ZY2h6Sau) | `hmc.sytes.net` | `10256` | en | 0.15.10 alpha | A Minecraft best server opened right now many Minigames and Survival Lifesteal and available in Minecraft 0.14.3-0.15.10 |
| [HyperMC \| Explore The New Update! LifeSteal S5 0.14.3-0.15.10](https://discord.gg/S5ZY2h6Sau) | `comm-01.eu-central.sodiumnodes.org` | `10256` | en | 0.15.10 alpha | A Minecraft's best Server many Minigames and available 0.14.3-0.15.10 |
| HyperMC \| Hacked by hypermc team!! :) | `51.81.243.191` | `25799` | en | 0.15.10 alpha | 🔥I make a New Give SMP for Minecraft 0.15.x/0.14.3 just join now Minecraft server 🔥  YouTube my @mineshorst-y3g |
| [HyperVN Network \| Survival &amp; PVP](https://hypervn.tctgames.com.vn) | `mc.hypervn.net` | `25565` | vi | Minecraft Java | Chào mừng đến với HyperVN - Máy chủ Minecraft Việt Nam chính thức! 🥳  Được phát triển và quản lý bởi TCTGames - Công ... |
| i Survival ✕ [1.7 - 26.3] i | `mysticraft.org` | `19132` | es | 26.63 | 🌌 Mysticraft \| Survival Único para Java y Bedrock  ¿Buscas un servidor donde realmente valga la pena empezar desde c... |
| [IAcraft.net — el server con IA VIVA [1.16+ ✔Bedrock]](https://iacraft.net/) | `play.IAcraft.net` | `19132` | es | 26.40 | ⚡ ¿Y si tu servidor tuviera una IA de verdad jugando contigo? ⚡  En IAcraft no hablas con menús: hablas con una IA VI... |
| [iAkunaMC » XP Triplicado + Unban ALLÚhttps://loja.iakunamc.com - Suporte ao Craftsman End adicionado](https://discord.iakunamc.com) | `iakunamc.com` | `19132` | en |  | ✨ iAkunaMC — YOUR NEW DESTINATION!  - Looking for a competitive, stable server with an active community?   - Discover... |
| [iBedWars GreenWixi](https://greenwix.fun) | `bw.gwix.fun` | `6000` | en | 26.60 | Do you want to check the best BedWars on Bedrock for today? |
| [IDITISMP (1.21+) ▶ discord.gg/iditismp](https://store.iditismp.net/) | `play.iditismp.net` | `19132` | en | 26.62 | Welcome to IditiSMP, the ultimate Shop Survival experience built for action and progression! Battle it out in our hig... |
| [ii BloodMine ii](https://bloodmine-pe.ru) | `bmpe.pw` | `19132` | ru | 0.15.9 alpha | Вам достаточно просто посетить сервер, немного освоиться на нем и практически сразу вам что-то да и понравится. Средн... |
| ii GREENWIX ii [HUB] | `play.greenwix.fun` | `19132` | en | 26.60 | Aucune description. |
| ii MINELUX ii BETA | `minelux.eu` | `19132` | fr | 26.50 | - Minelux est un serveur PvP/Faction qui à ouvert ses portes en 2021 pour la Beta, qui nous prépare à une magnifique ... |
| [ImpendMC (1.20 - 1.21)](https://store.impendmc.net) | `play.impendmc.net` | `19132` | en | 26.60 | We’re a Minecraft network where you can meet new people in the PvP community and just have fun. We’ve got Random Kit,... |
| InfernalMC \| Seasson 1 | `InfernalMC.minecraft.pe` | `10091` | en | 0.15.10 alpha | THIS IS A MCPE 0.14 TO 0.15 SERVER |
| [InnerWorld](https://www.innerworld.live) | `sp.innerworld.live` | `18101` | es | 26.60 | [PT] InnerWorld é um MMORPG para Minecraft Bedrock com classes, missões, história rica, equipamentos raros, aprimoram... |
| [Inostropia](https://www.youtube.com/@Inostropia-809) | `mc.inostropia.com` | `25711` | en | 26.63 | Dive into a complex 6-year-old history of factions, politics, and wars, mainly shaped by players like you! On the Ino... |
| [InsanityCraft](https://www.insanitycraft.net/) | `mps.insanitycraft.net` | `19132` | en | 26.60 | [1.21] InsanityCraft is one of the oldest networks in the world with the most popular game modes! With over a decade ... |
| [InstaCraft Survival](https://www.myinstacraft.com/) | `mc.myinstacraft.com` | `19132` | en | 26.62 | 🌿 InstaCraft Survival — friendly, no-grief community since March 2020.  ⚙️ Java-style survival mechanics with Java + ... |
| [Invalid Server](http://www.capenw.org) | `bedrock.capenw.org` | `19132` | tr | 1.0.0 | Cape Network Türkiyenin Java - Bedrock Sunucusu!  Girişler: Java & Bedrock  Version: 1.16.5+ Java Sürümleri & Tüm Bed... |
| [Ironhaven Network — Minecraft](https://ironhaven.gg/minecraft/) | `73.164.1.196` | `19132` | en | 26.30 | Ironhaven Minecraft is one survival world for everyone: Java and Bedrock players share it through Geyser, so PC, cons... |
| IRUNA CHRONICLES S.1✶ | `iruna.online` | `45574` | en | 26.51 | Unleash Your Adventure: The Ultimate Cross-Play Semi-RPG Minecraft Experience  Step into a world crafted for true adv... |
| [i》》DEATHZONE NETWORK [1.7/26.2]《《i](https://foro.deathzone.net/) | `deathzone.net` | `19132` | es | 26.45 | 🌟 ¿BUSCANDO UN SERVIDOR QUE MEJORE TU CONEXIÓN Y FPS? DEATHZONE NETWORK 🌟  » Survival 1.19 [1.7x - 1.19x]  » Survival... |
| [JackpotMC \| POWER VANILLA OUT NOW!](https://www.jackpotmc.com) | `bedrock.jackpotmc.com` | `19132` | en | 26.60 | JackpotMC is a server focused on PvP game modes, with our latest game mode being Lifesteal SMP. This is a one of kind... |
| [JD Bros](https://www.jdbros.de/startseite) | `play.jdbros.de` | `19132` | de | 26.60 | Wir bieten dir ein unverwechselbares Erlebnis auf unserem Citybuild Server exklusiv für die Bedrock Edition!  Mit eig... |
| [Join To Open Server List](https://youtu.be/MBj3NuCjyFo) | `bedrockconnect.covewolf.com` | `7777` | en | 26.60 | Aucune description. |
| Join To Open Server List | `104.238.130.180` | `19132` | en | 26.60 | Aucune description. |
| [Join today!](https://ecpe.network) | `play.ecpe.network` | `19132` | en | 26.60 | OP Factions  Team up with your friends to fight for /f top on our OP Factions gamemode! Whether you want to lead your... |
| [JonGames denMS - Faction Economy Survival 1.14.4 Website 4 instructions: jongames.com/minecraft](https://jongames.com/minecraft) | `bedrock.jongames.com` | `19132` | en | 26.63 | JonGames Minecraft 1.14.4 Server (1.9 - 1.18 clients supported)  Peaceful Guilds with land claiming and Economy game-... |
| Juko&#039;s Minecraftparadise | `mc.futro.dns64.de` | `19132` | de | 26.52 | ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  JUKO'S MINECRAFTPARADISE  Bedrock SMP · 10 Plätze  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  Ke... |
| [Jukut Goreng SMP](http://www.jukutgoreng.my.id) | `be.jukutgoreng.my.id` | `26016` | id | 26.40 | Enak, Krispi, Bergizi  Intinya Semi Vanilla |
| [Kaizen Network](https://kaizenmc.id/) | `mps.kaizenmc.id` | `19132` | id | 26.63 | Kaizen Network adalah server Minecraft Indonesia yang menghadirkan pengalaman bermain terbaik untuk semua pemain.  De... |
| Kandang Alwi | `Kalwi.id` | `19132` | id | 26.63 | Don't cheat |
| KASTW-幻月殤恆伺服器 | `ser.kastw.cc` | `19132` | zh | 26.60 | 這個嘛... 地圖雖然還在，但有些隨著更新有點...壞掉。  期待有緣人一同更新啦~ |
| KatipunanSMP [1.21-21.6] | `play.katipunansmp.com` | `19132` | en | 26.60 | Katipunan SMP  Joining Information  Java: katipunansmp.ddns.net  Bedrock: katipunansmp.ddns.net  Port: 19132  Version... |
| [KAWAISMP](https://www.kawaismp.net) | `play.kawaismp.net` | `19132` | id | 26.33 | Aucune description. |
| [KazuoSMP \| Nella Kontol! #KazuoGacor √](https://chat.whatsapp.com/GIW9qjV5BB07vK3qv7A4rj?s=cl&p=a&ilr=4) | `Kz.run.place` | `22106` | en | 1.1.7 | 🔥 KAZUOSMP IS NOW OPEN! 🔥  The only SURVIVAL FACTIONS server for MCPE 0.14.3...0.15.10...0.16...1.1.7 from INDONESIA ... |
| [KBLK MC • mc.kblk.space](https://kblk.space) | `mc.kblk.space` | `19132` | ro | 26.52 | KBLK MC - server Minecraft de survival românesc, fără pay-to-win, pentru Java (1.20 – 26.3) și Bedrock (26.30 – 26.52... |
| [KernelHost11](http://kernelhost11.top) | `minecraft.kernelhost11.top` | `56989` | pt-BR | 26.51 | A KernelHost11 consiste em uma infraestrutura tecnológica completa, cujo ecossistema engloba o desenvolvimento da int... |
| [KingdomCraft-S13](https://kingdomcraft.co.nz) | `server.kingdomcraft.co.nz` | `19132` | en | 26.61 | Kingdomcraft SMP is a Kingdoms Server, we have created our own User Interface so server moderation with staff is not ... |
| [Kingdoms and Ruins](https://www.kingdomsandruins.com) | `kingdomsandruins.com` | `25565` | en | 26.51 | [NEW] Kingdoms & Ruins 1.19  BEDROCK - JAVA CROSSPLAY  Kingdoms and Ruins is aiming to build a Towny Server with a wi... |
| KingSMP \| HALLOWEEN IS HERE! | `KingSMP.net` | `19132` | vi | 26.60 | Đây là máy chủ sinh tồn   Không toxic   Không scam |
| Kirby Survival Economy | `kirbysmp.cloudplay.fun` | `26317` | en | 26.60 | Survival with a full player-run economy. You start with $300 in a digital wallet, then earn more from jobs like minin... |
| Kitmap Olympia | `play.olympiamcbe.com` | `19132` | fr | 26.60 | Aucune description. |
| [KittiMC Server](https://www.facebook.com/kittimcminecraftszerver/) | `kittimc.serveminecraft.net` | `19132` | hu | 1.20.10 | ●➤ Non-Stop Fut (0/30)  ●●➤ Verzió: 1.13.0  ●●●➤ WHITELIST SZERVER!!!  ●●●●➤ Jelentkezni Discord csatornánkon lehet! ... |
| [KnightHC](http://www.knighthc.pl) | `knighthc.pl` | `19132` | pl | 26.60 | KnightHC.pl – Survival + Gildie na Minecraft Bedrock  KnightHC.pl to polski serwer Minecraft Bedrock Edition, który ł... |
| [KretMC → wystartowaliśmy!](https://www.kretmc.pl) | `play.kretmc.pl` | `19132` | pl | 26.60 | KretMC.pl - Najlepszy serwer Minecraft!  Minecraft Bedrock: play.kretmc.pl port: 19132  Wersja: 1.8-1.20  Ilosc sloto... |
| KuzeSMP + HappySMP | `49.12.82.39` | `25906` | es | 0.15.10 alpha | este es un nuevo servidor SMP |
| [Kyoto-U (Uji) Minecraft Server](https://www.ujimc.cc.cd/) | `98.142.241.156` | `19129` | zh | 26.52 | # UJIMC — Kyoto University Open Minecraft Server  **Official Website**  https://www.ujimc.cc.cd/  Welcome to **UJIMC*... |
| [Lanf Countries Earth](http://minecraft.bald1nh0.net) | `minecraft.bald1nh0.net` | `19132` | en | 26.52 | Small family-friendly Bedrock server focused on building and exploring. Adventure/Creative style gameplay, relaxed an... |
| [LateCraft Survival 0.14.X #1 3/75](http://none) | `a.latecraft.ru` | `19150` | en | 0.14.3 alpha | LateCraft is a server created in 31.05.2020 by player Lituty. Currently, the available modes are Anarchy, Survival, a... |
| LateCraft Survival 0.14.X #1 4/75 | `LateCraft.ru` | `19150` | ru | 0.14.3 alpha | Aucune description. |
| Lava - FactionsLava SESSION 1 | `forever.blazebr.xyz` | `26991` | pt-BR | 0.15.10 alpha | 🍃 FOREVER RAIZ — Servidor MCPE 0.15.10 focado em progressão, economia, competição e diversão. Evolua seu rank, conqui... |
| [LavaMC Lifesteal](https://discord.gg/regGbbh5sF) | `94.130.13.217` | `40390` | en | 0.15.10 alpha | LavaMC is a new Lifesteal server!  Gear up using the Shop-GUI and fight other players. Gain 20 hearts or get banned a... |
| [ldp.scmain.com \| [1.16 - 1.21]](https://ldp.scmain.com/) | `ldp.scmain.com` | `19132` | en | 26.60 | LDP SMP is no wiping server*, where you earn ≈3$ by play**.  Dynamic prices ingame shop(items growing and falling lik... |
| [LEATplex](http://leatplex.net) | `mc.leatplex.net` | `19132` | en | 26.60 | POTSHOT: MAGIC AND MAYHEM UPDATE!  LEATplex is a Minecraft minigames server. We currently support Bedrock Edition 26.... |
| [Legendcy Survival \|\| 1.21.11-26.2](https://legendcysite.lordy.xyz/) | `legendcy.lordy.xyz` | `25569` | en | 26.52 | The Legendcy Survival is a modern survival server. Our survival has a wide spread of custom features. Such as global ... |
| LegendSMPR.exaroton.me | `LegendSMPR.exaroton.me` | `19132` | it | 26.60 | ⚔️ Un nuovo mondo, una nuova era!  Ciao a tutti ragazzi! 👋  Abbiamo aperto un nuovo server Minecraft Survival GDR isp... |
| [LemonCloud](https://lemoncloud.org) | `mps.lemoncloud.net` | `19132` | en | 26.63 | Welcome to LemonCloud! Our awesome gamemodes:  Prison  Factions  Skyblock  Creative  KitPvP  Survival  Join now! @  I... |
| LemonSMP \| Unique Survival Experience | `play.lemonsmp.org` | `19132` | en | 26.60 | LemonSMP is a feature-rich Survival SMP running on Minecraft 1.21.11 with Simple Voice Chat and with a fully custom e... |
| [Liebe auf den ersten Block](https://InfinityCraft.de) | `InfinityCraft.de` | `19132` | en | 26.10 | 🇩🇪 Deutsch 🇩🇪  InfinityCraft - Liebe auf den ersten Block  Herzlich willkommen auf InfinityCraft, deinem Citybuild-, ... |
| [LifeMC.net](http://Store.LifeMC.net) | `lifemc.net` | `19132` | en | 26.45 | Welcome to LifeMC, a highly competitive, feature-rich Minecraft survival experience where every decision matters, eve... |
| [LIFESTEAL SMP](https://store.lifestealsmp.com) | `mps.lifestealsmp.com` | `19132` | en | 26.62 | We are a semi-vanilla Minecraft server with a unique feature where you can steal hearts from other players. PvP is al... |
| LifeTale Lifesteal Season 2 - 0.14.X - 0.15.X | `LifeTale.minecraftr.us` | `10014` | en | 0.15.10 alpha | Play , Fight , Make Team And Win |
| Lime Kitmap | `lime-mc.eu` | `19132` | fr | 26.30 | Aucune description. |
| [LimeDex &gt; GRIEF](http://shop.lime-d.ru) | `lime-d.ru` | `12022` | ru | 1.1.0 | Данный проект для вас Выживание, гриф, дешевый донат, хороший онлайн, отзывчивая администрация и многое другое именно... |
| [LimeDex &gt; GRIEF](http://shop.lime-d.ru) | `lime-d.ru` | `12000` | ru | 1.1.0 | Данный сервер с грифом, специально для русских игроков, заходи не пожалеешь. |
| [Linesia V6](https://www.linesia.net/) | `play.linesia.net` | `19132` | fr | 26.60 | Linesia est un serveur Minecraft Mcpe/Bedrock axé sur le mode de jeu KitMap, une expérience divertissante riche en Pv... |
| [LKSMP](https://lksmp.fun/) | `bedrock.lksmp.fun` | `8100` | en | 26.62 | A peaceful place for you and your friends to have fun and vibe  Survival Server  Features:  *Land claims  *Custome sk... |
| LokiCraftSMP S-2 | `lokicraft.ddns.net` | `6117` | en | 0.15.10 alpha | Welcome To LokiCraftSMP S-2 |
| [Loot.Team - Survival 26.3](https://loot.team) | `loot.team` | `19132` | en | 26.51 | Semi-vanilla Minecraft server with PvP and a minimal set of QoL features: /home, /tpa, /spawn and private messages. N... |
| LootMC | `Lootmc.com` | `19132` | en | 26.60 | §3Noonmc |
| LOSTANARCHY • Java + Bedrock | `lostanarchy.pineserver.xyz` | `25532` | en | 26.60 | Welcome to LostAnarchy — a fresh Java and Bedrock crossplay anarchy server built around freedom, survival and permane... |
| LoungeSMP | `bedrock.loungesmp.xyz` | `25627` | en | 26.60 | Active Semi-vanilla SMP, no resets, weekly events, player shops, jobs, warps, keep inventory, and toggle PvP off by d... |
| [loyal smp S3](https://discord.gg/Nq6hgqScMV) | `38.134.40.36` | `4358` | en | 26.63 | the most best server where u can do whatever you want |
| [Luminara SMP](https://luminaramc.org) | `br.luminaramc.org` | `53778` | en | 26.63 | Refreshed Semi-Vanilla 1.21 SMP  Luminara (formerly known as Nether Depths) is a semi-vanilla survival multiplayer se... |
| [LUMINOUS NETWORK](https://linktr.ee/LuminousBisnis) | `luminousnet.xyz` | `19009` | id | 26.60 | 🌟 WELCOME DI LUMINOUS NETWORK 🌟  Bergabunglah dengan komunitas Minecraft kami yang ramah dan seru! Kami menawarkan pe... |
| LUNAR MC S4 » Anti Abuse | `play.lunarbd.fun` | `5010` | en | 26.60 | Lunar MC is a Bangladesh based Lifesteal SMP server made for both Java and Bedrock players Enjoy smooth gameplay low ... |
| [Lungo Blue • Survival • LGBTQ+](https://lungo.blue) | `lungo.blue` | `19132` | en | 26.45 | Lungo Café [Vanilla] [LGBTQ+] [26.2]  Server Name: Lungo Café  Server Address: lungo.blue  Version: Bedrock / Java 26... |
| [Luxuria \| Practice](https://dc.gg/luxuria) | `LUXURIAPVP.COM` | `26425` | en | 26.60 | # BEDROCK PRACTICE PvP  Welcome to our Minecraft Bedrock Practice PvP server!  Improve your skills, challenge other p... |
| [Lyno Kitmap V2.5](http://lyno.tebex.io) | `play.lynokitmap.com` | `19132` | fr | 26.50 | **__LYNO KITMAP V2.5__**  ═════════════════════  **Lyno** fait son retour le **__VENDREDI 14 AOÛT À 18H30__** () avec... |
| [LysaMC](https://store.lysamc.net) | `play.lysamc.net` | `19132` | en | 26.50 | Welcome to LysaMC - A Minecraft Network for Everyone  Something for every player. Multiple game modes, active communi... |
| LÀNG BĂNG VN [1.17x ⇨ 1.26x ] | `Pe.LangBangVN.Net` | `19132` | en | 26.63 | \|==== Server🚫 ====\|  1.0 ： Không đốt rừng ( vi phạm ban 7 ngày - vĩnh viễn )  1.1 ： Không sử dụng các loại phần mềm... |
| MagicCraft Minecraft 0.15.10 | `194.102.181.219` | `3952` | en | 0.15.10 alpha | Welcome to MagicCraft!  MagicCraft is a 24/7 online Lifesteal and Magic server designed for MCPE 0.14, MCPE 0.15, and... |
| [MagmaMC](https://www.magmamc.net/) | `bedrock.magmamc.net` | `19132` | en | 26.63 | MagmaMC 💎 \| Java and Bedrock support - Survival Minecraft Server  IP: play.magmamc.net  Version: 26.1.2  Website: ht... |
| Maintenance | `AsianUHCs.ddns.net` | `3626` | en | 0.15.10 alpha | Just A PvP Server |
| [Make Waves ༄ discord.gg/makewaves](https://eyserrver.com) | `mps.eyserver.com` | `19132` | en | 26.60 | The official Minecraft server for the YouTuber Eystreem who has over 7 million subscribers and 100 million monthly vi... |
| Make Waves ༄ discord.gg/makewaves | `play.eyserver.com` | `19132` | en | 26.60 | Welcome my dear player!  Hope you'll have fun in our new server!  -Ancient Piggy Official |
| [ManaCube Bedrock](https://manacube.com) | `bedrock.manacube.com` | `19132` | en | 26.63 | ManaCube is a flourishing minecraft community renowned for its wide variety of engaging Minecraft servers. Our unique... |
| [MasterCraft RankUP OP](https://redemaster.net/) | `pe.redemaster.net` | `19132` | es | 26.60 | MasterCraft foi fundado em 2016 por Jheyson Henrique por puro Hobby e hoje somos juntamente com nossos jogadores um d... |
| [MASTERDROCK [EU]](http://discord.masterdrock.com) | `play.masterdrock.com` | `21341` | en | 26.60 | Server Pokemon Minecraft Bedrock [Mod SERP Pokédrock]  » Crates  » Commands  » Structures  » Compatible with Xbox, Pl... |
| [MayariSMP [26.3] DUNGEONS 🏹 ECONOMY](http://mayarismp.tebex.io) | `play.mayari.space` | `19025` | en | 26.52 | Mayari support both Java and Bedrock. Earn money from quests, get rewards from voting and join events for amazing pri... |
| [mc.AENAT.net](http://aenat.net) | `mc.aenat.net` | `19132` | vi | 26.52 | AENAT là một máy chủ Minecraft được xây dựng theo định hướng Survival RPG, nơi mỗi người chơi đều có thể bắt đầu từ c... |
| [mc.mariscolandia.com](https://discord.gg/YsbAxH3c4) | `mc.mariscolandia.com` | `19132` | es | 26.52 | 🌌 Mariscolandia es un servidor de Minecraft con supervivencia, economía, rangos, eventos, misiones y una comunidad en... |
| [MC4FUN ▫ 1.18.2 - 26.1.2](http://www.mc4fun.net) | `bedrock.mc4fun.net` | `19132` | tr | 26.60 | MC4FUN - Türkiye'nin En İyi Minecraft Sunucusu \| Turkey's Best Minecraft Server  IP: mc.mc4fun.net  Website: https:/... |
| [MCC Network](https://discord.gg/dB2ZJVp) | `mccnetwork.uk` | `19132` | en | 26.60 | Welcome to MCC Network   We are a friendly, feature-rich Minecraft Bedrock server network established in 2016 offerin... |
| [MCHub.com](https://mchub.com) | `mps.mchub.com` | `19132` | en | 26.60 | Welcome to McHub - Your Ultimate Minecraft Adventure!  Dive into a world of endless possibilities on McHub, where thr... |
| McSb Are Back! | `92.119.165.177` | `8218` | en | 0.15.10 alpha | McSb Comeback |
| MelesiaFFA | `melesia.mcbe.fr` | `19149` | fr | 26.60 | Melesia Kitffa |
| [Meow](https://www.mineverso.com/) | `mc.mineverso.com` | `19132` | es | 26.60 | Servidor actualizado y optimizado por profesionales para que puedas disfrutar de una buena experiencia sin latencia (... |
| MeowSMP \|\| Opened!! (!) 0.14.3-0.15.10 MultiVersion (!) | `meuwsmp.duckdns.org` | `24628` | en | 0.15.10 alpha | MeowSMP, Pillars, PvP-Games, Mace-PvP, MaceTAG and more! join and enjoy the special features!! |
| MeowSMP \|\| Opened!! (!) 0.14.3-0.15.10 MultiVersion (!) | `meowmcpe.duckdns.org` | `24628` | en | 0.15.10 alpha | MeowSMP, Back now! Mace PvP, PvP-Games, Survival, Pillars, And more! |
| MINEBOX \| NETWORK * Felices Fiestas * | `mbox.shockbyte.me` | `8116` | es | 0.15.10 alpha | Servidor survival para mcpe 0.15.10 y 0.14.3 con muchas modalidades como parcelas, Casttlesays, MinaMoney, BlockHunt,... |
| Minecraft BD [1.8-26.2] | `pe.minecraftbd.org` | `19132` | en | 26.45 | ⭐ Welcome to MinecraftBD! 🇧🇩  Join the Bangladeshi Minecraft community and experience a friendly survival adventure w... |
| Minecraft Bedrock Server | `wertie3020.duckdns.org` | `19132` | en | 26.51 | this server is a old anarcy server with a lot of history   most players stop playing becos the world was coruped for ... |
| [Minecraft EvoPixel](https://minecraft.evopixel.ro) | `mc.evopixel.ro` | `19132` | en | 1.21.120 | Minecraft EvoPixel is a high-performance Minecraft server designed for a seamless and immersive gaming experience. Wi... |
| Minecraft Server | `Avorium.org` | `19132` | en | 26.60 | A Community based Server, with the Best Combat Style on every Server. We make Games for our Community. |
| Minecraft: PE Server | `game.ikymas.my.id` | `40477` | en | 0.14.3 alpha | You can build in here! |
| [Minecraft: PE Server](http://MChost) | `51.38.205.167` | `13847` | en | 0.15.10 alpha | CoreMC s-2 Lifesteal join now. Mostly Online in night! |
| Minecraft: PE Server | `91.98.80.233` | `25928` | en | 0.15.10 alpha | Aucune description. |
| Minecraft: PE Server | `play.craftymc.bond` | `13965` | en | 1.1.7 | 📌 SERVER INFORMATION  Super excited to drop this here. If you're tryna find a wild, fast-paced survival server to gri... |
| Minecraft: PE Server | `voidpe.mcindo.my.id` | `29003` | id | 0.15.10 alpha | ⚔️ VoidPE — Minecraft Anarchy 0.15.10  Selamat datang di VoidPE, server Minecraft Pocket Edition versi 0.15.10 yang m... |
| Minecraft: PE Server | `2builders2tools.cowdie.com` | `16380` | en | 0.15.10 alpha | MINECRAFT GENISYS ONLY 2B2T ( 2 BUILDER 2 TOOLS ) . NO RULES . |
| [Minecraft: PE Server](https://dreammcofficial.netlify.app) | `DreamMC.sodn.online` | `3250` | en | 0.15.10 alpha | A Survival Server Has a Lot of Fun.Enjoy The Server by playing it.  Visit our Website https://dreammcofficial.netlify... |
| [Minehut](https://sites.google.com/view/drevil) | `bedrock.minehut.com` | `19132` | en | 26.60 | mine until you can't no more on mcpe.  Guide To Join  Join Server IP:bedrock.minehut.com Port:19132 once you join the... |
| [Minekube](http://gymben.eu.cc) | `play.gymben.eu.cc` | `19132` | de | 26.60 | ???? GymbenMC \| Kleiner Citybuild mit RIESEN-Community-Feeling \| Jetzt Clan gründen & Teil der Familie werden!  ???... |
| MineLimit \| We&#039;re back, and better than ever. | `Play.CoffeeVerse.Org` | `25565` | en | 26.44 | Server IP: play.coffeeverse.org  Version: 1.8 - 26.*  Discord: https://discord.gg/BupJrVytXe  Step into CoffeeVerse, ... |
| [MinePlanet » Xbox «](http://mineplanet.top) | `play.mineplanet.top` | `19136` | en | 26.60 | 🐔 Animal Farms  🔪 Unique Clan System with Wars  🔑 Prison System for Griefers  💰 Player Trading System  🏹 Boss Fights ... |
| [MINESIVE [1.21 - 26.3]](http://store.minesive.com) | `be.minesive.com` | `19132` | id | 26.60 | Minesive New Era |
| [MineSpazio \| ¡únete ahora!](https://tienda.minespazio.com/) | `db.minespazio.com` | `19132` | en | 26.51 | Aucune description. |
| [MineSuperior [26.3] TOWNY SKYBLOCK SURVIVAL](https://store.minesuperior.net/) | `br.mcs.gg` | `19132` | en | 26.62 | Discover MineSuperior – your ultimate 1.21 Minecraft: Java Edition destination, meticulously curated by a seasoned ma... |
| Misaki Practice | `play.misaki.host` | `25601` | zh | 26.0 | Misaki is a Chinese minecraft bedrock edition pvp server by Prokits. |
| MMC eBLOCK Survive. Loot. Extract. | `victoryfirestudios.com` | `6013` | en | 26.60 | Military Simulation server  discord : discord.gg/nqTgqRyDVG |
| ModsCraft \| Survival, Dupe, Grief, BedWars | `craft.pe` | `19132` | en | 26.60 | Aucune description. |
| [ModsCraft \| Survival, Dupe, Grief, BedWars](https://craft.pe/) | `play.modscraft.net` | `19132` | ru | 26.60 | :: ModsCraft :: 1.1-1.20 . |
| MomentumMC | `cp.momentummc.ca` | `19132` | en | 26.63 | MomentumMC  Survival /SMP Server  Java/Bedrock Supported  Usually Current Version!  Featuring an amazing community bu... |
| Monsters Anarchy | `monstersanarchy.verixen.net` | `19132` | en | 26.60 | -Monsters Anarchy- (BEDROCK)  -18,800+ Days Played  -The server has no resets! The world is over two years old (start... |
| [MONTE VERDE SURVIVAL](http://www.monteverdesurvival.com.br) | `play.monteverdesurvival.com.br` | `9078` | pt-BR | 26.50 | Monte Verde Survival é um servidor brasileiro de Minecraft Bedrock focado em sobrevivência séria, exploração e progre... |
| [MoonWix https://discord.gg/haFVFRF63](http://magmanode) | `moonwixmc.minecraft.pe` | `27698` | tr | 0.15.10 alpha | MoonWix 0.14.3 - 0.15.10 Minigames Server |
| [MRGNetwork](http://store.playmrg.net) | `playmrg.net` | `19132` | en | 26.60 | Welcome to MystrickGames, a premium Minecraft Bedrock Edition minigame network! We are dedicated to bringing you the ... |
| multiserver.webhop.me | `multiserver.webhop.me` | `19132` | en | 26.40 | Welcome to Ultragys's Multiserver! You can chill at this server, hang out with others, mine, roleplay, and do some Pv... |
| [MYLIFECRAFT [26.3]](https://www.mylifecraft.net/) | `play.mylifecraft.net` | `25570` | es | 26.60 | 🌿 ¡Bienvenido a MyLifeCraft!*🌿  Aquí no es solo un servidor… es un mundo vivo, en constante evolución, donde cada jug... |
| [Mynolia KitMap V1](https://discord.gg/nJkFq9TZDR) | `82.153.202.184` | `19132` | fr | 26.60 | Le meilleur kitmap de mcbe fr. |
| [Mypex Core](https://play.mypex.net/?src=top4) | `185.207.214.91` | `19132` | en | 26.30 | Mypex is an independent voxel game with its own client (not Minecraft). Anarchy mode: a world of floating islands, fo... |
| [Mythblock.me \| 26.3 \| Unique OneBlock](https://mythblock.me) | `mythblock.me` | `19132` | en | 26.63 | MythBlock  A OneBlock server that goes far beyond one block  Java: mythblock.me \| Bedrock: mythblock.me, Port 19132 ... |
| NationMC Earth | `NationMC.net` | `19132` | en | 26.60 | NationMC is a next-generation Earth SMP running on a custom 1:500 Earth world, where you and your friends can build r... |
| Navalia | `navaliamc.fr` | `19132` | fr | 26.50 | Un très bon serveur KitMines (mélange de KitMap et KitMines) |
| Nawasena \| Survival Mix | `mc.nawa-sena.com` | `5731` | en | 26.63 | 🌿 NAWASENA — SURVIVAL MIX 🌿  Looking for a relaxing survival server with meaningful progression and plenty of activit... |
| [Neolya PvP Faction](https://neolya.ddns.net) | `neolya.ddns.net` | `19132` | fr | 26.60 | Neolya est un serveur PvP Faction dont le but est de dominer le serveur! |
| NeonCraft SMP | `play.neoncraft.org` | `19132` | en | 1.21.93 | Hi! Take a moment to read what our server is about ;   ► SMP with landclaim and economy  ► Playable on Java AND Bedro... |
| [Netherite · New Prison season in 2d 5h 4m](http://netherite.gg) | `mps.netherite.gg` | `19132` | en | 26.62 | Netherite is an innovative, qualitative, and unique Minecraft Network focused on the game modes SMP, Lifesteal, and S... |
| [NetherixMC - Faction v1.0.0](https://netherixmc.net) | `oyna.netherixmc.net` | `19132` | tr | 26.60 | 🔥 NETHERIXMC – FACTION Dünyasına Hoş Geldin! 🔥  Olağanüstü bir Faction deneyimi seni bekliyor! Strateji, takım savaşı... |
| [NEW GAME BLASTERWARS](http://Galaxite.net) | `play.galaxite.net` | `19132` | en | 1.0.0 | Galaxite is a featured Bedrock Edition Minecraft Server, made by Blockception.  Players can choose 6 game modes to pl... |
| New Ip and Port IP\|PixelSky.blazebr.xyzPORTA\|19132 | `pixelgames.blazebr.xyz` | `25808` | it | 0.15.10 alpha | 🎮 PIXELGAMES — A ERA CLÁSSICA DO MCPE ESTÁ DE VOLTA!  Reviva a experiência clássica do Minecraft Pocket Edition no Pi... |
| [NEW IP: bedrock.meadowsmp.com](https://store.meadowsmp.com/) | `meadowsmp.com` | `19132` | en | 26.63 | 🌷 Welcome to Meadow SMP  Meadow SMP is a friendly, cross-platform Minecraft server for players who love survival, bui... |
| [NEW IP: bedrock.meadowsmp.com](https://store.meadowsmp.com/) | `play.meadowsmp.com` | `19132` | en | 26.63 | 🌷 Welcome to Meadow SMP  Meadow SMP is a friendly, cross-platform Minecraft server for players who love survival, bui... |
| [Newwind](https://newwindserver.com) | `craft.newwindserver.com` | `19132` | en | 26.62 | Minecraft survival with clans, dungeons, quests, PVP, events, and hundreds of custom items, all while preserving the ... |
| [NG: Farewell 2016 - 2026](https://nethergames.org) | `play.nethergames.org` | `19132` | en | 26.60 | Welcome to the NetherGames Network!  We're a friendly community-based Minecraft Bedrock Edition server network (and a... |
| [NightCore \| Season 16 0.14.3 x 0.15.10](http://nightcore.great-site.net) | `NightCore.minecraft.pe` | `25794` | en | 0.15.10 alpha | Aucune description. |
| [Nitrogen Survival](https://linktr.ee/nitro.net) | `play.nitrogen.zone` | `19132` | en | 26.60 | Welcome to Nitrogen. Our server has the most loyal community in Minecraft. We're a Network that offers Skyblock, Surv... |
| [NixxoSMP.lat](https://www.nixxosmp.lat/?s=lst-mcpocket) | `nixxosmp.lat` | `19132` | es | 26.60 | ⚔️ NIXXOSMP — Survival PvP estilo DonutSMP en español  Economía entre jugadores, PvP de verdad y duelos al instante. ... |
| No Gods Only Blocks \| 1.21.4 | `ngob.org` | `19132` | de | 26.20 | ❌NO RULES – Grief, raid, hack, PvP – anything goes  ❌ NO RESETS – This world stays forever  ❌ NO PAY-TO-WIN – No rank... |
| [NOBLEREALMS \| 26.3+ Towny Survival](https://store.noblerealms.com) | `play.noblerealms.com` | `19132` | en | 26.60 | Java IP: play.noblerealms.com  Bedrock IP: play.noblerealms.com Port: 19132  Discord: discord.gg/noblerealms  Join th... |
| Noctalia V2 | `82.153.202.190` | `19134` | en | 26.60 | Noctalia-KitMap-Farm2win |
| [Noesantara Network \| 1.18 - Latest](https://store.noesantara.id/) | `noesantara.id` | `19132` | id | 26.63 | Noesantara Network — Di Mana Mimpi Menjadi Nyata  Server Noesantara Network Yang Dahulu Dikenal Dengan Nama Aetherium... |
| NORD FJELL One world. One history. | `mc.nord-fjell.com` | `19132` | en | 26.51 | Breathing the gentle warm breeze sweeping across ancient Burkina Faso, taking time to enjoy top-tier gaming on my han... |
| [NordikMC \| Everything you do pays \| No P2W](http://nordikmc.com) | `play.nordikmc.com` | `19132` | en | 26.50 | YOU GET PAID FROM THE SECOND YOU LOG IN  No sign-up. No menu. No class to pick.  Mine a block, get paid. Chop a tree,... |
| [NovaPrime](https://npbe.net) | `play.npbe.net` | `19132` | en | 26.30 | Aucune description. |
| [NuansaCraft Survival Economy](https://nuansacraft.com) | `play.nuansacraft.com` | `19132` | en | 26.51 | NuansaCraft is a survival multiplayer server made for Indonesian players who want more than just another vanilla worl... |
| [NULLMC](https://nullmc.net) | `play.nullmc.net` | `19132` | en | 26.52 | NullMC Network  A competitive Minecraft network built for players who enjoy survival, strategy, and large-scale PvP. ... |
| Nusantara-smp server | `nusantaraserver.zapto.org` | `19142` | en | 26.52 | Server survival economy with rupiah currency   Stable FPS and light server that is suitable for playing with your fri... |
| [Nusantarabatu \| 1.21 - Latest](https://linktr.ee/nusantarabatu) | `nusantarabatu.id` | `19132` | id | 26.63 | NusantaraBatu \| 1.20 - Latest  Survival -New Gamemode Coming soon  Ip Java : nusantarabatu.id  IP Bedrock : nusantar... |
| [ObiSky ⌛](https://discord.gg/VtA2sRrQ9f) | `play.obisky.com` | `19132` | en | 26.45 | Welcome to ObiSky!  ObiSky is an upcoming community-based Minecraft: Bedrock Edition server! Our goal is to create a ... |
| OCEAN PVP | `162.33.24.110` | `9140` | en | 26.63 | Competitive Bedrock PvP without Pay-to-Win.  Dynasty PvP is built around fair, skill-based combat and a polished PvP ... |
| [OG Network](https://www.og-network.net/) | `og-smp.net` | `19132` | en | 26.63 | This server aims to bring back the old style of Minecraft without Pay2Win garbage.  You can expect a vanilla experien... |
| [OG Network](https://og-network.net) | `og-network.net` | `19132` | en | 26.63 | The OG Network is a minecraft server dedicated to reviving the old style minecraft experience. We are not pay2win, an... |
| [OHO Network](http://www.ohoth.com) | `play.ohoth.com` | `19132` | th | 26.51 | OHOTH is a Thai-themed Survival SMP that you can play on both Java and Bedrock (PC, mobile and console) with the same... |
| OICECRAFT MC | `66.51.96.72` | `25560` | en | 26.61 | OICELANDS MC — Bedrock Survival Server Description  OICELANDS MC is a survival world built for players who want more ... |
| [Old&#039;s Cool FreeBuild &amp; Survival &gt; 26.30 - 26.60 &lt;](http://pldm.ml) | `pldm.ml` | `19132` | pl | 26.60 | Aucune description. |
| [OPBlocks](https://opblocks.com) | `bedrock.opblocks.com` | `19132` | en | 26.60 | OPBlocks is a high-quality Minecraft Prison, Survival SMP, and Skyblock server featuring unique content and an amazin... |
| [OPSUCHT](https://www.opsucht.net) | `opsucht.net` | `19132` | de | 26.63 | Herzlich willkommen auf der Vote-Seite von OPSUCHT.NET!  OPSUCHT.NET ist am 23.10.2025 sieben Jahre alt geworden.  Du... |
| [ORACLEPVP │ discord.gg/oracle │ [26.2]](https://store.oraclepvp.net/) | `oraclepvp.net` | `19132` | en | 26.60 | Play the on the #1 ONECHUNK MINECRAFT SERVER, which offers chunk teams, chunk upgrades, weekly competion and 7 PVE lo... |
| Orbiting \| Network Minijuegos - 0/18 | `orbiting.holynodes.com` | `25580` | en |  | Orbiting Pearl Party  Server games and farm!  Version: MCPE 0.15.x  IP: orbiting.holynodes.com  Port: 25580 |
| [OrderSMP](https://www.ordersmp.net/) | `ordersmp.net` | `19132` | en | 26.63 | Welcome, citizen. OrderSMP is a free survival server run by the Order: a calm, slightly too organized administration ... |
| [OreoMC](https://store.oreo.gg/) | `play.oreo.gg` | `19132` | en | 26.63 | OreoMC is a Java and Bedrock Survival + Lifesteal SMP! Designed from the ground up with custom content in mind. If yo... |
| [Origins Rebirth](https://originsrebirth.com) | `play.originsreborn.org` | `19132` | en | 26.63 | Embark on an extraordinary Minecraft journey with Origins Rebirth (Formally Origins Reborn), where the immersive Orig... |
| [OriginsReimagined](https://www.originsreimagined.com) | `server.originsreimagined.com` | `19240` | en | 26.63 | A fully original remake of the Origins mod! We update frequently with fun features. For more info go to originsreimag... |
| [Overy Network](https://overymc.fr/) | `play.overymc.fr` | `19132` | fr | 26.60 | Certains serveurs passent. D'autres marquent toute une génération.  Overy, c'est bien plus qu'un simple serveur Minec... |
| [OxinTowny 26.60](http://map.hbmc.net) | `oxin.hbmc.net` | `19132` | tr | 26.60 | 🇹🇷 OXINTOWNY \| BEDROCK TOWNY   Kendi kasabanı kur, topraklarını genişlet, ekonomini geliştir ve diğer oyuncularla bi... |
| [PaffMC - Lobby (Duels, FFA, KOTH)](https://paffmc.net) | `play.paffmc.net` | `19132` | en | 26.60 | French Bedrock PvP server: ranked duels with Elo, FFA, KOTH, loot zones and world bosses. Free, no pay-to-win. Join: ... |
| [Paladium](https://paladium-pvp.fr/) | `play.paladium-bedrock.fr` | `19132` | fr | 26.50 | Aucune description. |
| [PELAR Bedrockis](http://pelar.ee) | `mc.pelar.ee` | `19132` | en | 26.63 | Pelar on kõige vanem tegutsev Minecrafti server Eestis!   Meid tuntakse kogenud meeskonna, mõnusa mängijaskonna ja hu... |
| [Pigraid](http://pigraid.gg) | `pigraid.gg` | `19132` | en | 26.10 | One of the original Minecraft Bedrock Edition servers, we offer a rich KitPvP experience which is not Pay2Win, you ca... |
| [Pillars](http://Newcitymc.site) | `Play.newcitymc.site` | `19132` | en | 26.50 | Aucune description. |
| [PinnaMC PRISON SAISON 1](https://pinnamc.com) | `play.pinnamc.com` | `19132` | en | 26.60 | PinnaMC is a Prison OP server you can play in your own language: English, Français, Español, Deutsch, Português, Ital... |
| [PINOY SMP](https://discord.gg/g4UbY6AdT) | `15.204.150.91` | `20427` | en | 0.15.10 alpha | PinoySMP, Survival, pvp, normal playing join now here. By Photonoobie  No hacks  Lifesteal  survival |
| Pio Valenzuela UnOfficial Self Hosted Dedicated Server | `147.185.221.225` | `34876` | en | 26.52 | Aucune description. |
| [PixelCraft \| Updeta New!! ( 0.14x 0.15.10 ) Plugin Clan New :)](https://discord.gg/VasnXCr86) | `93.115.106.210` | `3509` | ar | 0.15.10 alpha | Owners   Taha  Mohamad  https://discord.gg/VasnXCr86 |
| pixelsky.blazebr.xyz \| 19132 | `pvmg.blazebr.xyz` | `19138` | es | 0.15.10 alpha | Português(Brazil)   Atualizado 2025!  MiniGames (10 MiniGames):  BedWars  SkyWars  TheBridge  MlgBlock, Entre outros ... |
| [PixelZone \| Uptime: 1hr 1min 8sec v0.14.x - v0.15.10](http://xewes99418@aratrin.com) | `Pixelatedzones.ddns.net` | `7530` | ar | 0.15.10 alpha | 🌟 ₱ƗӾɆⱠƵØ₦Ɇ \| العودة إلى الأيام الذهبية! 🌟 📱 الإصدارات المدعومة: MCPE 0.14.x & 0.15.10 ━━━ [ الوصف باللغة العربية ] ... |
| [PLANET BEACON \| 26.3 \| Cross-Play ✦✦ Earth Towny ✦✦ Skyblock ✦✦ and more! ✦✦](https://planetbeacon.minesite.org/) | `planetbeacon.ddns.net` | `19132` | en | 26.63 | This is a new and improved [26.3] Planet Beacon server as a new legacy! This server has SKYBLOCK, CREATIVE PLOTS, SUR... |
| [Playblocks](https://store.playblocks.net) | `pe.playblocks.net` | `19132` | en | 26.60 | Playblocks  Here is a list of features for everyone to look forward to:  ■ POWER SMP REALM: BECOME A SUPER HERO! Choo... |
| PlayNova RenasBey ve Pikachu 0.14.3 ü bıraktı | `playnova.best` | `19132` | en | 0.15.10 alpha | This server is a very nice and carefully prepared global server with language support. |
| PlayVerse 0/100 | `playverse.blazebr.xyz` | `26811` | pt-BR | 0.15.10 alpha | Aucune description. |
| [Plutonium S1](https://www.plutonium.best/) | `mcpe.plutonium.best` | `19132` | fr | 26.60 | Plutonium : L'Expérience PvP Faction incontournable   Plutonium s'est imposé comme une référence historique parmi les... |
| Plutoo | `plutoo.mcbe.fr` | `19142` | en | 26.45 | Aucune description. |
| PMC9f929fb64963c22a3ed0fdb4b0f93c0c | `play.denxycraft.org` | `25565` | en | Minecraft Java | Aucune description. |
| PMCf40191f92d9444c1950a278dc7b93c31 | `play.bloxblast.net` | `19132` | en | 26.52 | BloxBlast SMP Your Survival Adventure  Welcome to BloxBlast SMP, a Minecraft survival server where you can explore, b... |
| PocketMC FF \| Season: 1 | `PM.pocketmc.net` | `10046` | en | 0.15.10 alpha | Minecraft 0.14.3 - 0.15.10 the best server  LifeSteal-UHC-PvP Alpha-buy item/sell item-Shop gui-Free Fire all ranks-F... |
| [PocketMine-MP Server](https://store.legionmc.uk/) | `play.legionmc.uk` | `19132` | en | 26.50 | Legion Network is a friendly and fun-loving community with Gamemodes for everyone to play! We support both Java and B... |
| PocketMine-MP Server | `caraillenoir.com` | `19132` | fr | 26.50 | Aucune description. |
| PocketMine-MP Server | `azeri.mcbe.fr` | `19137` | fr | 26.45 | Aucune description. |
| PocketMine-MP Server | `myno.mclobby.fr` | `19132` | fr | 26.50 | ** # Myno Network **   *Myno est un Network créé en 2026, avec pour but de révolutionner MCBE avec plusieurs mode de ... |
| PocketMine-MP Server | `82.153.202.184` | `19134` | fr | 26.50 | ** # Elyndra V5 **   *Elyndra est un serveur KitMap Bedrock fondé en 2025. Dont version 4 qui a déjà rassemblé plus d... |
| PocketMine-MP Server | `slayne-mcpe.fr` | `19132` | fr | 26.40 | Aucune description. |
| [PocketMine-MP Server](https://discord.gg/D6SAb3jcSE) | `practice.mcpe.fr` | `19132` | fr | 26.50 | Volcasia Practice est un serveur Minecraft Bedrock dédié au PvP compétitif et à l’entraînement. Affrontez d’autres jo... |
| PocketMine-MP Server | `94.130.13.217` | `40317` | en | 0.15.10 alpha | OneBlock |
| [PocketMine-MP Server](http://futonium.eu) | `play.futonium.eu` | `19132` | fr | 26.60 | FUTONIUM est un serveur Faction pour Minecraft Bedrock. Ouverture officielle le 21 octobre à 18 h.  Tu pars de zéro d... |
| [PocketMine-MP Server](https://earthreborn.fr/) | `play.earthreborn.fr` | `19132` | fr | 26.60 | EarthReborn est un serveur Minecraft Bedrock Earth où chaque joueur peut créer sa nation, développer son économie, no... |
| PocketMine-MP Server | `2.192.197.161` | `19132` | it | 1.21.70 | Server di tigre96tbf  Dopo che Dany ha chiuso il suo server (Il Dany Game Server) la maggior parte degli staffers di ... |
| [PocketMobs \| SEASON 1 \| The #1 Bedrock Pokémon Server](https://store.pocketmobs.com) | `play.pocketmobs.com` | `19132` | en | 26.60 | PocketMobs is a Pokémon server for Minecraft Bedrock, on phone, Xbox, PlayStation, Switch and PC.  Season 1 is live: ... |
| [PokeBedrock](http://pokebedrock.com) | `play.pokebedrock.com` | `19132` | en | 26.60 | In the first time ever, anyone can play Pokemon on Minecraft Bedrock. Our servers are running at highest speed so you... |
| [PokéFind](https://www.pokefind.co/) | `play.pokefind.co` | `19132` | en | 26.63 | Join thousands of Trainers on our New Server, PokeFind! PokeFind is a combination of Pokemon Games and some Pokemon G... |
| [Pokémania](https://pokemania.cc/) | `pokemania.cc` | `19132` | fr | 26.63 | POKÉMANIA SAISON 1 — L’AVENTURE COMMENCE !  Tu rêves de devenir le meilleur dresseur Pokemon ?  Alors prépare-toi à d... |
| [PortalWix Born in 2 february 2023!](http://www.bluegs.xyz) | `play.bluegs.xyz` | `19132` | en | 0.15.10 alpha | Enjoy a new experience in mcpe!, BlueGames takes inspiration entirely from HypixelPE and have created a perfect found... |
| [PortalWix Born in 2 february 2023!](https://info.veozax.xyz) | `vZSMP.minecraft.pe` | `19132` | es | 0.15.10 alpha | E vuelto , el mejor servidor que e creado va a volver 0.14.3 x 0.15.10 todo mejor todo actualizado todo vuelve |
| [PortalWix Born in 2 february 2023!](https://portalwix.com/) | `portalwix.com` | `19132` | en | 0.15.10 alpha | Aucune description. |
| [Potato Games](https://www.potatogames.site) | `potatogames.mc.gg` | `34115` | en | 26.63 | Welcome to Potato Games- an amazing Minecraft Bedrock Minigame server! Unlike other Minigame servers, Potato Games re... |
| Power By AetherAPI [20] §0- Blocks Blocks Blocks! | `2b2t.nthr.cc` | `25693` | es | 0.15.10 alpha | Server anarquico para Craftsman 0.15.10 |
| PowerNukkitX Server | `landazia.fr` | `19132` | fr | 26.60 | # _**LANDAZIA KITMAP OG**_  ------------------------------------  **Landazia** est un serveur Minecraft Bedrock innov... |
| [PowerNukkitX Server](https://discord.gg/7Y6PTsNnaS) | `endionium.mcbe.fr` | `19132` | fr | 26.60 | Aucune description. |
| PowerNukkitX Server | `volt.mcbe.fr` | `19132` | fr | 26.60 | Le meilleur kitmap en 2026 ! |
| PowerNukkitX Server | `root-mcbe.fr` | `19133` | fr | 26.60 | Aucune description. |
| PowerNukkitX Server | `gm1-wh16.wh-game.net` | `19135` | fr | 26.50 | KUNAY KITMAP — UN NOUVEAU DÉPART  Kunay revient avec une ambition claire : relancer le KitMap Bedrock et proposer une... |
| [PowerNukkitX Server](https://palakitmap.wh-web.fr/) | `palakitmap.eu` | `19136` | fr | 26.50 | Aucune description. |
| PowerNukkitX Server | `artelia.mcbe.fr` | `19132` | ja | 26.50 | ⛓️・ARTELIA PRISON 💎  🔮 Bienvenue à Artelia, une prison pas comme les autres…  ⛏️ Mine. 💰 Gagne. 📈 Progresse. 👑 Domine... |
| PowerNukkitX Server | `play.ploto.fr` | `19132` | fr | 26.60 | Le meilleur kitmap français inspiré du serveur Paladium pour son Clicker et de Plutonium pour sa Boule de Neige infin... |
| [PROJECTS](https://projects.gg) | `play.projects.gg` | `19132` | tr | 26.60 | 🗺️ 1.16.5-26.2 Survival & Skyblock & Hunger Games (26.2 Tabanlı)  🔹 IP: mc.projects.gg / Site: https://projects.gg/  ... |
| [PROVANAS » discord.gg/provanas [1.21.8+]](https://www.provanas.com) | `mobil.provanas.com` | `19132` | tr | 26.51 | Survival Vadi \| SkyBlock Aincrad \| BoxPvp \| SMP  Serüvenimize 2014 yılında survival ile başlamış olmaktan gurur du... |
| [PROWNETWORK](https://be.prownetwork.net/) | `play.prownetwork.net` | `19132` | id | 26.52 | Aucune description. |
| [PROWNETWORK](https://prownetwork.net/) | `be.prownetwork.net` | `19132` | id | 26.52 | ProwNetwork adalah server Minecraft Indonesia yang berdiri sejak tahun 2020. Selama bertahun-tahun, ProwNetwork telah... |
| [PVPSMP - pvpsmp.com](https://www.pvpsmp.com) | `mcps.pvpsmp.net` | `19132` | en | 26.52 | PVPSMP is a dual-mode server network with one shared economy and a ton of great features. Players can choose and easi... |
| [pvpTH&gt;&gt;&gt;&gt;&gt;[Loy Krathong Festival]](https://pvp-th--guestMC.replit.app/) | `pvpth.ddns.net` | `7406` | en | 0.15.10 alpha | ​⚔️ pvpTH — The Ultimate Thai MCPE PvP Experience! 🇹🇭🌐  ​Get ready for hardcore action! pvpTH is back for Minecraft P... |
| QuarrionCraft SMP | `23.230.3.105` | `19132` | en | 26.40 | QuarrionCraft is a small vanilla+ semi-anarchy survival server built to keep Minecraft feeling like Minecraft, lightl... |
| Radium | `radium.mcbe.fr` | `19177` | fr | 26.60 | Radium est un serveur Minecraft Bedrock PvP Faction proposant une expérience complète mêlant combat, stratégie, écono... |
| RAGEMINE | `tpm.ragemine.net` | `19132` | es | 26.45 | Accesibilidad Atlética Total La profunda devoción por la actividad física que define el carácter del ciudadano venezo... |
| [RainyPvP](https://rainypvp.net) | `play.rainypvp.net` | `19132` | en | 26.60 | RainyPvP  Looking for a Bedrock Server with multiple features and creative ideas? We got all of that!  It Contains:  ... |
| RANKS! KITS! PURE VANILLA | `170.23.77.107` | `25584` | en | 26.62 | REVIVE SMP!  A hardcore civilization world with Kingdoms, wars, and storylines, but all unscripted! Proximity text ch... |
| [RayBigWorld • Friendly SMP](https://map.raybigworld.duckdns.org/) | `raybigworld.duckdns.org` | `19132` | en | 26.63 | RayBigWorld is a cross-play survival SMP that connects Java and Bedrock players on a single shared world. Built for f... |
| [REDE REVO [1.12 - 26.2] 🍃 NOVA ᴛᴇᴍᴘᴏʀᴀᴅᴀ ɴóʀᴅɪᴄᴀ (xxɪɪ) - ᴏ ɪɴᴠᴇʀɴᴏ ᴄʜᴇɢᴏᴜ!](https://rederevo.com) | `jogar.rederevo.com` | `19132` | pt-BR | 26.60 | Bem-Vindos a Rede Revo, a rede de servidores mais incrível que você já encontrou.  Aceitamos jogadores da 1.12 até a ... |
| [RELEASED - ORANGE SMP - HIGH QUALITY](https://discord.gg/orangesmpde) | `5.231.74.57` | `19132` | de | 26.62 | 🔥 ORANGE SMP — HIGH QUALITY CROSSPLAY SMP 🔥  Willkommen auf ORANGE SMP – dem Survival-SMP, auf dem Java und Bedrock z... |
| [RENDERYCRAFTY 2026](http://renderycrafty.pages.dev) | `erci.ilkom.tech` | `19132` | en | 26.51 | RenderyCrafty Server  Survival Multiplayer  RenderyCrafty, also known as RC Server, is a survival Minecraft server lo... |
| [RESTLESS Network [1.8-26.3]](https://restlessmc.net/join/) | `play.restlessmc.net` | `19132` | en | 26.52 | Restless MC is a Java + Bedrock network built around three different experiences: Kingdom SMP, Heartfall Lifesteal, a... |
| [RetireX Online](https://cybox.kr) | `cybox.kr` | `19132` | en | 26.60 | RETIREX ONLINE  Drift through corners. Boost down the straight. Race inside Minecraft.  RetireX Online is a custom ka... |
| [Retro&#039;s Factions](https://retrosfactions.net) | `play.retrosfactions.net` | `443` | en | 26.51 | Retro's Factions is an old-school Factions server. I first ran it in 2020 and rebuilt it from scratch in 2026. Bedroc... |
| Retronix | `retronix.club` | `19132` | en | 26.60 | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐑𝐞𝐭𝐫𝐨𝐧𝐢𝐱 — 𝐁𝐫𝐢𝐧𝐠𝐢𝐧𝐠 𝐁𝐚𝐜𝐤 𝐏𝐯𝐏 𝐢𝐧 𝟐𝟎𝟐𝟔!  𝐖𝐡𝐚𝐭 𝐢𝐬 𝐑𝐞𝐭𝐫𝐨𝐧𝐢𝐱..?  Retronix is a Minecraft: Pocket Edition (MCPE)... |
| [RevengeTech \| SkyBlock &amp; Prison](https://revengetech.net/mcps) | `play.revengetech.net` | `19140` | en | 26.60 | Game modes:  - SkyBlock: grow your island, build generators, fight in the Warzone and KOTH  - Prison: mine, rank up a... |
| [RevivalSMP](https://revivalsmp.net) | `revivalsmp.net` | `19132` | en | 26.51 | RevivalSMP — Lifesteal Survival   Steal hearts. Survive the competition. Become a legend.   What We Offer:   • Lifest... |
| [RevolutionWorlds](http://revolutionworlds.xyz) | `revolutionworlds.xyz` | `19132` | pt-BR | 26.60 | Servidor de MiniGames Versão Bedrock e Java  TNTRUN  PARKOUR  FACTIONS  PVP  SKYWARS  BEDWARS  BUILDBATTLE  HIDE AND ... |
| [Revora Server](https://discord.gg/bV8VGDTFfN) | `15.204.22.45` | `25577` | en | 26.52 | Welcome to Poke Revora, a custom Minecraft Bedrock Pokémon experience powered by Poke Revival and created by Legendar... |
| [ReySMP \| 0.14.3 - 0.15.10 - 1.1.x](https://www.mediafire.com/file/9m3sqm5a0e8kr3o/Pack_De_Plugins_By_AffzKiller.zip/file) | `ReySMP.ddns.net` | `10026` | en | 0.15.10 alpha | 🚨🔥 **REYSMP — OFFICIAL GRAND LAUNCH!** 🔥🚨  ❤️ LIFESTEAL SURVIVAL IS NOW LIVE! ❤️  @everyone @here  🎉 THE WAIT IS OVER... |
| [RezzCraft pull up a chair, friend](https://www.rezzcraft.us/) | `bedrock.rezzcraft.us` | `19132` | en | 26.60 | [Bedrock & Java] RezzCraft - Friendly Survival SMP \| Land Claims, Player Shops, Daily Quests  Looking for a long-ter... |
| [RIVERSMP ➠ store.rivernetwork.net](https://store.rivernetwork.net) | `rivernetwork.net` | `19132` | en | 26.60 | 🌊 RiverNetwork SMP – The Best SMP Experience! 🌊  RiverNetwork SMP isn’t just another Minecraft server – it’s the best... |
| [RolePlay \| Season 3](http://axiomlandpe.ir) | `Play.AxiomLand.IR` | `19132` | en | 1.21.100 | rubika : @AxiomLand |
| Rootakses SMP | `play.rootakses.my.id` | `23719` | id | 26.52 | Tautan Grup:  https://chat.whatsapp.com/LYqu9Y0eksRKueoRSKDHJX?s=cl&p=a&mlu=4&iam=0  Aturan yang wajib lu ketahui seb... |
| [RuinSpirit Server Network](https://ruinspirit.net) | `mc.ruinspirit.net` | `19132` | de | 26.62 | Willkommen auf RuinSpirit – Dein neues Minecraft-Heim!  Java: mc.ruinspirit.net  Bedrock: mc.ruinspirit.net:19132  Ha... |
| [RulerCraft ♦ The World Is Yours ♦](https://www.rulercraft.com) | `play.rulercraft.com` | `25565` | en | 26.60 | What RulerCraft offers:  Earth:  - Full scale world of Earth with all continents, ores and different biomes.  Towny: ... |
| RulerMC » SMP &amp; Practice [1.8 - 26.3] | `play.rulermc.com` | `19132` | en | 26.62 | 🌍 SMP  A fresh survival world built for long-term play:  • Teams: build a crew and fight for the top  • Skills, level... |
| SA CRAFTERS NETWORK [26.2] | `mc.playmc.co.za` | `19132` | en | 26.51 | Welcome to SA Crafters! SA's best Minecraft server.  Join IP: playmc.co.za  Bedrock IP: mc.playmc.co.za  Bedrock Port... |
| [SABATO alle 18:00....](http://titanet.it) | `mc.titanet.it` | `19132` | it | 26.63 | Un NUOVO modo di giocare a Minecraft ⚡  Survival+ ⚡ una Survival Earth Moddata MA SENZA MOD! Mappa del Mondo Reale!  ... |
| [Sakura Realms ✿](https://store.sakurarealms.net) | `mp.sakurarealms.net` | `19132` | en | 26.62 | Sakura Realms ｡･::･ﾟ★ - an enhanced vanilla smp server! [​Latest Version]  Ever wish Mojang would add simple things t... |
| SakuraLand Practice | `prac.sakuraland.net` | `19132` | zh | 0.15.10 alpha | 0.14.3-0.15.10 MCPE pvp server |
| [Saloon Network Minecraft Sunucuları](https://saloonnetwork.com) | `play.saloonnetwork.com` | `19132` | tr | 26.62 | ŞİMDİ YENİ OYUN CAPTIVE (BOXED) DE SİZLERLE! DÜNYADA İLK DEFA SALOON NETWORK'TE!  Saloon Network 2018 yılında temelle... |
| Saturnian Wolves [1.21.8+] | `play.saturnianwolves.xyz` | `19132` | en | 26.52 | Saturnian Wolves SMP  Fresh Java + Bedrock Crossplay Survival  Saturnian Wolves SMP is a fresh survival server built ... |
| [SavagePvP 0.14.3 X 0.15.10](http://FreeMCHosting) | `92.119.165.177` | `7300` | en | 0.15.10 alpha | Hey Guys SavagePvP is PvPModes + LifeSteal fight Servers  Here We Make Events and other Cool Thinges players : Like  ... |
| [SB Network Hub](http://sbpvp.com) | `play.sbpvp.com` | `19132` | en | 26.50 | SB Network is a Minecraft Bedrock network built around competitive PvP and a high-quality multiplayer experience.  ⚔️... |
| ScannerPlay.com Server-1 [Latest] | `s1.minecraft-be.scannerplay.com` | `19132` | en | 1.20.32 | Latest version |
| ScannerPlay.com Server-2 [1.19.21.01] | `s2.minecraft-be.scannerplay.com` | `19133` | en | 1.19.21 | 1.19.21.01 version |
| SchlaflosGames \| CityBuild • API5 | `schlaflosgames.de` | `19132` | de | 26.60 | Du suchst ein Server auf dem Freundlichkeit, Hilfsbereitschaft und Spaß an erster Stelle stehen?  Dann bist Du bei un... |
| [Schradernator SMP Survival · Skyblock · Creative · Minigames](https://mc.schradernator.com/?src=smp-list-mcps) | `play.schradernator.com` | `19132` | en | 26.60 | Schradernator SMP is a free Minecraft Bedrock server that opened in October 2026.  HOW TO JOIN  Address: play.schrade... |
| [SEACRAFT Survival SMP](https://minecraftpocket-servers.com/) | `202.93.247.6` | `19132` | id | 26.32 | 🌊 SEACRAFT — Survival SMP (Bedrock & Java Cross-Play)  Selamat datang di SEACRAFT! Server survival komunitas yang ram... |
| Seas ✦ #1 Server Indonesia ★ | `seasia.fun` | `19132` | id | 26.50 | Aucune description. |
| Season 2, The New Dawn. | `168.119.88.183` | `7024` | en | 26.61 | IMPORTANT!  -The server will reset soon and add support for both Bedrock and Java edition!  FallenMC \| Non-Toxic Bed... |
| [SECRET SMP ╰┈➤ SURVIVAL S4 RELEASED](https://secretsmp.fun/) | `play.secretsmp.fun` | `2017` | en | Minecraft Java | hi |
| SEKAISMP | `sekai.hopto.org` | `19132` | id | 26.60 | Aucune description. |
| [SemiSurvivalCraft](https://www.semisurvivalcraft.com) | `mp.semisurvivalcraft.com` | `19132` | en | 26.63 | SemiSurvivalCraft  Welcome to SemiSurvivalCraft! We're a Cross Platform Semi Vanilla Survival Minecraft server with a... |
| [SERB-CRAFT](https://www.serb-craft.com) | `pe.serb-craft.com` | `19132` | en | 26.62 | Welcome to SERB-CRAFT! Balkan server with its own AntiCheat!  We offer a wide variety of fun servers ranging from Sur... |
| Serelia - V1 | `serelia.mcbe.fr` | `19161` | fr | 26.60 | Aucune description. |
| Server | `83.147.217.194` | `19132` | en | 26.60 | Server IP Address   83.147.217.194  Port  19132  Join fractured SMP we have Java PvP and a starter kit plus a beautif... |
| [Server is online](https://miranasmp.com) | `play.miranasmp.com` | `19132` | en | 26.63 | MiranaSMP is a bedrock survival server hosted in Singapore, with low ping for players in the Singapore, Malaysia, Ind... |
| Server is Shutting down.. | `play.starcrestmc.net` | `17330` | en | Minecraft Java | We are a new and upcoming towny-style server with kitpvp, plots, bedwars, survival and more, our goal is to be 100% n... |
| [Server online!](http://Forum.glmidnight.co.uk) | `play.glmidnight.co.uk` | `19132` | en | 1.20.70 | GL Midnight's SMP offers you:  - 24/7!  - Infraction History (Web)  - TPA system  - Unlimited homes  - Discord Server... |
| [Server Unreachable](https://craftbit.net) | `play.craftbit.net` | `19132` | en | 1.0.0 | We're a new and upcoming Minecraft server that supports both Java and Bedrock edition. Our server is aiming to give a... |
| [Servicraft: Towny con empresas, bancos y bolsa.](http://servicraft.org) | `servicraft.org` | `19132` | es | 26.51 | Bienvenido a Servicraft  ¡Te damos la bienvenida a Servicraft, un servidor de Minecraft que te ofrece una experiencia... |
| [Sezon 2! Baw się dobrze!](https://astoria.studio) | `mc.astoria.studio` | `19132` | pl | 26.60 | Tworzymy własne rozwiązania, dla wygody graczy obsługujemy wiele platform , w tym Windows, Android, iOS, Java, Xbox. ... |
| ShadowUHC : NEW MAPS | `ShadowUHCs.ddns.net` | `2327` | en | 0.15.10 alpha | Aucune description. |
| ShadowUHCs NEVER DIES!! | `92.119.165.177` | `6518` | en | 0.15.10 alpha | Aucune description. |
| [SHADOWYN ▸ Season 2 [ 1.20 - 1.21x ]](https://www.shadowyn.id/) | `shadowyn.id` | `19132` | id | 26.51 | Aucune description. |
| [SheepSMP 26.3](https://sheepsurvival.tebex.io) | `sheepsmp.com` | `19132` | en | 26.63 | A survival server that's totally "ewe"-nique!  Join the flock on a server where the fun never *shears* out! With cust... |
| [Shulkerboxes](http://chukerboxes.com) | `ivanos-076802.bedrock.shulkerboxes.com` | `19132` | pt-BR | 26.60 | Um mundo normal de survival.  Aviso: você nasce em um deserto |
| SIEGEWORKS \| Java and Bedrock | `siegeworks.net` | `25565` | en | 26.45 | Siegeworks is semi-anarchy survival where your base is safe most of the time, until it isn't.  Claim land for chunk b... |
| [Silvavita Smp](http://web.silvavita.id) | `silvavita.id` | `19132` | id | 26.62 | Aucune description. |
| SiphonMC | `Play.SiphonMC.net` | `19132` | en | 26.62 | Bedrock Server IP: Play.SiphonMC.net  Bedrock Server Port: 19132  -Leveling system, Skilling system, Player reward sy... |
| [SKYBARS \| АНАРХИЯ • ВЫЖИВАНИЕ • ОДИН БЛОК](https://skybars.me) | `mps.skybars.me` | `19132` | en | 26.60 | SkyBars - free Minecraft server for phone and PC. Bedrock (MCPE) and Java crossplay, versions 1.8 up to the latest.  ... |
| [SKYCRAFTERS 🎮 🖱 [26.2]](http://skycraftermc.net) | `play.skycraftersmc.net` | `19132` | en | 26.63 | Skycrafters is a crossplay Minecraft network where Java and Bedrock players build side by side. Hosted in an Australi... |
| [SkyHold](https://skyhold.in) | `skyhold.in` | `19132` | en | 26.51 | Welcome to SkyHold, a skyblock server for Minecraft Bedrock Edition. Start on a block of grass over the void and grow... |
| [SlothCraft Bedrock](http://Slothiesdevelopment.com) | `161.129.180.25` | `19132` | en | 26.60 | an anarchy server |
| [SMILEMORECRAFT [26.3+] NEW DUNGEONS SOON](https://www.smilemorecraft.com/) | `mc.smilemorecraft.com` | `19132` | en | 26.63 | Come join the fastest growing SMP on Minecraft! 💖 SmileMoreCraft is a 1.21+ Survival Server that NEVER WIPES! We have... |
| [SMP SERVER](https://www.astrocraft.org) | `mcps.astrocraft.org` | `19132` | en | 26.60 | 🌌 Astro SMP – Where the Entire Server Shapes the World  The world doesn't start infinite... you unlock it together.  ... |
| [SMPSSB](https://bongsb.site/) | `147.185.221.26` | `49219` | en | 26.60 | SUPPORT ONLY BEDROCK FOR CHILL CHIL Last version.  Online 24/7, disable ping/online player.  Please join and enjoy  A... |
| [Snug SMP](https://store.snugsmp.com) | `mc.snugsmp.com` | `19132` | en | 26.60 | SnugSMP has been running for around eight months and regularly has 20 to 50 players online, so there is almost always... |
| SolCraft SMP disc meta returns! | `sol-craft.xyz` | `19132` | en | 26.60 | Java & bedrock! Voice chat support  No grief  Very few commands and economy can be entirely ignored!  Great hardware ... |
| Solstad | `solstad.kildal.net` | `19132` | en | 26.63 | Vanilla bedrock server, restarted every night @4 CET for backup and upgrade build. Has been running from about Bedroc... |
| [Something smells fishy...](https://discord.fishy.gg) | `smp.fishy.gg` | `19132` | en | 26.60 | 🎣 Fishy SMP — Java + Bedrock Cross-Play Survival  Cast your line, stay a while.  One world, every platform. Join from... |
| Sonaba | `sonaba.net` | `19132` | en | 26.50 | Welcome to Sonaba Network.  The first and ever practice server to support 1.18+ bedrock versions with tons of default... |
| [SoulCraft транспорт, кирки 3x3](http://soulcraft-pe.ru) | `soulcraft-pe.ru` | `19132` | en | 26.0 | Start playing SoulCraft now!   Vote Reward /kit bonus  INFO =) For playing get into the portal!  1 portal= Server Sur... |
| [SparklyPower](https://sparklypower.net/) | `ps.sparklypower.net` | `19132` | pt-BR | 26.60 | SparklyPower, o melhor servidor de Minecraft Survival brasileiro, com crossplay PC e celular. Desde 2014 trazendo Sur... |
| Spicy SMP | `Spicysmp.revivehost.net` | `2248` | en | 26.45 | 🌶️ SPICY SMP · Custom 1.21.11 · Java + Bedrock  Build without losing it. Fight when you want to.  🏗️ Builder's Bag ho... |
| SpiderUHCs \| NEW MAPS | `45.142.104.112` | `8008` | en | 0.15.10 alpha | SpiderUHCs — PvP Practice Server  SpiderUHCs is a fresh Minecraft PvP practice server focused on competitive fights, ... |
| SpiderUHCs \| NEW MAPS | `SpiderUHCs.ddns.net` | `8008` | en | 0.15.10 alpha | SpiderUHCs — PvP Practice Server  SpiderUHCs is a fresh Minecraft PvP practice server focused on competitive fights, ... |
| SPIDERWIX Open world S8 - 0.15.10 | `sw.ddns.net` | `6468` | en | 0.15.10 alpha | 🔥 𝐍𝐎𝐓 𝐉𝐔𝐒𝐓 𝐀 𝐒𝐄𝐑𝐕𝐄𝐑, 𝐈𝐓'𝐒 𝐀 𝐋𝐄𝐆𝐀𝐂𝐘. 👑 \| 𝐒𝐏𝐈𝐃𝐄𝐑𝐖𝐈𝐗 ⚔️ \| 𝐌𝐂𝐏𝐄 0.15.10 🕷️ |
| [SplitCraft SMP](https://splitcraft.net/) | `mc.splitcraft.net` | `19132` | en | 26.62 | 🌸 SplitCraft 🌸  Build under the starry sky  splitcraft.net • Java + Bedrock, consoles too  Survival, but it actually ... |
| [SpX Gaming Official Server](https://minecraft.spxgaming.it) | `bedrock.spxgaming.it` | `26494` | it | 26.60 | ⚡ SPX GAMING — OLTRE LA SOLITA SURVIVAL  Dimentica il Minecraft di sempre. Su SpX Gaming la Survival prende una nuova... |
| StablePVP 1.21+ | `voidsmp.me` | `19132` | en | 26.60 | **Void SMP** (BLISS PLUGIN)  JAVA AND BEDROCK CAN JOIN   BLISS PLUGIN  No Crystal / Anchor PVP  EU Region  Weekly Eve... |
| [stacksanarchy](https://discord.gg/T8TvHmvSN) | `Stacksanarchy.mcserv.me` | `19132` | en | 26.52 | StacksAnarchy is a fun anarchy server that anyone can play!  Have fun doing whatever you want. You can be a builder, ... |
| StarCraft S2 | `5.39.63.207` | `3729` | en | 0.15.10 alpha | 🔥 StarCraft Survival — Pure Survival Vibes 🔥  Ek asli vanilla survival experience jahan skill hi sab kuch hai! 💥  ⚔️ ... |
| [StarLight Network OPEN BACK!!!](http://starlightmc.net) | `play.starlightmc.net` | `19132` | en | 26.60 | ✨ WELCOME TO STARLIGHT NETWORK ✨  The Most Aesthetic & Premium Minecraft Bedrock Experience  Why play on StarLight? S... |
| Stelar Survival v0.15 - S 1 Halloween | `stelar.sytes.net` | `25888` | es | 0.15.10 alpha | Un servidor de survival mixto, con rankup y economía y mucho más que ofrece una experiencia vanilla para 0.15.10 y 0.... |
| [StormyLand Survival Season 11](https://stormyland.org) | `survival.stormyland.org` | `19132` | en | 26.63 | NOTE: This is a Whitelisted Server, you need to join the StormyLand Discord, and either message me or submit your Gam... |
| StrenghtSMP Season 5 | `Strengthsmp.ddns.net` | `10017` | en | 0.15.10 alpha | Aucune description. |
| [STWMCPE - Clavas &amp; Elytra&#039;s (1.7.4 BETA)](http://dsc.gg/stwmcpe) | `stwmcpebr.ddns.net` | `25986` | pt-BR | 26.60 | Aucune description. |
| [SunRealms (ɴᴇᴡ) PRISON S6 RELEASING NOW](https://sunrealms.net) | `mps.sunrealms.net` | `19132` | en | 26.63 | SunRealms - Best Minecraft Gens, Prison, Skyblock, Survival, Dungeons & Cobblemon Server 2026  IP: mps.sunrealms.net ... |
| [SuomiCraft PE](https://suomicraftpe.ddns.net/) | `suomicraftpe.ddns.net` | `19132` | en | 26.60 | SuomiCraft PE is a Finnish Minecraft Bedrock Edition server featuring various minigames and gamemodes.  We have on th... |
| SuperLand CiTy - v0.14 x 0.15 | `SuperLandCiTy.ddns.net` | `25575` | es | 0.15.10 alpha | 🔥 ¡EL SURVIVAL MÁS ÉPICO DE CRAFTSMAN! 🔥  🎮 SuperLand CiTy \| 100% supervivencia con mecánicas únicas \| V. 0.15.10 y... |
| Survival | `160.191.77.60` | `10907` | en | 0.15.10 alpha | Survival Server \| Mcpe & Craftsman v0.14x - 0.15.10! |
| [Survival - Oneblock - Dungeons](https://store.revonicmc.com) | `play.revonicmc.com` | `19132` | en | 26.63 | Welcome to RevonicMC – your gateway to boundless adventure!  BEDROCK SUPPORTED  Stay Connected:  • IP: play.revonicmc... |
| [Survival - Oneblock - Dungeons](http://wildphire.net) | `play.wildphire.net` | `19132` | en | 26.63 | Wildphire is a talented and passionate team dedicated to creating top-tier content for the Minecraft Marketplace. Fro... |
| [Survival - Oneblock - Dungeons](https://www.utopiverse.net) | `play.utopiverse.net` | `19132` | en | 26.63 | ADD "Utopiverse" AS A FRIEND!  Who are we?  We are an extensive Minecraft network that offers players a unique gamepl... |
| [SurvivalMC - Halloween](https://discord.gg/M4VHcGPxz9) | `SurvivalMC.minecraft.pe` | `10698` | en | 0.15.10 alpha | Fully Survival!!! |
| [SurvivalSF SkyBlockSF VanillaPlus](https://sourcemc.com.br/) | `jogar.sourcemc.com.br` | `10309` | it | 26.60 | Minecraft Vanilla  Explore um vasto mundo cheio de maravilhas naturais, onde você pode construir, minerar e descobrir... |
| SurvivalTopia - A Minecraft MMORPG | `survivaltopiagame.play-network.io` | `9040` | en | 26.63 | SurvivalTopia 🌍⚔️ is a 100% No Pay-To-Win Minecraft MMORPG server!  Fight epic monsters 🐉, earn powerful weapons & ar... |
| [SurViValVanila](https://discord.gg/74p6MHAKv7) | `survanila.ddns.net` | `19003` | en | 26.52 | Build & Chill in Survival Server and Endstone Server in Vietnam |
| [sVanilla Survival](http://corn.gg) | `corn.gg` | `19132` | en | 26.63 | sVanilla Survival goes back to the roots of what a Semi-Vanilla SMP should be. Vanilla, with few quality of life modi... |
| [SwiftServers \| Free Minecraft servers](https://samplecraft.net) | `pixelattack.swiftservers.org` | `19132` | de | 26.60 | **Willkommen auf unserem Minecraft‑SMP!**   Unser Server bietet dir ein Survival‑Erlebnis, das deutlich über das hina... |
| sᴛᴀʀᴍᴄᴠɴ.ᴄᴏᴍ - 1.18.2 » 1.21+ | `starmcvn.com` | `19132` | en | 26.51 | Aucune description. |
| [sᴛᴀʀᴍᴄᴠɴ.ᴄᴏᴍ - 1.18.2 » 1.21+](http://starmcvn.com/) | `Pe.starmcvn.com` | `19132` | en | 26.51 | STARMCVN NETWORK [1.16.5 - 1.19+]  Discord: starmcvn.com/discord  Đây là server chơi chung giữ mcpc và mcbe  Server k... |
| [TalonMC \| SKYBLOCK JUST RELEASED!](https://www.talonmc.net) | `bedrock.talonmc.net` | `19132` | en | 26.60 | TalonMC is the ultimate Minecraft Prison & Skyblock experience, built BY the community, FOR the community! We offer a... |
| [Tavern](https://tavernmc.net) | `tavernmc.net` | `19132` | en | 26.60 | Dive into a unique survival experience where PVPers and PVErs thrive! Level up your skills, battle epic bosses, conqu... |
| [TB craft the best server!](https://tbstudio.be/en-US/Minecraft/TBCraft/Home) | `play.tbstudio.be` | `19132` | en | 26.60 | TB Craft  Step into the world of TB Craft, the ultimate survival & community server for Minecraft Bedrock Edition!  P... |
| TC Test Server | `tcminecraft.net` | `25652` | en | 26.60 | Hello,    I'm BobbyTowers and this is the test server for TowersCraft. Join and test stuff or try to crash the server! |
| Teebz Linux Place | `teebz.serveminecraft.net` | `19150` | en | 26.60 | Unofficial server with pokemon in Minecraft bedrock |
| [TerminaMC.com](https://TerminaMC.com) | `TerminaMC.com` | `19132` | en | 26.60 | 🏰 WILL YOU BE THE HERO OR THE VILLAIN? 🔥  The world of Termina is yours to shape. Will you build a thriving town and ... |
| Terra | `terra.playcelestial.net` | `19137` | en | 26.51 | Aucune description. |
| [TerraeMC](https://terraemc.net) | `play.terraemc.net` | `19132` | en | 26.45 | Looking for a Minecraft server that offers a unique and exciting survival experience on both Bedrock and Java edition... |
| [The Blockade Network](https://theblockcade.com) | `play.theblockcade.com` | `20076` | en | 26.60 | The Blockcade is a cross-play Minecraft network for Java and Bedrock players.  LifeSteal: Kill players to steal their... |
| The greatest server, some might say | `seaberria.cloud-ip.cc` | `19132` | en | 26.62 | Seaberria is a semi-vanilla server (vanilla with quality of life plugins) for both Java and Bedrock players.  It was ... |
| The heavan Reborn. | `rth2.ddns.net` | `19132` | zh | 26.33 | 此房為重度模組房 怪物已不同以往請特別小心 (此房僅使用市集模組）  新增了數種別具風格的強大boss  還有新礦洞 新結構 新生態  各個模組細節都在開局說明書裡 請找個地方保留好 以備不時之需  後期有到下界推薦先挖石英 可合成強... |
| [The original Peaceful Vanilla Club experience](https://www.peacefulvanilla.club) | `bedrock.peacefulvanilla.club` | `19132` | en | 26.63 | ✅ No Fast Travel: Wander and Explore!  Say goodbye to teleportation on this semi-vanilla server. No /tp, /tpa, or /wa... |
| TheCloud Factions | `81.16.176.236` | `25583` | en | 26.51 | A bedrock only factions server with modern features and without the clutter and complicated gameplay!  Join Through F... |
| THEMCLIFE SMP \| Towny Survival Build a town. Live a life. - Java &amp; Bedrock | `TheMCLifeSMP.com` | `19132` | en | 26.60 | Hey! We're THEMCLIFE SMP, a small, friendly Towny survival server that Java and Bedrock players share.  **What you'll... |
| [TheNRK](https://nrkcraft.enjin.com) | `play.thenrk.net` | `19132` | en | 26.20 | TheNRKNetwork (1.7 - 1.16)About the server:TheNRK is the server that offers something that no other server brings, bu... |
| ThroneWix - S1 | `51.81.243.191` | `26121` | en | 0.15.10 alpha | Founder. @sh1v8m |
| [Timelapse PvP](https://discord.gg/FqQduhw33S) | `timelapsepvp.verixen.net` | `19132` | en | 26.60 | > Looking for a Bedrock Blurry’s Java PvP Server without all the clutter?   >   > Timelapse Network delivers smooth p... |
| [TopLand » 1.20.0 - 26.60 support!](https://toplandmc.ir) | `Play.TopLandMc.iR` | `19132` | en | 26.60 | Website » http://toplandmc.ir  Telegram » https://t.me/TopLandMc  Rubika » https://rubika.ir/TopLandMc |
| [TorchCraft.nl](https://www.torchcraft.nl/) | `play.torchcraft.nl` | `19132` | tr | 26.60 | TorchCraft is de gezelligste server van Nederland. Naast veel gezelligheid hebben we leuke (en unieke) gamemodes, sne... |
| [TorchlightMC](http://www.torchlightmc.net) | `torchlightmc.net` | `25576` | en | 26.60 | We are a PVE centered and protected crossplay server. We have proximity voice and a discord for communication. We hav... |
| Towers Craft. | `tcminecraft.com` | `25633` | en | 26.60 | TC Minecraft, is back! I bought a server! I just didn't want to have to host it my self anymore.  Just uploaded the O... |
| [ToxMania » Survival · Beta](https://www.toxmania.net) | `toxmania.net` | `19132` | en | 26.60 | ToxMania – player-driven Survival SMP for Bedrock & Java  Join: toxmania.net · Port 19132  Claims that really protect... |
| TR Survival v26.60+ KLANLAR! | `oyna.trsurvival.com.tr` | `19132` | tr | 26.61 | -Seviye ve rütbe sistemi  -Meslek Sistemi  -Hikaye Modu  -Kazgeliş  -Görevler |
| [TrashMCPE](http://discord.trashmcpe.com) | `play.trashmcpe.in` | `19132` | en | 26.45 | ENGLISH:  Hey you, do you know Trash MCPE? Let me introduce it to you :exclamation:  Trash MCPE is a India 1st Only M... |
| TropicMine | `tropicmine.net` | `19132` | de | 26.60 | TropicMine 🌴 – Dein Crossplay City-Build-Server für Java & Bedrock!  Baue deine Träume, verdiene Geld im Farmer-Shop,... |
| [TrovePrisons](https://www.troveprison.com) | `play.troveprison.com` | `25634` | en | 26.61 | ⛏️ Trove Prisons  A Bedrock prison server where every block counts.  Mine. Sell. Rank up. Prestige.  Work your way th... |
| Tuhwentee | `play.tuhwentee.com` | `40011` | en | 26.45 | Welcome to Tuhwentee  Custom Hardcore Minecraft for Java & Bedrock  Build a home, earn your rewards, and make every l... |
| [Tularia](https://tularia.fr/) | `play.tularia.fr` | `19132` | fr | 1.21.100 | Tularia est un serveur mcpe qui vous propose plusieurs modes de jeu avec pleins de nouveautés et d'ajout pour plaire ... |
| [TwendyMC • Netzwerk (26.1.2)](https://shop.twendymc.net) | `pe.twendymc.net` | `19132` | de | 26.40 | - Herzlich willkommen auf der Vote-Seite von -  TwendyMC.net  ⭐Dein Minecraft Crossplay Netzwerk ⭐  Pocket/Bedrock-IP... |
| [TWERION.NET](https://www.twerion.net) | `bedrock.twerion.net` | `19132` | en | 26.63 | 🔹 Our Game Modes at a Glance:  ⚔️ BedWars  Play action-packed team battles where you must protect your bed and destro... |
| u00a76Billion MC | `sv5.tgmc.ir` | `30009` | ar | 1.21.50 | The Best Server Bedrock Persian  بهترین سرور ایرانی ماینکرفت بدراک |
| [UltraMine !! Lobby !! 1.1 - 1.21](http://ultramine.net) | `ultramine.net` | `19132` | ru | 1.21.50 | ⚡ UltraMine — это уникальные Minecraft Pocket Edition сервера, созданные для комфортной игры и приятного времяпровожд... |
| [Unilands \| Skywars](http://shop.unilands.club) | `as.unilands.club` | `19132` | en | 26.60 | its unilands but in asia so asia people get better ping |
| Unilands \| Skywars | `eu.unilands.club` | `19132` | nl | 26.60 | unilands but i bought a region in the netherlands |
| [Unilands \| Skywars](https://unilands.club/) | `unilands.club` | `19132` | en | 26.60 | bedwars bridge ffa duels private games custom maps |
| [UNIMC NETWORK [ᴘᴄ-ᴘᴇ]](https://www.unimc.vn) | `global.unimc.vn` | `19132` | vi | 26.63 | 🌟 UniMC Network - unimc.vn 🌟  Máy chủ Minecraft Việt Nam 2026  Tham gia để trải nghiệm ngay những tính năng  độc đáo ... |
| UniversoCraft [0.15.10]server Beta | `51.81.243.191` | `25982` | es | 0.15.10 alpha | ▸ UNIVERSOCRAFT UniversoCraft es un servidor de Minecraft con un equipo profesional y sólido detrás, que contiene jue... |
| Unix | `unix.f5.si` | `19132` | ja | 26.60 | Ranked Duels, UnRanked Duels, FFA |
| [UnrealTactical Network.](https://www.youtube.com/channel/UCvQ6SLBfeclQq3j3BMgDQLQ) | `unrealtactical.com` | `19132` | en | 26.60 | Unrealtactical is a family-friendly survival/Smp server offering a variety of exciting features, including free items... |
| updating.. | `fusionmc.minecraft.pe` | `4309` | en | 0.15.10 alpha | The best mcpe/craftsman minigames server! 🤫🔥 |
| [va](http://valerialion.org) | `va.wither.host` | `27121` | en | 26.63 | To all those who stumble upon this arbitrary server in the infinite mass of Minecraft servers:  Birch's World will be... |
| ValenNW 26.60 √ | `valennw.club` | `19132` | tr | 26.60 | Aucune description. |
| Valeryan | `valeryan.my.id` | `19132` | id | 26.61 | VALERYAN ANARCHY ECO  Server Anarchy Eco Minecraft Bedrock.  Fitur utama  Bounty & PvP, duel dan PvP Arena  Ekonomi l... |
| ValkyrieNetwork \| Unban All 0.14 - 0.15 | `vn.minecraft.pe` | `25694` | en | 0.15.10 alpha | ValkyrieNetwork Minecraft pe 0.14.x - 0.15.x  12 MiniGames |
| ValkyrieNetwork \| Unban All 0.14 - 0.15 | `sppvp.ddns.net` | `25694` | en | 0.15.10 alpha | ValkyrieNetwork   owner : _AdEm_DZ_ + DragSO + MajicJB + AnasSO |
| [ValorMC \| SMP](https://valormc.net/) | `bedrock.valormc.net` | `19132` | en | 26.60 | Claim your land, pick a job and earn. ValorMC is a brand new Survival SMP for Java and Bedrock!  ValorMC is the survi... |
| [Vanilla Europa \| Don&#039;t wait for help to arrive.](http://store.vanillaeuropa.com/) | `play.vanillaeuropa.com` | `19132` | en | 26.63 | Server IP: play.vanillaeuropa.com  Discord: https://discord.gg/mcstmJK  The Best European Survival Minecraft Server. ... |
| [VANTA NETWORK](https://store.vanta-network.net/) | `vanta-network.net` | `19132` | en | 26.51 | Welcome to Vanta Network! We are a crossplay (Java & Bedrock) PvP and nations server.  We focus on sword, spear, and ... |
| [VANTAGE](https://vantagesmp.xyz) | `vantagesmp.xyz` | `19132` | en | 26.50 | Geyser/Floodgate crossplay, Folia 26.2, no whitelist, shard economy, lobby safe / wilds PvP-grief, no land claims |
| [VARILX](https://veylor.net) | `veylor.net` | `19132` | de | 26.51 | Veylor.NET ist ein deutscher Survival Minecraft Server auf Version 26.3 für Java und Bedrock. Beide Editionen spielen... |
| Vegeance | `vegeance.com` | `19132` | pt-BR | 26.60 | Aucune description. |
| [Venity Network](https://www.venitymc.com) | `play.venitymc.com` | `19132` | en | 26.60 | Venity Network is a Minecraft Bedrock server network that features multiple game modes, including BedWars, SkyWars, T... |
| [Venstone ・ Serveur Survie](https://venstone.xyz) | `bedrock.venstone.xyz` | `40009` | fr | 26.63 | ✅ Ouvert à tous  👥 Communauté active – Trouvez facilement des coéquipiers et passez de bons moments.  🏠 Système de cl... |
| [VeoZax SMP \| 0.14.x - 0.15.10 - 1.1.x](https://info.veozax.xyz) | `VZSMP.minecraft.pe` | `25590` | en | 0.15.10 alpha | VeoZax Server is a Multiplayer server for MCPE/Craftsman 0.14.x - 0.15.10 - 1.1.x versions. |
| [VeoZax SMP \| 0.14.x - 0.15.10 - 1.1.x](https://info.veozax.xyz) | `play.veozax.xyz` | `25590` | en | 0.15.10 alpha | # VeoZax SMP \| 0.14.x - 0.15.10 - 1.1.x \| LS + MG + RP Server  📌 SERVER INFO:  • Server Name: VeoZax SMP  • Server ... |
| [Versai Network](http://store.versai.pro) | `versai.pro` | `19132` | en | 26.60 | Versai.pro is a competitive practice PvP server with lots of features to offer:  Mace  Elytra Mace  NethPot  Crystal ... |
| VerseMC | `play.versemc.it` | `19132` | it | 26.60 | Server Totalmente Italiano.   Per cercare di ricostruire la community con un progetto serio e duraturo nel tempo!  Ti... |
| VeryCraft SURVIVAL 0.14 | `VeryCraft.mc-serv.fun` | `19133` | en | 0.14.3 alpha | Looking for a good survival and minigame server? This is the place for you! You'll find mining, PvP, jobs, economy, j... |
| [VibesMC](http://vibesmc.com) | `37.187.149.114` | `25578` | en | 26.51 | Build. Create. Survive. |
| [Viciante Survival Brasileiro](https://www.viciante.com.br/) | `jogar.viciante.com.br` | `19132` | pt-BR | 26.63 | 🎮 O Viciante é um dos melhores servidores de Minecraft Survival brasileiro com economia, focado em conteúdo exclusivo... |
| [VisionHQ](http://visionpvp.com) | `caldera.visionpvp.com` | `19132` | en | 26.50 | 🌌VisionHQ \| Minecraft Bedrock 🌌  VisionHQ has been in development for about 5 years, it is a custom OP Factions and ... |
| [Voice Chat Games!](https://coreygames.com) | `CoreyGames.net` | `19132` | en | 26.63 | Corey Games is a Minecraft network streamed live on YouTube & Twitch, with Voice Chat and VR supported. Send 300+ com... |
| [VOIDHAVEN](http://www.vhaven.xyz) | `play.vhaven.xyz` | `19132` | id | 26.51 | VOIDHAVEN SMP  Semi-Anarchy Survival Indonesia.  ⚔️ Free PvP • 💰 Player Economy • 🏪 Player Shops • 🛡️ Expensive Land ... |
| VOIDSMP | `voidmc.mcserver.us` | `19132` | en | 26.45 | WELCOME TO VOIDMC SURVIVAL!   Build your empire, explore the world, make friends, become rich, or start a war — the c... |
| [VolexMC Beta](http://www.volexmc.net) | `play.volexmc.net` | `19132` | tr | 26.60 | VolexMC - Gelişmiş Factions, yeni ve ileri seviye özel sistemler,mobil destekli arayüzler ve daha fazlası... |
| [VolteraMC \| Fantastic Update!](http://www.volteramc.net) | `play.volteramc.net` | `19132` | id | 26.63 | Aucune description. |
| [Voltraz](https://discord.voltraz.xyz) | `voltraz.xyz` | `19132` | id | 26.63 | *🌍 Selamat Datang di Voltraz MC*  Selamat datang di Voltraz MC, server Minecraft semi-RPG yang penuh petualangan, fit... |
| [waffle♥sonne&#039;nin sunucusu](http://wafflesonne.com/) | `wafflesonne.com` | `19132` | tr | 26.52 | waffle&sonne minecraft  Sunucu Türü: Survival  IP: wafflesonne.com  Sunucu Sürümü: 1.19.2 Java (1.9+ java ve son suru... |
| Waria Roleplay | `en.waria.eu` | `19132` | en | 26.60 | Waria RP - Your City, Your Story!  Welcome to Waria RP, a Minecraft Bedrock roleplay server where you can create your... |
| [Waria Roleplay](https://waria.eu/rp) | `mc.waria.eu` | `19132` | fr | 26.60 | Waria RolePlay est un serveur mcpe roleplay qui existe depuis 2020.  Dans la ville de Waria, vous pouvez  - Crée votr... |
| Warlandia Halloween S5 - 0.15.10 | `172.96.140.62` | `5424` | en | 0.15.10 alpha | Official launch after 2 years😊 and please try out my server, who trying to find an SMP🤙 this server has no shop (add ... |
| Warlandia Halloween S5 - 0.15.10 | `15.235.216.145` | `25579` | ko | 0.15.10 alpha | 0.14.0 x 0.15.10 more add |
| Wartungsarbeiten | `Magmamc.de` | `19132` | de | 26.30 | Magmamc.de ist ein Free-to-Play Minecraft-Server für Java und Bedrock von Version 1.8 bis 1.21.11 (der Server läuft a... |
| Wasil SMP \| v26.60 | `wasil.my.id` | `7777` | id | 26.63 | Achievement ON..  Wasil SMP adalah server bertema Survival Vanilla Bedrock yaitu server yang berfokus pada gameplay v... |
| [WaterdogPE](http://slmc.ir) | `play.slmc.ir` | `19132` | en | 26.50 | SkyLine, a PocketMine Minecraft Bedrock server. Experience a fusion of strategic Bedwars competition and a deep, inte... |
| WehaveTrees | `mps.wehavetrees.gg` | `19132` | en | 26.60 | 🌲 Welcome to WeHaveTrees – Survival with a Fresh Twist! 🌲  ✅ Java & Bedrock Support \| 📌 IP: wehavetrees.gg \| 🔗 Disc... |
| [Welcome to Kaboom!](https://kaboom.pw) | `play.kaboom.pw` | `19132` | en | 26.63 | Kaboom is a Minecraft multiplayer server that combines free OP with anarchy. Use powerful operator commands to push t... |
| [welcome to starluck](https://discord.com/invite/BtrK4zu7nD) | `74.112.77.140` | `1065` | en | 26.60 | Welcome to Starluck MCPE!  We hope you join our growing community by joining our discord server! We hope to see you t... |
| Welcome to the server of cobbleDRock! | `CobbleDrock-HYAT.exaroton.me` | `23332` | en | 26.52 | Unofficial server with pokemon in Minecraft bedrock |
| Welcome to the server of pupperzak! | `BSF1.exaroton.me` | `19132` | en | 26.60 | Aucune description. |
| [welloby anarchy » Java 1.7.2–26.3 + Bedrock](https://welloby.com) | `bedrock.welloby.com` | `25620` | en | 26.63 | Welloby is a small anarchy-inspired survival server. Build a hidden base, form a group, raid, trade, or explore on yo... |
| [WindPvP - https://windpvp.com](https://windpvp.com/wiki/welcome) | `mps.windpvp.com` | `19132` | en | 26.60 | Hello everyone!  I've been working on a Minecraft server that is very different from most of the ones you see.  Inste... |
| WINTERMCSMP | `51.161.84.202` | `25654` | en | 0.15.10 alpha | Aucune description. |
| [WorthyDeath](https://worthydeath.com) | `domination-brooks.tun.ply.gg` | `19132` | en | 26.60 | 🎮 WORTHY: Bedrock Edition is welcome!  Play on phone, tablet, Xbox, PlayStation, Switch or Windows together with Java... |
| [WoutWoot \| woutwoot.com](https://woutwoot.com) | `bedrock.woutwoot.com` | `19132` | en | 26.60 | WoutWoot is pseudo-anarchy survival with a real player-driven economy.  ⚔ No claims. Anything can be raided. Hide you... |
| [www.KoalaServers.net \| 26.1+](https://www.koalaservers.net) | `play.koalaservers.net` | `19132` | en | 26.60 | Our aim is for a close to vanilla taste, but with the added flavor of jobs, economy, player ran shops, and warps. We ... |
| [XdGaming CoreCraft](http://xdgamingcommunity.com) | `162.249.172.214` | `19132` | en | 26.52 | Addons: CoreCraft, Edd's Veinminer, More Ores, Player tools for claiming and grief protection, warps, Longer Days & m... |
| [XOREK \| Games Clans Surv Bedrock](https://my.aezamine.com) | `aezamine.com` | `19132` | en | 26.60 | Tired of crashes and cheating on servers? Go to the reliable AézaMine server.  Join the best! |
| [YASKOMC » Minecraft Sunucu Ağı](https://yasko-mc.rf.gd/) | `play.yasko-mc.rf.gd` | `19132` | tr | 26.60 | 🇹🇷 YaskoMC — Türkiye Haritalı SMP  Gerçek Türkiye'de Minecraft oynamaya hazır mısın?  YaskoMC'nin haritası gerçek uyd... |
| You can do anything | `147.185.221.213` | `7257` | en | 26.52 | Indonesia  Kamu bisa melakukan apa saja di sini 😆, jadi tunggu apa lagi? Ayo bergabung sekarang 😆.  Terkadang ada ser... |
| [Yozza SMP » Java &amp; Bedrock Survival](https://yozzasmp.com/) | `play.yozzasmp.com` | `25674` | en | 26.60 | 🌟 Welcome to Yozza! 🌟  Yozza is a fun, friendly Minecraft server made for both Bedrock and Java players. Play on your... |
| [YUMMYMC SMP [26.3] discord.gg/yummymc](https://store.yummymc.net/) | `mpc.yummymc.net` | `19132` | en | 26.60 | A food-themed Survival SMP with a friendly, grief-free community! Custom Jobs, Fishing, Farming, Land Claims & weekly... |
| [ZA LIFESTEAL SEASON 3 ┃ (1.8 - 26.3 ⭐)](https://zalifesteal.xyz) | `play.zalifesteal.xyz` | `17075` | en | 26.51 | ☆CALLING ALL MINECRAFT PLAYERS☆  ⚡ WELCOME TO ZA LIFESTEAL SEASON 3  🌏OUR SERVER IS  ✅ 27/7  ✅ CROSSPLAY (SUPPORT BOT... |
| ZackCraft [0.14.X - 0.15.10] | `zackcraft.sytes.net` | `8303` | en | 0.15.10 alpha | Welcome To The Server ZackCraft  You can Play it the server in 0.14.X or 0.15.10  Have Fun 😃😃😃 |
| [ZedMC 1.8 - 26.3](https://zdmc.ir) | `play.zdmc.ir` | `19132` | en | 26.62 | ZedMC is an Iranian Minecraft server featuring Java & Bedrock cross-play, SMP survival, and a free-to-play experience... |
| [ZenPvP](http://www.zenpvp.net) | `br.zenpvp.net` | `19132` | en | 26.60 | ZenPvP Network  Prison \| Skyblock \| Factions \| Survival \| Gens  We stride to provide the "Ultimate Experience" to... |
| [ZenyLand • Best Server [ Resmi ]](https://zenyland.com) | `play.zenyland.com` | `19132` | id | 26.33 | 🌏 ZenyLand merupakan sebuah server Minecraft yang support semua platform. Mulai dari Java, Bedrock, MCPE, Xbox, PS. K... |
| [Zerix Network » Halloween Update Release \| EU-NA-AS-OCE \| discord.gg/mcbepvp](https://mcbepvp.club) | `mcbepvp.club` | `19132` | en | 26.60 | Aucune description. |
| [Zerix Network » Halloween Update Release \| EU-NA-AS-OCE \| discord.gg/mcbepvp](https://zerix.ml) | `zerix.ml` | `19132` | en | 26.60 | Zerix Network  is a competitive MCBE PvP server, built with passion since 2018.  MCBEPVP is Zerix’s global Practice P... |
| [zorveth smp](https://zorveth-smp.netlify.app) | `zorveth.my.id` | `5016` | en | 26.62 | 🏰 WELCOME TO ZORVETH SMP 🏰  The Ultimate Minecraft Bedrock Economy Experience!  🌟 SERVER FEATURES 🌟  💰 Economy Surviv... |
| ZyrvexNetwork | `Zyrvex.octoheberg.eu` | `25571` | en | 26.60 | Zyrvex  Gamemodes :  - KBFFA  - TNT TAG  - INFECTED  - SHEEPWARS  - SOON..  COSMETICS   LEVELS  RANKS  FISHING |
| [\| Veltrix V3 \|](http://veltrixmc.eu) | `veltrixmc.fr` | `19132` | fr | 26.60 | Aucune description. |
| \|\|\| Histeria V8 \| | `histeria.fr` | `19132` | en | 26.60 | Aucune description. |
| [\|\|\| Histeria V8 \|](http://Mcpe.guru/Histeria) | `Histeria.eu` | `19132` | fr | 26.60 | Pvp fac |
| \|\|\| Histeria V8 \| | `play.histeria.eu` | `19132` | en | 26.60 | Macintosh Macintosh Minecraft   💻 🖥 |
| [\|\|\| Histeria V8 \|](https://histeria.fr) | `play.histeria.fr` | `19132` | fr | 26.60 | Serveur Minecraft PvP-Faction !   (English version below)   Chers joueurs,   Permettez-moi de te présenter Histeria !... |
| [\|\|\| INFECTION NETWORK [1.17x - 1.21x] \|\|\| TIENDA » ¡Descuentos en tienda.infection.fun!](https://tienda.infection.fun/) | `infection.fun` | `19132` | es | 26.63 | Infection Network es un servidor donde siempre escuchamos a la comunidad y hacemos lo mejor para mejorar día a día, c... |
| [~ ---[- EterCube - 1.21.4 -]--- ~](https://etercube.fr) | `mc.etercube.fr` | `19132` | fr | 26.63 | EterCube est un serveur Minecraft Faction dont le but est d'unir les communautés Java et Bedrock sur un environnement... |
| [¡ENTRA YA!](https://discord.com/invite/rmufJbWQC7) | `mc.superdou.net` | `19132` | es | 26.51 | \|\|\|\|\|\| JAVA EDITION y BEDROCK Edition, IP: mc.superdou.net \| Puerto para jugadores de bedrock: 19132. \|\|\|\|... |
| §0Pre-Alpha Legacy 0.14.X - 0.15.10 | `pre-alphalegacy.sytes.net` | `25998` | es | 0.15.10 alpha | Craftsman_legacy es uno de los servers que no se conforma con pvp si no que se agrega toda variedad tanto como surviv... |
| [§g[SDT-X] SkyBlock \| 1/50](http://www.sdt-x.top) | `mc.sdt-x.top` | `19132` | zh | 26.60 | 𝓜𝓲𝓷𝓮𝓬𝓻𝓪𝓯𝓽 𝓑𝓮𝓭𝓻𝓸𝓬𝓴 𝓢𝓓𝓣-𝓧 𝐒𝐤𝐲𝐁𝐋𝐨𝐜𝐤 𝓢𝓮𝓻𝓿𝓮𝓻  ✨ 我們是 純基岩版 海島生存 伺服器  🎉 更多資訊請關注我們的官方平台 🎉  🌟 遊戲特色 🌟  🔹 遊戲幣VIP、地圖: 玩家可於遊戲內賺取 "金... |
| [§pGrieferKing \| Eine neue Ära beginnt...](https://www.grieferking.de/) | `play.grieferking.de` | `19132` | de | 26.20 | ✨ Features im Überblick:  Crossplay-Unterstützung: Spiele gemeinsam mit deinen Freunden, egal ob sie auf Java oder Be... |
| [§qHash§iCube §j\| Hub Sunucusu](https://hashcube.net) | `oyna.hashcube.net` | `19132` | tr | 26.60 | 2016'dan bu yana Minecraft: Bedrock Edition sürümünde Türkiye'nin en büyük sunucusu olan HashCube, günümüzde SkyBlock... |
| [§s\|LAVA§s-LAND§s\| ➥](http://Lvbe.ir) | `Play.lvbe.ir` | `19132` | ar | 26.60 | به دنیای Lava Land خوش آمدید!  Lava Land یک سرور ماینکرفت بدراک با هدف ایجاد یک تجربه جذاب و متفاوت برای بازیکنان است... |
| [§uMineQ - Play With Friends!](http://dc.mineq.net/) | `MineQ.Net` | `19132` | es | 26.60 | Bienvenidos a MINEQ, servidor de Minecraft Bedrock donde si te gusta el PvP ¡este es el lugar perfecto para ti!  Pero... |
| [§u✦ АuraLife §u\| — §u1.21–26.60](https://auralife.uz) | `auralife.uz` | `19132` | en | 26.60 | AuraLife — O‘zbekiston Minecraft Bedrock survival serveri. Iqtisod, clanlar, PvP, duellar, eventlar va o‘zbek/rus til... |
| [§xACE MC \| BEST SMP](http://acemc.co) | `mp.acemc.co` | `19132` | en | 26.60 | 🌟 Welcome to our BRAND NEW 1.20 Survival Server! BEDROCK COMPATIBLE! It's just been released, and we couldn't be more... |
| «RL» | `raidlands.org` | `19132` | en | 26.33 | Welcome to Raid Lands, in the server you must protect your base to prevent players from raiding and destroying your b... |
| » BlockLegends « :: 0.14.X - 0.15.10 :: | `BlockLegends.ddns.net` | `26204` | id | 0.15.10 alpha | Hello, This is BlockLegends Real.  Kalau kamu mau main BlockLegends sila buka Minecraft dan sila taip.  IP : BlockLeg... |
| » BlockLegends « :: 0.14.X - 0.15.10 :: | `138.201.48.55` | `26204` | id | 0.15.10 alpha | Hello, This Is BlockLegends  Server ini boleh di main gunakan.  Versi : 0.14.X - 0.15.10  Server ini dari Asia : Oran... |
| [» Hesu! «](https://hesu.org/store) | `hesu.org` | `19132` | en | 26.60 | Hesu is the next-gen PvP Practice network.  We're available on Windows, iOS, Android, PlayStation, Xbox, Nintendo Swi... |
| » Mineverye™ « [under repair] \| 1.7.2 - 26.3 [AVAILABLE NOW] survival \| Bedwars-ComingSoon \|It is be | `stamina-crystal.tun.ply.gg` | `9795` | en | 26.10 | Aucune description. |
| » REINOS PERDIDOS | `bedrock.reinosperdidos.com` | `19132` | pt-BR | 26.60 | Reinosejurfhhheiwiiwjsjdjdsjjeejjejejwueue |
| [» SIMPLEX SMP « The Premium Survival](https://discord.gg/2gAsymnXfd) | `simplexsmp.eu` | `19132` | en | 26.63 | ⛏️ Welcome to SimplexSMP – Your Chill Survival Escape! 🌿  No Pay-to-Win. No confusing systems.  Just pure survival, g... |
| [» SİMİTSMP [AÇIK BETA YAYINDA] - oyna.simitsmp.com «](http://www.simitsmp.com) | `oyna.simitsmp.com` | `19132` | tr | 26.60 | Özel simit tarifleri, dengeli ₺ ve Simit Coin ekonomisi, ayrı Lobi ve Survival dünyaları, kasalar ve hilesiz rekabetl... |
| [» Tidal](https://store.tidalpvp.com) | `tidalpvp.com` | `19132` | en | 26.63 | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐓𝐢𝐝𝐚𝐥 - 𝐓𝐡𝐞 #𝟏 𝐬𝐩𝐨𝐭 𝐟𝐨𝐫 𝐞𝐯𝐞𝐫𝐲𝐭𝐡𝐢𝐧𝐠 𝐏𝐯𝐏  “𝐖𝐡𝐚𝐭 𝐢𝐬 𝐓𝐢𝐝𝐚𝐥..?”  Tidal is a fresh and upcoming Minecraft: Bedro... |
| [»SCB NETWORK» ](https://add.skycitybrasil.net) | `bed.skycitybrasil.net` | `14051` | pt-BR | 26.60 | 🕹️SkyCityBrasil Network🕹️  Survival🌎  SkyWars⚔  Arena PVP⚔  KitPvP⚔️  💻  IP: jogar.skycitybrasil.net  Versão: 1.8x a ... |
| [ð¥ FLAMEBOURNE SMP ð¥](https://flamebournesmp.com) | `play.flamebournesmp.com` | `25750` | en | 26.62 | **FLAMEBOURNE SMP**  Looking for an SMP where your progress actually matters? FlameBourneSMP is a long-term Java & Be... |
| [ɪɴᴀᴄʀᴀꜰᴛ [1.7-26.3]](http://www.inacraft.my.id) | `play.inacraft.my.id` | `19132` | id | 26.52 | INACRAFT  Minecraft Server Indonesia yang memiliki banyak gameplay seperti  - SKYBLOCK custom  - SURVIVAL  - RPG-DUNG... |
| [ɪᴏɴᴄʀᴀꜰᴛ ꜱʟɪᴍᴇꜰᴜɴ ʀᴘɢ ꜱᴇᴀꜱᴏɴ 9](https://linktr.ee/ioncraft) | `play.ioncraft.my.id` | `19132` | id | 26.45 | Rekomendasi Versi Client Minecraft 1.21.*  𝗜𝗣 𝗝𝗔𝗩𝗔 & 𝗕𝗘𝗗𝗥𝗢𝗖𝗞 = play.ioncraft.my.id  BEDROCK PORT = 19132  𝗙𝗶𝘁𝘂𝗿 𝗙𝗶𝘁𝘂𝗿... |
| [ʀᴘɢ 🔥 IMPERIO LATINO [1.16-26.2] 🔥 ꜱᴍᴘ](https://imperiolatino.tebex.store/) | `play.imperiolatino.online` | `19132` | es | 26.60 | ¡EL SERVIDOR DE MINECRAFT #1 DE TODA LATINOAMÉRICA! 🎮🔥  👑 IMPERIOLATINO 👑  Nuestro servidor está dedicado para toda l... |
| [ʙʟᴏᴄᴋʏᴍᴄ.ᴏʀɢ](http://store.blockymc.org) | `play.blockymc.org` | `19132` | en | 26.30 | BlockyMC delivers an exciting OneBlock SkyBlock experience! Progress through over 30 unique phases as you break block... |
| [ʙᴏxᴍᴄ.ɴᴇᴛ ✦ THANKSGIVING ✦](https://store.boxmc.net) | `boxmc.net` | `19132` | en | 26.60 | BoxMC.net is the true BoxSMP Challenge experience, with exclusive and super fun powers for Java and Bedrock players. ... |
| [ʚ ESKMC NETWORK (1.17 - 26.x) ɞ](https://tienda.eskmc.net/) | `eskmc.net` | `19132` | es | 26.62 | Servidor de BoxPvP con una gran variedad, entra y prueba! |
| [ʜᴀɴᴇᴅᴀɴᴍᴄ.ᴄᴏᴍ \| 1.21 - 1.21.11 \| ᴅɪѕᴄᴏʀᴅ.ɢɢ⁄ᴏʏᴜɴᴄᴜ ʙᴏxᴘᴠᴘ ʏᴇɴɪ sᴇᴢᴏɴ ʏᴀᴋıɴᴅᴀ](http://www.hanedanmc.com) | `play.hanedanmc.com` | `19132` | tr | 26.60 | Tüm Platfromlardan Girebileceğiniz Minecraft Sunucumuz 4 yıldır aktif ve sıfırlanmama garantisi sunuyor.  Towny & Sky... |
| [ʜᴀʏʟᴀᴢᴏʏᴜɴᴄᴜ ・ ᴘʟᴀʏ.ʜᴀʏʟᴀᴢᴏʏᴜɴᴄᴜ.ᴄᴏᴍ ・](https://www.haylazoyuncu.com) | `play.haylazoyuncu.com` | `19132` | tr | 26.52 | Haylaz Oyuncu 1.16.5 - 23.1.2 sürümleriyle giriş yapılabilen hub sunucudur açılış yakın zamanda! |
| [ʟɪᴠᴀᴍᴄ ɴᴇᴛᴡᴏʀᴋ ➠ 1.18 - 26.2](https://livamc.com/) | `bedrock.livamc.com` | `19132` | tr | 26.60 | LivaMC — Türk Minecraft Sunucusu: SMP, SkyBlock, Towny ve BoxPvP  📱 Bedrock IP: bedrock.livamc.com (port 19132) \| 🌐 ... |
| ʟᴇɢᴀᴄʏꜱᴄʜᴏᴏʟ | `legacyschool.my.id` | `25040` | id | 26.51 | LegacySchoolSMP. Dari nama saja sudah jelas.... WELCOME TO LEGACYSCHOOLSMP. Bisa di bilang rip-off Sans SMP :v. Legac... |
| [ʟᴇᴍᴏɴ ɴᴇᴛᴡᴏʀᴋ [ 1.21 ]](http://store.lemoncraft.fun) | `play.lemoncraft.fun` | `19132` | en | 26.60 | 🌿 Survival SMP (Chill or Competitive — Your Choice)  Jump into our Survival SMP where you can play your way:  PvP wit... |
| [ХАБ \| выбери сервер](https://appleks.ru/) | `appleks.ru` | `19132` | ru | 1.1.7 | Добро пожаловать на сервер appleks, где твоё мастерство выживать и находчивость будут подвержены настоящей проверке! ... |
| [ᄽMuzCraftᄿ 1.8.9 - 26.3](https://muzcraft.com/oyna) | `MC.MUZCRAFT.COM` | `19132` | pt | 26.63 | Türk Minecraft server ip MC.MUZCRAFT.COM Java ve Pocket/Bedrock Edition sunucumuz sizlere Faction ve SkyBlock oyun mo... |
| ᴀ ᴢ ᴜ ʀ ᴇ ᴄ ʀ ᴀ ғ ᴛ ● Survival Server | `palley.mineidhost.com` | `19132` | id | 26.60 | AZURE CRAFT!  Selamat datang di Azure Survival, server Minecraft bertema Fantasy RPG Survival dengan sistem ekonomi d... |
| [ᴀꜱᴛʀɪᴅ ᴄʟᴏᴜᴅ ● ʙᴏᴛᴘᴠᴘ ᴘʀᴀᴄᴛɪᴄᴇ](https://discord.gg/6wck37kJgg) | `play.astridcloud.xyz` | `19132` | en | 26.51 | Welcome to ASTRIDCLOUD!  Embark on an immersive Minecraft RPG adventure in a world designed for thrill-seekers and ch... |
| ᴄʜᴇʀʀʏᴍᴄ.ᴀsɪᴀ 1.21.11 | `cherrymc.id.vn` | `19132` | vi | 26.63 | CherryMC.asia tự hào giới thiệu 3 cụm máy chủ SMP, Skyblock và RPG – nơi hội tụ những trải nghiệm Minecraft hấp dẫn n... |
| ᴄʜᴇʀʀʏᴍᴄ.ᴀsɪᴀ 1.21.11 | `cherrymc.asia` | `19132` | vi | 26.63 | CherryMC.asia tự hào giới thiệu 3 cụm máy chủ SMP, Skyblock và RPG – nơi hội tụ những trải nghiệm Minecraft hấp dẫn n... |
| [ᴄʟᴏᴜᴅ ꜱᴍᴘ ⚡ ꜱᴇᴀꜱᴏɴ ᴠ](https://store.cloudsmp.xyz) | `cloudsmp.xyz` | `19132` | id | 26.63 | Cloud SMP adalah sebuah server minecraft yang berdiri sejak 2021. Cloud SMP pertama kali di rilis oleh Chairawan Chan... |
| [ᴇʟᴅᴇʀsᴇᴀ ɴᴇᴛᴡᴏʀᴋ \| [1.20 - Latest]](https://eldersea.fun/) | `mc.eldersea.fun` | `19132` | id | 26.51 | Eldersea Network  The Next Generation Minecraft Server  Rasakan keseruan survival faction dengan rpg items, cosmetics... |
| ᴊᴀᴡᴀᴄᴀᴍᴘ | `jawacamp.my.id` | `25562` | id | 26.62 | Aucune description. |
| [ᴊᴏɴᴀʀᴄʜʏ.ᴄᴏᴍ 1.5.2 - 26.3 𝓰ₗₒᵣᵧ ₜₒ ᵣₑₐₗ ₐₙₐᵣ𝒸ₕᵧ](https://www.jonarchy.com) | `Jonarchy.com` | `19132` | en | 26.63 | Jonarchy. Try out now! 1.5.2 - 26.3 \|   We got blocked by Microsoft use our mod: https://github.com/1x09lol/Jonarchy... |
| [ᴋɪᴛᴀ ɴᴇᴛᴡᴏʀᴋ [1.20 - ʟᴀᴛᴇꜱᴛ]](http://www.kitasmp.com) | `play.kitasmp.com` | `19132` | en | 26.62 | Kita SMP — Survival Economy Bedrock Indonesia 🌊  A fun and active Indonesian Minecraft Bedrock server with economy, l... |
| [ᴍɪɴᴇᴄʀᴀꜰᴛ.ᴘʟ ▪ 1.8 — 26.3 ▪ ʙᴇᴅʀᴏᴄᴋ](https://minecraft.pl/) | `bedrock.minecraft.pl` | `19132` | en | 26.60 | Minecraft.pl is the oldest and longest-standing Polish Minecraft community - proudly active for over 15 years. Since ... |
| ᴍᴄ.ASIANET.ꜰᴜɴ \| 1.21+ | `mc.asianet.fun` | `26026` | en | 26.51 | 🌏 ASIA NETWORK - Dominate the Battlefield! ⚔️  Welcome to Asia Network, the ultimate Minecraft PvP experience optimiz... |
| [ᴘʟᴀʏ.BOXREALM.ɴᴇᴛ \| 26.1.2+](https://store.boxrealm.net/) | `play.boxrealm.net` | `19132` | en | 26.60 | BoxRealm is the #1 BoxSMP Server welcoming all players on both Java and Bedrock. Join the rest of our incredible comm... |
| ᴘʟᴀʏ.FIREVANILLA.ɴᴇᴛ ▷ gg/firevanilla | `Firevanilla.net` | `19132` | en | 26.60 | Box pvp |
| [ᴘʟᴀʏ.HYPING.ꜰʀ](https://playhyping.com) | `PLAY.PLAYHYPING.NET` | `19132` | fr | 26.60 | Hyping est une référence incontournable des serveurs Minecraft en 2025 grâce à son écoute active de sa communauté et ... |
| [ᴘʟᴀʏ.ONEBLOCKY.ᴄᴏᴍ](https://store.oneblocky.com) | `mine.oneblocky.com` | `19132` | en | 26.60 | Oneblocky is the ultimate Oneblock SkyBlock adventure! 🌍 Break your way through 30+ phases and build the island of yo... |
| [ᴘʟᴀʏ.ɪɴᴇʀᴛɪᴀᴍᴄ.ɴᴇᴛ](https://inertiamc.net) | `mps.inertiamc.net` | `19132` | en | 26.52 | InertiaMC mixes classic LifeSteal combat with a custom generator economy. Every fight matters here because winning st... |
| [ᴛʀɪɴɪᴛʏɪɴᴅᴏɴᴇꜱɪᴀ.ᴄᴄ - ᴀɴᴀʀᴄʜʏ ʀᴘɢ](https://store.trinityindonesia.cc) | `trinityindonesia.cc` | `19132` | id | 26.51 | 🇮🇩  Selamat datang di Trinity Indonesia, server Anarchy RPG mendebarkan yang menawarkan pengalaman bermain penuh kebe... |
| [ᴠᴀʟᴇɴᴍᴄ](https://valenmc.fun) | `play.valenmc.fun` | `54936` | en | 26.33 | 🌿ValenMC \| play.valenmc.fun \| ⭐ The BEST Minecraft Server Ever! Economy, PVP Oriented, Server with exclusive events... |
| [• ReallyWorld • ЗАХОДИ НА](http://reallyworld.ru) | `mc.reallyworld.ru` | `19132` | ru | 26.63 | Grief server |
| ₊˚ ✧ ━━━━━━━━━⊱ SOMNI SMP ⊰━━━━━━━━━ ✧ ₊˚ ⋆˖⁺‧₊☽ Sleep is for the Weak ☽₊‧⁺˖⋆ | `play.somnismp.xyz` | `25566` | en | 26.51 | Somni Smp is a primarily vanilla-based survival server, made by the players for the players, dedicated to creating a ... |
| [∞ Іnfіnіtе Gаmеѕ ∞](https://ign.gg) | `2b2e.org` | `19132` | en | 1.2.0 | 2b2e is a Minecraft Bedrock Edition anarchy server founded on the 25th of March 2020. 2b2e is one of the oldest anarc... |
| ∞ Іnfіnіtе Gаmеѕ ∞ | `2b2tmcpe.org` | `19132` | en | 1.2.0 | 2b2tmcpe.org Minecraft Bedrock Edition anarchy server  No rules \| Hacking allowed \| 350k+ unique players \| Join th... |
| ∞ Іnfіnіtе Gаmеѕ ∞ | `cpe.ign.gg` | `19132` | en | 1.2.0 | cpe.ign.gg Minecraft Bedrock Edition anarchy server  No rules \| Hacking allowed \| 350k+ unique players \| Join the ... |
| [∞ Іnfіnіtе Gаmеѕ ∞](https://ign.gg) | `2b2tPE.org` | `19132` | en | 1.2.0 | 2b2tPE.org (also 2b2tBE.org) is the unofficial pocket (or bedrock) edition of the java 2b2t.org for mobile and window... |
| [∞ Іnfіnіtе Gаmеѕ ∞](https://ign.gg) | `play.2b2t.be` | `19132` | en | 1.2.0 | 2B2TBE is a Cross Platform Server built upon an Anarchy Society where players can expect absolute freedom.  This will... |
| [∞ Іnfіnіtе Gаmеѕ ∞](http://shop.skyblockpe.com) | `play.skyblockpe.com` | `19132` | en | 1.2.0 | Welcome to SkyBlockPE  We are an amazing Skyblock server with awesome people like you! Join today and build your own ... |
| [⋯⋯⋯⋯⋯⋯⋯ HuntMC ⋯⋯⋯⋯⋯⋯⋯](https://orbitmc.club) | `orbitmc.club` | `19132` | en | 26.51 | OrbitMC  OrbitMC is a Brazilian PvP and Practice server with Java and Bedrock crossplay. Fight in competitive duels a... |
| [╭ BOSSCRAFT ☺ 1.17-26.3 ╮](http://www.bosscraft.net) | `bosscraft.net` | `19132` | en | 26.60 | Bosscraft its a server minigames |
| [╭ BOSSCRAFT ☺ 1.17-26.3 ╮](http://www.bosscraft.net) | `bedrock.bosscraft.net` | `19132` | en | 26.60 | Add BOSSCRAFT2025 as a friend to join!  Bosscraft offers Prison, Skyblock and Survival (SMP) on Minecraft Version 1.2... |
| [▎ 汉堡服务器 - 生存服\| 【 QQ群:786887910 】 &lt;- 累积5000+注册 \| 稳定运营 -&gt; [重锤] [风弹] [长矛] [死神镰刀]](http://hbs.i9k.top) | `mchamburger.top` | `11930` | zh | 0.14.3 alpha | 加入我们：  mchamburger.top:11930  QQ群：786887910  服务器名称： Hamburger Server（汉堡服务器 / HBS）  游戏版本： MCPE 0.14.x（Genisys 1.6dev 核... |
| [▚▞ ✦ MigosMc.net 1.8-26.3 ✦ Призы /free ✦](https://migosmc.net) | `mc.migosmc.net` | `19132` | ru | 26.63 | Начните играть в MigosMc прямо сейчас!  Голосование награда /бонус набор |
| [▶ Britania ◀ [1.21.10]](http://britania-mc.com) | `play.britania-mc.com` | `19132` | fr | 26.33 | Britania : Un serveur ou règne la joie de vivre! Rejoignez un serveur Freebuild où règne la bonne humeur ! Nous avons... |
| ▶ polis ▪ JE 26.3 ▪ BE 26.62 | `hitlermc.com` | `19132` | en | 26.62 | 100% Vanilla MCBE server, no grif no stealing  discord.gg/6ZMJ6zXsKw |
| [▶ ᴋɴɪɢʜᴛ ɴᴇᴛᴡᴏʀᴋ [ᴊᴀᴠᴀ-ʙᴇᴅʀᴏᴄᴋ] ◀](https://knightnw.com) | `bedrock.knightnw.com` | `19132` | tr | 26.60 | ⚔️ KnightNW (Knight Network) — 2018'den beri açık Türk Minecraft sunucusu  KnightNW, Skyblock, Survival SMP ve Factio... |
| [◀ CUBORIX NETWORK ▶](https://cuborix.com) | `mc.cuborix.com` | `19132` | es | 26.33 | 🚀 ¡Bienvenido a CUBORIX!  El servidor de Minecraft definitivo donde la diversión no tiene límites.  🎮 +20 MODALIDADES... |
| [◁═════[‐ COMPLEX GAMING ‐]═════▷](https://www.mc-complex.com/) | `mps.mc-complex.com` | `19132` | en | 26.62 | Complex Gaming is one of the best Minecraft Bedrock and MCPE servers, a friendly crossplay network where Bedrock (MCP... |
| [◆ 💎 DIAMONDSMP ◆](https://store.diamondsmp.net/) | `play.diamondsmp.net` | `25835` | en | 26.51 | Welcome To DiamondSMP!  We’re thrilled to finally share the news…  Our brand new Minecraft server is launching soon! ... |
| [●●● Catlix Network ●●●](https://catlix.net) | `play.catlix.net` | `19132` | ro | 26.60 | Aucune description. |
| [★ ALANNETWORK ★ - 1.21.x \| discord.gg/7QhBYaJcDQ \| [play.alannw.com]](http://alannw.com) | `play.alannw.com` | `19132` | tr | 26.60 | 🚀 ALAN NETWORK \| 1.21.x & Bedrock Sürümünün En Efsane Adresi!  Büyük maceraya hazır mısın? play.alannw.com adresinde... |
| [★ CRISPY NETWORK ★ NEW ERA](https://crispymc.net/) | `bedrock.crispymc.net` | `19132` | en | 26.63 | Crispy Network is an Indonesian Minecraft server that has been running since 2018. Designed to offer a unique experie... |
| ★ MBG INDONESIA ★ | `mbg678.aternos.me` | `40466` | id | 26.60 | Untuk seru-seruan aja nih lagi pengen cari temen mabar walaupun sederhana tetap Oke |
| ★ 𝕺𝖗𝖎𝖊𝖓 • ꜱᴋʏᴡᴀʀꜱ ★ | `orienmc.xyz` | `19132` | en | 26.60 | ⚔️ OrienMC is a Minecraft Bedrock server built for PvP! Battle in SkyWars, The Bridge, Duels, and FFA, join events, a... |
| ★★ 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗦𝗠𝗣 𝗘𝗩𝗘𝗥 ★★ | `KiwiSMP.fun` | `19132` | en | 26.60 | Aucune description. |
| [☘ 굳럭키 서버 시즌 7 알파 ☘](https://www.goodlucky.io?utm_source=minecraftpocket-servers&utm_medium=info&utm_campaign=mc_server_list) | `goodlucky.io` | `19132` | ko | 26.62 | GoodLucky Server |
| [☠ NO TOTEM HARDCORE ☠ [1.8/26.3]](https://www.nototem.net/) | `nototem.net` | `19132` | en | 26.51 | [h5][size=36px]IP: [color=#3598db]nototem.net[/color][/size]  [size=36px]Discord: discord.gg/jhG2E6yAW[/size]  [size=... |
| [⚔ ImperiumMC \| COMING SOON](https://imperiummc.net/) | `play.imperiummc.net` | `19132` | en | 26.52 | ImperiumMC - Rome-Themed OP Prison  Step into the Roman Empire and build your legacy. Mine your way through 100 ranks... |
| ⚔ UHCF 2H30 ┃ ● OUVERT | `play.hcfcore.fr` | `8180` | fr | 26.51 | HCFCore 26.2 – HCF Java & Bedrock – SOTW Dimanche 13 septembre 2026 : rejoignez une expérience HCF Old-School hardcor... |
| ⚔ Waves Gamer \| Java + Bedrock Crossplay \| Survival · OneBlock · Lifesteal | `play.mc.wavesgamer.com` | `19132` | en | 26.52 | Waves Gamer is a small, UK-hosted Minecraft network built around one idea: everything you get here, you earn by playi... |
| ⚔ 𝗡𝗲𝘅𝘂𝘀𝗣𝗘 𝗢𝗣 𝗙𝗮𝗰𝘁𝗶𝗼𝗻𝘀 ⚔ | `play.nexuspe.net` | `19132` | en | 26.50 | Aucune description. |
| [⚝ VAYLAND ⚝](https://vayland.net/) | `mc.vayland.net` | `19132` | en | 26.52 | ❤️Welcome to the game project VayLand⚡.  We took the best, discarded the unnecessary and made interesting. Always up ... |
| ⚠ ＭＣＬＩＯＮＰＲＯＪＥＣＴ ⚠ // ВЗЛОМ /hack | `65.21.9.208` | `25703` | ru | 26.52 | Minecraft Survival Server for All  Version Bedrock: All  Java: 1.0 - 1.21  Enjoy |
| ⚡ Germanycraft.de Netzwerk \| 1.21.11 + | `germanycraft.de` | `19132` | de | 26.40 | Über GermanyCraft – Mehr als nur ein ServerGermanyCraft ist mehr als nur ein Server — es ist eine kleinere Community.... |
| [⚡ PLAY.KITSUE.NET ⚡ • [26x]](http://mc.kitsue.net) | `play.kitsue.net` | `19132` | vi | 26.52 | máy chủ minecraft java hỗ trợ bedrock |
| [⚡ TITAN MC ➔ SEASON 4 IS LIVE! ⚡](http://titansmp.myftp.biz) | `titansmp.myftp.biz` | `19132` | en | 26.63 | Aucune description. |
| ⚡ 𝗧𝗮𝗹𝗲𝗖𝗿𝗮𝗳𝘁 𝗣𝗿𝗶𝘀𝗼𝗻𝘀 » 𝗪𝗛𝗜𝗧𝗘𝗟𝗜𝗦𝗧 ⚡ | `150.251.116.44` | `22450` | en | 26.52 | TaleCraft Prisons is a medieval prison server for Minecraft Bedrock.  Start as a Serf and mine your way up to God thr... |
| [⚡𝗦𝗘𝗚𝗔 - 𝗣𝗥𝗔𝗖𝗧𝗜𝗖𝗘⚒️](http://cora.land) | `segamc.net` | `19132` | en | 26.60 | Aucune description. |
| [⛏ ClassicVanilla.org ⛏](https://classicvanilla.org) | `mc.classicvanilla.org` | `19132` | en | 26.63 | [Java/Bedrock] A Minecraft server with classic vanilla experience and the latest version!  • We respect the work of o... |
| [⛏ Servidor Oficial Premium Mundo-Minecraft ⛏](https://www.mundo-minecraft.com/) | `server.mundo-minecraft.com` | `19132` | es | 26.62 | 🎉 Mundo-Minecraft.com – Servidor Premium de Construcción desde 2010 🎉  ¡Bienvenido a Mundo-Minecraft.com, una comunid... |
| [✦ 2 ᴏʏᴜɴ ᴍᴏᴅᴜ ✦](https://granosnetwork.com) | `Oyna.GranosNetwork.Com` | `19132` | tr | 26.51 | Sunucumuzda eyalet sistemi var townyden farklı olarak kendi kasabanı falan kurma gibi bir şey yok. Hazırda 5 tane eya... |
| ✦ [ 拾光澪隅 ] ✦ 允許盜版 | `miomc.top` | `19132` | zh | 26.51 | Aucune description. |
| [✦ ARSYANET ✦ ┃ 1.21.X](https://arsyanet.site) | `arsyanet.my.id` | `19132` | id | 26.62 | 🌟 ArsyaNet adalah server Minecraft Bedrock bertema Survival RPG dengan berbagai fitur custom, gameplay yang menarik, ... |
| ✦ ARVEE PRISON ✦ » Rise to the Top | `play.arvee.world` | `19132` | en | 26.52 | Looking for more than ordinary Minecraft survival? Welcome to Arvee Survival!  ⚔️ EliteMobs RPG — fight dangerous eli... |
| ✦ AsterMC ✦ · Survival among the stars | `play.astermc.org` | `19132` | en | 26.60 | AsterMC is a BRAND NEW, Space-themed survival server with factions, economy, OP-enchants, custom skins, custom plugin... |
| [✦ BestPE.pl ✦ ┃ Survival 26.1.2 - 26.3](https://bestpe.pl) | `bestpe.pl` | `19132` | pl | 26.52 | Naszym celem nie jest tworzenie przesadnie skomplikowanego serwera pełnego niepotrzebnych systemów. Stawiamy na przyj... |
| [✦ BLOCKPATE.DE ✦ Dein Imperium. Deine Legende.](http://blockpate.de) | `play.blockpate.de` | `19132` | de | 26.60 | 🔥 BLOCKPATE.DE 🔥  🎮 Ein modernes Minecraft-Netzwerk mit eigenen Spielwelten, Systemen und jeder Menge Möglichkeiten! ... |
| [✦ BRADGE SMP ┃ survival done properly](http://bradgesmp.nl) | `bedrock.bradgesmp.nl` | `25269` | en | 26.51 | BradgeSMP is a survival SMP for Java and Bedrock. No pay-to-win, no resets. Duels with kits, weekly  events like sple... |
| ✦ ELITE REBORN ✦ | `95.68.69.47` | `19132` | en | 26.40 | We are a minecraft medieval roleplay server with a friendly and fast growing community.  Mostly we focus on survival ... |
| [✦ EpikLava ✦ │ BoxPvP](https://www.epiklava.com) | `mcpe.epiklava.com` | `19132` | tr | 26.63 | Aucune description. |
| [✦ GROW WITH US ✦](https://pixelgrew.com) | `play.pixelgrew.net` | `19132` | en | 26.63 | Ultimate SMP |
| [✦ KOLOSOK SURVIVAL ✦](http://roulette77.in/live-roulette) | `kolosok.xyz` | `19132` | en | 26.51 | I am searching for a low-latency Minecraft server that doesn't have an overwhelming amount of custom plugins. Most of... |
| [✦ Leone Network ᛫ 1.21-26.2 ✦](http://shop.leonemc.net) | `Bedrock.LeoneMC.net` | `19132` | en | 26.60 | IP: LeoneMC.net \| Java & Bedrock Compatible  Game Modes (8+ and counting):  - Lifesteal SMP – Steal hearts, dominate... |
| [✦ LUNEX SMP ✦](http://lunexsmp.vercel.app) | `play.lunexsmp.my.id` | `19132` | id | 26.63 | Selamat datang di LUNEXSMP, sebuah server Minecraft Survival EcoPvP bertema DonutSMP tempat petualangan tanpa batas d... |
| [✦ MINECITY » Jetzt dein Abenteuer starten!](https://minecity.at/) | `mc.Minecity.at` | `19132` | de | 26.63 | WILLKOMMEN IN MINECITY  Eine Stadt. Ein Server. Deine Geschichte.  MineCity verbindet modernes CityBuild mit eigenen ... |
| [✦ MysticMeadow Network ✦](http://mysticmeadow.eu) | `malls-sandwich.tun.ply.gg` | `19132` | en | 26.60 | # 🌿 MysticMeadow \| Your Next Survival Adventure! ✨  **🌍 Explore. Build. Survive. Thrive.**  Welcome to **MysticMeado... |
| ✦ PreyxStudios ✦ │ Java + Bedrock | `play.preyxstudios.net` | `19132` | de | 26.60 | PreyxStudios – dein deutsches Netzwerk für Java und Bedrock  Ob Handy, Konsole, Windows oder Java: Bei uns spielen al... |
| [✦ Pumkincraft │ Belediye ve ülke ✦](https://pumkincraft.com/) | `oyna.pumkincraft.com` | `19132` | tr | 26.63 | Sizlere müjdeli bir haberimiz var! Yepyeni bir Towny sunucu açıyoruz ve bu epik macerada sizinle birlikte olmak için ... |
| [✦ REDESTAR ➠ 1.13+ - 26.2 ✦](https://loja.redestars.com) | `redestars.com` | `19132` | pt-BR | 26.62 | Servidor de sobrevivencia JAVA & BEDROCK |
| [✦ SKY X NETWORK (V6) ✦](https://skyxnetwork.net/) | `skyxnetwork.net` | `19132` | en | 26.60 | SkyXNetwork is a Minecraft server with Survival, Mining Tycoon and Skygen. Survival is the main mode, so if you just ... |
| ✦ STARNYXMC NETWORK ✦ [1.13/1.21] | `65.75.210.63` | `19132` | en | 26.51 | × Server for Minecraft PE 0.15.10  • RankUp  • Farming area  • PvP Zone  • Survival  • Shop / Sell Ítems  • Daily mis... |
| [✦ TALVORA NETWORK ✦](https://junkyhangout.netlify.app/#home) | `junkyhangoutsv.srein.xyz` | `25963` | en | 26.60 | 🔥 JUNKY HANGOUT SMP 🔥  Junky Hangout SMP is a community survival Minecraft server where players can build, grind, tra... |
| [✦ USSR SPACE ✦](https://t.me/UssrSpace) | `mc.ussr.space` | `19132` | ru | 26.63 | 🚀 USSR SPACE — Выживание нового поколения!  🎮 ПОДДЕРЖКА ВСЕХ УСТРОЙСТВ  • Java Edition (ПК) — порт 25565  • Bedrock E... |
| ✦ VOIDRUSH ✦ | `play.voidrush.org` | `19132` | en | 26.63 | ⚔️ VOIDRUSH — A CUSTOM RPG ADVENTURE IN THE VOID ⚔️  📱 Play on phone, tablet, console or PC. Bedrock and Java players... |
| [✦ ᴄʀᴀꜰᴛʀɪᴠᴀ \| 1.19.3 - 26.2 ✦](http://www.tekelcraft.net) | `oyna.tekelcraft.net` | `19132` | tr | 26.45 | TekelCraft, kaliteli ve eğlenceli bir SkyBlock deneyimi sunmayı amaçlayan topluluk odaklı bir Minecraft sunucusudur. ... |
| [✦ 𝗖𝗼𝗿𝗮 - 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗲 ⚔️](http://cora.land) | `play.cora.land` | `19132` | en | 26.60 | What is Cora Network?  Cora is a fun and enjoyable server for all the PvP and Skillful players.We also offer an amazi... |
| [✧ AsteriaMC ✧](https://asteria-mc.xyz/) | `be.asteria-mc.xyz` | `64511` | en | 26.52 | AsteriaMC — towns, nations and Survival for Java + Bedrock.  Build your own town on an Earth map, join a nation and t... |
| [✧ LUNAMOON SMP ✧ v26.2](http://discord.gg/lunamoonsmp) | `lunamoonsmp.com` | `19132` | en | 26.60 | ⋆.˚ LUNAMOON SMP 🌙 .⭒˚  JOIN LUNAMOON TO MAKE FRIENDS AND MORE!! |
| [✧ SERA × NANIMEID ✧](http://www.seramc.top) | `play.seramc.top` | `19132` | id | 26.60 | 🌍 SERA MC — Minecraft Survival Indonesia  Bosen main survival yang itu-itu aja?  Yuk cobain SERA MC! ✨  🎮 Support Jav... |
| ✧ SoLuna SMP ✧ | `solunasmp.ddns.net` | `19132` | th | 26.60 | SoLuna SMP — Premier Minecraft 26.3 Crossplay Survival RPG Server (Java & Bedrock)  Looking for the best Minecraft 26... |
| [✨ LAMANITAS CREW ✨ » ¡Aventuras Épicas!](http://www.laub.cl) | `play.laub.cl` | `19132` | es | 26.60 | 🌿 LAMANITAS — Survival tranquilo, casi vanilla  Un servidor para vivir y construir a tu ritmo, sin presión.  Aquí no ... |
| [✯ Minezinho \| 1.8 - 1.21.x ✯](https://minezinho.com/) | `jogar.minezinho.com` | `19132` | pt-BR | 26.60 | Seja parte do maior e mais acolhedor servidor de Minecraft da comunidade brasileira! No Minezinho, oferecemos uma exp... |
| ❤ THE LAST HEART ❤ | `152.228.198.167` | `22157` | en | 26.51 | Welcome to The Last Heart! A Dutch/Belgian lifesteal survival server built around short seasons.  HOW IT WORKS  - Lif... |
| [❤ ᴘᴇʙʙʟᴇ ǫᴜᴇꜱᴛ ❤ v1.294](https://pebble.quest/wiki/getting-started/) | `mc.pebble.quest` | `8075` | en | 26.62 | ✦ Pebble Quest ✦ — Custom Skyblock done right!  IP: pebble.quest (Java 1.21+)  Build your island from nothing into an... |
| ❦PvPCraft MG❦ Autumn | `Play.pvpcraft.ru` | `19132` | en | 0.14.3 alpha | Pvp |
| ➶ 𝗖𝗼𝗿𝗮 - 𝗟𝗮𝘁𝗲𝘀𝘁 🛡️ | `cora.land` | `19132` | en | 26.60 | Aucune description. |
| [➶ 𝗛𝗟 » ¡𝗡𝗲𝘄 𝗦𝗲𝗮𝘀𝗼𝗻 𝟭𝟭!](https://huarizoland-tienda.tebex.io/) | `play.huarizoland.com` | `19132` | es | 26.60 | ⚡Servidor Factions, Economía, Minas con Pvp, Nether, End, Bosses, Crates y mucho más. |
| [➶ 𝗦𝗘𝗔𝗦𝗢𝗡 𝟭𝟬 𝗢𝗨𝗧 𝗡𝗢𝗪 ⚔️](https://store.zeqa.net/) | `zeqa.net` | `19132` | en | 26.60 | Welcome to Zeqa  What is Zeqa?  Zeqa is the largest non-featured Bedrock PvP server in the world.  You can play with ... |
| [⟡ BELSARUN NETWORK ⟡ │ [1.19 - 26.2]](https://belsarun.tebex.io/) | `belsarun.net` | `19132` | es | 26.60 | Belsarun Network \| Survival Semi-Custom  Una nueva aventura comienza aquí. Explora Dungeons, descubre minas llenas d... |
| [⭐ DISASTERMC ⭐](https://store.disastermc.fun) | `play.disastermc.fun` | `19162` | en | 26.52 | Best Smp Server! |
| [⭐ ROSHERCRAFT - Java &amp; Bedrock - [1.21.X] ⭐](https://roshercraft.com.tr/) | `play.roshercraft.com.tr` | `19132` | tr | 26.60 | RosherCraft oyuncularına kaliteli ve eşsiz bir deneyim sunan minecraft oyun sunucusudur. |
| [⭐ SPOT!](https://spotgames.net/) | `mobile.spotgames.net` | `19132` | pt-BR | 26.62 | Já estamos aqui há mais de 12 anos fazendo modos divertidos para todo mundo. Sempre colocamos coisas novas e melhoram... |
| [⮞ MINECRAFT.SI ⮜](https://minecraft.si/) | `play.minecraft.si` | `19132` | en | 26.60 | Slovenski Minecraft Network  Sedaj tudi na mobilnih napravah. |
| [【★★★★★】🔥 CHILLSMP [26.2]【★★★★★】 Sulfur Update! ❤ JOIN OUR DISCORD ❤ ■](https://shop.chillsmp.org/) | `op.chillsmp.org` | `19132` | en | 26.62 | Welcome to ChillSMP. Our server has the friendliest community on Minecraft.  We're always innovating and pushing to i... |
| [【★★★★★】🔥 COSMOSMC [26.2]【★★★★★】 Sulfur Update! ❤ JOIN OUR DISCORD ❤ ■](https://cosmosmc.org) | `gems.cosmosmc.org` | `19132` | en | 26.62 | Welcome to CosmosMC. Our server has the friendliest community on Minecraft. We're a Network that offers the best of t... |
| 大神伺服器 • DaShen Network | `pe.dashen.dev` | `34604` | zh | 26.52 | 🌿 DaShen Network｜大神伺服器 暑期招募  想找一個可以真正「住下來」的 Minecraft 生存伺服器嗎？  DaShen 大神伺服器以長期生存為主要方向。  我們希望玩家今天蓋下去的基地、城市、商業區與各種工程，不是... |
| [廢土基岩村 bedrock.mcfallout.net - 經典原味生存](http://mcfallout.net) | `bedrock.mcfallout.net` | `19132` | zh | 26.60 | 廢土伺服器是目前台港澳最大的生存伺服器，共有超過20萬玩家加入，尖峰時段線上人數超過1500人、每個月有10,000名玩家保持活躍的伺服器。 #minecraft  享受Minecraft，工廠、農場、紅石、水流，盡量發揮你的創意。 ... |
| [星辰服](http://xcsw.shop) | `103.39.66.10` | `12999` | en | 26.60 | ✦ Farming and retirement, accompanied by the stars ✦  —740 days, we have made a home in this world.  This isn't a fla... |
| [楽しいサーバーです](https://2b2tjb.jp/) | `2b2tjb.jp` | `19132` | ja | 26.60 | JEでもBEでも入れる 2B2T サーバーです。  ルールはありません。  何かしたからといってBANなどはしません。  ※Servercrusherを作る人は対象外です(BANします)  チート, PK などなんでもOK。  BE版... |
| [潜小贝养老服\|长期开服\|永不跑路](https://shulker.cn) | `play.sk3.top` | `37777` | zh | 26.51 | Aucune description. |
| [牛牛的草原 ≫ 26.30-26.51](https://cowgl.tech) | `cowgl.tech` | `19132` | zh | 26.60 | 歡迎來到牛牛的草原！我們是一個提供多款刺激有趣的Minecraft小遊戲伺服器，包括TNTRun、跑酷、SMP、捉迷藏、空島生存、床戰等。我們的伺服器致力於提供一個優質的遊戲環境和社群平台，讓玩家可以輕鬆交友、與其他玩家互動並一起探索... |
| [麦迪之城[大厅服] \| 1.21.5x~1.26.5x](https://mcsm.cc) | `mcsm.cc` | `19132` | zh | 26.51 | Aucune description. |
| [ ＭｉｎｅＯｒｅ  ШАЛКЕРЫ \| МАШИНЫ \| АД ](http://mineore.org) | `mineore.org` | `19132` | en | 26.60 | Your new Minecraft BE adventure begins here! 😎 Build, explore the world, and grow alongside your friends on our survi... |
| [ ＭｉｎｅＯｒｅ  ШАЛКЕРЫ \| МАШИНЫ \| АД ](http://mineore.ru) | `mineore.ru` | `19132` | ru | 26.60 | Лучший сервис mineore.ru👑 |
| [ ❤ ᴄʟᴜʙʙʏ ɴᴇᴛᴡᴏʀᴋ ❤ (ᴠ26.40 - 26.63)](https://www.minese.web.id/clubby-network) | `play.clubbymc.my.id` | `19239` | en | 26.63 | ⚙️ Welcome to Clubby Network [New Season 21]⚙️  🖥 Social Media 🖥  🌐 Website: https://www.minese.web.id/clubby-network... |
|  NAUTICMC BEDROCK | `bedrock.nauticmc.net` | `19132` | en | 26.60 | Server for Minecraft 1.19.80 Active HCF |
| [ SoulCraft #1 выживание](http://soulcraft-pe.ru) | `SoulCraft-pe.ru` | `19133` | ru | 26.0 | Start playing SoulCraft now!   Vote Reward /kit bonus  IP: soulcraft-pe.ru: 19132  Website: http://soulcraft-pe.ru  V... |
| [ SoulCraft #2 гриферство](http://soulcraft-pe.ru) | `soulcraft-pe.ru` | `19134` | ru | 26.0 | Начните играть в SoulCraft прямо сейчас!   Голосование награда /бонус набор  ИС: soulcraft-pe.ru: 19132  Сайт: [я на ... |
|  CuteLand  | `Play.CuteLandMc.iR` | `19132` | en | 26.60 | 🎀 Welcome to CuteLand SMP! 🎀  Looking for a friendly Minecraft Bedrock SMP with fun features and an active community?... |
| [ Feplex АНАРХИЯ](https://bungee.host) | `fecraft.ru` | `19132` | ru | 26.60 | ▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧  ✏️ ЗАБИРАЙ СВОИ новогодние ПОДАРКИ от Домера и Пионера - /free  ✏️ ДЕНЬ СКИДОК НА ДОНАТ 90%!  ✏️... |
| [︵‿୨♡୧‿︵ Plasmodia ︵‿୨♡୧‿︵](http://plasmodia.org) | `play.plasmodia.org` | `19132` | en | 26.63 | Chill SMP \| Land Claiming \| Jobs \| No Resets \| Optional PvP  We are a community-focused Minecraft server built fo... |
| [ＡｌｐｈａＭＰ §0- Ｓｕｒｖｉｖａｌ ＆ ｇｒｉｅｆ](https://discord.gg/2Q7thT6cKd) | `AlphaMP.ddns.net` | `19824` | es | 0.14.3 alpha | Server Original: Unity   ahora renombrado como AlphaMP  • grief  • server en español  • nada más que la simpleza de u... |
| [ＢｒｅａｄｉｘＷｏｒｌｄ](http://play.breadixpe.net) | `Play.breadixpe.ru` | `19132` | ru | 26.50 | Welcome to BreadixWorld with a lot of minigames like  Arcade, Skywars,Survival Games, Bedwars, Duel, Survival, Murder... |
| [ＫＡＡＲＩＯ ＮＥＴＷＯＲＫ ► 1.8 - 26.3](https://www.kaario.net) | `oyna.kaario.net` | `19132` | tr | 26.51 | Sunucumuzda Bulabileceğiniz Oyun Modları:  • Survival  • BoxPvP  • Creative  • Bedwars  • Pratik & FFA  • Daireden So... |
| [ＯａｓｙｓＰＥ  Гриф, Дуэли, Кейсы](https://oasys-pe.com) | `oasys-pe.com` | `19132` | en | 26.60 | Bester Play2Earn-Server für Minecraft: Bedrock Edition. Jetzt beitreten!  Server mit einem Klick hinzufügen -> https:... |
| [ＰＡｎｅｔｗｏｒｋ ＭＩＮＩＧＡＭＥＳ](https://pagamingop.github.io/shop) | `160.191.77.60` | `6169` | en | 0.15.10 alpha | This server provides you a lot of features which you will only find in latest Minecraft servers   Our active staffs a... |
| [ＳＣ ➙ ＨＵＢ](http://pay.san-pe.fun) | `san-pe.fun` | `19132` | tr | 26.60 | Aucune description. |
| ＴｕｒｋｍｅｎＷｉｘ | `172.96.140.62` | `5159` | en | 1.1.7 | 𝐌𝐞𝐭𝐚𝐂𝐫𝐚𝐟𝐭 New server 0.14.x \| 𝐬𝐮𝐫𝐯𝐢𝐯𝐚𝐥 \| 𝐦𝐢𝐧𝐢-𝐠𝐚𝐦𝐞𝐬 \| 𝟕/𝟐𝟒 \| |
| [𝕯𝖎𝖛𝖎𝖓𝖎𝖙𝖞 \| ⚔ 𝐒𝐔𝐌𝐎 ⚔](https://divinitymc.org) | `divinitymc.org` | `19132` | en | 26.50 | Divinity |
| 𝗘𝗔: 𝗠𝗲𝗴𝗮𝗪𝗮𝗹𝗹 | `play.earena.cn` | `19132` | en | 26.50 | ElysianArena - Modern Proxy Architecture · Multi-Minigames · Smooth & Stable Experience  📋 Server Basic Information  ... |
| [𝗘𝗡: 𝗠𝗜𝗡𝗜𝗚𝗔𝗠𝗘𝗦 𝗦𝟮 𝗢𝗨𝗧 𝗡𝗢𝗪♛](https://www.erilanetwork.com) | `oyna.erilanetwork.com` | `19132` | tr | 26.60 | 🎮 Erila Network Minecraft Bedrock Türkiye'nin en iyi sunucusu!  2024 yılında Minecraft Bedrock oyuncuları için kurula... |
| [𝗟𝘆𝗱𝗼𝘅𝗠𝗖 - REPLAYS IN BRIDGER!](http://lydoxmc.net) | `lydoxmc.net` | `19132` | en | 26.60 | Welcome to LydoxMC!   What is LydoxMC?   LydoxMC is a competitive Minecraft Bedrock minigames network.   Play excitin... |
| [𝗡𝗘𝗪: 𝗦𝗧𝗥𝗜𝗞𝗘 𝗙𝗙𝗔 𝗢𝗨𝗧 𝗡𝗢𝗪](https://blog.inpvp.net/) | `play.inpvp.net` | `19132` | en | 26.60 | InPvP is a Minecraft Bedrock Edition network operating several multiplayer servers and experiences across mobile devi... |
| [𝗢𝘃𝗲𝗿𝗕𝗹𝗮𝘀𝘁 𝗡𝗲𝘁𝘄𝗼𝗿𝗸](http://overblast.eu) | `play.overblast.eu` | `19132` | fr | 26.60 | Découvrez un serveur Minecraft unique, spécialisé dans le OneBlock et le SkyBlock, pensé pour offrir une expérience c... |
| [🄼🅈 𝗚𝗹𝗼𝗯𝗮𝗹 𝗖𝗿𝗲𝗮𝘁𝗶𝘃𝗲 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 🌍](https://www.mychunk.org) | `mychunk.org` | `19132` | ko | 26.63 | 🚀 MyChunk.org : Global Minecraft Creative Server  Experience the ultimate freedom of a server where your imagination ... |
| 🇮🇶 ﺖﻓﺍﺮﻛ ﻕﺍﺮﻋ\|\| CRAFT IRAQ | `Iraq-Craft.ddns.net` | `25911` | en | 0.15.10 alpha | Aucune description. |
| [🌍 WILLOW HAVEN 🌍 📌 Live Maps 📌](https://www.kingdomscalling.com/) | `enter.kingdomscalling.com` | `19132` | en | 26.51 | 🗺️Introducing the WORLD OF ANCALADORE🗺️  Join with: enter.kingdomscalling.com Bedrock Port 19132  NEW Worlds  * Ancal... |
| [🍁 Kuschlige Herbststimmung auf Blockstal 🍁 \| mcMMO - Jobs - Quests - MyPet - uvm.](http://www.blockstal.de) | `blockstal.de` | `19132` | de | 26.63 | Blockstal ist eine kleine, gemütliche und familiäre Community. Wir gehen alle friedlich und freundlich miteinander um... |
| [🎃 Halloween](https://wertzuigames.net) | `WertzuiGames.net` | `19132` | en | 26.60 | Hello, Halloween! 🧛 🌧️ Explore our spooky map variants 🧟, find the 7 hidden pumpkins 🎃, grab some ghoulish cosmetics ... |
| [🎃 ＭＣＺｏｎｅ 🎃 HALLOWEEN \| СТРАШНО \| ВЕСЕЛО \| КОНФЕТЫ 🍬](http://mc-zone.org) | `mc-zone.org` | `19132` | en | 26.60 | Your world. Your adventures! 🚀  Welcome to MCZone—a Minecraft Bedrock server featuring survival, anarchy, and SkyWars... |
| [🏹 SERIFION WEB 🏹](https://web.serifionweb.fun) | `serifionweb.fun` | `19133` | en | 26.45 | # SERIFION WEB — YOUR NEXT MINECRAFT NETWORK  Welcome to **Serifion Web**, a growing Minecraft network focused on del... |
| [💠 STABLEBLOCKS SMP 💠 [26.X] ⚒ ,i, SMP REBORN UPDATE! ʟɪᴠᴇ ɴᴏᴡ ,i,](http://store.stableblocks.net) | `stableblocks.net` | `19132` | en | 26.62 | Welcome to an adventurous and engaging economy based anti grief SMP!  - Take part in an awesome friendly community.  ... |
| [🔥 ARENAHUB MUMBAI \| play.arenahub.pro \| 1.21.1 Cross-Play](https://arenahub.pro/) | `play.arenahub.pro` | `19132` | en | 26.52 | Welcome to ArenaHub Mumbai! The best Indian server for Mobile and PC players featuring OneBlock, Lifesteal, Custom Cr... |
| [🔥 ʜᴇʟʟɴᴀʜ ɴᴇᴛᴡᴏʀᴋ - ꜱᴇᴀꜱᴏɴ 1 🔥 「1.21.x」](http://www.hellnah.id) | `hellnah.id` | `19005` | en | 26.60 | 𝗛𝗘𝗟𝗟𝗡𝗔𝗛 𝗡𝗘𝗧𝗪𝗢𝗥𝗞 — 𝗡𝗘𝗪 𝗘𝗥𝗔  HellNah is a Java & Bedrock Crossplay Minecraft Server built for players looking for a lon... |
| [🗡 CERBERUSCRAFTMC [26.2 &amp; BEDROCK] 🗡](https://www.cerberusgamingnetwork.co.uk/?i=2) | `cerberusmc.my.pebble.host` | `19132` | en | 26.60 | Compatibility: ALL Versions, Java & Bedrock! See /discord for support.  **Player Cosmetics! Custom Timed Events and W... |
| [🛏 ꜱʜᴀᴅᴏᴡɪɴɢ ʙᴇᴅᴡᴀʀѕ 🛏](http://www.shadowing.com.tr) | `oyna.shadowing.com.tr` | `25844` | tr | 26.60 | Shadowing Minecraft Sunucusu:  Sunucumuz SMP, SkyBlock ve BedWars Olmak Üzere 3 Oyun Modundan Oluşmaktadır. Sunucumuz... |
| 🛡 Rede Nexus » (1.19-1.21.x) 🛡 | `redenexus.minesrv.net` | `25652` | pt-BR | 26.51 | 🌌 REDE NEXUS — Mais que um servidor, uma comunidade!  Jogue, explore, conquiste sua história! Conectando jogadores, c... |
| [🥔 ALOO SMP](https://site.aloosmp.fun) | `play.aloosmp.fun` | `19132` | en | 26.60 | 🥔 ALOO SMP 🥔  The Ultimate 24/7 Public Survival, PvP & Mini-Games Experience!  ⚡ OVERVIEW ⚡  Welcome to Aloo SMP, the... |
| [🪓 YOURSMP 🪓](https://yoursmp.net) | `yoursmp.net` | `19132` | en | 26.60 | Welcome to YourSMP.net — The Ultimate Crossplay SMP Experience!  Looking for a friendly, modern, and engaging Surviva... |
<!-- SERVERS:END -->

## Licence

Code et structure : [MIT](LICENSE). Les noms, descriptions et images des serveurs appartiennent à leurs propriétaires respectifs. Un propriétaire qui souhaite retirer son serveur peut ouvrir une issue ou une pull request.
