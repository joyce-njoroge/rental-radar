#imports
from flask import Flask, make_response,request,jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse, abort
from datetime import datetime, timedelta
# from flask_bcrypt import Bcrypt
from werkzeug.security import check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,  get_jwt_identity, current_user
from models import db,User, Listing, Location, Property, RentalTerms, Review, UserFavoriteProperty, NewestListing, FeaturedListing, PropertyInquiry
import bcrypt



# initiasing app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '332nsdbd993h3bd84920'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '3dw72g32@#!'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)  # Access token expiration time (1 hour in this example)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

migrate =Migrate(app,db) 
db.init_app(app)
api = Api(app)

jwt = JWTManager(app)
# bcrypt = Bcrypt(app)



class UserResource(Resource):
   
    def get(self):
        
        user_list = [{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'registration_date': user.registration_date.isoformat()
        } for user in User.query.all()]

        # Include the access token in the response data
        access_token = create_access_token(identity="some_identity")  # You can pass the user's identity here
        response_data = {
            'users': user_list,
            'access_token': access_token
        }

        return response_data, 200

    def post(self):
        data = request.get_json()

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if role not in User.VALID_ROLES:
            return {'message': f"Invalid role. Allowed roles are: {', '.join(User.VALID_ROLES)}"}, 400

        # Check if username already exists in the database
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            return {'message': 'Username already exists. Please choose a different username.'}, 409

        # Check if email already exists in the database
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return {'message': 'Email address already exists. Please use a different email.'}, 409

        password = data.get('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        new_user = User(username=username, email=email, hashed_password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        # Generate role-specific access tokens based on the user's role
        access_token = create_access_token(identity=new_user.id, additional_claims={'role': role})

        response_data = {
            'message': 'User created successfully',
            'user': {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email,
                'role': new_user.role,
                'registration_date': new_user.registration_date.isoformat()
            },
            'access_token': access_token  # generated access token with role-specific name
        }
        
        return response_data, 201

 
 
class UserResourceId(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            user_data = user.to_dict()

            # Include the access token in the response data
            access_token = create_access_token(identity=user.id)  # You can pass the user's identity here
            response_data = {
                'user': user_data,
                'access_token': access_token
            }

            return response_data, 200
        else:
            return {'message': 'User not found'}, 404

    def patch(self, user_id):
        user = User.query.get(user_id)
        if user:
            data = request.get_json()
            # Update user attributes based on the data received in the request
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.hashed_password = data.get('hashed_password', user.hashed_password)
            user.role = data.get('role', user.role)
            db.session.commit()
            return {'message': 'User updated successfully'}, 200
        else:
            return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404

class CheckUsernameAndEmail(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

        response_data = {
            'usernameExists': False,
            'emailExists': False,
        }

        if existing_user:
            if existing_user.username == username:
                response_data['usernameExists'] = True
            if existing_user.email == email:
                response_data['emailExists'] = True

        return response_data



class UserLoginResource(Resource):
    def post(self):
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')  # Use 'password' instead of 'hashed_password'

        if not email or not password:
            return {'message': 'Email and password are required'}, 400

        # Check if the user with the provided email exists
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'message': 'User not found'}, 404

        # Verify the provided password against the hashed password in the database
        if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            return {'message': 'Invalid credentials'}, 401

        # Generate access token if the login is successful
        access_token = create_access_token(identity=user.id)

        response_data = {
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'registration_date': user.registration_date.isoformat()
            },
            'access_token': access_token
        }

        return response_data, 200





class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return {'message': 'You are authorized to access this protected resource.'}, 200
    


#property access

class PropertyResource(Resource):
    def get(self):
        properties = Property.query.all()
        property_list = [
            {
                'id': property.id,
                'property_title':property.property_title,
                'property_type': property.property_type,
                'property_category': property.property_category,
                'property_rent': property.property_rent,
                'bedrooms': property.bedrooms,
                'bathrooms': property.bathrooms,
                'amenities': property.amenities,
                'square_footage': property.square_footage,
                'main_image': property.main_image,
                'images': property.images,
                'house_tour_video': property.house_tour_video,
                'property_documents': property.property_documents,
                'furnished': property.furnished,
                'description': property.description,
                'location_details': property.location_details,
                'country': property.country,
                'city_town': property.city_town,
                'neighborhood_area': property.neighborhood_area, 
                'address': property.address,
                'property_owner_name': property.property_owner_name,
                'property_owner_photo': property.property_owner_photo,
                'contact_phone': property.contact_phone,
                'contact_whatsapp': property.contact_whatsapp,
                'contact_email': property.contact_email, 
                'facebook': property.facebook,
                'twitter': property.twitter,
                'instagram': property.instagram,
                'linkedin': property.linkedin,
                'other_social_media': property.other_social_media,
                'preferred_contact_method': property.preferred_contact_method,
                'additional_details': property.additional_details,
                    }
                    for property in properties
                ]
        response= make_response( property_list,200)
                
        return response
    
    def post(self):
        data = request.get_json()
        # Extract the required fields from the JSON data
        property_title = data.get('property_title')
        property_type = data.get('property_type')
        property_category = data.get('property_category')
        property_rent = data.get('property.rent')
        bedrooms = data.get('bedrooms')
        bathrooms = data.get('bathrooms')
        amenities = data.get('amenities')
        square_footage = data.get('square_footage')
        main_image = data.get('main_image')
        images = data.get('images')
        house_tour_video = data.get('house_tour_video')
        property_documents = data.get('property_documents')
        furnished = data.get('furnished', 'Y')
        description = data.get('description')
        location_details = data.get('location_details')
        country = data.get('country')
        city_town = data.get('city_town')
        neighborhood_area = data.get('neighborhood_area')
        address = data.get('address')
        property_owner_name =  data.get('property.property_owner_name')
        property_owner_photo = data.get('property.property_owner_photo')
        contact_phone = data.get('property.contact_phone')
        contact_whatsapp = data.get('property.contact_whatsapp')
        contact_email = data.get('property.contact_email')
        facebook = data.get('property.facebook')
        twitter = data.get('property.twitter')
        instagram = data.get('property.instagram')
        linkedin = data.get('property.linkedin')
        other_social_media = data.get('property.other_social_media')
        preferred_contact_method = data.get('property.preferred_contact_method')
        additional_details = data.get('property.additional_details')

        # Create a new Property object and add it to the database
        new_property = Property(
            property_title=property_title,
            property_type=property_type,
            property_category=property_category,
            property_rent=property_rent,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            amenities=amenities,
            square_footage=square_footage,
            main_image=main_image,
            images=images,
            house_tour_video=house_tour_video,
            property_documents=property_documents,
            furnished='furnished' 'Y',
            description=description,
            location_details=location_details,
            country=country,
            city_town=city_town,
            neighborhood_area=neighborhood_area,
            address=address,
            property_owner_name=property_owner_name,
            property_owner_photo=property_owner_photo,
            contact_phone=contact_phone,
            contact_whatsapp=contact_whatsapp,
            contact_email=contact_email,
            facebook=facebook,
            twitter=twitter,
            instagram=instagram,
            linkedin=linkedin,
            other_social_media=other_social_media,
            preferred_contact_method =preferred_contact_method,
            additional_details =additional_details,
        )
        db.session.add(new_property)
        db.session.commit()

        # Prepare the success message
        success_message = f"Property with ID {new_property.id} has been successfully created."

        return {
            'message': success_message,
             'id': new_property.id,
            'property_title': new_property.property_title,
            'property_type': new_property.property_type,
            'property_category': new_property.property_category,
            'property_rent': new_property.property_rent,
            'bedrooms': new_property.bedrooms,
            'bathrooms': new_property.bathrooms,
            'amenities': new_property.amenities,
            'square_footage': new_property.square_footage,
            'main_image': new_property.main_image,
            'images': new_property.images,
            'house_tour_video': new_property.house_tour_video,
            'property_documents': new_property.property_documents,
            'furnished': new_property.furnished,
            'description': new_property.description,
            'location_details': new_property.location_details,
            'country': new_property.country,
            'city_town' : new_property.city_town,
            'neighborhood_area' : new_property.neighborhood_area,
            'address' : new_property.address,
            'property_owner_name': new_property.property_owner_name,
            'property_owner_photo': new_property.property_owner_photo,
            'contact_phone': new_property.contact_phone,
            'contact_whatsapp': new_property.contact_whatsapp,
            'contact_email': new_property.contact_email,
            'facebook': new_property.facebook,
            'twitter': new_property.twitter,
            'instagram': new_property.instagram,
            'linkedin': new_property.linkedin,
            'other_social_media': new_property.other_social_media,
            'preferred_contact_method': new_property.preferred_contact_method,
            'additional_details': new_property.additional_details,
        }, 201 # 201 Created status code




class PropertyResourceId(Resource):
    def get(self, id=None):
        if id is None:
            # If id is not provided, return all properties
            properties = Property.query.all()
            property_list = [
                {
                    'id': property.id,
                    'property_title': property.property_title,
                    'property_type': property.property_type,
                    'property_category': property.property_category,
                    'property_rent': property.property_rent,
                    'bedrooms': property.bedrooms,
                    'bathrooms': property.bathrooms,
                    'amenities': property.amenities,
                    'square_footage': property.square_footage,
                    'main_image': property.main_image,
                    'images': property.images,
                    'house_tour_video': property.house_tour_video,
                    'property_documents': property.property_documents,
                    'furnished': property.furnished,
                    'description': property.description,
                    'location_details': property.location_details,
                    'country': property.country,
                    'city_town' : property.city_town,
                    'neighborhood_area' : property.neighborhood_area,
                    'address' : property.address,
                    'property_owner_name': property.property_owner_name,
                    'property_owner_photo': property.property_owner_photo,
                    'contact_phone': property.contact_phone,
                    'contact_whatsapp': property.contact_whatsapp,
                    'contact_email': property.contact_email,
                    'facebook': property.facebook,
                    'twitter': property.twitter,
                    'instagram': property.instagram,
                    'linkedin': property.linkedin,
                    'other_social_media': property.other_social_media,
                    'preferred_contact_method': property.preferred_contact_method,
                    'additional_details': property.additional_details,
                }
                for property in properties
            ]
            return property_list
        else:
            # If id is provided, return a specific property by ID
            property = Property.query.get(id)
            if property:
                return {
                    'id': property.id,
                    'property_title': property.property_title,
                    'property_type': property.property_type,
                    'property_category': property.property_category,
                    'property_rent': property.property_rent,
                    'bedrooms': property.bedrooms,
                    'bathrooms': property.bathrooms,
                    'amenities': property.amenities,
                    'square_footage': property.square_footage,
                    'main_image': property.main_image,
                    'images': property.images,
                    'house_tour_video': property.house_tour_video,
                    'property_documents': property.property_documents,
                    'furnished': property.furnished,
                    'description': property.description,
                    'location_details': property.location_details,
                    'country': property.country,
                    'city_town' : property.city_town,
                    'neighborhood_area' : property.neighborhood_area,
                    'address' : property.address,
                    'property_owner_name': property.property_owner_name,
                    'property_owner_photo': property.property_owner_photo,
                    'contact_phone': property.contact_phone,
                    'contact_whatsapp': property.contact_whatsapp,
                    'contact_email': property.contact_email,
                    'facebook': property.facebook,
                    'twitter': property.twitter,
                    'instagram': property.instagram,
                    'linkedin': property.linkedin,
                    'other_social_media': property.other_social_media,
                    'preferred_contact_method': property.preferred_contact_method,
                    'additional_details': property.additional_details,
                }
            else:
                return {'message': 'Property not found'}, 404
    
    def patch(self, id):
        data = request.get_json()

        # Query the database for the property with the given ID
        property = Property.query.get(id)

        if property:
           
            for key, value in data.items():
                if value is not None:
                    setattr(property, key, value)

            
            db.session.commit()

            
            success_message = f"Property with ID {id} has been successfully updated."

            return {
                'id': property.id,
                'property_title': property.property_title,
                'property_type': property.property_type,
                'property_category': property.property_category,
                'property_rent': property.property_rent,
                'bedrooms': property.bedrooms,
                'bathrooms': property.bathrooms,
                'amenities': property.amenities,
                'square_footage': property.square_footage,
                'main_image': property.main_image,
                'images': property.images,
                'house_tour_video': property.house_tour_video,
                'property_documents': property.property_documents,
                'furnished': property.furnished,
                'description': property.description,
                'location_details': property.location_details,
                'country': property.country,
                'city_town' : property.city_town,
                'neighborhood_area' : property.neighborhood_area,
                'address' : property.address,
                'property_owner_name': property.property_owner_name,
                'property_owner_photo': property.property_owner_photo,
                'contact_phone': property.contact_phone,
                'contact_whatsapp': property.contact_whatsapp,
                'contact_email': property.contact_email,
                'facebook': property.facebook,
                'twitter': property.twitter,
                'instagram': property.instagram,
                'linkedin': property.linkedin,
                'other_social_media': property.other_social_media,
                'preferred_contact_method': property.preferred_contact_method,
                'additional_details': property.additional_details,
            }, 200
        else:
            return {'message': 'Property not found'}, 404
        
        
    def delete(self, id):
       
        property = Property.query.get(id)

        if property:
            
            db.session.delete(property)
            db.session.commit()
            return {'message': 'Property deleted successfully'}, 200
        else:
            return {'message': 'Property not found'}, 404



class ListingResource(Resource):
    # @jwt_required()
    def get(self):
        
        # current_user_id = get_jwt_identity()
        # current_user = User.query.get(current_user_id)

        # if current_user.role != 'tenant':
        #     return {'message': 'Only admin users can view the listings.'}, 403

        listings = Listing.query.all()
        listing_list = [
            {
                'id': listing.id,
                'title': listing.title,
                'description': listing.description,
                'rent': listing.rent,
                'place': listing.place,
                'size': listing.size,
                'utilities': listing.utilities,
                'media': listing.media,
            }
            for listing in listings
        ]
        response= make_response( listing_list,200)
        return response
    
    
    
    # post method using flask.request
    def post(self):
        data = request.get_json()
        if data:
            # Extract data from the JSON payload
            title = data.get('title')
            description = data.get('description')
            rent = data.get('rent')
            place = data.get('place')
            size = data.get('size')
            utilities = data.get('utilities')
            media = data.get('media')

            # Create a new Listing object and add it to the database
            new_listing = Listing(
                title=title,
                description=description,
                rent=rent,
                place=place,
                size=size,
                utilities=utilities,
                media=media
            )
            db.session.add(new_listing)
            db.session.commit()

            # Prepare the success message
            success_message = f"Listing with ID {new_listing.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_listing.id,
                'title': new_listing.title,
                'description': new_listing.description,
                'rent': new_listing.rent,
                'place': new_listing.place,
                'size': new_listing.size,
                'utilities': new_listing.utilities,
                'media': new_listing.media
            }, 201  # 201 Created status code
        else:
            return {'message': 'Invalid JSON data'}, 400
 

class ListingResourceId(Resource):
    def get(self, id=None):
        if id is None:
            # If id is not provided, return all listings
            listings = Listing.query.all()
            listing_list = [
                {
                    'id': listing.id,
                    'title': listing.title,
                    'description': listing.description,
                    'rent': listing.rent,
                    'place': listing.place,
                    'size': listing.size,
                    'utilities': listing.utilities,
                    'media': listing.media,
                }
                for listing in listings
            ]
            return listing_list
        else:
            # If id is provided, return a specific listing by ID
            listing = Listing.query.get(id)
            if listing:
                return {
                    'id': listing.id,
                    'title': listing.title,
                    'description': listing.description,
                    'rent': listing.rent,
                    'place': listing.place,
                    'size': listing.size,
                    'utilities': listing.utilities,
                    'media': listing.media,
                }
            else:
                return {'message': 'Listing not found'}, 404

    

    def patch(self, id):
        data = request.get_json()
        if data:
            listing = Listing.query.get(id)
            if listing:
                # Update the listing attributes based on the provided data
                for key, value in data.items():
                    setattr(listing, key, value)

                # Commit changes to the database
                db.session.commit()

                # Prepare the success message
                success_message = f"Listing with ID {id} has been successfully updated."

                return {
                    'message': success_message,
                    'id': listing.id,
                    'title': listing.title,
                    'description': listing.description,
                    'rent': listing.rent,
                    'place': listing.place,
                    'size': listing.size,
                    'utilities': listing.utilities,
                    'media': listing.media,
                }, 200
            else:
                return {'message': 'Listing not found'}, 404
        else:
            return {'message': 'Invalid JSON data'}, 400  # 400 Bad Request status code

    def delete(self, id):
        listing = Listing.query.get(id)
        if listing:
            # Delete the listing from the database
            db.session.delete(listing)
            db.session.commit()
            return {'message': 'Listing deleted successfully'}, 200
        else:
            return {'message': 'Listing not found'}, 404
        
class NewestListingResource(Resource):
    def get(self):
        newest_listings = NewestListing.query.all()
        newest_listing_list = [
            {
                'id': listing.id,
                'title': listing.title,
                'description': listing.description,
                'rent': listing.rent,
                'place': listing.place,
                'size': listing.size,
                'utilities': listing.utilities,
                'media': listing.media,
            }
            for listing in newest_listings
        ]
        response = make_response(newest_listing_list, 200)
        return response
    
    def post(self):
        data = request.get_json()
        if data:
            # Extract data from the JSON payload
            title = data.get('newest_title')
            description = data.get('newest_description')
            rent = data.get('newest_rent')
            place = data.get('newest_place')
            size = data.get('newest_size')
            utilities = data.get('newest_utilities')
            media = data.get('newest_media')

            # Create a new NewestListing object and add it to the database
            new_listing = NewestListing(
                title=title,
                description=description,
                rent=rent,
                place=place,
                size=size,
                utilities=utilities,
                media=media
            )
            db.session.add(new_listing)
            db.session.commit()

            # Prepare the success message
            success_message = f"Newest Listing with ID {new_listing.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_listing.id,
                'title': new_listing.title,
                'description': new_listing.description,
                'rent': new_listing.rent,
                'place': new_listing.place,
                'size': new_listing.size,
                'utilities': new_listing.utilities,
                'media': new_listing.media
            }, 201  # 201 Created status code
        else:
            return {'message': 'Invalid JSON data'}, 400

class NewestListingResourceId(Resource):
    def get(self, id=None):
        if id is None:
            # If id is not provided, return all newest listings
            newest_listings = NewestListing.query.all()
            newest_listing_list = [
                {
                    'id': listing.id,
                    'title': listing.title,
                    'description': listing.description,
                    'rent': listing.rent,
                    'place': listing.place,
                    'size': listing.size,
                    'utilities': listing.utilities,
                    'media': listing.media,
                }
                for listing in newest_listings
            ]
            return newest_listing_list
        else:
            # If id is provided, return a specific newest listing by ID
            newest_listing = NewestListing.query.get(id)
            if newest_listing:
                return {
                    'id': newest_listing.id,
                    'title': newest_listing.title,
                    'description': newest_listing.description,
                    'rent': newest_listing.rent,
                    'place': newest_listing.place,
                    'size': newest_listing.size,
                    'utilities': newest_listing.utilities,
                    'media': newest_listing.media,
                }
            else:
                return {'message': 'Newest listing not found'}, 404


class FeaturedListingResource(Resource):
    def get(self):
        featured_listings = FeaturedListing.query.all()
        featured_listing_list = [
            {
                'id': listing.id,
                'title': listing.title,
                'description': listing.description,
                'rent': listing.rent,
                'place': listing.place,
                'size': listing.size,
                'utilities': listing.utilities,
                'media': listing.media,
            }
            for listing in featured_listings
        ]
        response = make_response(featured_listing_list, 200)
        return response
    
    def post(self):
        data = request.get_json()
        if data:
            # Extract data from the JSON payload
            title = data.get('featured_title')
            description = data.get('featured_description')
            rent = data.get('featured_rent')
            place = data.get('featured_place')
            size = data.get('featured_size')
            utilities = data.get('featured_utilities')
            media = data.get('featured_media')

            # Create a new FeaturedListing object and add it to the database
            new_listing = FeaturedListing(
                title=title,
                description=description,
                rent=rent,
                place=place,
                size=size,
                utilities=utilities,
                media=media
            )
            db.session.add(new_listing)
            db.session.commit()

            # Prepare the success message
            success_message = f"Featured Listing with ID {new_listing.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_listing.id,
                'title': new_listing.title,
                'description': new_listing.description,
                'rent': new_listing.rent,
                'place': new_listing.place,
                'size': new_listing.size,
                'utilities': new_listing.utilities,
                'media': new_listing.media
            }, 201  # 201 Created status code
        else:
            return {'message': 'Invalid JSON data'}, 400

class FeaturedListingResourceId(Resource):
    def get(self, id=None):
        if id is None:
            # If id is not provided, return all featured listings
            featured_listings = FeaturedListing.query.all()
            featured_listing_list = [
                {
                    'id': listing.id,
                    'title': listing.title,
                    'description': listing.description,
                    'rent': listing.rent,
                    'place': listing.place,
                    'size': listing.size,
                    'utilities': listing.utilities,
                    'media': listing.media,
                }
                for listing in featured_listings
            ]
            return featured_listing_list
        else:
            # If id is provided, return a specific featured listing by ID
            featured_listing = FeaturedListing.query.get(id)
            if featured_listing:
                return {
                    'id': featured_listing.id,
                    'title': featured_listing.title,
                    'description': featured_listing.description,
                    'rent': featured_listing.rent,
                    'place': featured_listing.place,
                    'size': featured_listing.size,
                    'utilities': featured_listing.utilities,
                    'media': featured_listing.media,
                }
            else:
                return {'message': 'Featured listing not found'}, 404



    
class LocationResource(Resource):
    def get(self):
        locations = Location.query.all()
        location_list = [
            # {
            #     'id': location.id,
            #     'city': location.city,
            #     'neighborhood': location.neighborhood,
            #     'specific_area': location.specific_area
            # }
            location.to_dict() for location in locations
        ]
        return location_list

class ReviewResource(Resource):
    def get(self):
        reviews = Review.query.all()
        review_list = [
            {
                'id': review.id,
                'user_id': review.user_id,
                # 'listing_id': review.listing_id,
                'property_id': review.property_id,
                'full_name': review.full_name,
                'address': review.address,
                'email': review.email,
                'comment': review.comment,
                'review_date': review.review_date.strftime('%Y-%m-%d %H:%M:%S')
            }
            for review in reviews
        ]
        return review_list


    def post(self):
        data = request.get_json()
        if data:
            # Extract data from the JSON payload
            user_id = data.get('user_id')
            property_id = data.get('property_id')
            full_name = data.get('full_name')
            address = data.get('address')
            email = data.get('email')
            comment = data.get('comment')

            # Automatically set the review date to the current date and time
            review_date = datetime.now()

            # Check if the required fields are present in the request
            if not all([user_id, property_id, comment]):
                return {'message': 'All fields are required'}, 400

            # Create a new Review object and add it to the database
            new_review = Review(
                user_id=user_id,
                property_id=property_id,
                full_name=full_name,
                address=address,
                email=email,
                comment=comment,
                review_date=review_date
            )
            db.session.add(new_review)
            db.session.commit()

            # Prepare the success message
            success_message = f"Review with ID {new_review.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_review.id,
                'user_id': new_review.user_id,
                'property_id': new_review.property_id,
                'full_name': new_review.full_name,
                'address': new_review.address,
                'email': new_review.email,
                'comment': new_review.comment,
                'review_date': new_review.review_date.strftime('%Y-%m-%d %H:%M:%S')
            }, 201  # 201 Created status code
        else:
            return {'message': 'Invalid JSON data'}, 400

      
class ReviewResourceId(Resource):
    def get(self, id):
        review = Review.query.get(id)
        if review:
            return {
                'id': review.id,
                'user_id': review.user_id,
                # 'listing_id': review.listing_id,
                'property_id': review.property_id,
                'full_name': review.full_name,
                'address': review.address,
                'email': review.email,
                'comment': review.comment,
                'review_date': review.review_date.strftime('%Y-%m-%d %H:%M:%S')
            }, 200
        else:
            return {'message': 'Review not found'}, 404
        
    def patch(self, id):
        data = request.get_json()
        if data:
            review = Review.query.get(id)
            if review:
                # Update the review attributes based on the provided data
                if 'user_id' in data:
                    review.user_id = data['user_id']
                # if 'listing_id' in data:
                #     review.listing_id = data['listing_id']
                if 'property_id' in data:
                    review.property_id = data['property_id']
                if 'full_name' in data:
                    review.full_name = data['full_name']
                if 'address' in data:
                    review.address = data['address']
                if 'email' in data:
                    review.email = data['email']
                if 'comment' in data:
                    review.comment = data['comment']
                if 'review_date' in data:
                    try:
                        review_date = datetime.strptime(data['review_date'], '%Y-%m-%d').date()
                    except ValueError:
                        return {'message': 'Invalid review_date format. Expected format: YYYY-MM-DD'}, 400
                    review.review_date = review_date
                # Commit changes to the database
                db.session.commit()

                # Prepare the success message
                success_message = f"Review with ID {id} has been successfully updated."

                return {
                    'message': success_message,
                    'id': review.id,
                    'user_id': review.user_id,
                    # 'listing_id': review.listing_id,
                    'property_id': review.property_id,
                    'full_name': review.full_name,
                    'address': review.address,
                    'email': review.email,
                    'comment': review.comment,
                    'review_date': review.review_date.strftime('%Y-%m-%d')
                }, 200
            else:
                return {'message': 'Review not found'}, 404
        else:
            return {'message': 'Invalid JSON data'}, 400

    def delete(self, id):
        review = Review.query.get(id)
        if review:
            # Delete the review from the database
            db.session.delete(review)
            db.session.commit()
            return {'message': 'Review deleted successfully'}, 200
        else:
            return {'message': 'Review not found'}, 404


class Favorite(Resource):
    def get(self):
        user_fav_properties = UserFavoriteProperty.query.all()
        user_fav_property_list = [
            {
                'id': fav_property.id,
                'user_id': fav_property.user_id,
                'listing_id': fav_property.listing_id,
                'property_id': fav_property.property_id,
            }
            for fav_property in user_fav_properties
        ]
        return user_fav_property_list

    def post(self):
        data = request.get_json()
        if data:
            # Extract data from the JSON payload
            user_id = data.get('user_id')
            listing_id = data.get('listing_id')
            property_id = data.get('property_id')

            # Create a new UserFavoriteProperty object and add it to the database
            new_user_fav_property = UserFavoriteProperty(
                user_id=user_id,
                listing_id=listing_id,
                property_id=property_id
            )
            db.session.add(new_user_fav_property)
            db.session.commit()

            # Prepare the success message
            success_message = f"UserFavoriteProperty with ID {new_user_fav_property.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_user_fav_property.id,
                'user_id': new_user_fav_property.user_id,
                'listing_id': new_user_fav_property.listing_id,
                'property_id': new_user_fav_property.property_id,
            }, 201  # 201 Created status code
        else:
            return {'message': 'Invalid JSON data'}, 400

class FavoriteId(Resource):
    # def patch(self, id):
    #     data = request.get_json()
    #     if data:
    #         user_fav_property = UserFavoriteProperty.query.get(id)
    #         if user_fav_property:
    #             # Update the UserFavoriteProperty attributes based on the provided data
    #             if 'user_id' in data:
    #                 user_fav_property.user_id = data['user_id']
    #             if 'listing_id' in data:
    #                 user_fav_property.listing_id = data['listing_id']
    #             if 'property_id' in data:
    #                 user_fav_property.property_id = data['property_id']

    #             # Commit changes to the database
    #             db.session.commit()

    #             # Prepare the success message
    #             success_message = f"UserFavoriteProperty with ID {id} has been successfully updated."

    #             return {
    #                 'message': success_message,
    #                 'id': user_fav_property.id,
    #                 'user_id': user_fav_property.user_id,
    #                 'listing_id': user_fav_property.listing_id,
    #                 'property_id': user_fav_property.property_id,
    #             }, 200
    #         else:
    #             return {'message': 'UserFavoriteProperty not found'}, 404
    #     else:
    #         return {'message': 'Invalid JSON data'}, 400

    def delete(self, id):
        user_fav_property = UserFavoriteProperty.query.get(id)
        if user_fav_property:
            # Delete the UserFavoriteProperty from the database
            db.session.delete(user_fav_property)
            db.session.commit()
            return {'message': 'UserFavoriteProperty deleted successfully'}, 200
        else:
            return {'message': 'UserFavoriteProperty not found'}, 404

class InquiryResource(Resource):
    def get(self):
        inquiries = PropertyInquiry.query.all()
        inquiry_list = [
            {
                'id': inquiry.id,
                'name': inquiry.name,
                'email': inquiry.email,
                'phone': inquiry.phone,
                'address': inquiry.address,
                'message': inquiry.message,
                'inquiry_date': inquiry.inquiry_date.strftime('%Y-%m-%d %H:%M:%S'),
                'property_id': inquiry.property_id
            }
            for inquiry in inquiries
        ]

    def post(self):
        data = request.get_json()
        if data:
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            address = data.get('address')
            message = data.get('message')
            property_id = data.get('property_id')

            # Extract inquiry_date from the incoming data (you can modify the format as needed)
            inquiry_date = datetime.datetime.now()

            new_inquiry = PropertyInquiry(
                name=name,
                email=email,
                phone=phone,
                address=address,
                message=message,
                property_id=property_id,
                inquiry_date=inquiry_date
            )
            db.session.add(new_inquiry)
            db.session.commit()

            success_message = f"Inquiry with ID {new_inquiry.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_inquiry.id,
                'name': new_inquiry.name,
                'email': new_inquiry.email,
                'phone': new_inquiry.phone,
                'address': new_inquiry.address,
                'message': new_inquiry.message,
                'inquiry_date': new_inquiry.inquiry_date.strftime('%Y-%m-%d %H:%M:%S'),
                'property_id': new_inquiry.property_id
            }, 201
        else:
            return {'message': 'Invalid JSON data'}, 400

class InquiryResourceId(Resource):
    def get(self, id):
        inquiry = PropertyInquiry.query.get(id)
        if inquiry:
            inquiry_data = {
                'id': inquiry.id,
                'name': inquiry.name,
                'email': inquiry.email,
                'phone': inquiry.phone,
                'address': inquiry.address,
                'message': inquiry.message,
                'inquiry_date': inquiry.inquiry_date.strftime('%Y-%m-%d %H:%M:%S'),
                'property_id': inquiry.property_id
            }
            return inquiry_data
        else:
            return {'message': 'Inquiry not found'}, 404

    def delete(self, id):
        inquiry = PropertyInquiry.query.get(id)
        if inquiry:
            db.session.delete(inquiry)
            db.session.commit()
            return {'message': 'Inquiry deleted successfully'}, 200
        else:
            return {'message': 'Inquiry not found'}, 404

api.add_resource(InquiryResource, '/inquiries')
api.add_resource(InquiryResourceId, '/inquiries/<int:id>')
api.add_resource(UserResource, '/users')
api.add_resource(UserResourceId, '/users/<int:user_id>')
api.add_resource(LocationResource, '/locations')
api.add_resource(PropertyResource, '/properties')
api.add_resource(PropertyResourceId, '/properties/<int:id>')
api.add_resource(ListingResource, '/listings')
api.add_resource(ListingResourceId, '/listings/<int:id>')
api.add_resource(NewestListingResource, '/newestlistings')
api.add_resource(NewestListingResourceId, '/newestlistings/<int:id>')
api.add_resource(FeaturedListingResource, '/featuredlistings')
api.add_resource(FeaturedListingResourceId, '/featuredlistings/<int:id>')
api.add_resource(ReviewResource, '/reviews')
api.add_resource(ReviewResourceId,  '/reviews/<int:id>')
api.add_resource(Favorite, '/fav')
api.add_resource(FavoriteId, '/fav/<int:id>')
api.add_resource(UserLoginResource, '/login')
api.add_resource(ProtectedResource, '/protected')
api.add_resource(CheckUsernameAndEmail, '/check_username_and_email')



if __name__ == '__main__':
    app.run(port=5600,debug=True)