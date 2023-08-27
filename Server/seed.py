from app import app
import datetime
from models import User, Listing, Location, Property, RentalTerms,  Review, UserFavoriteProperty,Payment, FeaturedListing, NewestListing, PropertyInquiry, db

# Function to seed the database with sample data
def seed_data():
    # Clear the existing data from all tables
    User.query.delete()
    Listing.query.delete()
    FeaturedListing.query.delete()
    Location.query.delete()
    NewestListing.query.delete()
    Property.query.delete()
    RentalTerms.query.delete()
    Review.query.delete()
    UserFavoriteProperty.query.delete()
    Payment.query.delete()
    PropertyInquiry.query.delete()


    user1 = User(username='braxton', email='braxton@example.com', hashed_password='123456', role='tenant')
    user2 = User(username='shaffie', email='shaffie@example.com', hashed_password='123456', role='owner')
    

    db.session.add_all([user1, user2])
    db.session.commit()

    # Seed data for locations
    location1 = Location(city='mombasa', neighborhood='Neighborhood A', specific_area='Area A', latitude='0.000', longitude='0.000')
    location2 = Location(city='', neighborhood='Neighborhood B', specific_area='Area B', latitude='0.000', longitude='0.000')

    db.session.add_all([location1, location2])
    db.session.commit()
    
    # Seed data for listings
    inquiries_data = [
        {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123-456-7890',
            'address': '123 Main St, City',
            'message': 'I am interested in this property. Please provide more details.',
            'property_id': 1
        },
        {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'phone': '987-654-3210',
            'address': '456 Elm St, Town',
            'message': 'Can you tell me about the utilities included?',
            'property_id': 2
        },
        
    ]

    for inquiry_data in inquiries_data:
        inquiry = PropertyInquiry(**inquiry_data)
        db.session.add(inquiry)

    db.session.commit()

    
     # Seed data for listings
    listing_data = [
        {
            'id': 1,
            'location_id': 1,
            'title': 'Spacious Downtown Office Suite',
            'description': 'A modern and spacious office suite located in the heart of downtown. It features large windows for ample natural light, a reception area, three private offices, a conference room, and a break area. Perfect for a growing business.',
            'rent': '3,400/month',
            'place': '4404 Brian Plains, Port Marie, Lamu',
            'size': '1000 sqft',
            'utilities': 'High-speed WiFi, parking space, security (CCTV)',
            'media': 'https://cdn.pixabay.com/photo/2013/09/14/19/53/city-182223_640.jpg'
        },
        {
            'id': 2,
            'location_id': 2,
            'title': 'Cozy Studio Apartment near the Park',
            'description': 'This charming studio apartment is just a short walk from the local park. It offers an open floor plan with a fully equipped kitchen, a comfortable living area, and a separate sleeping area. Ideal for a single professional or student.',
            'rent': '3,000/month',
            'place': '456 Elm Avenue, Kisumu',
            'size': '500 sqft',
            'utilities': 'High-speed WiFi, parking space, security (CCTV)',
            'media': 'https://cdn.pixabay.com/photo/2019/03/08/20/14/kitchen-living-room-4043091_640.jpg'
        },
         {
        'id': 3,
        'title': 'Prime Retail Space on Main Street',
        'location_id': 3,
        'description': 'An excellent opportunity to lease a prime retail space on Main Street. The property features a spacious layout, large display windows, and high foot traffic. Ideal for a boutique, cafe, or specialty shop.',
        'rent': '5,200/month',
        'place': '789 Main Street, Downtown, Eldoret',
        'size': '1500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2015/08/25/11/50/shopping-mall-906721_640.jpg',
        'utilities': 'WiFi, parking space'
        },
        {
        'id': 4,
        'title': 'Luxury Penthouse with Stunning Views',
        'location_id': 4,
        'description': 'Experience luxury living in this exquisite penthouse apartment boasting breathtaking views of the city skyline. It offers high-end finishes, a gourmet kitchen, a private terrace, and access to exclusive amenities such as a fitness center and pool.',
        'rent': '$8,500/month',
        'place': '10 Highrise Avenue, Skyview Heights, Nakuru',
        'size': '2,800 square feet',
        'media': 'https://cdn.pixabay.com/photo/2014/06/21/20/16/real-estate-374107_1280.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
         },
    {
        'id': 5,
        'title': 'Industrial Warehouse with Loading Dock',
        'location_id': 1,
        'description': 'This spacious industrial warehouse is equipped with a loading dock, high ceilings, and ample storage space. It\'s perfect for businesses requiring logistics support or additional inventory space.',
        'rent': '$4,000/month',
        'place': '111 Warehouse Lane, CBD, Nairobi',
        'size': '5,000 sqft',
        'media': 'https://cdn.pixabay.com/photo/2018/12/09/17/57/hall-3865370_1280.jpg',
        'utilities': 'Parking space, security (guardmen), back-up power'
    },
    {
        'id': 6,
        'title': 'Stylish 2-Bedroom Apartment',
        'location_id': 5,
        'description': 'Embrace the vibrant city life in this stylish 2-bedroom apartment situated in a trendy neighborhood. It features a modern kitchen, spacious living area, and access to nearby restaurants, shops, and entertainment options.',
        'rent': '1,000/month',
        'place': '222 Oak Street, Trendyville, Nairobi',
        'size': '900 square feet',
        'media': 'https://cdn.pixabay.com/photo/2014/07/31/21/41/apartment-406901_640.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 7,
        'title': 'Commercial Office Space with Flexible Layout',
        'location_id': 3,
        'description': 'This versatile commercial office space offers a flexible layout that can be customized to suit your business needs. It includes private offices, open work areas, a conference room, and a reception area. Conveniently located near major highways.',
        'rent': '4,500/month',
        'place': '333 Eastleigh, Nairobi',
        'size': '3500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2015/11/15/20/49/modern-office-1044807_1280.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 8,
        'title': 'Quaint Cottage with Private Garden',
        'location_id': 2,
        'description': 'Escape to this charming cottage nestled in a serene neighborhood. It boasts a private garden, a cozy living area, a fully equipped kitchen, and two comfortable bedrooms. A perfect retreat for nature lovers.',
        'rent': '1,800/month',
        'place': '252 Mark Plains, Umoja, Nairobi',
        'size': '1200 sqft',
        'media': 'https://cdn.pixabay.com/photo/2016/08/15/00/45/log-cabin-1594361_1280.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
    },
    {
        'id': 9,
        'title': 'Retail Space in Busy Shopping Plaza',
        'location_id': 2,
        'description': 'Take advantage of this prime retail space located in a bustling shopping plaza. With high visibility and a steady flow of customers, it presents an excellent opportunity for your business to thrive.',
        'rent': '3,800/month',
        'place': '555 Plaza Avenue, Kinoo, Nairobi',
        'size': '1000 sqft',
        'media': 'https://cdn.pixabay.com/photo/2018/10/15/14/58/cape-town-3749167_1280.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 10,
        'title': 'Modern Office Suite with River View',
        'location_id': 1,
        'description': 'Enjoy panoramic river views from this modern office suite. It offers a professional environment with a reception area, private offices, a conference room, and a break area. Conveniently located near downtown amenities.',
        'rent': '3,800/month',
        'place': '666 Riverside Drive, Kisii',
        'size': '1500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2016/10/16/10/30/office-space-1744803_640.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
    }
      
    ]

    for listing in listing_data:
        new_listing = Listing(
            id=listing['id'],
            location_id=listing['location_id'],
            title=listing['title'],
            description=listing['description'],
            rent=listing['rent'],
            place=listing['place'],
            size=listing['size'],
            utilities=listing['utilities'],
            media=listing['media']
        )
        db.session.add(new_listing)

    db.session.commit()

    # Seed data for the Featured Listings
    featured_listings = [
        {
            'title': 'Chic Urban Townhouse',
            'description': 'Contemporary townhouse in the heart of the city. Modern design and convenient access to shops and restaurants.',
            'rent': '$2500.00',
            'place': '1357 Urban Street, Metropolis, Nairobi',
            'size': '1000 sqft',
            'utilities': 'Water and trash included',
            'media': 'https://cdn.pixabay.com/photo/2020/08/29/10/24/home-5526694_640.jpg'
        },
        {
            'title': 'Lakefront Cottage',
            'description': 'Quaint cottage situated on the shores of a serene lake. Ideal for a peaceful retreat.',
            'rent': '$1600.00',
            'place': '2468 Lakeside Lane, Tranquil Waters, Kisumu',
            'size': '600 sqft',
            'utilities': 'Tenant responsible for all utilities',
            'media': 'https://cdn.pixabay.com/photo/2021/10/03/03/48/living-room-6676758_640.jpg'
        
        },
        {
            'title': 'Luxury Urban Penthouse',
            'description': 'High-end penthouse offering breathtaking city skyline views. Modern amenities and sleek design.',
            'rent': '$4500.00',
            'place': '7890 Skyline Avenue, Kongowea, Kilifi',
            'size': '1500 sqft',
            'utilities': 'Included (except electricity)',
            'media': 'https://cdn.pixabay.com/photo/2017/12/10/03/18/beautiful-3009151_640.jpg'
        },
        {
            'title': 'Rustic Mountain Retreat',
            'description': 'Rustic cabin retreat in the mountains. Perfect for those seeking a peaceful escape from city life.',
            'rent': '$1200.00',
            'place': '6543 Mountain Trail, Bamburi, Mombasa',
            'size': '500 sqft',
            'utilities': 'Propane heating included',
            'media': 'https://cdn.pixabay.com/photo/2017/03/13/20/19/architecture-2141045_640.jpg'
        },
        {
            'title': 'Secluded Forest Cabin',
            'description': 'Charming cabin tucked away in a secluded forest. Privacy and tranquility guaranteed.',
            'rent': '1400.00',
            'place': '8765 Forest Lane, Mtwapa, Mombasa',
            'size': '550 sqft',
            'utilities': 'Tenant responsible for all utilities',
            'media': 'https://cdn.pixabay.com/photo/2017/10/01/00/49/architecture-2804069_640.jpg'
        },
        {
            "description": "Luxury penthouse with stunning city views. High-end finishes, private terrace, and access to exclusive amenities.",
            "media": "https://cdn.pixabay.com/photo/2016/09/16/21/38/kitchen-1675190_1280.jpg",
            "place": "123 Highrise Avenue, Skyline Heights, Nairobi",
            "rent": "7500.00",
            "size": "2000 sqft",
            "title": "Stunning City View Penthouse",
            "utilities": "WiFi, parking space, security (CCTV)"
        },
        {
            "description": "Modern studio apartment in the heart of downtown. Efficient layout and close to shops and entertainment.",
            "media": "https://cdn.pixabay.com/photo/2016/10/16/10/30/office-space-1744803_640.jpg",
            "place": "456 Main Street, Kabete, Nairobi",
            "rent": "$2200.00",
            "size": "500 sqft",
            "title": "Downtown Studio Apartment",
            "utilities": "Water and trash included"
        },
        {
            "description": "Charming cottage with a cozy fireplace. Perfect for a peaceful winter retreat.",
            "media": "https://cdn.pixabay.com/photo/2017/03/21/17/38/kitchen-2165756_640.jpg",
            "place": "789 Hearth Lane, Murogo, Naivasha",
            "rent": "$1900.00",
            "size": "700 sqft",
            "title": "Winter Cottage Getaway",
            "utilities": "Tenant responsible for all utilities"
        },
        {
            "description": "Spacious office suite with flexible layout. Ideal for a growing business.",
            "media": "https://cdn.pixabay.com/photo/2017/06/28/21/32/the-interior-of-the-2452233_640.jpg",
            "place": "333 Business Boulevard, Commercial Center, Nakuru",
            "rent": "4000.00",
            "size": "1500 sqft",
            "title": "Flexible Office Suite",
            "utilities": "WiFi, parking space"
        },
        {
            "description": "Cozy one-bedroom apartment with balcony. Enjoy beautiful sunset views over the city.",
            "media": "https://cdn.pixabay.com/photo/2016/09/04/12/38/living-room-1643855_640.jpg",
            "place": "555 Sunset Lane, Parklands, Nairobi",
            "rent": "1700.00",
            "size": "600 sqft",
            "title": "Sunset View Apartment",
            "utilities": "Water and trash included"
        },
        {
            "description": "Modern townhouse with open-concept living. Close to parks and recreational areas.",
            "media": "https://cdn.pixabay.com/photo/2012/11/19/16/26/house-66627_640.jpg",
            "place": "987 Parkside Street, M0shi, Meru",
            "rent": "$2800.00",
            "size": "1800 sqft",
            "title": "Contemporary Townhouse",
            "utilities": "Tenant responsible for all utilities"
        },
        {
            "description": "Charming historic home with original features. Located in a peaceful neighborhood.",
            "media": "https://cdn.pixabay.com/photo/2013/09/24/12/06/apartment-185778_640.jpg",
            "place": "789 Heritage Lane, Lenana, Kajiado",
            "rent": "$2400.00",
            "size": "1600 sqft",
            "title": "Historic Charm Home",
            "utilities": "WiFi, parking space"
        },
        {
            "description": "Spacious warehouse with loading dock. Ideal for businesses requiring storage and logistics support.",
            "media": "https://cdn.pixabay.com/photo/2014/08/11/21/35/room-416049_640.jpg",
            "place": "111 Commerce Lane, Rongai, Nairobi",
            "rent": "4200.00",
            "size": "5000 sqft",
            "title": "Industrial Warehouse",
            "utilities": "Parking space, security (guardmen), back-up power"
        },
        {
            "description": "Urban loft living with exposed brick walls. Enjoy the trendy city lifestyle.",
            "media": "https://cdn.pixabay.com/photo/2018/05/02/09/02/baby-boy-3368017_640.jpg",
            "place": "432 Loft Street, Uptown, Nairobi",
            "rent": "2600.00",
            "size": "900 sqft",
            "title": "Urban Loft Living",
            "utilities": "Water included"
        },
        {
            "description": "Seaside cottage with direct beach access. Perfect for a relaxing coastal escape.",
            "media": "https://cdn.pixabay.com/photo/2014/08/11/21/41/design-416064_640.jpg",
            "place": "543 Beachfront Road, Shoreline Cove, Kisumu",
            "rent": "3800.00",
            "size": "1200 sqft",
            "title": "Seaside Cottage",
            "utilities": "Water included"
        }
        ]


    # Add seed data to the database
    for listing_data in featured_listings:
        new_listing = FeaturedListing(
            title=listing_data['title'],
            description=listing_data['description'],
            rent=listing_data['rent'],
            place=listing_data['place'],
            size=listing_data['size'],
            utilities=listing_data['utilities'],
            media=listing_data['media']
        )
        db.session.add(new_listing)

    # Commit the changes to the database
    db.session.commit()
    
        # Seed data for the Newest Listings
    newest_listings = [
        {
            'title': 'Historic Downtown Loft',
            'description': 'Elegant loft apartment located in a historic downtown building. Exposed brick walls and original hardwood floors.',
            'rent': '2200.00',
            'place': '1234 Elm Street, Vintage City, Nairobi',
            'size': '800 sqft',
            'utilities': 'Tenant responsible for all utilities',
            'media': 'https://cdn.pixabay.com/photo/2017/12/10/03/18/balcony-3009152_640.jpg'
        },
        {
            'title': 'Mountain View Chalet',
            'description': 'Cozy chalet nestled in the mountains with stunning panoramic views. Perfect for outdoor enthusiasts.',
            'rent': '1800.00',
            'place': '5678 Summit Road, Alpine Haven, Kikuyu',
            'size': '700 sqft',
            'utilities': 'Electricity and heating included',
            'media': 'https://cdn.pixabay.com/photo/2015/11/06/11/48/multi-family-home-1026488_640.jpg'
        },
        {
            'title': 'Luxury Penthouse Suite',
            'description': 'Exquisite penthouse offering breathtaking city views. High-end amenities and spacious layout make this an ideal urban oasis.',
            'rent': '1800.00',
            'place': '5678 Maple Lane, Townsville, Thika',
            'size': '650 sqft',
            'utilities': 'Tenant responsible for all utilities',
            'media': 'https://cdn.pixabay.com/photo/2015/11/07/21/29/livingroom-1032733_640.jpg'
        },
        {
            'title': 'Lakeside Retreat Cabin',
            'description': 'Rustic cabin located by a serene lake. Ideal for nature enthusiasts seeking a peaceful getaway.',
            'rent': '$1500.00',
            'place': '2468 Lakeview Drive, Wilderness, Mombasa',
            'size': '500 sqft',
            'utilities': 'Propane heating and electricity included',
            'media': 'https://cdn.pixabay.com/photo/2018/07/27/00/32/interior-design-3564955_640.jpg'
        },
        {
            'title': 'Modern Studio Apartment',
            'description': 'Stylish studio apartment in a vibrant urban neighborhood. Efficient layout and contemporary design.',
            'rent': '2000.00',
            'place': '1357 Main Street, Metrotown, Kisii',
            'size': '400 sqft',
            'utilities': 'Water and trash included',
            'media': 'https://cdn.pixabay.com/photo/2017/12/06/11/55/interior-3001598_640.jpg'
        },
        {
            'title': 'Spacious Family Home',
            'description': 'Large family home with multiple bedrooms and ample living space. Fenced backyard and proximity to schools.',
            'rent': '3200.00',
            'place': '7890 Oak Avenue, Homestead, Kapsabet',
            'size': '2200 sqft',
            'utilities': 'Tenant responsible for all utilities',
            'media': 'https://cdn.pixabay.com/photo/2015/05/05/01/10/house-753270_640.jpg'
        },
        {
            'title': 'Quaint Countryside Bungalow',
            'description': 'Charming bungalow set in a peaceful countryside setting. Perfect for those seeking a quiet and picturesque home.',
            'rent': '1700.00',
            'place': '6543 Meadow Lane, Serenity Hills, Kisumu',
            'size': '750 sqft',
            'utilities': 'Tenant responsible for all utilities',
            'media': 'https://cdn.pixabay.com/photo/2015/09/08/22/03/luggage-930804_640.jpg'
        },
        {
            'title': 'Modern High-Rise Condo',
            'description': 'Sleek and modern condo in a high-rise building. Panoramic city views and access to top-notch amenities.',
            'rent': '3800.00',
            'place': '8765 Skyscraper Avenue, Nairobi, NR 56789',
            'size': '1200 sqft',
            'utilities': 'Included (except electricity)',
            'media': 'https://cdn.pixabay.com/photo/2016/06/05/22/13/home-1438305_640.jpg'
        },
        {
            'title': 'Coastal Beach House',
            'description': 'Beachfront property with direct access to the ocean. Perfect for those who love the sun, sand, and sea.',
            'rent': '4500.00',
            'place': '5432 Shoreline Drive, Kisumu, CA 34567',
            'size': '1500 sqft',
            'utilities': 'Water included',
            'media': 'https://cdn.pixabay.com/photo/2020/06/27/16/40/apartment-5346460_640.jpg'
        },
    ]

    # Add seed data to the database
    for listing_data in newest_listings:
        new_listing = NewestListing(
            title=listing_data['title'],
            description=listing_data['description'],
            rent=listing_data['rent'],
            place=listing_data['place'],
            size=listing_data['size'],
            utilities=listing_data['utilities'],
            media=listing_data['media']
        )
        db.session.add(new_listing)

    # Commit the changes to the database
    db.session.commit()

    # Seed data for properties
    property1 = Property(
        property_type='Villa',
        property_category='Residential',
        property_title= 'A luxurious villa featuring 4 bedrooms, & 4 bathrooms',
        property_rent = 45600,
        bedrooms=4,
        bathrooms=4,
        amenities='Parking, Laundry Facilities, Air Conditioning, Security Systems, Swimming Pools',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2017/04/10/22/28/residence-2219972_640.jpg',
        images='https://cdn.pixabay.com/photo/2013/10/12/18/05/villa-194671_640.jpg, https://cdn.pixabay.com/photo/2020/04/17/12/28/pool-5055009_640.jpg, https://cdn.pixabay.com/photo/2015/11/06/11/45/interior-1026446_640.jpg, https://cdn.pixabay.com/photo/2016/10/13/09/06/travel-1737168_640.jpg, https://cdn.pixabay.com/photo/2015/11/06/11/45/interior-1026454_640.jpg, https://cdn.pixabay.com/photo/2016/10/13/09/08/travel-1737171_640.jpg, https://cdn.pixabay.com/photo/2020/03/21/20/04/real-estate-4955093_640.jpg, https://cdn.pixabay.com/photo/2017/03/30/00/24/villa-2186906_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/052/461/original/alb_kaleido1007_1080p_24fps.mp4',
        property_documents=None,
        furnished='Yes',
        description='This is a luxurious villa available for rent in Kilimani, Nairobi, Kenya, at Kshs 45,600 per month. It features 4 bedrooms, 4 bathrooms, and amenities like parking, laundry facilities, air conditioning, security systems, and swimming pools. Close to schools and parks, it offers convenience for families. The owner, Jane Ngugi, can be contacted at +61 2 9876 5432 (WhatsApp too) or janengugi@gmail.com. The fully furnished villa includes a captivating house tour video. However, please note that pets are not allowed. With a beautiful garden and modern interior, this villa offers a luxurious and inviting home for residents.',
        location_details='Close to schools and parks.',
        location_id = 2,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Kilimani',
        address='456 Maple Ave, Kilimani, Nairobi',
        user_id = 2,
        property_owner_name='Jane Ngugi',
        property_owner_photo='https://cdn.pixabay.com/photo/2020/08/21/08/46/african-5505598_640.jpg',
        contact_phone='0798765432',
        contact_whatsapp='0798765432',
        contact_email='janengugi@gmail.com',
        facebook='facebook.com/maria.silva',
        twitter=None,
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='whatsapp',
        additional_details='The property management does not allow pets',
    )
    property2 = Property(
        property_type='Apartment',
        property_category='Residential',
        property_title= 'A modern apartment available for rent in Nairobi, Kenya. This residential gem offers two bedrooms, & one bathroom',
        property_rent = 30000,
        bedrooms=2,
        bathrooms=1,
        amenities='Parking, Elevator, Balcony, Gym',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2016/11/18/17/20/living-room-1835923_640.jpg',
        images= 'https://cdn.pixabay.com/photo/2017/12/27/14/41/window-3042834_640.jpg, https://cdn.pixabay.com/photo/2018/01/29/07/55/modern-minimalist-bathroom-3115450_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/19/apartment-2094666_640.jpg, https://cdn.pixabay.com/photo/2014/08/11/21/31/wall-panel-416041_640.jpg, https://cdn.pixabay.com/photo/2015/11/07/21/29/livingroom-1032733_640.jpg, https://cdn.pixabay.com/photo/2017/12/27/14/42/furniture-3042835_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/002/004/original/20140614-SoudertonPA-YellowFlowersBreeze.mp4',
        property_documents=None,
        furnished='No',
        description='This is a modern apartment available for rent in Nairobi, Kenya, at Kshs 30,000 per month. This residential gem offers two bedrooms, one bathroom, and comes with convenient amenities such as parking, an elevator, balcony, and gym. The main image displays a stylish living room, capturing the apartment contemporary ambiance. Located in the bustling Midtown area, the apartment is within walking distance to shopping and public transport, ensuring easy accessibility. The owner, Alex Johnson, can be contacted at +1 123-456-7890 or WhatsApp at +1 417-123-4567. For inquiries, reach out via email at alex@example.com. Social media enthusiasts can connect with Alex on Facebook, Twitter, and Instagram. The property features a captivating house tour video showcasing the apartments stunning view and desirable location. Pets are allowed with a deposit, making it a pet-friendly choice for tenants. With its modern design and convenient location, this apartment promises an exceptional living experience for those seeking contemporary city living.',
        location_details='Walking distance to shopping and public transport.',
        location_id = 1,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Midtown',
        address='789 Park Ave, Midtown, Nairobi',
        user_id = 1,
        property_owner_name='Alex Johnson',
        property_owner_photo='https://cdn.pixabay.com/photo/2022/01/23/23/43/couple-6962202_640.jpg',
        contact_phone='0723417890',
        contact_whatsapp='0717123567',
        contact_email='alex@example.com',
        facebook='facebook.com/alex.johnson',
        twitter='twitter.com/alex_johnson',
        instagram='instagram.com/alex.johnson',
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='email',
        additional_details='Pets allowed with deposit.',
    )
    property3 = Property(
        property_type='House',
        property_category='Residential',
        property_title= 'A spacious family home for rent',
        property_rent = 150600,
        bedrooms=4,
        bathrooms=3.5,
        amenities='Garage, Garden, Fireplace',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2014/07/31/00/30/vw-beetle-405876_640.jpg',
        images='https://cdn.pixabay.com/photo/2017/07/09/03/19/home-2486092_640.jpg, https://cdn.pixabay.com/photo/2016/08/26/15/06/home-1622401_640.jpg, https://cdn.pixabay.com/photo/2014/07/10/17/17/bedroom-389254_640.jpg, https://cdn.pixabay.com/photo/2016/01/31/14/32/architecture-1171462_640.jpg, https://cdn.pixabay.com/photo/2017/03/28/12/10/chairs-2181947_640.jpg, https://cdn.pixabay.com/photo/2017/08/02/01/01/living-room-2569325_640.jpg, https://cdn.pixabay.com/photo/2015/10/20/18/57/furniture-998265_640.jpg',
        house_tour_video= 'https://static.videezy.com/system/resources/previews/000/053/090/original/alb_kaleido1068_1080p.mp4',
        property_documents='https://example.com/documents/property2.pdf',
        furnished='Yes',
        description='This is a spacious family home for rent in Nairobi, Kenya, at Kshs 150,600 per month. It features four bedrooms, three and a half bathrooms, and modern amenities like a garage, garden, and fireplace. The main image showcases a vintage VW Beetle, adding to its unique charm. The interior has a warm and inviting atmosphere with modern design. Located in a quiet Suburbia neighborhood, the house is close to schools and parks, ideal for families. The owner, David Smith, can be reached at +1 416-555-1234 or WhatsApp at +1 418-555-1234. Contact email is david@example.com, and WhatsApp is the preferred method. The property offers a virtual house tour video and documents available at example.com/documents/property2.pdf. Open house events are held on weekends. This family home presents an exceptional living experience with its spacious layout, beautiful garden, and modern amenities in a serene and convenient Nairobi location.',
        location_details='Quiet neighborhood near schools and parks.',
        location_id = 2,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Suburbia',
        address='123 Maple St, Suburbia, Kisumu ',
        user_id = 2,
        property_owner_name='David Smith',
        property_owner_photo='https://cdn.pixabay.com/photo/2017/02/16/23/10/smile-2072907_640.jpg',
        contact_phone='0755591234',
        contact_whatsapp='0755591234',
        contact_email='david@example.com',
        facebook=None,
        twitter=None,
        instagram=None,
        linkedin='linkedin.com/in/david-smith',
        other_social_media=None,
        preferred_contact_method='whatsapp',
        additional_details='Open house on weekends.',
    )
    property4 = Property(
        property_type='Condo',
        property_title= 'A cozy and modern one-bedroom condo located in Nairobi',
        property_category='Residential',
        property_rent = 16700,
        bedrooms=1,
        bathrooms=1,
        amenities='Swimming Pool, Fitness Center',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2019/12/17/04/52/lounge-4700728_640.jpg',
        images='https://cdn.pixabay.com/photo/2019/03/08/20/14/kitchen-living-room-4043091_640.jpg, https://cdn.pixabay.com/photo/2023/01/10/20/56/nyc-7710506_1280.jpg, https://cdn.pixabay.com/photo/2016/11/18/17/20/living-room-1835923_640.jpg, https://cdn.pixabay.com/photo/2014/08/11/21/39/wall-416060_640.jpg',
        house_tour_video=None,
        property_documents=None,
        furnished='Yes',
        description='This is a cozy and modern condo located in Nairobi, Kenya, available for rent at Kshs 16,700 per month. This residential property offers one bedroom and one bathroom, making it an ideal choice for individuals or couples. The condo comes furnished and includes amenities such as a swimming pool and fitness center, providing residents with opportunities for relaxation and fitness. The main image showcases the inviting lounge area, setting the tone for a comfortable living space. The condo is situated in a serene environment close to downtown Nairobi, with convenient access to public transportation. Downtown amenities are easily accessible, making daily activities and entertainment readily available to residents. The owner, Maria Salim, can be contacted via phone at +1 418-123-4567 or through WhatsApp at +1 415-123-4567. Her preferred contact method is phone. For further details or to arrange a viewing, interested parties can reach out to Maria at maria@example.com. The rent includes utilities, making it convenient for tenants. With its prime location, modern amenities, and serene environment, this cozy condo offers an excellent living experience for those seeking a comfortable and well-equipped home in Nairobi.',
        location_details='Close to downtown and public transportation.',
        location_id = 1,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Downtown',
        address='456 Elm St, Downtown, Nairobi',
        property_owner_name='Maria Salim',
        user_id = 1,
        property_owner_photo='https://cdn.pixabay.com/photo/2019/11/04/19/51/hands-4602022_640.jpg',
        contact_phone='0718123456',
        contact_whatsapp='0715124567',
        contact_email='maria@example.com',
        facebook='facebook.com/maria.salim',
        twitter=None,
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Utilities included in rent.',
    )
    property5 = Property(
        property_type='Studio',
        property_title= 'A charming studio apartment in Nakuru, Kenya, with 1 bedroom and a single bathroom',
        property_category='Residential',
        property_rent = 20000,
        bedrooms=0,
        bathrooms=1,
        amenities='Laundry Facilities, High-speed Internet',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2013/09/24/11/06/house-185714_640.jpg',
        images= 'https://cdn.pixabay.com/photo/2018/06/26/15/56/condo-3499679_640.jpg, https://cdn.pixabay.com/photo/2019/12/26/16/51/luxury-suite-4720815_640.jpg, https://cdn.pixabay.com/photo/2017/03/19/01/18/living-room-2155353_640.jpg, https://cdn.pixabay.com/photo/2017/03/19/01/43/living-room-2155376_1280.jpg',
        house_tour_video= 'https://static.videezy.com/system/resources/previews/000/004/382/original/COWS_AT_THE_GRASS.mp4',
        property_documents=None,
        furnished='Yes',
        description='This is a charming studio apartment in Nakuru, Kenya, available for rent at Kshs 20,000 per month. It offers a single bathroom, laundry facilities, and high-speed internet. The studio is furnished and equipped with all the essentials for comfortable living. The main image showcases the exterior of the building. Conveniently located in the city center, the studio provides easy access to public transport, cafes, and shops. The area is bustling with amenities, making it an ideal choice for those seeking a lively urban lifestyle. The owner, Sophie Turner, can be contacted via phone or WhatsApp at +254 708276919 or through email at sophie@example.com. She is also available on Instagram at instagram.com/sophie_turner. The preferred contact method is email. Please note that pets are not allowed in the studio. With its prime location and essential amenities, this studio apartment is perfect for individuals looking for a cozy and well-connected living space in the heart of Nakuru.',
        location_details='In the heart of the city, near cafes and shops.',
        location_id = 2,
        country='Kenya',
        city_town='Nakuru',
        neighborhood_area='City Center',
        address='789 Oxford St, Highlands, Nakuru',
        user_id = 2,
        property_owner_name='Sophie Turner',
        property_owner_photo= 'https://cdn.pixabay.com/photo/2017/02/16/23/10/smile-2072907_640.jpg',
        contact_phone= '0708276919',
        contact_whatsapp= '0708276919',
        contact_email='sophie@example.com',
        facebook=None,
        twitter='twitter.com/sophie_turner',
        instagram='instagram.com/sophie_turner',
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='email',
        additional_details='No pets allowed.',
    )
    property6 = Property(
        property_title= 'This is a 3-bedroomed townhouse located in Mombasa, Kenya, available for rent at Kshs 20,000 per month',
        property_type='Townhouse',
        property_category='Residential',
        property_rent = 20000,
        bedrooms=3,
        bathrooms=2.5,
        amenities='Garage, Patio',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2016/07/05/13/02/elegant-1498631_640.jpg',
        images='https://cdn.pixabay.com/photo/2017/01/14/12/48/hotel-1979406_640.jpg, https://pixabay.com/photos/living-room-sofa-couch-2569325/,https://pixabay.com/photos/living-room-interior-design-1835923/, https://cdn.pixabay.com/photo/2016/12/30/07/55/bedroom-1940169_640.jpg, https://cdn.pixabay.com/photo/2016/12/30/07/55/bedroom-1940169_640.jpg, https://cdn.pixabay.com/photo/2014/10/16/08/41/bathroom-490781_640.jpg, https://cdn.pixabay.com/photo/2018/08/21/23/35/bath-3622540_640.jpg, https://cdn.pixabay.com/photo/2016/12/30/07/59/kitchen-1940174_640.jpg',
        house_tour_video= 'https://static.videezy.com/system/resources/previews/000/038/659/original/alb_glitch1045_1080p_24fps.mp4',
        property_documents=None,
        furnished='No',
        description='This is a residential townhouse located in Mombasa, Kenya, available for rent at Kshs 20,000 per month. It offers three bedrooms, two and a half bathrooms, a garage, and a patio. The property is unfurnished and has modern features, including an elegant interior and recent renovations. The main image showcases the townhouse exterior.The property is situated in a family-friendly suburb with easy access to parks and schools. The owner, Michael Brown, can be contacted via phone or WhatsApp at +61 2 8765 4321 or through email at michael@gmail.com. The preferred contact method is via phone.With its spacious layout and outdoor space, this townhouse provides a comfortable living environment for potential tenants. It is an excellent option for those seeking a quality home in a peaceful and convenient location.',
        location_id = 1,
        location_details='Family-friendly neighborhood with parks and schools.',
        country='Kenya',
        city_town='Mombasa',
        neighborhood_area='Suburb',
        address='567 Park St, Bamburi, Mombasa',
        user_id = 1,
        property_owner_name='Michael Brown',
        property_owner_photo = 'https://cdn.pixabay.com/photo/2020/08/21/08/46/african-5505598_640.jpg',
        contact_phone='0787654321',
        contact_whatsapp= '0787654321',
        contact_email='michael@gmail.com',
        facebook=None,
        twitter='twitter.com/michael_brown',
        instagram=None,
        linkedin='linkedin.com/in/michael-brown',
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Recent renovations.',
    )
    property7 = Property(
        property_type='Apartment',
        property_category='Residential',
        property_title='A modern apartment available for rent in Nairobi, Kenya. This residential gem offers two bedrooms, & one bathroom',
        property_rent=30000,
        bedrooms=2,
        bathrooms=1,
        amenities='Parking, Elevator, Balcony, Gym',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2015/11/06/11/48/multi-family-home-1026484_640.jpg',
        images='https://cdn.pixabay.com/photo/2021/10/03/03/48/living-room-6676758_640.jpg, https://cdn.pixabay.com/photo/2018/02/12/10/07/modern-minimalist-bedroom-3147893_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/19/apartment-2094666_640.jpg, https://cdn.pixabay.com/photo/2021/10/06/15/05/bedroom-6686061_640.jpg, https://cdn.pixabay.com/photo/2016/03/28/09/31/home-1285134_640.jpg, https://cdn.pixabay.com/photo/2016/10/20/20/52/kitchen-1756631_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/002/004/original/20140614-SoudertonPA-YellowFlowersBreeze.mp4',
        property_documents=None,
        furnished='No',
        description='This is a modern apartment available for rent in Nairobi, Kenya, at Kshs 30,000 per month. This residential gem offers two bedrooms, one bathroom, and comes with convenient amenities such as parking, an elevator, balcony, and gym. The main image displays a stylish living room, capturing the apartment contemporary ambiance. Located in the bustling Midtown area, the apartment is within walking distance to shopping and public transport, ensuring easy accessibility. The owner, Alex Johnson, can be contacted at +1 123-456-7890 or WhatsApp at +1 417-123-4567. For inquiries, reach out via email at alex@example.com. Social media enthusiasts can connect with Alex on Facebook, Twitter, and Instagram. The property features a captivating house tour video showcasing the apartments stunning view and desirable location. Pets are allowed with a deposit, making it a pet-friendly choice for tenants. With its modern design and convenient location, this apartment promises an exceptional living experience for those seeking contemporary city living.',
        location_details='Walking distance to shopping and public transport.',
        location_id=1,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Midtown',
        address='789 Park Ave, Midtown, Nairobi',
        user_id=1,
        property_owner_name='Alex Johnson',
        property_owner_photo='https://cdn.pixabay.com/photo/2019/10/22/13/43/portrait-4568762_640.jpg',
        contact_phone='0723457890',
        contact_whatsapp='07123456790',
        contact_email='alex@example.com',
        facebook='facebook.com/alex.johnson',
        twitter=None,
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='email',
        additional_details='Pets allowed with deposit.',
    )

    property8 = Property(
        property_type='House',
        property_category='Residential',
        property_title='A spacious family home for rent, features four bedrooms, three and a half bathrooms',
        property_rent=150600,
        bedrooms=4,
        bathrooms=3.5,
        amenities='Garage, Garden, Fireplace',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2017/10/06/04/33/new-housing-development-2821969_640.jpg',
        images='https://cdn.pixabay.com/photo/2019/12/30/20/47/cupboard-4730589_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/21/apartment-2094689_640.jpg, https://cdn.pixabay.com/photo/2015/11/06/11/48/multi-family-home-1026488_640.jpg, https://cdn.pixabay.com/photo/2016/07/26/18/28/kitchen-1543489_640.jpg, https://cdn.pixabay.com/photo/2017/01/11/16/13/bad-1972205_640.jpg, https://cdn.pixabay.com/photo/2014/08/11/21/33/room-416043_640.jpg, https://cdn.pixabay.com/photo/2015/03/14/19/59/kitchen-673729_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/053/090/original/alb_kaleido1068_1080p.mp4',
        property_documents='https://example.com/documents/property2.pdf',
        furnished='Yes',
        description='This is a spacious family home for rent in Nairobi, Kenya, at Kshs 150,600 per month. It features four bedrooms, three and a half bathrooms, and modern amenities like a garage, garden, and fireplace. The main image showcases a vintage VW Beetle, adding to its unique charm. The interior has a warm and inviting atmosphere with modern design. Located in a quiet Suburbia neighborhood, the house is close to schools and parks, ideal for families. The owner, David Smith, can be reached at +1 416-555-1234 or WhatsApp at +1 418-555-1234. Contact email is david@example.com, and WhatsApp is the preferred method. The property offers a virtual house tour video and documents available at example.com/documents/property2.pdf. Open house events are held on weekends. This family home presents an exceptional living experience with its spacious layout, beautiful garden, and modern amenities in a serene and convenient Nairobi location.',
        location_details='Quiet neighborhood near schools and parks.',
        location_id=2,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Kitusuri',
        address='123 Kitusuri, Nairobi ',
        user_id=2,
        property_owner_name='David Smith',
        property_owner_photo='https://cdn.pixabay.com/photo/2018/04/15/12/24/photo-shoot-3321569_640.png',
        contact_phone='0716555134',
        contact_whatsapp='0718551234',
        contact_email='david@example.com',
        facebook=None,
        twitter='twitter.com/david_smith',
        instagram=None,
        linkedin='linkedin.com/in/david-smith',
        other_social_media=None,
        preferred_contact_method='whatsapp',
        additional_details='Open house on weekends.',
    )

    property9 = Property(
        property_type='Cottage',
        property_category='Residential',
        property_title='Charming countryside cottage with scenic views and serene surroundings',
        property_rent=28000,
        bedrooms=2,
        bathrooms=1,
        amenities='Fireplace, Garden, Patio',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2015/11/06/11/48/multi-family-home-1026481_640.jpg',
        images='https://cdn.pixabay.com/photo/2013/09/24/12/08/apartment-185779_1280.jpg, https://cdn.pixabay.com/photo/2017/04/28/22/16/room-2269594_640.jpg, https://cdn.pixabay.com/photo/2016/09/16/21/38/kitchen-1675190_640.jpg, https://cdn.pixabay.com/photo/2013/09/21/14/31/sofa-184555_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/23/bathroom-2094716_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/058/975/original/alf_sample4.mp4',
        property_documents=None,
        furnished='Yes',
        description='Escape to this charming countryside cottage nestled among picturesque landscapes. Available for rent at Kshs 28,000 per month, this 2-bedroom, 1-bathroom cottage offers a cozy fireplace, garden, and patio. The main image showcases the cottage exterior against a backdrop of nature. Ideal for nature lovers seeking tranquility, the cottage provides a serene environment for relaxation. Nearby hiking trails and a nearby lake add to the appeal of this retreat. The owner, Emily Johnson, can be contacted at +1 456-789-1234 or emily@example.com. The cottages rustic charm and beautiful surroundings make it a unique and inviting place to call home.',
        location_details='Surrounded by nature, near hiking trails and a lake.',
        location_id=3,
        country='Kenya',
        city_town='Nakuru',
        neighborhood_area='Countryside',
        address='1230, River-Road, Nakuru',
        user_id=3,
        property_owner_name='Emily Johnson',
        property_owner_photo='https://cdn.pixabay.com/photo/2015/03/11/09/35/african-668398_640.jpg',
        contact_phone='0767891234',
        contact_whatsapp='0767891234',
        contact_email='emily@example.com',
        facebook=None,
        twitter=None,
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Ideal for nature enthusiasts.',
    )

    property10 = Property(
        property_type='Penthouse',
        property_category='Residential',
        property_title='Luxurious penthouse with stunning city skyline views',
        property_rent=65000,
        bedrooms=3,
        bathrooms=3.5,
        amenities='Swimming Pool, Private Terrace, Concierge Service',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2015/11/07/21/29/livingroom-1032733_640.jpg',
        images='https://cdn.pixabay.com/photo/2016/02/29/11/41/bathroom-1228427_640.jpg, https://cdn.pixabay.com/photo/2017/07/31/14/56/apartment-2558277_640.jpg, https://cdn.pixabay.com/photo/2019/04/23/09/04/indoor-4148898_640.jpg, https://cdn.pixabay.com/photo/2019/03/08/20/17/kitchen-4043098_640.jpg, https://cdn.pixabay.com/photo/2019/09/27/11/36/lounge-4508291_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/005/207/original/20140501-WoodwardPA-Birds.mp4',
        property_documents=None,
        furnished='Yes',
        description='Indulge in luxury with this exquisite penthouse featuring breathtaking city skyline views. Available for rent at Kshs 65,000 per month, this 3-bedroom, 3.5-bathroom penthouse offers high-end amenities, a private terrace, and access to a swimming pool and concierge service. The main image showcases the penthouse\'s elegant living space with city views. Located in a prestigious high-rise building, the penthouse offers an unparalleled urban living experience. The owner, James Anderson, can be contacted at +1 567-890-1234 or james@example.com. With its opulent design and prime location, this penthouse promises a sophisticated and luxurious lifestyle.',
        location_details='Located in a prestigious high-rise building.',
        location_id=1,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='City Center',
        address='456 Skyscraper Ave, Nairobi',
        user_id=4,
        property_owner_name='James Anderson',
        property_owner_photo='https://cdn.pixabay.com/photo/2017/06/09/05/17/woman-2385785_640.jpg',
        contact_phone='0778902304',
        contact_whatsapp=None,
        contact_email='james@example.com',
        facebook=None,
        twitter='twitter.com/james_anderson',
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Access to luxury amenities.',
    )

    property11 = Property(
        property_type='Studio',
        property_category='Residential',
        property_title='Contemporary studio apartment in the heart of the arts district',
        property_rent=22000,
        bedrooms=0,
        bathrooms=1,
        amenities='Modern Kitchen, In-Unit Laundry',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2014/05/08/22/30/villa-340451_640.jpg',
        images='https://cdn.pixabay.com/photo/2020/02/02/17/06/living-room-modern-tv-4813589_640.jpg, https://cdn.pixabay.com/photo/2016/01/23/23/52/dining-room-1158266_640.jpg, https://cdn.pixabay.com/photo/2017/08/25/20/01/gallery-2681238_640.jpg, https://cdn.pixabay.com/photo/2017/12/27/14/42/furniture-3042835_640.jpg, https://cdn.pixabay.com/photo/2014/10/16/08/39/bedroom-490779_640.jpg, https://cdn.pixabay.com/photo/2014/08/11/21/32/fireplace-416042_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/053/090/original/alb_kaleido1068_1080p.mp4',
        property_documents=None,
        furnished='Yes',
        description='Experience urban living at its finest with this modern studio apartment located in the heart of the arts district. Available for rent at Kshs 22,000 per month, this stylish studio features a contemporary design, modern kitchen, and in-unit laundry. The main image showcases the apartment\'s chic living space with large windows. Situated within walking distance of galleries, theaters, and cafes, the apartment offers a vibrant lifestyle for creative individuals. The owner, Sofia Martinez, can be contacted at +1 234-567-8901 or sofia@example.com. This studio apartment offers the perfect blend of comfort and artistic inspiration.',
        location_details='Located in the heart of the arts district.',
        location_id=4,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Arts District',
        address='789 Mwihani, Eldoret',
        user_id=5,
        property_owner_name='Sofia Martinez',
        property_owner_photo='https://cdn.pixabay.com/photo/2015/01/08/18/29/entrepreneur-593358_640.jpg',
        contact_phone='0745678901',
        contact_whatsapp=None,
        contact_email='sofia@example.com',
        facebook='facebook.com/sofia.martinez',
        twitter=None,
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Ideal for creative individuals.',
    )
    property12 = Property(
        property_type='Townhouse',
        property_category='Residential',
        property_title='Spacious townhouse with modern amenities and private backyard',
        property_rent=42000,
        bedrooms=4,
        bathrooms=2.5,
        amenities='Garage, Patio, Air Conditioning',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2018/05/02/09/02/baby-boy-3368017_640.jpg',
        images='https://cdn.pixabay.com/photo/2017/07/08/23/48/dining-room-2485946_640.jpg, https://cdn.pixabay.com/photo/2019/04/23/09/04/indoor-4148894_640.jpg, https://cdn.pixabay.com/photo/2016/11/14/02/28/apartment-1822409_640.jpg, https://cdn.pixabay.com/photo/2016/11/09/02/21/kitchen-1809844_640.jpg, https://cdn.pixabay.com/photo/2020/06/27/16/40/apartment-5346460_640.jpg, https://cdn.pixabay.com/photo/2018/01/18/15/32/apartment-3090517_640.jpg, https://cdn.pixabay.com/photo/2017/01/04/14/03/living-room-1952072_640.jpg, https://cdn.pixabay.com/photo/2019/12/26/18/39/home-4720969_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/049/723/original/LAM1228.mp4',
        property_documents='https://example.com/documents/property5.pdf',
        furnished='No',
        description='Discover this spacious townhouse available for rent at Kshs 42,000 per month. With 4 bedrooms and 2.5 bathrooms, this townhouse offers modern amenities including a garage, patio, and air conditioning. The main image features a stylish kitchen with contemporary design. The private backyard provides a relaxing outdoor space. Conveniently located near schools and shopping, this townhouse is perfect for families. The owner, Robert Williams, can be contacted at +1 345-678-9012 or robert@example.com. The townhouse offers a virtual house tour video and documents available at example.com/documents/property5.pdf. Make this townhouse your new family home.',
        location_details='Near schools and shopping.',
        location_id=2,
        country='Kenya',
        city_town='Nyeri',
        neighborhood_area='Suburbia',
        address='567 Oak Ln, Ndodori, Naivashi',
        user_id=6,
        property_owner_name='Robert Williams',
        property_owner_photo='https://cdn.pixabay.com/photo/2017/06/03/04/46/man-2367953_640.jpg',
        contact_phone='0756789012',
        contact_whatsapp=None,
        contact_email='robert@example.com',
        facebook=None,
        twitter='twitter.com/robert_williams',
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Nearby schools and shopping.',
    )

    property13 = Property(
        property_type='Villa',
        property_category='Residential',
        property_title='Luxurious beachfront villa with stunning ocean views',
        property_rent=90000,
        bedrooms=5,
        bathrooms=4.5,
        amenities='Swimming Pool, Private Beach Access, Gym',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2018/02/13/11/09/home-3150500_640.jpg',
        images='https://cdn.pixabay.com/photo/2014/08/11/21/31/apartment-416039_640.jpg, https://cdn.pixabay.com/photo/2014/11/11/22/54/bedroom-527645_640.jpg, https://cdn.pixabay.com/photo/2018/09/20/02/39/kitchen-3689917_640.jpg, https://cdn.pixabay.com/photo/2018/01/22/08/55/modern-minimalist-kitchen-3098477_640.jpg, https://cdn.pixabay.com/photo/2018/01/23/06/58/modern-minimalist-bedroom-3100786_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/24/bathroom-2094735_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/22/apartment-2094700_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/020/237/original/20140614-SoudertonPA-YellowFlowersBreeze.mp4',
        property_documents=None,
        furnished='Yes',
        description='Experience the epitome of luxury with this beachfront villa boasting breathtaking ocean views. Available for rent at Kshs 90,000 per month, this 5-bedroom, 4.5-bathroom villa features high-end amenities including a swimming pool, private beach access, and a gym. The main image captures the villa\'s elegance against the backdrop of the ocean. The interior is exquisitely designed for comfort and relaxation. Located on a pristine beach, this villa offers a serene and idyllic retreat. The owner, Maria Garcia, can be contacted at +1 567-123-4567 or maria@example.com. Indulge in the ultimate coastal living experience.',
        location_details='Beachfront location with private beach access.',
        location_id=5,
        country='Kenya',
        city_town='Mombasa',
        neighborhood_area='Beachfront',
        address='123 Ocean Blvd, Mombasa',
        user_id=7,
        property_owner_name='Maria Garcia',
        property_owner_photo='https://cdn.pixabay.com/photo/2014/11/19/10/52/man-537136_640.jpg',
        contact_phone='0781234567',
        contact_whatsapp=None,
        contact_email='maria@example.com',
        facebook=None,
        twitter=None,
        instagram='instagram.com/maria.garcia',
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Direct access to a pristine beach.',
    )
    property14 = Property(
        property_type='Loft',
        property_category='Residential',
        property_title='Chic industrial loft in a historic downtown building',
        property_rent=32000,
        bedrooms=1,
        bathrooms=1.5,
        amenities='Exposed Brick Walls, High Ceilings',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2015/09/08/22/03/luggage-930804_640.jpg',
        images='https://cdn.pixabay.com/photo/2016/11/14/02/29/apartment-1822410_640.jpg, https://cdn.pixabay.com/photo/2015/01/16/11/19/hotel-601327_640.jpg, https://cdn.pixabay.com/photo/2021/11/08/00/30/living-room-6778197_640.jpg, https://cdn.pixabay.com/photo/2016/10/20/20/52/kitchen-1756631_640.jpg, https://cdn.pixabay.com/photo/2013/09/24/12/05/apartment-185777_640.jpg',
        house_tour_video=None,
        property_documents=None,
        furnished='Yes',
        description='Immerse yourself in urban charm with this chic industrial loft situated in a historic downtown building. Available for rent at Kshs 32,000 per month, this 1-bedroom, 1.5-bathroom loft boasts exposed brick walls and high ceilings. The main image showcases the loft\'s open-concept living area with an industrial aesthetic. Located within walking distance of cafes, shops, and entertainment, this loft offers a trendy downtown lifestyle. The owner, Michael Brown, can be contacted at +1 678-901-2345 or michael@example.com. Embrace the unique character of this historic loft.',
        location_details='Located in the heart of downtown.',
        location_id=1,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Downtown',
        address='789 Waiyaki-Way, Nairobi',
        user_id=8,
        property_owner_name='Michael Brown',
        property_owner_photo='https://cdn.pixabay.com/photo/2018/09/18/00/55/business-3685133_640.jpg',
        contact_phone='0789012345',
        contact_whatsapp='0789012345',
        contact_email='michael@example.com',
        facebook='facebook.com/michael.brown',
        twitter=None,
        instagram='instagram.com/michael.brown',
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Historic downtown building with character.',
    )

    property15 = Property(
        property_type='Farmhouse',
        property_category='Residential',
        property_title='Quaint farmhouse with spacious land and scenic views',
        property_rent=38000,
        bedrooms=3,
        bathrooms=2,
        amenities='Barn, Garden, Pastoral Views',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2012/11/19/16/26/house-66627_640.jpg',
        images='https://cdn.pixabay.com/photo/2016/06/23/19/41/living-room-1476062_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/22/apartment-2094701_640.jpg, https://cdn.pixabay.com/photo/2014/09/25/18/05/bedroom-460762_640.jpg, https://cdn.pixabay.com/photo/2019/04/23/09/04/indoor-4148892_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/24/bathroom-2094736_640.jpg',
        house_tour_video=None,
        property_documents=None,
        furnished='No',
        description='Escape to a tranquil countryside retreat with this charming farmhouse available for rent at Kshs 38,000 per month. With 3 bedrooms and 2 bathrooms, this farmhouse offers a barn, garden, and picturesque pastoral views. The main image showcases the rustic exterior of the farmhouse against a scenic backdrop. Situated on spacious land, this farmhouse is ideal for those seeking a peaceful and idyllic lifestyle. The owner, Sarah Thompson, can be contacted at +1 789-012-3456 or sarah@example.com. Embrace the simplicity and beauty of country living.',
        location_details='Surrounded by open fields and nature.',
        location_id=3,
        country='Kenya',
        city_town='Eldoret',
        neighborhood_area='Countryside',
        address='456 Nairobi Rd, Eldoret',
        user_id=9,
        property_owner_name='Sarah Thompson',
        property_owner_photo='https://cdn.pixabay.com/photo/2015/08/14/15/28/smiling-888532_640.jpg',
        contact_phone='0790123456',
        contact_whatsapp=None,
        contact_email='sarah@example.com',
        facebook=None,
        twitter=None,
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Ideal for nature enthusiasts.',
    )

    property16 = Property(
        property_type='Apartment',
        property_category='Residential',
        property_title='Modern apartment with stunning city views',
        property_rent=28000,
        bedrooms=2,
        bathrooms=2,
        amenities='Swimming Pool, Fitness Center, Balcony',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2015/11/06/11/48/multi-family-home-1026482_640.jpg',
        images='https://cdn.pixabay.com/photo/2019/06/02/12/27/apartment-4246371_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/24/kitchen-2094737_640.jpg, https://cdn.pixabay.com/photo/2017/10/03/09/43/plant-2811723_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/19/apartment-2094661_640.jpg, https://cdn.pixabay.com/photo/2019/12/09/12/59/architecture-4683476_640.jpg, https://cdn.pixabay.com/photo/2019/04/23/09/04/indoor-4148896_640.jpg, https://cdn.pixabay.com/photo/2014/08/11/21/35/room-416049_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/055/849/original/Summer15-Tokyo.mp4',
        property_documents=None,
        furnished='Yes',
        description='Elevate your urban lifestyle with this modern apartment featuring stunning city views. Available for rent at Kshs 28,000 per month, this 2-bedroom, 2-bathroom apartment offers a swimming pool, fitness center, and balcony. The main image showcases the apartment\'s sleek kitchen and living area with cityscape vistas. Located in a vibrant neighborhood, the apartment provides convenient access to dining and entertainment. The owner, Jennifer Smith, can be contacted at +1 456-789-0123 or jennifer@example.com. Experience contemporary living at its finest.',
        location_details='In a vibrant and bustling neighborhood.',
        location_id=1,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='City Center',
        address='789 Urban Plaza, Nairobi',
        user_id=10,
        property_owner_name='Jennifer Smith',
        property_owner_photo='https://cdn.pixabay.com/photo/2017/07/11/18/59/mentor-2494673_640.jpg',
        contact_phone='0789430123',
        contact_whatsapp='0789430123',
        contact_email='jennifer@example.com',
        facebook='facebook.com/jennifer.smith',
        twitter='twitter.com/jennifer_smith',
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Vibrant neighborhood with dining and entertainment options.',
    )

    property17 = Property(
        property_type='Cabin',
        property_category='Residential',
        property_title='Cozy mountain cabin with panoramic nature views',
        property_rent=25000,
        bedrooms=2,
        bathrooms=1,
        amenities='Fireplace, Deck, Scenic Trails',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2015/11/06/11/40/multi-family-home-1026386_640.jpg',
        images='https://cdn.pixabay.com/photo/2010/12/14/14/58/bath-3148_640.jpg, https://cdn.pixabay.com/photo/2021/11/08/00/30/kitchen-6778196_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/20/apartment-2094674_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/20/bathroom-2094682_640.jpg, https://cdn.pixabay.com/photo/2020/06/27/16/40/apartment-5346458_640.jpg, https://cdn.pixabay.com/photo/2018/07/20/16/19/interior-3551003_640.jpg',
        house_tour_video=None,
        property_documents=None,
        furnished='Yes',
        description='Embrace the serenity of mountain living with this cozy cabin available for rent at Kshs 25,000 per month. This 2-bedroom, 1-bathroom cabin features a fireplace, deck, and scenic trails. The main image captures the cabin\'s rustic charm against a backdrop of nature. Nestled in a picturesque mountain setting, this cabin offers a tranquil escape for outdoor enthusiasts. The owner, David Wilson, can be contacted at +1 567-890-2345 or david@example.com. Reconnect with nature and find solace in this charming mountain retreat.',
        location_details='Located in a picturesque mountain setting.',
        location_id=6,
        country='Kenya',
        city_town='Nanyuki',
        neighborhood_area='Mountain Range',
        address='123 Pine Ridge Rd, Nanyuki',
        user_id=11,
        property_owner_name='David Wilson',
        property_owner_photo='https://cdn.pixabay.com/photo/2017/09/16/14/33/electrician-2755679_640.jpg',
        contact_phone='0708902345',
        contact_whatsapp=None,
        contact_email='david@example.com',
        facebook=None,
        twitter=None,
        instagram='instagram.com/david.wilson',
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Ideal for outdoor enthusiasts.',
    )


    db.session.add_all([property1, property2, property3, property4, property5, property6, property7, property8, property9, property10, property11, property12, property13, property14, property15, property16, property17])
    db.session.commit()
    
    
    payment1 = Payment(
        user_id=user1.id,
        property_id=property2.id,
        amount=1200.0,
        payment_method='Credit Card',
    )
    payment2 = Payment(
        user_id=user2.id,
        property_id=property1.id,
        amount=800.0,
        payment_method='M-Pesa',
    )

    db.session.add_all([payment1, payment2])
    db.session.commit()
    # Seed data for rental terms
    rental_terms1 = RentalTerms(
        property_id=property1.id,
        rental_price=3500,
        security_deposit=1000,
        lease_duration_min=12,
        lease_duration_max=24,
        additional_fees='None'
    )
    rental_terms2 = RentalTerms(
        property_id=property2.id,
        rental_price=1200,
        security_deposit=800,
        lease_duration_min=6,
        lease_duration_max=12,
        additional_fees='Utilities not included'
    )

    db.session.add_all([rental_terms1, rental_terms2])
    db.session.commit()


    # Seed data for reviews
    review1 = Review(user_id=user1.id, property_id=property1.id, full_name='Gloriah Kadimane', address='303, Thika Road, Kamakis, Nairobi', email='Gloriahkadimane@gmail.com', comment='Great office space!')
    review2 = Review(user_id=user2.id, property_id=property2.id, full_name='Joyce Njoroge', address='46723, Eastleigh, Nairobi', email='Joycenjoroge@gmail.com', comment='Cozy apartment with a lovely view.')

    db.session.add_all([review1, review2])
    db.session.commit()

    # Seed data for user favorite properties
    user_favorite_property1 = UserFavoriteProperty(user_id=user1.id, listing_id=None, property_id=property2.id)
    user_favorite_property2 = UserFavoriteProperty(user_id=user2.id, listing_id=None, property_id=property1.id)

    db.session.add_all([user_favorite_property1, user_favorite_property2])
    db.session.commit()
    
    

# Run the seed function
if __name__ == '__main__':
    with app.app_context():
        seed_data()
