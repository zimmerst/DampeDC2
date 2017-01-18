# pseudocode for now.
import logging
from tqdm import tqdm
from DampeDataCrawler.utils.data_tools import verify_content, extract_metadata

log = logging.getLogger("crawler")

datacatalog= DataCatalog() # init with server settings.

log.info("checking for new files")
for datafile in tqdm(datacatalog.getNewFiles()):
    if not datafile.check_access(): datafile.mark(good=False,comment="could not access file")
    else:
        ftype = datafile.ftype
        if verify_content()

