import os

# Project root is one level up from 'app'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Resource Paths
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
XSD_PATH = os.path.join(BASE_DIR, "xsd", "maindoc",
                        "UBL-DespatchAdvice-2.1.xsd")
GENERATED_DIR = os.path.join(BASE_DIR, "generated")

# Ensure the generated directory exists
os.makedirs(GENERATED_DIR, exist_ok=True)
