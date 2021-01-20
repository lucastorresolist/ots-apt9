from Back.controller.base_controller import BaseController
from Back.dao_db.dao_marketplaces import MarketplaceDao


class MarketplaceController(BaseController):
    def __init__(self)-> None:
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao)