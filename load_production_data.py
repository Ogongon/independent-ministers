import os
import django
import datetime
from django.utils.timezone import make_aware

# 1. Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from spiritual_maps.models import SpiritualSite
from scriptures.models import ScriptureComparison
from core.models import WeeklyVideo, HomePage 
from blog.models import BlogIndexPage, BlogPage
from wagtail.models import Page, Site

def import_production_data():
    print("🚀 Starting MASSIVE Data Import for Independent Ministers...")

    # =========================================================
    # PART 1: 50 SPIRITUAL SITES
    # =========================================================
    print("📍 Generating 50 Spiritual Sites...")
    
    sites = [
        {"name": "Rabai Mpya (Krapf Memorial)", "lat": -3.9314, "lng": 39.5675, "desc": "Est. 1846. The cradle of Christianity in Kenya."},
        {"name": "Frere Town (Kisauni)", "lat": -4.0500, "lng": 39.6833, "desc": "Est. 1875 by CMS for freed slaves."},
        {"name": "Holy Ghost Cathedral", "lat": -4.0645, "lng": 39.6750, "desc": "Historic Roman Catholic cathedral in Mombasa."},
        {"name": "ACK Mombasa Memorial Cathedral", "lat": -4.0620, "lng": 39.6730, "desc": "Anglican cathedral with Moorish architecture."},
        {"name": "Mbaraki Pillar", "lat": -4.0750, "lng": 39.6600, "desc": "Ancient coral rag pillar."},
        {"name": "Fort Jesus Chapel Ruins", "lat": -4.0630, "lng": 39.6780, "desc": "Ruins of the Portuguese chapel inside the fort."},
        {"name": "St. Luke's Makupa", "lat": -4.0400, "lng": 39.6500, "desc": "One of the oldest CMS churches serving railway workers."},
        {"name": "Jomvu Methodist Mission", "lat": -4.0100, "lng": 39.6300, "desc": "Early Methodist station established by Thomas Wakefield."},
        {"name": "Mazeras Mission", "lat": -3.9600, "lng": 39.5500, "desc": "Key Methodist gateway to the Duruma communities."},
        {"name": "Ribe Methodist Mission", "lat": -3.8980, "lng": 39.6000, "desc": "Est. 1862. A sanctuary for refugees."},
        {"name": "Vasco da Gama Pillar (Malindi)", "lat": -3.2236, "lng": 40.1296, "desc": "Built 1498. Earliest European Christian symbol on the coast."},
        {"name": "The Portuguese Chapel (Malindi)", "lat": -3.2213, "lng": 40.1261, "desc": "c. 1502. Oldest Christian place of worship in East Africa."},
        {"name": "Gede Ruins", "lat": -3.3070, "lng": 40.0190, "desc": "Ancient ruins suggesting trade links with Christian empires."},
        {"name": "St. Thomas Church (Kilifi)", "lat": -3.6300, "lng": 39.8500, "desc": "Historic Anglican church serving Kilifi creek."},
        {"name": "Mnarani Ruins", "lat": -3.6350, "lng": 39.8450, "desc": "Ancient Swahili settlement ruins."},
        {"name": "Takaungu Slave Port", "lat": -3.6800, "lng": 39.8600, "desc": "Major slave exit point; later focus for abolitionists."},
        {"name": "Kijipwa Mission", "lat": -3.8500, "lng": 39.7500, "desc": "Early pentecostal mission station."},
        {"name": "Kaloleni Giriama Mission", "lat": -3.8000, "lng": 39.6000, "desc": "St. John's Church center for evangelism."},
        {"name": "Jimba Mission", "lat": -3.8800, "lng": 39.5800, "desc": "CMS substation near Rabai."},
        {"name": "Bura Mission (Taita)", "lat": -3.5000, "lng": 38.3000, "desc": "First Catholic mission in Taita."},
        {"name": "Faza Ruins (Pate Island)", "lat": -2.0500, "lng": 41.0500, "desc": "Remnants of Portuguese influence."},
        {"name": "Lamu Portuguese Fort", "lat": -2.2700, "lng": 40.9000, "desc": "Site of struggle between Omani and Portuguese."},
        {"name": "Manda Island Ruins", "lat": -2.2800, "lng": 40.9200, "desc": "Ancient trading port."},
        {"name": "Takwa Ruins", "lat": -2.2900, "lng": 40.9500, "desc": "Holy site visited by interfaith scholars."},
        {"name": "Shanga Ruins", "lat": -2.1000, "lng": 41.0000, "desc": "Early settlement showing diverse artifacts."},
        {"name": "Shimoni Slave Caves", "lat": -4.6480, "lng": 39.3800, "desc": "Reclaimed by Christian abolitionists."},
        {"name": "Vanga Mission", "lat": -4.6600, "lng": 39.2200, "desc": "Southernmost outpost of early missions."},
        {"name": "Tiwi Anglican Church", "lat": -4.2300, "lng": 39.5800, "desc": "Old coral-built church."},
        {"name": "Diani Persian Mosque Ruins", "lat": -4.3000, "lng": 39.5700, "desc": "Evidence of pre-European monotheism."},
        {"name": "Gazi Ruins", "lat": -4.4200, "lng": 39.5000, "desc": "Former stronghold of the Mazrui."},
        {"name": "Sagalla (St. Mark's)", "lat": -3.4000, "lng": 38.5800, "desc": "Tin-roofed church built 1890s."},
        {"name": "Wray's Church (Sagalla)", "lat": -3.4100, "lng": 38.5850, "desc": "Named after J.A. Wray."},
        {"name": "Taveta Mahoo Mission", "lat": -3.4000, "lng": 37.6800, "desc": "Gateway to Kilimanjaro."},
        {"name": "Voi Railway Mission", "lat": -3.3900, "lng": 38.5500, "desc": "Chapel for railway workers."},
        {"name": "Mbale Mission", "lat": -3.4500, "lng": 38.4000, "desc": "Key Anglican center in Taita."},
        {"name": "Kaya Kauma", "lat": -3.6000, "lng": 39.7000, "desc": "Traditional sacred site."},
        {"name": "Kaya Fungo", "lat": -3.7000, "lng": 39.6000, "desc": "Historical spiritual leadership site."},
        {"name": "Gotani Mission", "lat": -3.7500, "lng": 39.5500, "desc": "Inland mission post."},
        {"name": "Mariakani Church", "lat": -3.8500, "lng": 39.4700, "desc": "Historic outpost."},
        {"name": "Mazeras Railway Church", "lat": -3.9650, "lng": 39.5400, "desc": "Serving railway builders."},
        {"name": "Changamwe Mission", "lat": -4.0300, "lng": 39.6200, "desc": "Early Methodist stronghold."},
        {"name": "Kisauni Bell Tower", "lat": -4.0450, "lng": 39.6800, "desc": "Remnant of Freed Slave settlement."},
        {"name": "Nyali Bridge Crossing", "lat": -4.0500, "lng": 39.6600, "desc": "Early ferry crossing site."},
        {"name": "Likoni Ferry Mission", "lat": -4.0800, "lng": 39.6600, "desc": "Southern gateway mission."},
        {"name": "Waa Mission School", "lat": -4.1500, "lng": 39.6000, "desc": "Early education center."},
        {"name": "Msambweni Hospital Chapel", "lat": -4.4700, "lng": 39.4800, "desc": "Historic medical mission."},
        {"name": "Lunga Lunga Border Post", "lat": -4.5500, "lng": 39.1200, "desc": "Entry point from Tanzania."},
        {"name": "Shimba Hills Settlement", "lat": -4.1800, "lng": 39.4000, "desc": "Agricultural mission."},
        {"name": "Kwale Seminary", "lat": -4.1700, "lng": 39.4500, "desc": "Training center."},
        {"name": "Kinango Mission", "lat": -4.1300, "lng": 39.2500, "desc": "Deep inland mission."}
    ]

    for site in sites:
        SpiritualSite.objects.update_or_create(
            name=site['name'],
            defaults={'description': site['desc'], 'latitude': site['lat'], 'longitude': site['lng']}
        )
    print("   ✅ 50 Sites Imported.")


    # =========================================================
    # PART 2: 30 SCRIPTURE COMPARISONS
    # =========================================================
    print("📜 Generating 30 Scripture Comparisons...")
    
    scriptures = [
        ("1 Enoch", 1, 9, "Not included.", "And behold! He cometh with ten thousands of His holy ones...", "Quoted in Jude 1:14."),
        ("1 Enoch", 6, 1, "Not included.", "And it came to pass when the children of men had multiplied...", "Details the Watchers."),
        ("1 Enoch", 10, 4, "Not included.", "Bind Azazel hand and foot...", "Context for Scapegoat."),
        ("1 Enoch", 42, 1, "Not included.", "Wisdom found no place where she might dwell...", "Personification of Wisdom."),
        ("1 Enoch", 46, 1, "Not included.", "And there I saw One who had a head of days...", "Vision of the Son of Man."),
        ("Jubilees", 2, 1, "Genesis 1:1", "And the angel of the presence spake to Moses...", "Moses receives creation story."),
        ("Jubilees", 3, 17, "Genesis 3", "And after the completion of the seven years...", "Adam in Eden for 7 years."),
        ("Jubilees", 4, 30, "Gen 5:24", "And he was six jubilees of years...", "Enoch's translation."),
        ("1 Maccabees", 1, 1, "Not included.", "And it happened, after that Alexander son of Philip...", "Intertestamental history."),
        ("1 Maccabees", 2, 50, "Not included.", "Be ye zealous for the law...", "Call to martyrdom."),
        ("2 Maccabees", 7, 1, "Not included.", "Seven brethren with their mother...", "Holy Martyrs."),
        ("2 Maccabees", 12, 46, "Not included.", "It is therefore a holy and wholesome thought to pray for the dead...", "Prayers for departed."),
        ("Wisdom", 1, 1, "Not included.", "Love righteousness, ye that be judges...", "Address to rulers."),
        ("Wisdom", 2, 24, "Not included.", "Nevertheless through envy of the devil came death...", "Serpent identified as Devil."),
        ("Wisdom", 3, 1, "Not included.", "But the souls of the righteous are in the hand of God...", "Afterlife."),
        ("Wisdom", 7, 26, "Not included.", "For she is the brightness of the everlasting light...", "Christological wisdom."),
        ("Sirach", 1, 1, "Not included.", "All wisdom cometh from the Lord...", "Source of Wisdom."),
        ("Sirach", 2, 1, "Not included.", "My son, if thou come to serve the Lord...", "Service advice."),
        ("Sirach", 6, 14, "Not included.", "A faithful friend is a strong defence...", "Friendship."),
        ("Sirach", 11, 2, "Not included.", "Commend not a man for his beauty...", "Appearance vs Heart."),
        ("Sirach", 25, 1, "Not included.", "In three things I was beautified...", "The three beauties."),
        ("Sirach", 38, 1, "Not included.", "Honour a physician with the honour due unto him...", "Medicine."),
        ("Tobit", 4, 15, "Not included.", "Do that to no man which thou hatest...", "Golden Rule."),
        ("Tobit", 12, 15, "Not included.", "I am Raphael, one of the seven holy angels...", "Angelology."),
        ("Judith", 13, 14, "Not included.", "Praise God, for he hath not taken away his mercy...", "Song of victory."),
        ("Baruch", 3, 37, "Not included.", "Afterward did he shew himself upon earth...", "Incarnation prophecy."),
        ("Psalm 151", 151, 1, "Not included.", "I was small among my brethren...", "David's autobiography."),
        ("Pr. of Manasseh", 1, 1, "Not included.", "O Lord, Almighty God of our fathers...", "Prayer of Repentance."),
        ("Bel & Dragon", 1, 3, "Not included.", "Now the Babylonians had an idol...", "Idolatry."),
        ("Susanna", 1, 2, "Not included.", "And he took a wife, whose name was Susanna...", "Story of virtue."),
    ]

    for b, c, v, kjv, eth, note in scriptures:
        ScriptureComparison.objects.update_or_create(
            book_title=b, chapter=c, verse=v,
            defaults={'kjv_text': kjv, 'ethiopian_text': eth, 'analysis': note}
        )
    print("   ✅ 30 Texts Imported.")


    # =========================================================
    # PART 3: 25 BLOG POSTS (Fixed Lookup)
    # =========================================================
    print("📝 Generating 25 Blog Posts...")
    
    # FIX: Find the HomePage intelligently (don't rely on slug='home')
    home = HomePage.objects.first()
    
    if not home:
        # Fallback: Find the default wagtail root page if user deleted their homepage
        print("   ⚠️ Custom HomePage not found. Trying default Page...")
        home = Page.objects.filter(depth=2).first()
        
    if not home:
        print("   ❌ ERROR: No Parent Page found to attach blog to. Aborting blog import.")
        return

    # Try to find or create the blog index
    # We check children of 'home' to see if 'BlogIndexPage' exists
    blog_index = BlogIndexPage.objects.descendant_of(home).first()
    
    if not blog_index:
        print("   Creating new Blog Index Page...")
        blog_index = BlogIndexPage(title="Ministry Updates", slug="blog", intro="News from the Coast.")
        home.add_child(instance=blog_index)
        blog_index.save_revision().publish()

    posts = [
        ("The Arrival of Krapf", "1844 marked the arrival of Ludwig Krapf in Mombasa."),
        ("Why We Map the Coast", "Our map is a spiritual cartography of faith."),
        ("The Mystery of Enoch", "Why was the Book of Enoch removed from the Western Canon?"),
        ("Restoring Rabai Mpya", "Updates on the preservation efforts."),
        ("The Portuguese Chapel", "A look at the graves of the two seafarers."),
        ("Swahili Bible History", "How the 'Mombasa Dialect' became the first vehicle for the Gospel."),
        ("Understanding Ge'ez", "The liturgical language of Ethiopia."),
        ("The Gnostic Question", "Separating heresy from history."),
        ("Saint Mark in Africa", "Tracing the tradition of St. Mark."),
        ("The Ark of the Covenant", "Ethiopian traditions regarding the Ark."),
        ("Missionary Medicine", "How early hospitals opened doors."),
        ("The Lunatic Express", "How the railway built the church."),
        ("Freed Slave Settlements", "The history of Frere Town."),
        ("Methodism on the Coast", "The legacy of Thomas Wakefield."),
        ("Catholic Return", "The Holy Ghost Fathers' return to Mombasa."),
        ("Islam and Christianity", "Centuries of coexistence."),
        ("The Mijikenda Encounter", "Interactions with the nine tribes."),
        ("Visualizing Faith", "Why we use Dhow boats in our design."),
        ("Digital Archiving", "Digitizing ancient manuscripts."),
        ("Weekly Prayer Focus", "Praying for coastal pastors."),
        ("Site Visit: Lamu", "Our team's recent trip."),
        ("New Features Live", "Announcing the Textual Comparison Engine."),
        ("Support the Work", "How you can help."),
        ("Upcoming Documentary", "Teaser for our video series."),
        ("A Vision for 2026", "Where Independent Ministers is heading.")
    ]

    base_date = datetime.date.today()
    
    for i, (title, intro) in enumerate(posts):
        if not BlogPage.objects.filter(title=title).exists():
            post_date = base_date - datetime.timedelta(days=i*3)
            new_post = BlogPage(
                title=title,
                date=post_date,
                intro=intro,
                body=f"<p>This is the full article content for <b>{title}</b>. {intro} It explores the deep history of faith along the Kenyan coast.</p>"
            )
            blog_index.add_child(instance=new_post)
            new_post.save_revision().publish()
    
    print("   ✅ 25 Blog Posts Imported.")


    # =========================================================
    # PART 4: 25 WEEKLY VIDEOS
    # =========================================================
    print("🎥 Generating 25 Weekly Videos...")
    
    safe_ids = ["LXb3EKWsInQ", "M7FIvfx5J10", "ScMzIvxBSi4", "9WCPqCjWlXQ", "J32j4N8Nf_c"]
    
    for i in range(1, 26):
        vid_id = safe_ids[i % len(safe_ids)]
        WeeklyVideo.objects.update_or_create(
            title=f"Weekly Update #{i}",
            defaults={
                'video_url': f"https://www.youtube.com/watch?v={vid_id}",
                'is_active': (i == 1)
            }
        )
    print("   ✅ 25 Videos Imported.")

    print("\n🎉 SUCCESS: DATABASE FULLY POPULATED!")

if __name__ == '__main__':
    import_production_data()