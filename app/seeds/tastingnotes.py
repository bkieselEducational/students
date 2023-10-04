from app.models import db, TastingNote, environment, SCHEMA
from sqlalchemy.sql import text


def seed_tasting_notes():
    note1 = TastingNote(
        user_id=3,
        tea_id=1,
        note="Love this tea! Super organic",
        score=93,
        flavors=""
    )

    note2 = TastingNote(
        user_id=4,
        tea_id=1,
        note="Bought this for the blackberry note, but the yam and honey taste was the most prevalent thing in the liquor. It has a lingering sweetness that sticks in your throat after you swallow and that pleasantly funky flavor and aroma that all Taiwan blacks seem to have. Almost like the old paper in an ancient book that aged out of the musty stage. Starting to think that Taiwan blacks aren’t for me because of this note, but that’s alright, this one was a pleasant experience.",
        score=89,
        flavors="Honey, Sweet, Yams"
    )

    note3 = TastingNote(
        user_id=3,
        tea_id=2,
        note="Great taste!!",
        score=92,
        flavors=""
    )

    note4 = TastingNote(
        user_id=4,
        tea_id=2,
        note="Grabbed a sample of this from the tea box, but I’ve been procrastinating trying it since it didn’t seem very exciting. Yeah, it was way too light and mild for my tastes in black tea. The color came out quite clear as well. I didn’t add milk because that would drown out all tea taste. Instead, I added some raspberry extract so that my cup would taste like something. The tea itself didn’t taste bad. It did have a nice flavor, but it was too light.",
        score=86,
        flavors=""
    )

    note5 = TastingNote(
        user_id=3,
        tea_id=3,
        note="This tea has been comforting me during the ice storm today. Hope all my fellow Midwestern Steepsterites are warm and safe!",
        score=95,
        flavors=""
    )

    note6 = TastingNote(
        user_id=4,
        tea_id=3,
        note="I’ll continue sipping this for a few more rounds. It is a nice richly satisfying Shu, without any of the musty or ammonia-like smells, it has a certain earthiness to it, a deeply grounding sensation more than a taste. Next time I’ll probably give it the full on 3 minute treatment, as I’m one who tends to surrender to the dark side!",
        score=83,
        flavors="Cocoa, Earth"
    )

    note7 = TastingNote(
        user_id=3,
        tea_id=4,
        note="This is the best Earl Grey I have ever tasted. PERIOD!!!",
        score=100,
        flavors="Bergamot, Flowers, Lemon, Orange"
    )

    note8 = TastingNote(
        user_id=4,
        tea_id=4,
        note="Thanks so much for the awesome swap, derk!  The swap was inspired by this tea — an Earl I’d never heard of before.  (Have to try ALL the bergamot.)  The leaves here are larger than is typically seen flavored with bergamot so I went with two loose teaspoons for a mug, so as not to spill any leaves all over the place… so it could really be 1 1/2 teaspoons if I was really packing the leaves into the teaspoon. The flavor is lovely this way but I will try it with less leaves next time anyway.   The black tea is brisk enough with two teaspoons, without being overpowering, but I didn’t really expect any astringency from these big leaves.  The bergamot is tasty — bright, strong citrus, sometimes hints of cream occasionally which is unexpected… or maybe I’m just imaginging this/wishing this.  I miss my unnatural as all getout cream EGs.  It’s amazing that some bergamot can be the best tasting flavor ever, but then others can be the most disgusting flavor.  Maybe this isn’t my favorite bergamot ever (it’s great!) but that will be tough to find these days (which is exactly the reason derk offered to send some of this over).  I will certainly enjoy the remainder of this sample!",
        score=77,
        flavors=""
    )

    note9 = TastingNote(
        user_id=3,
        tea_id=5,
        note="This tea tastes smooth and milky with a little caramel in the finish. It doesn’t have that cardboard taste that I find many oolongs have, which is what turns me off of oolongs. I haven’t figured out the perfect steeping parameters yet, but I think I like it oversteeped a bit since it gives a richer flavor.",
        score=89,
        flavors="Butter, Coconut, Cream, Custard, Mango, Mineral, Paper, Popcorn, Rice, Sweet, Warm Grass, Toasted Rice, Vanilla, Walnut, Wood"
    )

    note10 = TastingNote(
        user_id=4,
        tea_id=5,
        note="The scent is very distinctive. I love it but can’t accurately discribe it. Never smelled anything quite like it before. Someone commented that the smell is typical of oolongs. As this is my first oolong I can’t second that. The taste is very smooth, sweet and buttery. In stead of leaning towards vegetal, is has a somewhat nutty basis (very faint). It also reminds me a bit of avocado’s, not in terms of exact taste, but rather in a likeness of character.",
        score=88,
        flavors=""
    )

    note11 = TastingNote(
        user_id=3,
        tea_id=6,
        note="Very smooth with a slightly bitter sweetnes and a great Qi.",
        score=85,
        flavors=""
    )

    note12 = TastingNote(
        user_id=4,
        tea_id=6,
        note="This tea is a very strong contender in the “pine/resin/astringent/drying” category. There is a surprisingly mild, yet very balanced array of complexity in the flavors of this tea. The body is smooth and viscous and the color is a nice deeper golden yellow. It is slightly sweet, slightly herbaceous, and has a reasonably sufficient amount of the astringent mouth-drying effect, but without the offputting bitterness – this is a character I look for in these types of teas, and value quite highly in evaluation. Overall, I’d say this is a lighter, more balanced, “little brother” version of the 2005 Shenlin YQH (a personal favorite of mine). The Baotang delivers in quality without the mushroomy/earthy notes and the more potent drying effects of the 05 YQH. I do recommend giving this tea a try, it is certainly high caliber.",
        score=87,
        flavors="Astringent, Drying, Herbaceous, Resin, Sweet"
    )

    all_tasting_notes1 = [note1, note2, note3, note4, note5, note6,
                         note7, note8, note9, note10, note11, note12]
    add_tasting_notes = [db.session.add(tasting_note) for tasting_note in all_tasting_notes1]
    db.session.commit()


    note13 = TastingNote(
        user_id=2,
        tea_id=7,
        note="This is quite possibly my favorite Earl Grey. So smooth, so creamy, doesn’t need anything added to it for the absolute perfect cup for breakfast or with a mid-afternoon piece of chocolate.",
        score=95,
        flavors="Cream"
    )

    note14 = TastingNote(
        user_id=4,
        tea_id=7,
        note="This tea is a cup of coziness. Vanilla and earl grey together definitely give off a birthday cake-y essence. Divine with milk and sugar.",
        score=85,
        flavors="Bergamot, Vanilla"
    )

    note15 = TastingNote(
        user_id=2,
        tea_id=8,
        note="I apologize; this tea deserves a better tasting note than I have energy to write. It is a delicious, somewhat floral, creamy oolong though, and that’s what I needed/wanted tonight. Looking forward to trying the rest of my oolong samples from Fong Mong Tea! I did reserve enough of this to try it again when I have time to properly review it.",
        score=91,
        flavors=""
    )

    note16 = TastingNote(
        user_id=4,
        tea_id=8,
        note="Mmm, this is good. It tastes like a combination of a green oolong and a plain ol’ green tea to me. There is a slight floral aspect, but it’s very mellow. There’s a bright, fresh “green” taste to it with a little nuttiness and strong notes of fruit, with a slightly creamy texture. Thanks for the sample, Fong Mong Tea!",
        score=87,
        flavors="Creamy, Floral, Vegetal"
    )

    note17 = TastingNote(
        user_id=2,
        tea_id=9,
        note="One of my all-time favourites. The base tastes stronger than usual, fuller and more robust, but probably because I used more leaf. It’s good though! I should do that in the morning rather than 9pm.",
        score=100,
        flavors=""
    )

    note18 = TastingNote(
        user_id=4,
        tea_id=9,
        note="I got this as a sample with my recent order and I have been dying to try it. The leaves have a very strong maple fragrance. The tea itself is more nutty than anything. I had high hopes for maple, but it’s still a great tea. Sweet and light!",
        score=80,
        flavors=""
    )

    note19 = TastingNote(
        user_id=2,
        tea_id=10,
        note="As soon as the liquor hits the tongue it IS quite candy-like…nice and sweet! Then it’s smooth, creamy, buttery, and sweet. There is a lovely smooth-floral after taste – much like honeysuckle! I’m going to do multiple infusions on this one!",
        score=89,
        flavors=""
    )

    note20 = TastingNote(
        user_id=4,
        tea_id=10,
        note="What a gorgeous tea! Intoxicating-smelling and delicious, this is definitely the nicest Tieguanyin I’ve got my hands on so far. This is my tea happy place, for sure. It’s fascinating to evolve with it through the infusions, and the experience makes me feel so privileged and content. This is floral, green, sweet, and creamy in ways that change slightly between infusions but that remain perfectly balanced. Delicate and yet satisfyingly robust!",
        score=88,
        flavors=""
    )

    note21 = TastingNote(
        user_id=2,
        tea_id=11,
        note="Wow, this tea is pretty extraordinary. The jasmine is incredibly fragrant, and pairs perfectly with the cherry and stone fruit notes of the black tea. This is one of those teas that made my jaw drop.",
        score=92,
        flavors="Cherry, Jasmine, Stonefruit"
    )

    note22 = TastingNote(
        user_id=4,
        tea_id=11,
        note="This is the first true tea I am trying from the new set of samples I got from derk, thanks a lot my friend! :) As for the tea, it’s magnificent. Bitter-sweet. Very mouth-watering, soft and biting mouthfeel. Perfect balance of the jasmine florals and dian hong maltiness. Long lasting and evolving aftertaste. One of a kind.",
        score=85,
        flavors="Anise, Biting, Bitter, Citrus, Coffee, Floral, Jasmine, Malt, Smooth, Sweet, Vanilla"
    )

    note23 = TastingNote(
        user_id=2,
        tea_id=12,
        note="One of my all time favourites. Can’t stand this smoking aroma!",
        score=99,
        flavors="Earth, Plum, Smoke, Smoked"
    )

    note24 = TastingNote(
        user_id=4,
        tea_id=12,
        note="Has the aroma of Laphroiag or Talisker whisky with the smell of phenols, creosote and tar coming strongly through. If you like peaty whiskies you’ll love this taste but the aroma is even more incredible. If it tasted like it smelt it would probably be undrinakable but the taste though peaty has no bad aftertastes and is quite rich in texture. I thought I would try a cup and ended up having another straight after.",
        score=90,
        flavors="Campfire, Earth, Medicinal, Pine, Smoke, Tobacco, Whiskey"
    )

    all_tasting_notes2 = [note13, note14, note15, note16, note17, note18,
                         note19, note20, note21, note22, note23, note24]
    add_tasting_notes2 = [db.session.add(tasting_note) for tasting_note in all_tasting_notes2]
    db.session.commit()


    note25 = TastingNote(
        user_id=2,
        tea_id=13,
        note="The aroma of the rinse was rich, buttery, like a floral crispy pastry. The first sip reminded me of the caramelization of meat or sweet potatoes roasted in honey. Later, I got an intensely floral flavor – again like honey. There was something in the experience that reminded of a church smell if churches smelled good – maybe somewhere in the area of old library book about bees and summer flowers.",
        score=95,
        flavors="Floral, Honey, Meat, Sweet Potatoes"
    )

    note26 = TastingNote(
        user_id=3,
        tea_id=13,
        note="The brewed tea smells lovely, I’m getting notes of caramel, subtle roast, nuts (pecan?), and minerals. It sort of smells like a “more roasty” praline! On the sip I’m getting notes of minerally earth, roasted nuts, and a touch of honey-baked bread. There is a florality in the aftertaste, but I can’t place it. The sweetness and toasty/nutty notes really do give me a sort of praline or nougat impression. I think my only complaint is that it is a touch drying, and I wonder if dropping my leaf amount just slightly might smooth that out.",
        score=88,
        flavors="Bread, Candy, Caramel, Drying, Earth, Floral, Honey, Mineral, Nutty, Roasted, Roasted Nuts, Sweet"
    )

    note27 = TastingNote(
        user_id=2,
        tea_id=14,
        note="The first time I tried this I didn’t care for it, so I stashed it in a drawer and forgot about it. That was about 2 years ago, and I just dug it back out again. With some aging, the vanilla has become so strong, with just a touch of cedar. The oolong is bright green and fresh, with a pop of lilac. Really interesting base combined with the vanilla and cedar.",
        score=85,
        flavors=""
    )

    note28 = TastingNote(
        user_id=3,
        tea_id=14,
        note="Smelled amazing, but the taste was just a bit off!",
        score=86,
        flavors=""
    )

    all_tasting_notes3 = [note25, note26, note27, note28]
    add_tasting_notes3 = [db.session.add(tasting_note) for tasting_note in all_tasting_notes3]
    db.session.commit()

    # note1 = TastingNote(
    #     user_id=3,
    #     tea_id=1,
    #     note="",
    #     score=,
    #     flavors=""
    # )

    # note2 = TastingNote(
    #     user_id=4,
    #     tea_id=1,
    #     note="",
    #     score=,
    #     flavors=""
    # )


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_tasting_notes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tasting_notes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM tasting_notes"))

    db.session.commit()
