from CarStats.scraping.scraper import Scrap
from CarStats.stats.tools import Stats

################################################################################
################################################################################
################################################################################
#
#
#Scraps data and build the dict data
scraping=Scrap()
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

