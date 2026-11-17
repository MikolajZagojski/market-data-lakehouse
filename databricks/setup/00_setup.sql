-- Sets up the catalog, medallion schemas and the landing volume.

CREATE CATALOG IF NOT EXISTS market_data
    COMMENT 'Daily US stock market data from the Twelve Data API';

CREATE SCHEMA IF NOT EXISTS market_data.raw
    COMMENT 'Source files stored unchanged, as returned by the API';
CREATE SCHEMA IF NOT EXISTS market_data.bronze
    COMMENT 'Source data in Delta format with ingestion metadata, no transformations';
CREATE SCHEMA IF NOT EXISTS market_data.silver
    COMMENT 'Validated, typed and deduplicated daily prices';
CREATE SCHEMA IF NOT EXISTS market_data.gold
    COMMENT 'Business level metrics: returns, moving averages, volatility, sector aggregates';

CREATE VOLUME IF NOT EXISTS market_data.raw.landing
    COMMENT 'API responses uploaded by the ingestion job, partitioned by ingestion date';