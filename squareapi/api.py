import os

from dotenv import load_dotenv, find_dotenv
from square.client import Client as SquareClient
from square.api.invoices_api import InvoicesApi

load_dotenv(find_dotenv)

SQUARE_ACCESS_TOKEN = os.getenv("SQUARE_ACCESS_TOKEN")
SQUARE_LOCATION_ID = os.getenv("SQUARE_LOCATION_ID")
SQUARE_ENVIRONMENT = os.getenv("SQUARE_ENVIRONMENT")

square = SquareClient(
    access_token=SQUARE_ACCESS_TOKEN,
    environment=SQUARE_ENVIRONMENT,
)

def get_invoices():
    """Get all invoices from a square account."""
    invoices_api = InvoicesApi(square)
    invoices = invoices_api.list_invoices(location_id=SQUARE_LOCATION_ID)
    return invoices.body["invoices"]
