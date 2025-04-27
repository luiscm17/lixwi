import re
from typing import Union
from PIL import Image

def is_math_problem(image: Union[str, Image.Image]) -> bool:
    """
    Valida si una imagen contiene un problema matemático.
    Por ahora retorna True como placeholder hasta implementar la lógica real.
    
    Args:
        image: Ruta de la imagen o objeto Image de PIL
        
    Returns:
        bool: True si parece un problema matemático
    """
    return True