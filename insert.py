import json
import psycopg2


file_path = r'D:\1._University of OULU\actual_project\final.json'

DB_CONFIG = {
    "dbname": "NewDB",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432",
}

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_levels(categories, max_levels=6):
    levels = categories[:max_levels] + [None] * (max_levels - len(categories))
    return levels

# Process data
def process_data(json_data):
    processed_data = []

    for item in json_data:
        try:
            
            levels = extract_levels(item.get('categories', []))
            other_attributes = json.loads(item.get('other_attributes', '{}'))
            row = {
                "prod_id": item.get('product_id'),
                "level1": levels[0],
                "level2": levels[1],
                "level3": levels[2],
                "level4": levels[3],
                "level5": levels[4],
                "level6": levels[5],
                "name": item.get('name'),
                "image_url": item.get('image_url'),
                "description": item.get('description'),
                "all_attributes": item.get('other_attributes'),
                "size": other_attributes.get('size'),
                "volume": other_attributes.get('volume'),
                "weight": other_attributes.get('weight'),
                "length": other_attributes.get('length'),
                "brands": other_attributes.get('brand'),
                "url": other_attributes.get('url'),
                "colour": other_attributes.get('colour'),
                "amount": other_attributes.get('amount'),
                "gender": other_attributes.get('gender'),
                "material": other_attributes.get('material'),
                "garment": other_attributes.get('garment'),
                "country_made_of": other_attributes.get('country_made_of'),
                "furniture": other_attributes.get('furniture'),
                "outdoor": other_attributes.get('outdoor'),
                "pet": other_attributes.get('pet'),
                "ingredients": other_attributes.get('ingredients'),
                "Camera Resolution": other_attributes.get('Camera Resolution'),
                "Motion Detection": other_attributes.get('Motion Detection'),
                "Audio Recording Capability": other_attributes.get('Audio Recording Capability'),
                "Night Vision Range": other_attributes.get('Night Vision Range'),
                "Weather Resistance": other_attributes.get('Weather Resistance'),
                "Facial Recognition": other_attributes.get('Facial Recognition'),
                "Battery Life": other_attributes.get('Battery Life'),
                "Video Compression Format": other_attributes.get('Video Compression Format'),
                "Screen Size": other_attributes.get('Screen Size'),
                "Touchscreen Capability": other_attributes.get('Touchscreen Capability'),
                "Calendar Integration": other_attributes.get('Calendar Integration'),
                "Anti-Slip Backing": other_attributes.get('Anti-Slip Backing'),
                "Fire Resistance": other_attributes.get('Fire Resistance'),
                "Pet Friendly": other_attributes.get('Pet Friendly'),
                "UV Resistance": other_attributes.get('UV Resistance'),
                "Scent Intensity": other_attributes.get('Scent Intensity'),
                "Burn Time": other_attributes.get('Burn Time'),
                "Essential Oil Content": other_attributes.get('Essential Oil Content'),
                "Allergen-Free Certification": other_attributes.get('Allergen-Free Certification'),
                "3D Effect Availability": other_attributes.get('3D Effect Availability'),
                "Material Strength": other_attributes.get('Material Strength'),
                "Brush Bristle Type": other_attributes.get('Brush Bristle Type'),
                "Number of Shelves": other_attributes.get('Number of Shelves'),
                "Table Shape": other_attributes.get('Table Shape'),
                "Remote Control Compatibility": other_attributes.get('Remote Control Compatibility'),
                "Dimmer Feature": other_attributes.get('Dimmer Feature'),
                "Energy Efficiency": other_attributes.get('Energy Efficiency'),
                "Light Output Lumens": other_attributes.get('Light Output Lumens'),
                "Power Consumption": other_attributes.get('Power Consumption'),
                "Lamp Shade Type": other_attributes.get('Lamp Shade Type'),
                "Brightness Levels": other_attributes.get('Brightness Levels'),
                "Lighting Direction": other_attributes.get('Lighting Direction'),
                "Assembly Instructions": other_attributes.get('Assembly Instructions'),
                "Safety Features": other_attributes.get('Safety Features'),
                "Washability instructions": other_attributes.get('Washability instructions'),
                "Care Instructions": other_attributes.get('Care Instructions'),
                "Shrinkage Resistance": other_attributes.get('Shrinkage Resistance'),
                "Textile Certification": other_attributes.get('Textile Certification'),
                "Storage Capacity": other_attributes.get('Storage Capacity'),
                "Moisture-Wicking Properties": other_attributes.get('Moisture-Wicking Properties'),
                "Customizable Options": other_attributes.get('Customizable Options'),
                "Space-Saving Features": other_attributes.get('Space-Saving Features'),
                "Decorative Features": other_attributes.get('Decorative Features'),
                "Multi-Functionality": other_attributes.get('Multi-Functionality'),
                "Seat Height Adjustment": other_attributes.get('Seat Height Adjustment'),
                "Lumbar Support": other_attributes.get('Lumbar Support'),
                "Non-Slip Features": other_attributes.get('Non-Slip Features'),
                "Tilt Mechanism": other_attributes.get('Tilt Mechanism'),
                "Wheel Type": other_attributes.get('Wheel Type'),
                "Laptop Size Compatibility": other_attributes.get('Laptop Size Compatibility'),
                "Material Type": other_attributes.get('Material Type'),
                "Hardware Specifications": other_attributes.get('Hardware Specifications'),
                "Software Specifications": other_attributes.get('Software Specifications'),
                "Pockets": other_attributes.get('Pockets'),
                "Wind Resistance": other_attributes.get('Wind Resistance'),
                "Moisturizing Features": other_attributes.get('Moisturizing Features'),
                "Coverage Type": other_attributes.get('Coverage Type'),
                "Formula Type": other_attributes.get('Formula Type'),
                "Skin Compatibility": other_attributes.get('Skin Compatibility'),
                "Eco-Friendly Ingredients": other_attributes.get('Eco-Friendly Ingredients'),
                "Hydration Level": other_attributes.get('Hydration Level'),
                "Vegan Ingredients": other_attributes.get('Vegan Ingredients'),
                "Fragrance type/Free": other_attributes.get('Fragrance type/Free'),
                "Skin Tone Adaptability": other_attributes.get('Skin Tone Adaptability'),
                "Safety and Security features": other_attributes.get('Safety and Security features'),
                "Heat Resistance": other_attributes.get('Heat Resistance'),
                "Storage Compartments": other_attributes.get('Storage Compartments'),
                "Display Type": other_attributes.get('Display Type'),
                "Plant Type": other_attributes.get('Plant Type'),
                "Pot Type": other_attributes.get('Pot Type'),
                "Price": other_attributes.get('Price'),
                "Customization Availability": other_attributes.get('Customization Availability'),
                "Warranty": other_attributes.get('Warranty'),
                "Return Policy": other_attributes.get('Return Policy'),
                "Smartphone Compatibility": other_attributes.get('Smartphone Compatibility'),
                "Noise Level": other_attributes.get('Noise Level'),
                "Noise Emission": other_attributes.get('Noise Emission'),
                "Age Group": other_attributes.get('Age Group'),
                "RAM": other_attributes.get('RAM'),
                "Processor": other_attributes.get('Processor'),
                "Operating System": other_attributes.get('Operating System'),
                "Connectivity": other_attributes.get('Connectivity'),
                "Shipping Cost": other_attributes.get('Shipping Cost'),
                "Shipping Time": other_attributes.get('Shipping Time'),
                "Return Window": other_attributes.get('Return Window'),
                "Cooling Technology": other_attributes.get('Cooling Technology')
            }

            processed_data.append(row)
        except (json.JSONDecodeError, TypeError, KeyError) as e:
            pass

    return processed_data

def insert_data_to_db(data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()


        insert_query = """
        INSERT INTO public.products4 (
            prod_id, level1, level2, level3, level4, level5, level6, name, image_url, description,
            all_attributes, size, volume, weight, length, brands, url, colour, amount, gender,
            material, garment, country_made_of, furniture, outdoor, pet, ingredients,
            "Camera Resolution", "Motion Detection", "Audio Recording Capability", "Night Vision Range",
            "Weather Resistance", "Facial Recognition", "Battery Life", "Video Compression Format",
            "Screen Size", "Touchscreen Capability", "Calendar Integration", "Anti-Slip Backing",
            "Fire Resistance", "Pet Friendly", "UV Resistance", "Scent Intensity", "Burn Time",
            "Essential Oil Content", "Allergen-Free Certification", "3D Effect Availability",
            "Material Strength", "Brush Bristle Type", "Number of Shelves", "Table Shape",
            "Remote Control Compatibility", "Dimmer Feature", "Energy Efficiency", "Light Output Lumens",
            "Power Consumption", "Lamp Shade Type", "Brightness Levels", "Lighting Direction",
            "Assembly Instructions", "Safety Features", "Washability instructions", "Care Instructions",
            "Shrinkage Resistance", "Textile Certification", "Storage Capacity",
            "Moisture-Wicking Properties", "Customizable Options", "Space-Saving Features",
            "Decorative Features", "Multi-Functionality", "Seat Height Adjustment", "Lumbar Support",
            "Non-Slip Features", "Tilt Mechanism", "Wheel Type", "Laptop Size Compatibility",
            "Material Type", "Hardware Specifications", "Software Specifications", "Pockets",
            "Wind Resistance", "Moisturizing Features", "Coverage Type", "Formula Type",
            "Skin Compatibility", "Eco-Friendly Ingredients", "Hydration Level", "Vegan Ingredients",
            "Fragrance type/Free", "Skin Tone Adaptability", "Safety and Security features",
            "Heat Resistance", "Storage Compartments", "Display Type", "Plant Type", "Pot Type",
            "Price", "Customization Availability", "Warranty", "Return Policy",
            "Smartphone Compatibility", "Noise Level", "Noise Emission", "Age Group", "RAM",
            "Processor", "Operating System", "Connectivity", "Shipping Cost", "Shipping Time",
            "Return Window", "Cooling Technology"
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s)
        """

        for row in data:
            values = tuple(
                str(row.get(column, "") or "") for column in [
                    "prod_id", "level1", "level2", "level3", "level4", "level5", "level6", "name",
                    "image_url", "description", "all_attributes", "size", "volume", "weight", "length",
                    "brands", "url", "colour", "amount", "gender", "material", "garment",
                    "country_made_of", "furniture", "outdoor", "pet", "ingredients",
                    "Camera Resolution", "Motion Detection", "Audio Recording Capability",
                    "Night Vision Range", "Weather Resistance", "Facial Recognition", "Battery Life",
                    "Video Compression Format", "Screen Size", "Touchscreen Capability",
                    "Calendar Integration", "Anti-Slip Backing", "Fire Resistance", "Pet Friendly",
                    "UV Resistance", "Scent Intensity", "Burn Time", "Essential Oil Content",
                    "Allergen-Free Certification", "3D Effect Availability", "Material Strength",
                    "Brush Bristle Type", "Number of Shelves", "Table Shape",
                    "Remote Control Compatibility", "Dimmer Feature", "Energy Efficiency",
                    "Light Output Lumens", "Power Consumption", "Lamp Shade Type",
                    "Brightness Levels", "Lighting Direction", "Assembly Instructions",
                    "Safety Features", "Washability instructions", "Care Instructions",
                    "Shrinkage Resistance", "Textile Certification", "Storage Capacity",
                    "Moisture-Wicking Properties", "Customizable Options", "Space-Saving Features",
                    "Decorative Features", "Multi-Functionality", "Seat Height Adjustment",
                    "Lumbar Support", "Non-Slip Features", "Tilt Mechanism", "Wheel Type",
                    "Laptop Size Compatibility", "Material Type", "Hardware Specifications",
                    "Software Specifications", "Pockets", "Wind Resistance", "Moisturizing Features",
                    "Coverage Type", "Formula Type", "Skin Compatibility", "Eco-Friendly Ingredients",
                    "Hydration Level", "Vegan Ingredients", "Fragrance type/Free",
                    "Skin Tone Adaptability", "Safety and Security features", "Heat Resistance",
                    "Storage Compartments", "Display Type", "Plant Type", "Pot Type", "Price",
                    "Customization Availability", "Warranty", "Return Policy",
                    "Smartphone Compatibility", "Noise Level", "Noise Emission", "Age Group", "RAM",
                    "Processor", "Operating System", "Connectivity", "Shipping Cost",
                    "Shipping Time", "Return Window", "Cooling Technology",
                ]
            )
            cursor.execute(insert_query, values)

        conn.commit()
        print("Data inserted successfully.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



if __name__ == "__main__":
    json_data = load_json(file_path)
    processed_data = process_data(json_data)
    insert_data_to_db(processed_data)
