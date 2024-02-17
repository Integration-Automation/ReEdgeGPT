import asyncio
import json
from os import getenv
from pathlib import Path
from random import choice
from string import ascii_uppercase

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle


# If you are using jupyter pls install this package
# from nest_asyncio import apply


async def test_ask() -> None:
    bot = None
    try:
        bot = await Chatbot.create(cookies=json.loads(getenv("EDGE_COOKIES")), mode="Bing",
                                   plugin_ids=["c310c353-b9f0-4d76-ab0d-1dd5e979cf68"])
        prompt = """Rome (Italian and Latin: Roma, Italian: [ˈroːma] ⓘ) is the capital city of Italy. It is also the capital of the Lazio region, the centre of the Metropolitan City of Rome Capital, and a special comune (municipality) named Comune di Roma Capitale. With 2,860,009 residents in 1,285 km2 (496.1 sq mi),[2] Rome is the country's most populated comune and the third most populous city in the European Union by population within city limits. The Metropolitan City of Rome, with a population of 4,355,725 residents, is the most populous metropolitan city in Italy.[3] Its metropolitan area is the third-most populous within Italy.[5] Rome is located in the central-western portion of the Italian Peninsula, within Lazio (Latium), along the shores of the Tiber. Vatican City (the smallest country in the world)[6] is an independent country inside the city boundaries of Rome, the only existing example of a country within a city. Rome is often referred to as the City of Seven Hills due to its geographic location, and also as the "Eternal City". Rome is generally considered to be the cradle of Western civilization and Western Christian culture, and the centre of the Catholic Church.[7][8][9]

Rome's history spans 28 centuries. While Roman mythology dates the founding of Rome at around 753 BC, the site has been inhabited for much longer, making it a major human settlement for almost three millennia and one of the oldest continuously occupied cities in Europe.[10] The city's early population originated from a mix of Latins, Etruscans, and Sabines. Eventually, the city successively became the capital of the Roman Kingdom, the Roman Republic and the Roman Empire, and is regarded by many as the first-ever Imperial city and metropolis.[11] It was first called The Eternal City (Latin: Urbs Aeterna; Italian: La Città Eterna) by the Roman poet Tibullus in the 1st century BC, and the expression was also taken up by Ovid, Virgil, and Livy.[12][13] Rome is also called "Caput Mundi" (Capital of the World).

After the fall of the Empire in the west, which marked the beginning of the Middle Ages, Rome slowly fell under the political control of the Papacy, and in the 8th century, it became the capital of the Papal States, which lasted until 1870. Beginning with the Renaissance, almost all popes since Nicholas V (1447–1455) pursued a coherent architectural and urban programme over four hundred years, aimed at making the city the artistic and cultural centre of the world.[14] In this way, Rome first became one of the major centres of the Renaissance[15] and then became the birthplace of both the Baroque style and Neoclassicism. Famous artists, painters, sculptors, and architects made Rome the centre of their activity, creating masterpieces throughout the city. In 1871, Rome became the capital of the Kingdom of Italy, which, in 1946, became the Italian Republic.

In 2019, Rome was the 14th most visited city in the world, with 8.6 million tourists, the third most visited city in the European Union, and the most popular tourist destination in Italy.[16] Its historic centre is listed by UNESCO as a World Heritage Site.[17] The host city for the 1960 Summer Olympics, Rome is also the seat of several specialised agencies of the United Nations, such as the Food and Agriculture Organization (FAO), the World Food Programme (WFP) and the International Fund for Agricultural Development (IFAD). The city also hosts the Secretariat of the Parliamentary Assembly of the Union for the Mediterranean[18] (UfM) as well as the headquarters of many multinational companies, such as Eni, Enel, TIM, Leonardo, and banks such as BNL. Numerous companies are based within Rome's EUR business district, such as the luxury fashion house Fendi located in the Palazzo della Civiltà Italiana. The presence of renowned international brands in the city has made Rome an important centre of fashion and design, and the Cinecittà Studios have been the set of many Academy Award–winning movies.[19]

Name and symbol
Etymology
According to the Ancient Romans' founding myth,[20] the name Roma came from the city's founder and first king, Romulus.[1]

However, it is possible that the name Romulus was actually derived from Rome itself.[21] As early as the 4th century, there have been alternative theories proposed on the origin of the name Roma. Several hypotheses have been advanced focusing on its linguistic roots which however remain uncertain:[22]

From Rumon or Rumen, archaic name of the Tiber, which in turn is supposedly related to the Greek verb ῥέω (rhéō) 'to flow, stream' and the Latin verb ruō 'to hurry, rush';[b]
From the Etruscan word 𐌓𐌖𐌌𐌀 (ruma), whose root is *rum- "teat", with possible reference either to the totem wolf that adopted and suckled the cognately named twins Romulus and Remus, or to the shape of the Palatine and Aventine Hills;
From the Greek word ῥώμη (rhṓmē), which means strength.[c]
Other names and symbols
Rome has also been called in ancient times simply "Urbs" (central city),[23] from urbs roma, or identified with its ancient Roman initialism of SPQR, the symbol of Rome's constituted republican government. Furthermore, Rome has been called Urbs Aeterna (The Eternal City), Caput Mundi (The Capital of the world), Throne of St. Peter and Roma Capitale.

History
Main article: History of Rome
For a chronological guide, see Timeline of Rome.

Lazio (UK: /ˈlætsioʊ/ LAT-see-oh, US: /ˈlɑːt-/ LAHT-, Italian: [ˈlattsjo]) or Latium (/ˈleɪʃiəm/ LAY-shee-əm, US also /-ʃəm/ -⁠shəm;[4][5][6][7] from the original Latin name, pronounced [ˈɫati.ũː]) is one of the 20 administrative regions of Italy. Situated in the central peninsular section of the country, it has 5,714,882 inhabitants and a GDP of more than €197 billion per year, making it the country's second most populated region[1] and second largest regional economy after Lombardy. The capital of Lazio is Rome, which is also the capital and largest city of Italy.

Lazio is rich in a multi-millennial heritage: it sees the presence of the Etruscan civilization, then at the center of the Roman Empire, of the Holy Roman Empire, then of the Papal States, of the First French Empire and of the Italian Republic. The historical, artistic, cultural, architectural, archaeological and religious heritage of Lazio is immensely vast and rich in cultural diversity. Some of the greatest artists and historical figures lived and worked in Rome, such as Bramante, Raffaello Sanzio, Filippo Brunelleschi, Donatello, Michelangelo, Gian Lorenzo Bernini, Leonardo da Vinci, Francesco Borromini, Pietro da Cortona, Johann Wolfgang von Goethe, Rubens, Van Dyck and Diego Velázquez.

Today it constitutes a dynamic region. Lazio is a large center of services and international trade, industry, public services and tourism, supported by a privileged transport network thanks to its geographical position in the center of Italy and the presence of Rome within it.

Geography

Relief map of Lazio

Panorama of the Aniene Valley
Lazio comprises a land area of 17,242 km2 (6,657 sq mi) and it has borders with Tuscany, Umbria, and Marche to the north, Abruzzo and Molise to the east, Campania to the south, and the Tyrrhenian Sea to the west. The region is mainly flat, with small mountainous areas in the most eastern and southern districts.

The coast of Lazio is mainly composed of sandy beaches, punctuated by the headlands of Cape Circeo (541 m) and Gaeta (171 m). The Pontine Islands, which are part of Lazio, are off Lazio's southern coast. Behind the coastal strip, to the north, lies the Maremma Laziale (the continuation of the Tuscan Maremma), a coastal plain interrupted at Civitavecchia by the Tolfa Mountains (616 m). The central section of the region is occupied by the Roman Campagna, a vast alluvial plain surrounding the city of Rome, with an area of approximately 2,100 km2 (811 sq mi). The southern districts are characterized by the flatlands of Agro Pontino, a once swampy and malarial area, that was reclaimed over the centuries.

The Preapennines of Latium, marked by the Tiber valley and the Liri with the Sacco tributary, include on the right of the Tiber, three groups of mountains of volcanic origin: the Volsini, Cimini and Sabatini, whose largest former craters are occupied by the Bolsena, Vico and Bracciano lakes. To the south of the Tiber, other mountain groups form part of the Preapennines: the Alban Hills, also of volcanic origin, and the calcareous Lepini, Ausoni and Aurunci Mountains. The Apennines of Latium are a continuation of the Apennines of Abruzzo: the Reatini Mountains with Terminillo (2,213 m), Mounts Sabini, Prenestini, Simbruini and Ernici which continue east of the Liri into the Mainarde Mountains. The highest peak is Mount Gorzano (2,458 m) on the border with Abruzzo.

Climate
The region's climate, monitored by several dozen meteorological stations (many of which managed by the Lazio Regional Hydrographic and Mareographic Office), shows considerable variability from area to area. In general, along the coast, there is a mediterranean climate, the temperature values vary between 9–10°C (48–50°F) in January and 24–25°C (75–77°F) in July. Towards the interior, the climate is more continental and, on the hills, winters are cold and at night, temperatures can be quite frigid.

With particular regard to the sunshine duration, it should also be noted that, among the regional capital cities in Italy, Rome is the one with the highest number of hours of sunshine and days with clear skies during the year.

History
For the history of ancient Lazio, see Latium.
See also: List of museums in Lazio

The Appian Way (Via Appia), a road connecting Ancient Rome to the southern parts of Italy, remains usable even today.
The Italian word Lazio descends from the Latin word Latium, the region of the Latins, Latini in the Latin language spoken by them and passed on to the Latin city-state of Ancient Rome. Although the demography of ancient Rome was multi-ethnic, including, for example, Etruscans, Sabines and other Italics besides the Latini, the latter were the dominant constituent. In Roman mythology, the tribe of the Latini took their name from King Latinus. Apart from the mythical derivation of Lazio given by the ancients as the place where Saturn, ruler of the golden age in Latium, hid (latuisset)[8] from Jupiter there,[9] a major modern etymology is that Lazio comes from the Latin word "latus", meaning "wide",[10] expressing the idea of "flat land" meaning the Roman Campagna. Much of Lazio is in fact flat or rolling. The lands originally inhabited by the Latini were extended into the territories of the Samnites, the Marsi, the Hernici, the Aequi, the Aurunci and the Volsci, all surrounding Italic tribes. This larger territory was still called Latium, but it was divided into Latium adiectum or Latium Novum, the added lands or New Latium, and Latium Vetus, or Old Latium, the older, smaller region. The northern border of Lazio was the Tiber river, which divided it from Etruria.

The emperor Augustus officially united almost all of present-day Italy into a single geo-political entity, Italia, dividing it into eleven regions. The part of today's Lazio south of the Tiber river – together with the present region of Campania immediately to the southeast of Lazio and the seat of Neapolis – became Region I (Latium et Campania), while modern Upper Lazio became part of Regio VII – Etruria, and today's Province of Rieti joined Regio IV – Samnium.

After the Gothic conquest of Italy at the end of the fifth century, modern Lazio became part of the Ostrogothic Kingdom, but after the Gothic War between 535 and 554 and conquest by the Byzantine Empire, the region became the property of the Eastern Emperor as the Duchy of Rome. However, the long wars against the Longobards weakened the region. With the Donation of Sutri in 728, the Pope acquired the first territory in the region beyond the Duchy of Rome.

The strengthening of the religious and ecclesiastical aristocracy led to continuous power struggles between secular lords (Baroni) and the Pope until the middle of the 16th century. Innocent III tried to strengthen his own territorial power, wishing to assert his authority in the provincial administrations of Tuscia, Campagna and Marittima through the Church's representatives, in order to reduce the power of the Colonna family. Other popes tried to do the same. During the period when the papacy resided in Avignon, France (1309–1377), the feudal lords' power increased due to the absence of the Pope from Rome. Small communes, and Rome above all, opposed the lords' increasing power, and with Cola di Rienzo, they tried to present themselves as antagonists of the ecclesiastical power. However, between 1353 and 1367, the papacy regained control of Lazio and the rest of the Papal States. From the middle of the 16th century, the papacy politically unified Lazio with the Papal States,[11] so that these territories became provincial administrations of St. Peter's estate; governors in Viterbo, in Marittima and Campagna, and in Frosinone administered them for the papacy.

Lazio was part of the short-lived Roman Republic, after which it became a puppet state of the First French Republic under the forces of Napoleon Bonaparte. Lazio was returned to the Papal States in October 1799. In 1809, it was annexed to the French Empire under the name of the Department of Tibre, but returned to the Pope's control in 1815.

On 20 September 1870 the capture of Rome, during the reign of Pope Pius IX, and France's defeat at Sedan, completed Italian unification, and Lazio was incorporated into the Kingdom of Italy. In 1927, the territory of the Province of Rieti, belonging to Umbria and Abruzzo, joined Lazio. Towns in Lazio were devastated by the 2016 Central Italy earthquake.[12]"""
        print(f"prompt len is: {len(prompt)}")
        response = await bot.ask(
            prompt=prompt,
            conversation_style=ConversationStyle.balanced,
            simplify_response=True,
            search_result=True
        )
        # If you are using non ascii char you need set ensure_ascii=False
        print(json.dumps(response, indent=2, ensure_ascii=False).encode("utf-8"))
    except Exception as error:
        raise error
    finally:
        if bot is not None:
            await bot.close()


if __name__ == "__main__":
    # If you are using jupyter pls use nest_asyncio apply()
    # apply()
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(test_ask())
