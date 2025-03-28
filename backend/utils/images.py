import requests
from functools import lru_cache
import base64
from io import BytesIO
from PIL import Image
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@lru_cache(maxsize=100)
def url_to_base64(url: str, max_size: int = 512) -> str:
    """
    Fetch an image from a URL and convert it to base64 with caching.
    
    Args:
        url (str): The URL of the image to fetch
        max_size (int): Maximum dimension (width/height) for the image
        
    Returns:
        str: Base64 encoded image in data URI format
        
    Raises:
        Exception: If image fetch or processing fails
    """
    try:
        # Fetch image with timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Open image and convert to RGB
        img = Image.open(BytesIO(response.content))
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        # Resize if needed while maintaining aspect ratio
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = tuple(int(dim * ratio) for dim in img.size)
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            
        # Convert to JPEG format with compression
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=85, optimize=True)
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        return f'data:image/jpeg;base64,{img_str}'
        
    except requests.RequestException as e:
        logger.error(f"Failed to fetch image from URL: {e}")
        raise Exception(f"Failed to fetch image: {str(e)}")
    except Exception as e:
        logger.error(f"Failed to process image: {e}")
        raise Exception(f"Failed to process image: {str(e)}")

def validate_image(file_data: bytes, max_size_mb: float = 5.0) -> bool:
    """
    Validate image data for size and format.
    
    Args:
        file_data (bytes): The image file data
        max_size_mb (float): Maximum allowed file size in MB
        
    Returns:
        bool: True if image is valid, False otherwise
    """
    try:
        # Check file size
        size_mb = len(file_data) / (1024 * 1024)
        if size_mb > max_size_mb:
            logger.warning(f"Image size {size_mb:.2f}MB exceeds limit of {max_size_mb}MB")
            return False
            
        # Verify it's a valid image
        img = Image.open(BytesIO(file_data))
        img.verify()
        return True
        
    except Exception as e:
        logger.error(f"Image validation failed: {e}")
        return False

def compress_image(file_data: bytes, max_size: int = 300) -> str:
    """
    Compress and convert image to base64.
    
    Args:
        file_data (bytes): The image file data
        max_size (int): Maximum dimension (width/height) for the image
        
    Returns:
        str: Base64 encoded image in data URI format
        
    Raises:
        Exception: If image processing fails
    """
    try:
        img = Image.open(BytesIO(file_data))
        
        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        # Resize if needed
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = tuple(int(dim * ratio) for dim in img.size)
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            
        # Compress and convert to base64
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=85, optimize=True)
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        return f'data:image/jpeg;base64,{img_str}'
        
    except Exception as e:
        logger.error(f"Image compression failed: {e}")
        raise Exception(f"Failed to compress image: {str(e)}") 