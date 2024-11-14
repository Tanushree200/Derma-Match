# Define a dictionary of skincare ingredients along with their application instructions, ratings for each skin problem,
# information about compatibility with other ingredients, and descriptions
skincare_ingredients_info = {
  "Hyaluronic acid": {
    "instructions": "Apply a few drops to clean, damp skin before applying moisturizer. Can be used morning and night.",
    "ratings": {
      "acne": 4,
      "eczema": 5,
      "blackheads": 3,
      "hyperpigmentation": 4,
      "sensitive skin": 4,
      "fine lines and wrinkles": 5,
      "uneven skin texture": 4,
      "dullness": 4,
      "dark circles and puffiness": 4,
      "sun damage": 3,
      "enlarged pores": 3,
      "uneven skin tone": 4,
      "dehydrated skin": 5,
      "redness and irritation": 4,
      "melasma and age spots": 3
    },
    "incompatible_with": ["Vitamin C"]
  },
  "Salicylic acid": {
    "instructions": "Apply to cleansed skin, focusing on areas of concern. Can be used as a spot treatment or in a toner. Use at night.",
    "ratings": {
      "acne": 10,
      "eczema": 3,
      "blackheads": 9,
      "hyperpigmentation": 5,
      "sensitive skin": 4,
      "fine lines and wrinkles": 6,
      "uneven skin texture": 8,
      "dullness": 7,
      "dark circles and puffiness": 3,
      "sun damage": 4,
      "enlarged pores": 9,
      "uneven skin tone": 7,
      "dehydrated skin": 3,
      "redness and irritation": 4,
      "melasma and age spots": 5
    },
    "incompatible_with": ["Retinol"]
  },
  "Niacinamide": {
    "instructions": "Apply a few drops to clean skin before your moisturizer. Can be used both morning and night.",
    "ratings": {
      "acne": 8,
      "eczema": 9,
      "blackheads": 6,
      "hyperpigmentation": 7,
      "sensitive skin": 10,
      "fine lines and wrinkles": 6,
      "uneven skin texture": 8,
      "dullness": 7,
      "dark circles and puffiness": 6,
      "sun damage": 6,
      "enlarged pores": 8,
      "uneven skin tone": 9,
      "dehydrated skin": 7,
      "redness and irritation": 9,
      "melasma and age spots": 6
    },
    "incompatible_with": ["None"]
  },
  "Vitamin C": {
    "instructions": "Apply a few drops to clean skin, ideally in the morning. Can be followed by sunscreen.",
    "ratings": {
      "acne": 6,
      "eczema": 3,
      "blackheads": 4,
      "hyperpigmentation": 9,
      "sensitive skin": 5,
      "fine lines and wrinkles": 9,
      "uneven skin texture": 7,
      "dullness": 9,
      "dark circles and puffiness": 7,
      "sun damage": 8,
      "enlarged pores": 5,
      "uneven skin tone": 9,
      "dehydrated skin": 4,
      "redness and irritation": 3,
      "melasma and age spots": 9
    },
    "incompatible_with": ["Hyaluronic acid (can cause irritation when combined)"]
  },
  "Retinol": {
    "instructions": "Apply a small amount to clean, dry skin before bedtime. Gradually increase frequency.",
    "ratings": {
      "acne": 9,
      "eczema": 4,
      "blackheads": 8,
      "hyperpigmentation": 8,
      "sensitive skin": 3,
      "fine lines and wrinkles": 10,
      "uneven skin texture": 9,
      "dullness": 7,
      "dark circles and puffiness": 6,
      "sun damage": 7,
      "enlarged pores": 9,
      "uneven skin tone": 8,
      "dehydrated skin": 4,
      "redness and irritation": 3,
      "melasma and age spots": 7
    },
    "incompatible_with": ["Salicylic acid"]
  },
  "AHA (Alpha Hydroxy Acid)": {
    "instructions": "Apply to clean skin after cleansing, followed by moisturizer. Can be used in the evening.",
    "ratings": {
      "acne": 7,
      "eczema": 3,
      "blackheads": 8,
      "hyperpigmentation": 8,
      "sensitive skin": 4,
      "fine lines and wrinkles": 8,
      "uneven skin texture": 9,
      "dullness": 9,
      "dark circles and puffiness": 5,
      "sun damage": 8,
      "enlarged pores": 7,
      "uneven skin tone": 9,
      "dehydrated skin": 5,
      "redness and irritation": 4,
      "melasma and age spots": 8
    },
    "incompatible_with": ["Retinol", "Salicylic acid"]
  },
  "Zinc oxide": {
    "instructions": "Apply a thin layer to skin, especially on areas exposed to the sun. Reapply every 2 hours.",
    "ratings": {
      "acne": 8,
      "eczema": 9,
      "blackheads": 6,
      "hyperpigmentation": 7,
      "sensitive skin": 10,
      "fine lines and wrinkles": 5,
      "uneven skin texture": 6,
      "dullness": 5,
      "dark circles and puffiness": 7,
      "sun damage": 10,
      "enlarged pores": 5,
      "uneven skin tone": 7,
      "dehydrated skin": 7,
      "redness and irritation": 9,
      "melasma and age spots": 7
    },
    "incompatible_with": ["None"]
  },
  "Tea tree oil": {
    "instructions": "Dilute with a carrier oil and apply to affected areas. Can be used twice daily.",
    "ratings": {
      "acne": 9,
      "eczema": 4,
      "blackheads": 8,
      "hyperpigmentation": 5,
      "sensitive skin": 4,
      "fine lines and wrinkles": 4,
      "uneven skin texture": 6,
      "dullness": 4,
      "dark circles and puffiness": 3,
      "sun damage": 3,
      "enlarged pores": 7,
      "uneven skin tone": 5,
      "dehydrated skin": 4,
      "redness and irritation": 6,
      "melasma and age spots": 4
    },
    "incompatible_with": ["None"]
  },
  "Centella asiatica": {
    "instructions": "Apply directly to affected areas or mix with a moisturizer. Can be used twice daily.",
    "ratings": {
      "acne": 7,
      "eczema": 10,
      "blackheads": 5,
      "hyperpigmentation": 6,
      "sensitive skin": 10,
      "fine lines and wrinkles": 6,
      "uneven skin texture": 7,
      "dullness": 6,
      "dark circles and puffiness": 5,
      "sun damage": 6,
      "enlarged pores": 6,
      "uneven skin tone": 7,
      "dehydrated skin": 8,
      "redness and irritation": 10,
      "melasma and age spots": 5
    },
    "incompatible_with": ["None"]
  },
  "Retinol": {
    "instructions": "Apply a small amount to clean, dry skin before bedtime. Gradually increase frequency.",
    "ratings": {
      "acne": 9,
      "eczema": 4,
      "blackheads": 8,
      "hyperpigmentation": 8,
      "sensitive skin": 3,
      "fine lines and wrinkles": 10,
      "uneven skin texture": 9,
      "dullness": 7,
      "dark circles and puffiness": 6,
      "sun damage": 7,
      "enlarged pores": 9,
      "uneven skin tone": 8,
      "dehydrated skin": 4,
      "redness and irritation": 3,
      "melasma and age spots": 7
    },
    "incompatible_with": ["Salicylic acid"]
  },
  "Glycolic acid": {
    "instructions": "Apply a thin layer to clean skin, especially in the evening. Follow up with sunscreen during the day.",
    "ratings": {
      "acne": 8,
      "eczema": 3,
      "blackheads": 9,
      "hyperpigmentation": 9,
      "sensitive skin": 4,
      "fine lines and wrinkles": 8,
      "uneven skin texture": 9,
      "dullness": 9,
      "dark circles and puffiness": 5,
      "sun damage": 9,
      "enlarged pores": 8,
      "uneven skin tone": 9,
      "dehydrated skin": 5,
      "redness and irritation": 4,
      "melasma and age spots": 9
    },
    "incompatible_with": ["Retinol", "Salicylic acid"]
  },
  "Lactic acid": {
    "instructions": "Apply to clean skin after toning, preferably at night. Use sunscreen during the day.",
    "ratings": {
      "acne": 7,
      "eczema": 5,
      "blackheads": 7,
      "hyperpigmentation": 8,
      "sensitive skin": 6,
      "fine lines and wrinkles": 8,
      "uneven skin texture": 8,
      "dullness": 8,
      "dark circles and puffiness": 6,
      "sun damage": 7,
      "enlarged pores": 7,
      "uneven skin tone": 8,
      "dehydrated skin": 6,
      "redness and irritation": 4,
      "melasma and age spots": 7
    },
    "incompatible_with": ["Retinol", "Salicylic acid"]
  },
  "Benzoyl Peroxide": {
    "instructions": "Apply a small amount to affected areas, typically after cleansing. Can be used in the morning and at night.",
    "ratings": {
      "acne": 10,
      "eczema": 2,
      "blackheads": 8,
      "hyperpigmentation": 5,
      "sensitive skin": 3,
      "fine lines and wrinkles": 5,
      "uneven skin texture": 6,
      "dullness": 4,
      "dark circles and puffiness": 3,
      "sun damage": 4,
      "enlarged pores": 6,
      "uneven skin tone": 5,
      "dehydrated skin": 3,
      "redness and irritation": 4,
      "melasma and age spots": 4
    },
    "incompatible_with": ["Retinol"]
  },
  
  "Peptides": {
    "instructions": "Apply after cleansing and toning, followed by moisturizer. Can be used both morning and night.",
    "ratings": {
      "acne": 6,
      "eczema": 8,
      "blackheads": 5,
      "hyperpigmentation": 6,
      "sensitive skin": 9,
      "fine lines and wrinkles": 9,
      "uneven skin texture": 7,
      "dullness": 6,
      "dark circles and puffiness": 8,
      "sun damage": 6,
      "enlarged pores": 6,
      "uneven skin tone": 7,
      "dehydrated skin": 8,
      "redness and irritation": 9,
      "melasma and age spots": 6
    },
    "incompatible_with": ["None"]
  },
  "Ceramides": {
    "instructions": "Apply to clean skin, followed by a moisturizer. Can be used morning and night.",
    "ratings": {
      "acne": 5,
      "eczema": 9,
      "blackheads": 4,
      "hyperpigmentation": 6,
      "sensitive skin": 10,
      "fine lines and wrinkles": 6,
      "uneven skin texture": 7,
      "dullness": 7,
      "dark circles and puffiness": 5,
      "sun damage": 5,
      "enlarged pores": 5,
      "uneven skin tone": 6,
      "dehydrated skin": 9,
      "redness and irritation": 9,
      "melasma and age spots": 5
    },
    "incompatible_with": ["None"]
  },
  "Argan oil": {
    "instructions": "Apply a few drops to face and neck after cleansing. Can be used in both morning and night routines.",
    "ratings": {
      "acne": 5,
      "eczema": 8,
      "blackheads": 4,
      "hyperpigmentation": 6,
      "sensitive skin": 8,
      "fine lines and wrinkles": 8,
      "uneven skin texture": 7,
      "dullness": 8,
      "dark circles and puffiness": 6,
      "sun damage": 5,
      "enlarged pores": 4,
      "uneven skin tone": 6,
      "dehydrated skin": 8,
      "redness and irritation": 7,
      "melasma and age spots": 5
    },
    "incompatible_with": ["None"]
  },
  "Squalane": {
    "instructions": "Apply a few drops to face and neck after cleansing, or mix with your moisturizer.",
    "ratings": {
      "acne": 7,
      "eczema": 8,
      "blackheads": 6,
      "hyperpigmentation": 6,
      "sensitive skin": 9,
      "fine lines and wrinkles": 8,
      "uneven skin texture": 7,
      "dullness": 7,
      "dark circles and puffiness": 7,
      "sun damage": 6,
      "enlarged pores": 6,
      "uneven skin tone": 7,
      "dehydrated skin": 9,
      "redness and irritation": 8,
      "melasma and age spots": 6
    },
    "incompatible_with": ["None"]
  }
}



# Define a dictionary of skin types and corresponding skincare concerns
skincare_recommendations = {
    "normal": ["Hyaluronic acid", "Vitamin C", "Niacinamide", "Retinol", "Glycolic acid", "Ceramides", "Squalane", "Centella asiatica", "Peptides", "Benzoyl Peroxide", "AHA (Alpha Hydroxy Acid)"],
    "dry": ["Hyaluronic acid", "Vitamin C", "Niacinamide", "Ceramides", "Squalane", "Centella asiatica", "Peptides", "Argan oil"],
    "oily": ["Niacinamide", "Salicylic acid", "Glycolic acid", "Tea tree oil", "Squalane",  "Centella asiatica", "Peptides", "Benzoyl Peroxide", "AHA (Alpha Hydroxy Acid)"],
    "combination": ["Hyaluronic acid", "Niacinamide", "Retinol", "Squalane", "Salicylic acid", "Glycolic acid", "Ceramides",  "Centella asiatica",  "Peptides", "AHA (Alpha Hydroxy Acid)", "Witch hazel"],
    "sensitive": ["Hyaluronic acid", "Niacinamide", "Ceramides", "Squalane",  "Centella asiatica",  "Peptides", "AHA (Alpha Hydroxy Acid)"]
}


# Define a list of skin problems for the user to choose from
skin_problems_list = [
    "acne", "eczema", "blackheads", "hyperpigmentation", "sensitive skin", "fine lines and wrinkles",
    "uneven skin texture", "dullness", "dark circles and puffiness", "sun damage", "enlarged pores",
    "uneven skin tone", "dehydrated skin", "redness and irritation", "melasma and age spots"
]


skincare_ingredient_forms = {
    "Hyaluronic acid": "serum",
    "Vitamin C": "serum",
    "Niacinamide": "serum",
    "Retinol": "serum",
    "Ceramides": "moisturizer",
    "Squalane": "moisturizer",
    "Salicylic acid": "cleanser",
    "Glycolic acid": "toner",
    "Tea tree oil": "spot treatment",
    "Centella asiatica": "moisturizer",
    "Peptides": "serum",
    "Kojic acid": "serum",
    "Cica": "moisturizer",
    "AHA (Alpha Hydroxy Acid)":"serum",
    "Zinc oxide":"moisturizer",
    "Lactic acid":"serum",
    "Benzoyl Peroxide":"spot treatment",
}

def generate_skincare_routine(recommendations):
    skincare_routine = {}
    
    # Iterate through the recommendations dictionary
    for skin_type, ingredients in recommendations.items():
        for ingredient in ingredients:
            # Get the form of the ingredient
            form = skincare_ingredient_forms.get(ingredient, "unknown")
            
            # Check if the form already exists in the routine
            if form in skincare_routine:
                # If the ingredient isn't already in the list, append it
                if ingredient not in skincare_routine[form]:
                    skincare_routine[form].append(ingredient)
            else:
                # If the form isn't in the routine, create a new entry
                skincare_routine[form] = [ingredient]
    
    return skincare_routine







def recommend_skincare(skin_type, skin_problems, avoid_ingredients):
    # Get the recommended ingredients for the specified skin type
    recommended_ingredients = skincare_recommendations.get(skin_type.lower(), [])
    
    # Remove duplicates and filter out ingredients to avoid
    recommended_ingredients = list(set(recommended_ingredients) - set(avoid_ingredients))
    
    # Initialize a dictionary to store recommendations for each skin problem
    recommendations = {}
    
    # Iterate over each skin problem
    for problem in skin_problems:
        # Sort the ingredients by their rating for the current skin problem (if rating exists)
        sorted_ingredients = sorted(
            recommended_ingredients,
            key=lambda x: skincare_ingredients_info[x]["ratings"].get(problem, 0),  # Default rating to 0 if not found
            reverse=True
        )
        
        # Select the top two ingredients for the current skin problem
        recommendations[problem] = sorted_ingredients[:2]
    
    return recommendations




import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/index')
def index():
    skin_types = list(skincare_recommendations.keys())
    skin_problems = skin_problems_list
    return render_template('index.html', skin_types=skin_types, skin_problems=skin_problems, skincare_ingredients_info=skincare_ingredients_info)

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        skin_type = request.form['skin_type']
        skin_problems = request.form.getlist('skin_problems')
        avoid_ingredients = request.form.getlist('avoid_ingredients')
        
        recommendations = recommend_skincare(skin_type, skin_problems, avoid_ingredients)
        skincare_routine = generate_skincare_routine(recommendations)
        print("Skin Type:", skin_type)
        print("Skin Problems:", skin_problems)
        print("Avoid Ingredients:", avoid_ingredients)
        
        return render_template(
            'recommendations.html',
            recommendations=recommendations,
            skincare_ingredients_info=skincare_ingredients_info,
            skincare_routine=skincare_routine
        )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

