from CarStats.scraping.scraper_brands import ScrapBrands
from CarStats.stats.tools import Stats

################################################################################
################################################################################
################################################################################
#
#
#Scraps data and build the dict data
scraping=ScrapBrands()
scrap_=scraping()
################################################################################
################################################################################
################################################################################
#
#
# Make stats
staty = Stats(scrap_)
staty_ = staty()
################################################################################

