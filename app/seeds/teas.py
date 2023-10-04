from app.models import db, Tea, environment, SCHEMA
from sqlalchemy.sql import text


def seed_teas():
    tea1 = Tea(
        user_id=2,
        name="Taiwan Wild 'Shan Cha' Black Tea",
        company='What-Cha',
        type='Black Tea',
        sold_in='Loose Leaf',
        certification='',
        ingredients='Black Tea Leaves',
        caffeine='High',
        description='A most unique tea which is indigenous to Taiwan and still grows wild in certain areas. It is rarely sold as the plant loses its distinct characteristics when cultivated and so the only tea production is from the surviving wild growing bushes.',
        image_url='https://www.filepicker.io/api/file/TBYaZlNR5svTwLegnptw/convert?fit=max&h=480&w=940'
    )

    tea2 = Tea(
        user_id=2,
        name='Royal Ceylon Flowery Black Tea',
        company='Elephant Chateau',
        type='Black Tea',
        sold_in='Bulk, Loose Leaf',
        certification='Fair Trade, Kosher, Organic, Vegan',
        ingredients='Ceylon Black Tea, Organic Black Tea',
        caffeine='Medium',
        description='Royal Ceylon Flowery Black Tea leaves selected by the very best Ceylon Master Teamen and presented to you with the permission of the Elephant Chateau and the Ceylon Flavor Foundation. Every ethically sourced product we offer is certified organic and prepared with the utmost attention to quality.',
        image_url='https://www.filepicker.io/api/file/GsQJmEVRTtirFOiK0eX1/convert?fit=max&h=480&w=940'
    )

    tea3 = Tea(
        user_id=2,
        name='Special Dark',
        company='Mandala Tea',
        type="Pu'erh Tea",
        sold_in='Bulk, Loose Leaf',
        certification='',
        ingredients='',
        caffeine='',
        description="We call this Special Dark for good reason. This decadent tea is hand crafted in small batches within cotton bags, and fermented more extensively requiring great attention and intention. Creamy, rich, dark, and smooth. This cocoa-y indulgence is one of our most unique pu’er teas. An excellent change-up from the norm for you lovers of the shu.",
        image_url='https://www.filepicker.io/api/file/Foy1egmTcyLp5cpJKzHq/convert?fit=max&h=480&w=940'
    )

    tea4 = Tea(
        user_id=2,
        name='Persian Choice Royal Earl Grey',
        company="Alvin's of San Francisco",
        type='Black Tea',
        sold_in='',
        certification='',
        ingredients='',
        caffeine='',
        description='In the ancient Persian court, legend says that the ideas of royalty, excellence and the good life evolved around the sacred tea ceremonies where only the very best tea blends were served. Centuries later tea is still a staple of Persian cuisine. We are proud to present Persian Choice Royal Earl Gray Tea, a secret blend prepared in accordance with these ancient sentiments. Made from the absolute highest quality tea leaves from Ceylon, Assam, and Darjeeling, this pungent Earl Grey blend has been transformed into pure royalty.',
        image_url='https://www.filepicker.io/api/file/wgmZkAT3ul10JTAxdlvQ/convert?fit=max&h=480&w=940'
    )

    tea5 = Tea(
        user_id=2,
        name="J.E. Oolong Milky",
        company="THEODOR",
        type="Oolong Tea",
        sold_in="Loose Leaf",
        certification="Kosher",
        ingredients="Oolong Tea",
        caffeine="",
        description="In some way you and I are very much alike... I live in a huge, cozy, Haussmann-style apartment with view on the Eiffel Tower, with about twenty rooms, one more spacious than the one next to it. So we appreciate good things and we take delight in sitting on our sofa and drinking a ‘J.E Oolong Milky – Jin Xuan’ plain green tea, elixir of heaven, with milky and vanilla-flavored notes.",
        image_url="https://www.filepicker.io/api/file/uDVCOgTzTcmMoO6oRhQn/convert?fit=max&h=480&w=940"
    )

    tea6 = Tea(
        user_id=2,
        name="2012 EoT Baotang Puerh",
        company="The Essence of Tea",
        type="Pu'erh Tea",
        sold_in="Bulk, Loose Leaf",
        certification="Fair Trade, Vegan",
        ingredients="",
        caffeine="",
        description="Baotang is located in the Mengsong region of Menghai. This tea is produced from trees averaging around 300-400 years old in cooperation with a local friend from Menghai, who stayed in the village for 2 months this Spring, setting up a hand-processing workshop and processing the fresh leaves himself.",
        image_url="https://www.filepicker.io/api/file/XGTQheU2TmzRR21gCGIH/convert?fit=max&h=480&w=940"
    )

    user2_teas = [tea1, tea2, tea3, tea4, tea5, tea6]
    add_user2_teas = [db.session.add(user2_tea) for user2_tea in user2_teas]
    db.session.commit()

    tea7 = Tea(
        user_id=3,
        name="Creme de la Earl Grey",
        company="TeaLuxe",
        type="Black Tea",
        sold_in="Bulk, Loose Leaf",
        certification="",
        ingredients="Bergamot, Black Tea, Flower Petals",
        caffeine="",
        description="Quintessential English style tea with blended blue flowers and a twist of cream. A fabulous tea.",
        image_url="https://www.filepicker.io/api/file/1xcyNVAR163Dyu5cZDT7/convert?fit=max&h=480&w=940"
    )

    tea8 = Tea(
        user_id=3,
        name="Zhu Lu Alishan High Mt. Oolong Tea",
        company="fongmongtea",
        type="Oolong Tea",
        sold_in="Loose Leaf",
        certification="Fair Trade, Vegan",
        ingredients="Oolong, Oolong Tea, Oolong Tea Leaves",
        caffeine="Low",
        description="The tea liquor has a pale yellow hue matching its faintly fresh aroma. Once tasted, the tea presents itself with a fresh taste followed by a faintly sweet aftertaste. A relaxing and memorable oolong, ultimate comfort tea, is a great introduction to Taiwanese High Mt. Tea.",
        image_url="https://www.filepicker.io/api/file/T1rdJhT9T8WnhsrdcgvO/convert?fit=max&h=480&w=940"
    )

    tea9 = Tea(
        user_id=3,
        name="Maple Pecan Oolong",
        company="Butiki Teas",
        type="Oolong Tea",
        sold_in="Loose Leaf",
        certification="",
        ingredients="Nilgiri Frost Oolong, Organic Natural Flavors (Vegan), Pecans",
        caffeine="",
        description="Our Maple Pecan Oolong utilizes our Nilgiri Frost Oolong base. This smooth, silky tea has maple notes that develop into pecan notes then finish with maple notes that linger. Some citrus notes may also be detected. The flavors weave together brilliantly and are well balanced with the oolong base. With a little sugar the maple and pecan intensify for a wonderful desert treat that resembles a pecan pie. We recommend adding sugar slowly; too much sugar and the tea will taste like exactly like fresh maple syrup with a hint of pecan.",
        image_url="https://www.filepicker.io/api/file/vmXahoGCRTSoR9AsddnD/convert?fit=max&h=480&w=940"
    )

    tea10 = Tea(
        user_id=3,
        name="Hand Picked Tieguanyin Spring Oolong (2011)",
        company="Verdant Tea",
        type="Oolong Tea",
        sold_in="Loose Leaf",
        certification="",
        ingredients="Oolong Tea",
        caffeine="Medium",
        description="Through the first few steepings this tea tastes almost candy like. There are strong notes of orchid and honeysuckle that linger in the back of the throat like licorice root. In steeping three the extremely creamy and buttery quality of this tea comes through to support the floral nature. It tastes almost like fresh Spanish saffron and clover honey. Late in steeping, the floral and creamy notes continue and the complexity builds with the introduction of sweet grass notes. The flavor yields excellent infusions for about thirty steepings in a gaiwan, or 10 in a traditional tea pot.",
        image_url="https://www.filepicker.io/api/file/84cnuVtQM2H3tOExihbL/convert?fit=max&h=480&w=940"
    )

    tea11 = Tea(
        user_id=3,
        name="Alice",
        company="Whispering Pines Tea Company",
        type="Black Tea",
        sold_in="Loose Leaf",
        certification="",
        ingredients="Jasmine, Yunnan Black Tea",
        caffeine="High",
        description="After years of seeking the perfect jasmine black tea, the search comes to this — Alice. The highest quality Yunnan black tea scented perfectly with warm, inviting jasmine. Rich, powerful jasmine wafting through fields of malt and honey…It’s almost impossible to believe how much magic can fit in one tea, though some of us try to believe at least 6 impossible things before breakfast.",
        image_url="https://www.filepicker.io/api/file/sBSmjDwMS6oRMOFDazXG/convert?fit=max&h=480&w=940"
    )

    tea12 = Tea(
        user_id=3,
        name="Lapsang Souchong",
        company="Fortnum & Mason",
        type="Black Tea",
        sold_in="Loose Leaf",
        certification="",
        ingredients="",
        caffeine="",
        description="To give this tea its unmistakable flavour, the plucked leaves are placed in bamboo baskets and smoked over smouldering fires from particular pine trees. Once confined to China’s Fujian province, it is now enjoyed across the globe. Drink it alone, or add a spoonful to other black teas to lend them a hint of its aromatic flavour.",
        image_url="https://www.filepicker.io/api/file/OKhaP6spTVWcHBb0fRqK/convert?fit=max&h=480&w=940"
    )

    user3_teas = [tea7, tea8, tea9, tea10, tea11, tea12]
    add_user3_teas = [db.session.add(user3_tea) for user3_tea in user3_teas]
    db.session.commit()

    tea13 = Tea(
        user_id=4,
        name='"King of Duck Shit Aroma" Dan Cong Oolong Tea (Spring 2017)',
        company="Yunnan Sourcing",
        type="Oolong Tea",
        sold_in="Bulk, Loose Leaf",
        certification="",
        ingredients="Oolong Tea Leaves",
        caffeine="",
        description="It’s called “duck shit aroma” because in the Ping Keng Tou village area the soil has a somewhat yellow brown look to it and is unique to that area. With all teas the soil type is a key element in the tea’s taste. Villagers wanting to guard the uniqueness of their tea bushes told outsiders that the color and uniqueness of the soil in their village was due to copious amounts of duck shit and began to call the their Dan Cong “duck shit aroma”. True or not it’s an entertaining story which reveals why the tea has such a gross name.",
        image_url="https://www.filepicker.io/api/file/S0rP3pN3TRep79jQGnK1/convert?fit=max&h=480&w=940"
    )

    tea14 = Tea(
        user_id=4,
        name="Rivendell",
        company="Whispering Pines Tea Company",
        type="Oolong Tea",
        sold_in="Loose Leaf",
        certification="",
        ingredients="Oolong Tea, Tahitian Vanilla, Wildcrafted Roasted Cedar Leaves",
        caffeine="Medium",
        description="Rivendell opens with the taste of cedar, cherry, and caramel flowing through a luscious sweet body. The middle of the sip coats your mouth with a nectar-like sweetness and hints at vanilla and chocolate, with a touch of pine nut and mineral, reminiscent of spring water that has flowed over miles of untouched granite. The finish is clean with hints of lilac and pear, leaving an aftertaste of cedar and caramel. It tastes as if the purest water in the world flowed through miles of sugarcane fields, scattered with nectar-filled lilacs and orchids, passed through a forest of cedar and cherry trees, then poured over a pristine granite cliff straight into your cup. It’s pure nectar and caramel with light florals, a hint of berries and chocolate, a touch of pine nut, and heady evergreen sweetness.",
        image_url="https://www.filepicker.io/api/file/cLjVJp8rQdeg6S6t1lNP/convert?fit=max&h=480&w=940"
    )

    user4_teas = [tea13, tea14]
    add_user4_teas = [db.session.add(user4_tea) for user4_tea in user4_teas]
    db.session.commit()

    # tea7 = Tea(
    #     user_id=2,
    #     name="",
    #     company="",
    #     type="",
    #     sold_in="",
    #     certification="",
    #     ingredients="",
    #     caffeine="",
    #     description="",
    #     image_url=""
    # )


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_teas():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teas RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teas"))

    db.session.commit()
