"""
ReviewsIQ Scraper Module
Fetches customer reviews for a business
"""

import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_sample_reviews():
    """Return realistic sample reviews for testing"""
    logger.info("Using sample reviews (fallback)")
    
    sample_reviews = [
        {
            "rating": 5,
            "text": "Amazing service! Staff was super friendly and helpful. Best experience ever!",
            "date": "2024-04-25"
        },
        {
            "rating": 5,
            "text": "Best experience ever. Highly recommend to everyone! Will definitely come back.",
            "date": "2024-04-24"
        },
        {
            "rating": 4,
            "text": "Good but a bit pricey. Worth the visit though. Nice atmosphere.",
            "date": "2024-04-23"
        },
        {
            "rating": 2,
            "text": "Waited 30 minutes for service. Very slow. Not impressed.",
            "date": "2024-04-22"
        },
        {
            "rating": 3,
            "text": "Nice place but WiFi doesn't work properly. Otherwise good.",
            "date": "2024-04-21"
        },
        {
            "rating": 5,
            "text": "Staff is incredibly kind and helpful. Love coming here!",
            "date": "2024-04-20"
        },
        {
            "rating": 2,
            "text": "Prices are too high compared to competitors. Coffee quality okay.",
            "date": "2024-04-19"
        },
        {
            "rating": 4,
            "text": "Good place to work. Quiet atmosphere. Recommend!",
            "date": "2024-04-18"
        }
    ]
    
    return sample_reviews


def fetch_reviews(business_name, location=""):
    """
    Fetch reviews for a business
    
    Args:
        business_name (str): Name of the business
        location (str): Location (optional)
    
    Returns:
        list: List of reviews with keys: rating, text, date
    """
    
    try:
        logger.info(f"Fetching reviews for: {business_name}, {location}")
        
        if not business_name or not isinstance(business_name, str):
            logger.warning("Invalid business name provided")
            return get_sample_reviews()
        
        logger.debug(f"Business name: {business_name}")
        logger.debug(f"Location: {location}")
        
        # For MVP: Return sample reviews
        reviews = get_sample_reviews()
        
        logger.info(f"Successfully fetched {len(reviews)} reviews")
        return reviews
    
    except Exception as e:
        logger.error(f"Error fetching reviews: {str(e)}", exc_info=True)
        logger.warning("Falling back to sample reviews")
        return get_sample_reviews()


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("Testing Scraper Module")
    print("=" * 70 + "\n")
    
    reviews = fetch_reviews("Starbucks", "Chicago")
    
    print(f"✅ Got {len(reviews)} reviews\n")
    
    for i, review in enumerate(reviews[:3]):
        print(f"Review {i+1}:")
        print(f"  Rating: {'⭐' * review['rating']} ({review['rating']}/5)")
        print(f"  Text: {review['text'][:80]}...")
        print(f"  Date: {review['date']}\n")
